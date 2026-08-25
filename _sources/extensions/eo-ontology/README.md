# STAC Electro-Optical Extension Ontology

This building block defines the **ontology** (RDF vocabulary) for the elements introduced by the
[STAC Electro-Optical (EO) extension](https://github.com/stac-extensions/eo).

## Purpose

To provide Linked Data support for the STAC EO extension by giving each `eo:*` field a resolvable term
with a definition, so that STAC data mapped through the extension's JSON-LD context can be interpreted as
RDF.

## Scope

Describes **only** the elements the EO extension itself adds:

- `eo:cloud_cover`, `eo:snow_cover` — percentage cover estimates (Item/Collection)
- `eo:common_name` — a band's common spectral name, drawn from a fixed vocabulary
- `eo:center_wavelength`, `eo:full_width_half_max`, `eo:solar_illumination` — band optical properties

`eo:common_name`, `eo:center_wavelength`, `eo:full_width_half_max` and `eo:solar_illumination` apply to a
**Band object** (the `bands` array of STAC common metadata, shared with the Raster and Classification
extensions) — a structure this ontology does not itself define, since it is not the EO extension's own
concept; no `rdfs:domain` is asserted for them. STAC Item and Collection are defined by the STAC **core**
vocabulary and are **reused, not redefined**, here.

## SKOS vs. OWL

`eo:common_name` is a **fixed, extension-defined enumeration** (unlike `classification:classes`, which is
dataset-specific) — the extension's README publishes a closed table of 20 names with their wavelength
ranges. It is modeled as a proper `skos:ConceptScheme` (`eo:CommonBandNameScheme`) with one `skos:Concept`
per allowed value (`skos:notation` = the enum string, `skos:prefLabel`/`skos:definition` from the table)
— see `skos.ttl`. The remaining `eo:*` fields are plain numeric OWL datatype properties — see `owl.ttl`.

## File layout

- `skos.ttl` — `eo:CommonBandNameScheme` and its 20 members.
- `owl.ttl` — the `eo:*` datatype properties.
- `ontology.ttl` — the combined file (the one the register tooling loads/publishes).

Source of definitions: <https://github.com/stac-extensions/eo> (v2.0.0), including the Common Band Names
table.
