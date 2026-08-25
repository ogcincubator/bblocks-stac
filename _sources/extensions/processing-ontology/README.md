# STAC Processing Extension Ontology

This building block defines the **ontology** (RDF vocabulary) for the elements introduced by the
[STAC Processing extension](https://github.com/stac-extensions/processing).

## Purpose

To provide Linked Data support for the STAC Processing extension by giving each `processing:*` field a
resolvable term with a definition, so that STAC data mapped through the extension's JSON-LD context can
be interpreted as RDF.

## Scope

Describes **only** the elements the Processing extension itself adds:

- `processing:expression` — the processing chain/expression that produced the data
- `processing:lineage` — free-text lineage information
- `processing:level` — the processing level
- `processing:facility` — the producing facility
- `processing:datetime` — processing date/time (RFC 3339, UTC)
- `processing:version` — version of the processing software/chain
- `processing:software` — name/version map of software involved

STAC Item, Collection and Asset — and their core fields (`id`, `description`, `datetime`, `assets`,
`links`, …) — are defined by the STAC **core** vocabulary and are **reused, not redefined**, here. The
Processing schema block inherits them via its `bblocks://ogc.contrib.stac.item` and
`bblocks://ogc.contrib.stac.collection` imports, and re-describing them here would break that traceable
reuse.

Source of definitions: <https://github.com/stac-extensions/processing> (v1.2.0).
