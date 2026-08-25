# STAC Themes Extension Ontology

This building block defines the **ontology** (RDF vocabulary) for the elements introduced by the
[STAC Themes extension](https://github.com/stac-extensions/themes).

## Purpose

To provide Linked Data support for the STAC Themes extension by giving each `thns:*` term a resolvable
definition, so that STAC data mapped through the extension's JSON-LD context can be interpreted as RDF.

## Background

This closes a gap flagged during a register-wide dependency sweep: `https://w3id.org/ogc/stac/themes/`
was already used by the `themes` and `osc` schema blocks' `context.jsonld`, and by
`themes-shacl/transforms/dcat-themes.ttl`'s SPARQL rules, but no ontology block defined those terms. This
block is that definition; the term IRIs already in use (`thns:id`, `thns:name`, `thns:concepts`,
`thns:scheme`, `thns:schemes`) are **preserved as-is** rather than renamed, so existing consumers keep
working.

## Scope

Describes the Themes extension's own structure:

- `thns:schemes` — relates a STAC resource to a Theme (JSON key: `themes`)
- The **Theme Object**: `thns:scheme` (the KOS identifier) and `thns:concepts`
- The **Concept Object**: `thns:id`, `thns:name` (maps the spec's `title` field — see note below),
  `thns:description`, and `url` (mapped to `@id` in context, not a separate term)

STAC Item, Collection and Catalog are defined by the STAC **core** vocabulary and are reused, not
redefined, here.

**Note on `thns:name`:** the STAC Themes v1.0.0 JSON Schema names this field `title`, not `name`. The
existing `context.jsonld` files mapped a non-existent JSON key `"name"`, meaning the real `title` field was
never uplifted — this ontology's release also **fixes that context mapping** (see the `themes` and `osc`
schema blocks) to map `title` → `thns:name`, and adds a mapping for the previously-unmapped `description`
field. The RDF term stays `thns:name` for compatibility with existing consumers.

## SKOS vs. OWL

A Concept Object is exactly a SKOS concept reference (id/notation, title/label, description/definition),
so `thns:Concept` is a `skos:Concept` subclass with `id` → `skos:notation`, `name` → `skos:prefLabel`,
`description` → `skos:definition` — see `skos.ttl`. `thns:Theme` and the structural properties
(`schemes`, `scheme`, `concepts`) stay plain OWL — see `owl.ttl`. `thns:Theme` is **not** declared
`rdfs:subClassOf skos:ConceptScheme`, even though it plays that role conceptually, because `thns:scheme`
must stay a plain string (not an IRI) for compatibility with the existing `themes-shacl` SPARQL rules,
which `CONCAT` it as text.

## File layout

- `skos.ttl` — `thns:Concept` and its lexical properties.
- `owl.ttl` — `thns:Theme` and the structural properties.
- `ontology.ttl` — the combined file (the one the register tooling loads/publishes).

Source of definitions: <https://github.com/stac-extensions/themes> (v1.0.0).
