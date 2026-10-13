from __future__ import annotations

import argparse
import copy
import json
from decimal import Decimal
from pathlib import Path
from typing import Any
from urllib.parse import quote

from pyshacl import validate
from pystac.validation import validate_dict
from rdflib import RDF, XSD, BNode, Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.term import Identifier
from stac_model.runtime import Runtime
from stac_model.schema import SCHEMA_URI, MLModelProperties

SER = Namespace("https://w3id.org/ogc/stac/mlm/serialization/")
MLM = Namespace("https://w3id.org/ogc/stac/mlm/")
BLOCK = Path(__file__).resolve().parents[1] if "__file__" in globals() else None


def load_context(block: Path, assembled: Path) -> dict[str, Any]:
    """
    Load local term mappings without dereferencing arbitrary input contexts.
    """
    context = json.loads(assembled.read_text())["@context"]
    for path in sorted(block.parent.glob("*/context.jsonld")):
        if path.parent.name != "mlm":
            context.update(json.loads(path.read_text())["@context"])
    context.update(json.loads((block / "context.jsonld").read_text())["@context"])
    return context


def expand(term: str, context: dict[str, Any]) -> str:
    """
    Resolve a compact term against the block's locally assembled context.
    """
    if ":" in term:
        prefix, suffix = term.split(":", 1)
        namespace = context.get(prefix)
        if isinstance(namespace, str) and namespace.endswith(("/", "#")):
            return namespace + suffix
        return term
    definition = context.get(term)
    if isinstance(definition, dict):
        definition = definition.get("@id")
    if isinstance(definition, str) and not definition.startswith("@"):
        return expand(definition, context)
    return str(SER) + "member/" + quote(term, safe="")


def mapping(key: str, context: dict[str, Any]) -> tuple[URIRef, dict[str, Any], bool]:
    """
    Resolve a field predicate, its scoped context, and vocabulary coercion.
    """
    definition = context.get(key, {})
    if isinstance(definition, str):
        definition = {"@id": definition}
    scoped = {**context, **definition.get("@context", {})}
    term = definition.get("@id", key)
    if term == "@type":
        return URIRef(str(SER) + "member/" + quote(key, safe="")), scoped, False
    if term.startswith("@"):
        term = str(SER) + "member/" + quote(key, safe="")
    return URIRef(expand(term, scoped)), scoped, definition.get("@type") == "@vocab"


def validate_item(item: dict[str, Any]) -> None:
    """
    Validate MLM with stac-model and the complete Item with official JSON schemas.
    """
    if item.get("type") != "Feature":
        raise ValueError("MLM transforms accept STAC Items only, not Collections or Catalogs.")
    if SCHEMA_URI not in item.get("stac_extensions", []):
        raise ValueError(f"The Item must declare the supported MLM schema: {SCHEMA_URI}")
    properties = copy.deepcopy(item["properties"])
    # stac-model 0.7.0's classification adapter rejects schema-valid title/color_hint fields.
    # Keep the source unchanged. These fields are checked by the official schemas below.
    for output in properties.get("mlm:output", []):
        for alias in ("classification:classes", "classification_classes", "classes"):
            output.pop(alias, None)
    MLModelProperties.model_validate(properties)
    for asset in item.get("assets", {}).values():
        Runtime.model_validate({key.removeprefix("mlm:"): value for key, value in asset.items()})
    validate_dict(item)


