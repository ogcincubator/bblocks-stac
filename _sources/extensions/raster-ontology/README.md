# STAC Raster Extension Ontology

This building block defines the **ontology** (RDF vocabulary) for the elements introduced by the
[STAC Raster extension](https://github.com/stac-extensions/raster).

## Purpose

To provide Linked Data support for the STAC Raster extension by giving each `raster:*` field a resolvable
term with a definition, so that STAC data mapped through the extension's JSON-LD context can be
interpreted as RDF.

## Scope

Describes **only** the elements the Raster extension itself adds (v2.0.0 — data type, unit and nodata
moved to STAC common metadata's `bands` object in this version and are **not** raster-specific anymore):

- `raster:sampling` — area vs. point pixel sampling, a fixed 2-value enumeration
- `raster:bits_per_sample`, `raster:spatial_resolution`, `raster:scale`, `raster:offset`
- `raster:histogram` and the **Histogram Object** (`count`, `min`, `max`, `buckets`)

All of these apply to a **Band object** (the `bands` array of STAC common metadata, shared with the EO and
Classification extensions) — a structure this ontology does not itself define, since it is not the Raster
extension's own concept; no `rdfs:domain` is asserted for them.

## SKOS vs. OWL

`raster:sampling` is a fixed, extension-defined enumeration (`area` / `point`) and is modeled as a
`skos:ConceptScheme` (`raster:SamplingScheme`) with one `skos:Concept` per value — see `skos.ttl`. The
remaining fields and the `raster:Histogram` class are plain OWL — see `owl.ttl`.

## File layout

- `skos.ttl` — `raster:SamplingScheme` and its two members.
- `owl.ttl` — the `raster:*` properties and `raster:Histogram`.
- `ontology.ttl` — the combined file (the one the register tooling loads/publishes).

Source of definitions: <https://github.com/stac-extensions/raster> (v2.0.0).
