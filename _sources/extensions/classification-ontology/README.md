# STAC Classification Extension Ontology

This building block defines the **ontology** (RDF vocabulary) for the elements introduced by the
[STAC Classification extension](https://github.com/stac-extensions/classification).

## Purpose

To provide Linked Data support for the STAC Classification extension by giving each `classification:*`
field a resolvable term with a definition, so that STAC data mapped through the extension's JSON-LD
context can be interpreted as RDF.

## Scope

Describes **only** the elements the Classification extension itself adds:

- `classification:classes` — a codelist of coded data classes (Class Objects)
- `classification:bitfields` — bit fields whose bit combinations represent classes
- The **Class Object**: `value`, `name`, `title`, `description`, `color_hint`, `nodata`, `percentage`,
  `count`
- The **Bit Field Object**: `offset`, `length`, `classes`, `roles`, `name`, `description`

STAC Item, Collection and Asset are defined by the STAC **core** vocabulary and are **reused, not
redefined**, here.

## SKOS vs. OWL

Each `classification:classes` entry is exactly the pattern SKOS is designed for — a coded value with a
notation, a preferred label, and a definition — so `classification:Class` is modeled as a `skos:Concept`
subclass, with `value` → `skos:notation`, `name` → `skos:altLabel`, `title` → `skos:prefLabel`,
`description` → `skos:definition` (see `skos.ttl`). The extension mints no fixed, extension-wide concept
scheme: every dataset defines its own classes, so no `skos:ConceptScheme` individual is asserted — only
the class-level alignment.

The codelist containers (`classes`, `bitfields`), `classification:BitField`, and the per-class statistics
(`color_hint`, `nodata`, `percentage`, `count`, `offset`, `length`, `roles`) carry no SKOS meaning of their
own and stay plain OWL properties/classes (see `owl.ttl`).

## File layout

- `skos.ttl` — `classification:Class` and its lexical properties.
- `owl.ttl` — codelist containers, `classification:BitField`, and per-class statistics.
- `ontology.ttl` — the combined file (the one the register tooling loads/publishes).

Source of definitions: <https://github.com/stac-extensions/classification> (v2.0.0).