class ItemRDF:
    """
    Encode semantic field values with sufficient structure to reverse RDF serialization.
    """

    def __init__(self, context: dict[str, Any]) -> None:
        self.context = context
        self.graph = Graph()
        self.graph.bind("serialization", SER)
        self.graph.bind("mlm", MLM)
        for prefix, value in context.items():
            if not prefix.startswith("@") and isinstance(value, str) and value.endswith(("/", "#")):
                self.graph.bind(prefix, Namespace(value))

    def encode_value(self, value: Any, context: dict[str, Any], vocabulary: bool = False) -> Identifier:
        if isinstance(value, dict):
            return self.encode_object(value, context)
        if isinstance(value, list):
            node = BNode()
            self.graph.add((node, RDF.type, SER.Array))
            self.graph.add((node, SER.items, self.encode_list(value, context, vocabulary)))
            return node
        if value is None:
            return Literal("null", datatype=RDF.JSON)
        if vocabulary and isinstance(value, str):
            iri = expand(value, context)
            if not iri.startswith(str(SER) + "member/"):
                return URIRef(iri)
        if isinstance(value, float):
            return Literal(format(Decimal(repr(value)), "f"), datatype=XSD.decimal, normalize=False)
        return Literal(value)

    def encode_list(self, values: list[Any], context: dict[str, Any], vocabulary: bool = False) -> Identifier:
        if not values:
            return RDF.nil
        head = BNode()
        Collection(self.graph, head, [self.encode_value(value, context, vocabulary) for value in values])
        return head

    def encode_object(self, obj: dict[str, Any], context: dict[str, Any]) -> BNode:
        node = BNode()
        self.graph.add((node, RDF.type, SER.Object))
        if isinstance(obj.get("type"), str) and context.get("type") == "@type":
            iri = expand(obj["type"], context)
            if not iri.startswith(str(SER) + "member/"):
                self.graph.add((node, RDF.type, URIRef(iri)))
        predicates: set[URIRef] = set()
        for key, value in obj.items():
            predicate, scoped, vocabulary = mapping(key, context)
            if predicate in predicates:
                raise ValueError(f"Ambiguous context: multiple JSON fields map to {predicate}.")
            predicates.add(predicate)
            field = BNode()
            self.graph.add((node, SER.field, field))
            self.graph.add((field, SER.key, Literal(key)))
            self.graph.add((field, SER.predicate, predicate))
            definition = context.get(key, {})
            json_literal = isinstance(definition, dict) and definition.get("@type") == "@json"
            indexed = key in ("assets", "cube:variables", "cube:dimensions")
            if isinstance(definition, dict) and definition.get("@container") == "@index":
                indexed = True
            if value is None:
                kind = "null"
            elif json_literal:
                kind = "json"
                self.graph.add((node, predicate, Literal(json.dumps(value, allow_nan=False), datatype=RDF.JSON)))
            elif isinstance(value, dict) and indexed:
                kind = "map"
                for name, entry in value.items():
                    if not isinstance(entry, dict):
                        raise TypeError(f"Map {key!r} entry {name!r} must be an object.")
                    child = self.encode_object(entry, scoped)
                    self.graph.add((child, SER.mapKey, Literal(name)))
                    self.graph.add((node, predicate, child))
                    if key in ("cube:variables", "cube:dimensions"):
                        name_predicate = (
                            MLM.datacube_variable_name if key == "cube:variables" else MLM.datacube_dimension_name
                        )
                        self.graph.add((child, name_predicate, Literal(name)))
            elif isinstance(value, list):
                ordered = (
                    str(predicate).startswith(str(SER))
                    or isinstance(definition, dict) and definition.get("@container") == "@list"
                )
                kind = "array" if ordered else "set"
                head = self.encode_list(value, scoped, vocabulary)
                if ordered:
                    self.graph.add((node, predicate, head))
                else:
                    self.graph.add((field, SER.items, head))
                    for entry in Collection(self.graph, head):
                        self.graph.add((node, predicate, entry))
                member_class = {
                    MLM.input: MLM.ModelInput,
                    MLM.output: MLM.ModelOutput,
                    MLM.bands: MLM.BandVariableReference,
                    MLM.variables: MLM.BandVariableReference,
                    MLM.value_scaling: MLM.ValueScaling,
                }.get(predicate)
                if member_class is not None:
                    for entry in Collection(self.graph, head):
                        if isinstance(entry, BNode):
                            self.graph.add((entry, RDF.type, member_class))
            else:
                kind = "value"
                entry = self.encode_value(value, scoped, vocabulary)
                self.graph.add((node, predicate, entry))
                object_class = {MLM.input_structure: MLM.InputStructure, MLM.result: MLM.ResultStructure}.get(predicate)
                if isinstance(entry, BNode) and object_class is not None:
                    self.graph.add((entry, RDF.type, object_class))
            self.graph.add((field, SER.kind, Literal(kind)))
        return node

    def one(self, node: Identifier, predicate: Identifier) -> Identifier:
        values = list(self.graph.objects(node, predicate))
        if len(values) != 1:
            raise ValueError(f"Expected exactly one {predicate} on {node}, found {len(values)}.")
        return values[0]

    def decode_list(self, head: Identifier, context: dict[str, Any], seen: frozenset[Identifier]) -> list[Any]:
        result = []
        visited: set[Identifier] = set()
        while head != RDF.nil:
            if head in visited:
                raise ValueError("Cyclic RDF list.")
            visited.add(head)
            result.append(self.decode_value(self.one(head, RDF.first), context, seen))
            head = self.one(head, RDF.rest)
        return result

    def decode_value(self, value: Identifier, context: dict[str, Any], seen: frozenset[Identifier]) -> Any:
        if isinstance(value, Literal):
            if value.datatype == RDF.JSON:
                return json.loads(str(value))
            decoded = value.toPython()
            if isinstance(decoded, Decimal):
                return float(decoded)
            if not isinstance(decoded, (str, int, float, bool)):
                raise TypeError(f"Unsupported RDF literal datatype: {value.datatype}")
            return decoded
        if (value, RDF.type, SER.Array) in self.graph:
            if value in seen:
                raise ValueError("Cyclic JSON array structure in RDF.")
            return self.decode_list(self.one(value, SER.items), context, seen | {value})
        if (value, RDF.type, SER.Object) in self.graph:
            return self.decode_object(value, context, seen)
        if isinstance(value, URIRef):
            for key in context:
                if not key.startswith("@") and expand(key, context) == str(value):
                    return key
            raise ValueError(f"Unmapped vocabulary value: {value}")
        raise ValueError(f"Unrecognized RDF value: {value}")

    def decode_object(
        self, node: Identifier, context: dict[str, Any], seen: frozenset[Identifier] = frozenset()
    ) -> dict[str, Any]:
        if node in seen:
            raise ValueError("Cyclic JSON object structure in RDF.")
        seen = seen | {node}
        obj: dict[str, Any] = {}
        known = {RDF.type, SER.field, SER.mapKey, MLM.datacube_variable_name, MLM.datacube_dimension_name}
        for field in self.graph.objects(node, SER.field):
            key = str(self.one(field, SER.key))
            if key in obj:
                raise ValueError(f"Duplicate JSON field: {key}")
            predicate, scoped, _ = mapping(key, context)
            known.add(predicate)
            if self.one(field, SER.predicate) != predicate:
                raise ValueError(f"Field {key!r} does not match its declared semantic predicate.")
            kind = str(self.one(field, SER.kind))
            if kind == "map":
                entries: dict[str, Any] = {}
                for child in self.graph.objects(node, predicate):
                    name = str(self.one(child, SER.mapKey))
                    if name in entries:
                        raise ValueError(f"Duplicate map key: {name}")
                    if key in ("cube:variables", "cube:dimensions"):
                        name_predicate = (
                            MLM.datacube_variable_name if key == "cube:variables" else MLM.datacube_dimension_name
                        )
                        if self.one(child, name_predicate) != Literal(name):
                            raise ValueError(f"Datacube map key {name!r} disagrees with its semantic name.")
                    entries[name] = self.decode_object(child, scoped, seen)
                obj[key] = entries
            elif kind == "null":
                if list(self.graph.objects(node, predicate)):
                    raise ValueError(f"Explicit null field {key!r} also has an RDF value.")
                obj[key] = None
            elif kind == "set":
                head = self.one(field, SER.items)
                entries = set(Collection(self.graph, head))
                if entries != set(self.graph.objects(node, predicate)):
                    raise ValueError(f"Field {key!r} order metadata disagrees with its semantic values.")
                obj[key] = self.decode_list(head, scoped, seen)
            else:
                values = [value for value in self.graph.objects(node, predicate) if value not in (SER.Object, SER.Item)]
                if len(values) != 1:
                    raise ValueError(f"Field {key!r} must have exactly one RDF value.")
                if kind == "array":
                    obj[key] = self.decode_list(values[0], scoped, seen)
                elif kind in ("json", "value"):
                    obj[key] = self.decode_value(values[0], scoped, seen)
                else:
                    raise ValueError(f"Unknown serialization field kind: {kind}")
        if set(self.graph.predicates(node)) - known:
            raise ValueError(f"Unrecorded RDF predicates on JSON object {node}.")
        return obj


