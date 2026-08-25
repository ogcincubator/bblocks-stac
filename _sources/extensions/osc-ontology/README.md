# STAC ESA Open Science Catalog (OSC) Extension Ontology

This building block defines the **ontology** (RDF vocabulary) for the elements introduced by the
[STAC OSC extension](https://github.com/stac-extensions/osc).

## Purpose

To provide Linked Data support for the STAC OSC extension by giving each `osc:*` field a resolvable term
with a definition, so that STAC data mapped through the extension's JSON-LD context can be interpreted as
RDF.

## Retrofit note

This block replaces an earlier, broken placeholder version: the previous `ontology.ttl` declared its
`owl:Ontology` IRI as `https://w3id.org/ogc/stac/core/` — a copy of the STAC **core** ontology namespace —
and described none of the OSC extension's own elements. This version uses OSC's own namespace
(`https://w3id.org/ogc/stac/osc/`) and describes only what the extension itself adds.

The `osc` schema block's `context.jsonld` had also been copy-pasted from the `themes` schema block (it
mapped `thns:*` themes terms, which OSC's JSON Schema does not define). That has been replaced with a
correct mapping of OSC's own fields — see the `osc` schema block.

## Scope

Describes **only** the elements the OSC extension itself adds:

- `osc:type` — `project` or `product`, a fixed 2-value enumeration
- `osc:status` — `planned` / `ongoing` / `completed`, a fixed 3-value enumeration
- `osc:project`, `osc:region`, `osc:experiment` — free-text identifiers
- `osc:variables`, `osc:missions`, `osc:workflows` — free-text lists (not extension-defined controlled
  vocabularies, so kept as plain OWL, not SKOS)

STAC Item, Collection and Catalog are defined by the STAC **core** vocabulary and are reused, not
redefined, here.

## SKOS vs. OWL

`osc:type` and `osc:status` are fixed, extension-defined enumerations and are modeled as
`skos:ConceptScheme`s (`osc:ResourceTypeScheme`, `osc:StatusScheme`) — see `skos.ttl`. The remaining
fields are free text with no extension-defined controlled list, so they stay plain OWL datatype
properties — see `owl.ttl`.

## File layout

- `skos.ttl` — `osc:ResourceTypeScheme` and `osc:StatusScheme`.
- `owl.ttl` — the free-text `osc:*` datatype properties.
- `ontology.ttl` — the combined file (the one the register tooling loads/publishes).

Source of definitions: <https://github.com/stac-extensions/osc> (v1.0.0).
