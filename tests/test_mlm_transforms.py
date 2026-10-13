from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from urllib.request import urlopen

from pystac.errors import STACValidationError
from rdflib import RDF, Graph, Literal
from rdflib.collection import Collection
from rdflib.compare import isomorphic

ROOT = Path(__file__).resolve().parents[1]
BLOCK = ROOT / "_sources/extensions/mlm"
CONTEXT = ROOT / "build-local/annotated/contrib/stac/extensions/mlm/context.jsonld"
EXAMPLES = ROOT / "build-local/tests/contrib/stac/extensions/mlm"
SCRIPT = BLOCK / "transforms/item_rdf.py"
UNET_URL = (
    "https://raw.githubusercontent.com/Ouranosinc/resoterre/0.1.3-dev.10/"
    "notebooks/ml-model-package/unet_rdps_to_hrdps/unet_rdps_to_hrdps.json"
)
SPEC = importlib.util.spec_from_file_location("mlm_item_rdf", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
CODEC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CODEC)


class MLMTransformsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """
        Tests use built contexts and the original pinned Resoterre JSON document.
        """
        example = next(
            (path for path in EXAMPLES.glob("example_11_1.*") if path.suffix in (".json", ".geojson")), None
        )
        if example is None or not CONTEXT.exists():
            raise RuntimeError("Build the MLM block's examples and assembled context before running these tests.")
        with urlopen(UNET_URL, timeout=30) as response:
            cls.unet = json.load(response)

    def convert(self, item: dict, media_type: str = "text/turtle") -> tuple[str, dict]:
        rdf = CODEC.transform(json.dumps(item), "to-rdf", "application/geo+json", media_type, BLOCK, CONTEXT)
        decoded = CODEC.transform(rdf, "to-item", media_type, "application/json", BLOCK, CONTEXT)
        return rdf, json.loads(decoded)

    def test_unet_round_trip(self) -> None:
        """
        Tests exact Item values and graph equivalence through both RDF encodings.
        """
        for media_type, rdf_format in (("text/turtle", "turtle"), ("application/ld+json", "json-ld")):
            with self.subTest(media_type=media_type):
                rdf, decoded = self.convert(self.unet, media_type)
                self.assertEqual(decoded, self.unet)
                self.assertEqual(json.dumps(decoded, sort_keys=True), json.dumps(self.unet, sort_keys=True))
                rerendered, _ = self.convert(decoded, media_type)
                original_graph = Graph().parse(data=rdf, format=rdf_format)
                restored_graph = Graph().parse(data=rerendered, format=rdf_format)
                self.assertTrue(isomorphic(original_graph, restored_graph))

    def test_order_null_and_empty_values(self) -> None:
        """
        Tests channel and interface order, explicit nulls, and absent versus empty fields.
        """
        item = copy.deepcopy(self.unet)
        props = item["properties"]
        props["mlm:input"].reverse()
        props["mlm:accelerator"] = None
        props["mlm:pretrained_source"] = None
        input_obj = props["mlm:input"][1]
        input_obj["variables"].reverse()
        input_obj["resize_type"] = None
        input_obj["value_scaling"] = None
        input_obj["pre_processing_function"] = [
            {"format": "test", "expression": {"operation": "first"}},
            {"format": "test", "expression": {"operation": "second"}},
        ]
        props["mlm:output"].append(copy.deepcopy(props["mlm:output"][0]))
        props["mlm:output"][1]["name"] = "second_output"
        props["mlm:output"].reverse()
        props["custom:payload"] = {"null": None, "empty": [], "object": {}, "nested": [[1, None], [], [1]]}
        for media_type in ("text/turtle", "application/ld+json"):
            with self.subTest(media_type=media_type):
                _, decoded = self.convert(item, media_type)
                self.assertEqual(decoded, item)
                self.assertNotIn("value_scaling", decoded["properties"]["mlm:input"][0])
                self.assertEqual(decoded["properties"]["mlm:input"][1]["bands"], [])

    def test_upstream_items(self) -> None:
        """
        Tests the same converters against every built upstream MLM Item.
        """
        for path in sorted(EXAMPLES.iterdir()):
            if path.suffix not in (".json", ".geojson"):
                continue
            item = json.loads(path.read_text())
            if item.get("type") == "Feature":
                with self.subTest(example=path.name):
                    _, decoded = self.convert(item)
                    self.assertEqual(decoded, item)

    def test_semantic_edit_is_decoded(self) -> None:
        """
        Tests that RDF values, rather than an embedded source snapshot, drive JSON output.
        """
        rdf, _ = self.convert(self.unet)
        graph = Graph().parse(data=rdf, format="turtle")
        model = next(graph.subjects(CODEC.MLM.name, None))
        graph.set((model, CODEC.MLM.name, Literal("Updated semantic model name")))
        decoded = json.loads(
            CODEC.transform(graph.serialize(), "to-item", "text/turtle", "application/json", BLOCK, CONTEXT)
        )
        self.assertEqual(decoded["properties"]["mlm:name"], "Updated semantic model name")

    def test_invalid_mlm_fields(self) -> None:
        """
        Tests rejection by official model and schema validators without coercing the source.
        """
        for field, value in (("mlm:name", ""), ("mlm:pretrained", "false"), ("mlm:total_parameters", -1)):
            with self.subTest(field=field):
                item = copy.deepcopy(self.unet)
                item["properties"][field] = value
                with self.assertRaises((ValueError, STACValidationError)):
                    self.convert(item)

    def test_cross_reference_failures(self) -> None:
        """
        Tests graph constraints on references that remain structurally valid JSON.
        """
        for mutation, message in (
            ("variable", "Every MLM variable reference"),
            ("variable-object", "Every MLM variable reference"),
            ("dimension", "Every dimension named"),
            ("role", "mlm:model role"),
        ):
            with self.subTest(mutation=mutation):
                item = copy.deepcopy(self.unet)
                props = item["properties"]
                if mutation == "variable":
                    props["mlm:input"][0]["variables"][0] = "missing-variable"
                elif mutation == "variable-object":
                    props["mlm:input"][0]["variables"][0] = {"name": "missing-variable"}
                elif mutation == "dimension":
                    props["cube:variables"]["PR"]["dimensions"].append("missing-dimension")
                else:
                    next(asset for asset in item["assets"].values() if "mlm:artifact_type" in asset)["roles"] = ["data"]
                codec = CODEC.ItemRDF(CODEC.load_context(BLOCK, CONTEXT))
                codec.encode_object(item, codec.context)
                with self.assertRaisesRegex(ValueError, message):
                    CODEC.validate_graph(codec.graph, BLOCK)
                with self.assertRaises((ValueError, STACValidationError)):
                    self.convert(item)

    def test_wrong_scope_and_lossy_graph(self) -> None:
        """
        Tests explicit refusal of Collections and graphs lacking reversible structure.
        """
        with self.assertRaisesRegex(ValueError, "Items only"):
            CODEC.validate_item({"type": "Collection"})
        with self.assertRaisesRegex(ValueError, "serialization:Item root"):
            CODEC.transform(
                "<urn:model> <urn:name> \"example\" .", "to-item", "text/turtle", "application/json", BLOCK, CONTEXT
            )

    def test_bblocks_execution_interface(self) -> None:
        """
        Tests execution without __file__ through the Python transform metadata interface.
        """
        context = SimpleNamespace(bblock_files_path=str(BLOCK), jsonld_context_path=str(CONTEXT))
        namespace = {
            "input_data": json.dumps(self.unet),
            "transform_metadata": SimpleNamespace(
                context=context,
                metadata=SimpleNamespace(direction="to-rdf"),
                source_mime_type="application/geo+json",
                target_mime_type="text/turtle",
            ),
        }
        exec(compile(SCRIPT.read_text(), str(SCRIPT), "exec"), namespace)  # noqa: S102
        result = json.loads(
            CODEC.transform(namespace["output_data"], "to-item", "text/turtle", "application/json", BLOCK, CONTEXT)
        )
        self.assertEqual(result, self.unet)
        namespace = {
            "input_data": namespace["output_data"],
            "transform_metadata": SimpleNamespace(
                context=context,
                metadata=SimpleNamespace(direction="to-item"),
                source_mime_type="text/turtle",
                target_mime_type="application/json",
            ),
        }
        exec(compile(SCRIPT.read_text(), str(SCRIPT), "exec"), namespace)  # noqa: S102
        self.assertEqual(json.loads(namespace["output_data"]), self.unet)

    def test_original_upstream_variable_mismatch(self) -> None:
        """
        Tests rejection of the original upstream temperature-variable spelling mismatch.
        """
        item = json.loads((EXAMPLES / "example_4_1.geojson").read_text())
        variables = item["properties"]["cube:variables"]
        variables["2m_temperature"] = variables.pop("temperature_2m")
        with self.assertRaisesRegex(ValueError, "Every MLM variable reference"):
            self.convert(item)

    def test_asset_datacube_and_variable_objects(self) -> None:
        """
        Tests references to Datacube definitions on an attached model asset.
        """
        item = copy.deepcopy(self.unet)
        props = item["properties"]
        asset = next(asset for asset in item["assets"].values() if "mlm:artifact_type" in asset)
        for key in ("cube:variables", "cube:dimensions"):
            asset[key] = props.pop(key)
        asset["mlm:architecture"] = props["mlm:architecture"]
        props["mlm:input"][0]["variables"][0] = {
            "name": props["mlm:input"][0]["variables"][0],
            "format": "test",
            "expression": {"operation": "identity"},
        }
        _, decoded = self.convert(item)
        self.assertEqual(decoded, item)

    def test_float_precision_and_scaling_order(self) -> None:
        """
        Tests lossless numeric RDF literals and ordered normalization steps.
        """
        item = copy.deepcopy(self.unet)
        item["properties"]["custom:floats"] = [1.2345678901234567, 1e-300, 1e300, 1.0]
        item["properties"]["mlm:input"][0]["value_scaling"] = [
            {"type": "offset", "value": 1.2345678901234567},
            {"type": "scale", "value": 2.0},
        ]
        for media_type in ("text/turtle", "application/ld+json"):
            with self.subTest(media_type=media_type):
                _, decoded = self.convert(item, media_type)
                self.assertEqual(decoded, item)

    def test_corrupt_rdf_list(self) -> None:
        """
        Tests refusal of cyclic ordered channels rather than inventing an order.
        """
        rdf, _ = self.convert(self.unet)
        graph = Graph().parse(data=rdf, format="turtle")
        head = next(
            value for value in graph.objects(None, CODEC.MLM.variables)
            if value != RDF.nil and len(Collection(graph, value)) == 14
        )
        cells = list(Collection(graph, head))
        self.assertEqual(len(cells), 14)
        graph.set((head, RDF.rest, head))
        codec = CODEC.ItemRDF(CODEC.load_context(BLOCK, CONTEXT))
        codec.graph = graph
        with self.assertRaisesRegex(ValueError, "Cyclic RDF list"):
            codec.decode_object(next(graph.subjects(RDF.type, CODEC.SER.Item)), codec.context)


if __name__ == "__main__":
    unittest.main()