def validate_graph(graph: Graph, block: Path) -> None:
    """
    Run the shared MLM SHACL constraints with the vocabulary closure.
    """
    ontology = block.parent / "mlm-ontology"
    closure = Graph().parse(ontology / "ontology.ttl", format="turtle")
    validation_data = graph + closure
    conforms, results, _ = validate(
        validation_data,
        shacl_graph=str(ontology / "shapes.shacl"),
        inference="none",
    )
    if not conforms:
        shacl = Namespace("http://www.w3.org/ns/shacl#")
        messages = sorted({str(message) for message in results.objects(None, shacl.resultMessage)})
        raise ValueError("MLM SHACL validation failed:\n" + "\n".join(messages))


def transform(data: str, direction: str, source_type: str, target_type: str, block: Path, assembled: Path) -> str:
    """
    Convert a validated Item to RDF or decode a validated reversible RDF graph.
    """
    source_type = source_type.split(";", 1)[0]
    target_type = target_type.split(";", 1)[0]
    codec = ItemRDF(load_context(block, assembled))
    if direction == "to-rdf":
        if target_type not in ("text/turtle", "application/ld+json"):
            raise ValueError(f"Unsupported RDF output media type: {target_type}")
        item = json.loads(data)
        json.dumps(item, allow_nan=False)
        validate_item(item)
        root = codec.encode_object(item, codec.context)
        codec.graph.add((root, RDF.type, SER.Item))
        validate_graph(codec.graph, block)
        output = codec.graph.serialize(format="json-ld" if target_type == "application/ld+json" else "turtle")
        decoded = json.loads(transform(output, "to-item", target_type, "application/json", block, assembled))
        if json.dumps(decoded, sort_keys=True) != json.dumps(item, sort_keys=True):
            raise ValueError("RDF serialization changed the Item's JSON values.")
        return output
    if direction != "to-item":
        raise ValueError(f"Unknown transform direction: {direction}")
    if source_type not in ("text/turtle", "application/ld+json"):
        raise ValueError(f"Unsupported RDF input media type: {source_type}")
    if source_type == "application/ld+json":
        document = json.loads(data)
        check_expanded_jsonld(document)
    codec.graph.parse(data=data, format="json-ld" if source_type == "application/ld+json" else "turtle")
    roots = list(codec.graph.subjects(RDF.type, SER.Item))
    if len(roots) != 1:
        raise ValueError("Expected exactly one reversible MLM serialization:Item root.")
    validate_graph(codec.graph, block)
    item = codec.decode_object(roots[0], codec.context)
    validate_item(item)
    return json.dumps(item, indent=2, allow_nan=False)


def check_expanded_jsonld(value: Any) -> None:
    """
    Require expanded JSON-LD so RDF decoding never fetches input-supplied contexts.
    """
    if isinstance(value, dict):
        if "@context" in value:
            raise ValueError("Use expanded JSON-LD without external or inline contexts.")
        for child in value.values():
            check_expanded_jsonld(child)
    elif isinstance(value, list):
        for child in value:
            check_expanded_jsonld(child)


runtime = globals().get("transform_metadata")
if runtime is not None:
    context = runtime.context
    output_data = transform(
        globals()["input_data"],
        runtime.metadata.direction,
        runtime.source_mime_type,
        runtime.target_mime_type,
        Path(context.bblock_files_path),
        Path(context.jsonld_context_path),
    )
elif __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validated MLM STAC Item / reversible RDF transforms.")
    parser.add_argument("direction", choices=["to-rdf", "to-item"])
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--context", type=Path, required=True, help="Assembled MLM context.jsonld from a bblocks build."
    )
    parser.add_argument("--rdf-format", choices=["turtle", "jsonld"], default="turtle")
    args = parser.parse_args()
    rdf_type = "application/ld+json" if args.rdf_format == "jsonld" else "text/turtle"
    if BLOCK is None:
        raise ValueError("Cannot determine the MLM block source directory.")
    result = transform(
        args.input.read_text(), args.direction, rdf_type, rdf_type, BLOCK, args.context
    )
    args.output.write_text(result)
