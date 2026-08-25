# STAC Machine Learning Model (MLM) Extension Ontology

This building block defines the **ontology** (RDF vocabulary) for the elements introduced by the
[STAC MLM extension](https://github.com/stac-extensions/mlm).

## Purpose

To provide Linked Data support for the STAC MLM extension by giving each `mlm:*` field, and the
ModelInput/ModelOutput/InputStructure/ResultStructure/ValueScaling structures it defines, a resolvable
term with a definition, so that STAC data mapped through the extension's JSON-LD context can be
interpreted as RDF.

## Scope

Describes **only** the elements the MLM extension itself adds: model identity (`mlm:name`,
`mlm:architecture`), task/framework/accelerator requirements, `mlm:input`/`mlm:output` and their nested
structures. STAC Item and Collection are defined by the STAC **core** vocabulary and are reused, not
redefined.

Two deliberate reuses instead of redefinitions:

- `ModelOutput`'s `classification:classes` field reuses the **STAC Classification extension**'s own term
  (already an MLM dependency) — MLM does not mint a second definition of it.
- `mlm:pre_processing_function` / `mlm:post_processing_function` are declared
  `rdfs:subPropertyOf processing:expression` (**STAC Processing extension**) to record that they share its
  Expression Object shape, without literally being the same JSON property.

A few JSON field names collide across nested object types (`name`/`description` appear on both
ModelInput and ModelOutput; `input` names both the top-level field and ModelInput's own required
sub-object; `value`/`type` on ValueScaling are too generic to mint bare). These are minted under
distinguishing local names (`mlm:io_name`, `mlm:io_description`, `mlm:input_structure`, `mlm:scaling_type`,
`mlm:scaling_value`) — see the `rdfs:comment` on each for the JSON key it maps from.

## SKOS vs. OWL

Five MLM fields are genuine (mostly closed) enumerations and are modeled as `skos:ConceptScheme`s in
`skos.ttl`: `mlm:TaskScheme`, `mlm:AcceleratorScheme`, `mlm:ResizeTypeScheme` and
`mlm:ValueScalingTypeScheme` are closed; `mlm:FrameworkScheme` is marked non-exhaustive because the
extension also accepts free-text framework names. `mlm:dim_order` lists common values in a comment but is
**not** modeled as SKOS, since the extension does not close that list. Everything else — model metadata,
the ModelInput/ModelOutput/InputStructure/ResultStructure/ValueScaling classes and their non-enumerated
properties — is plain OWL, in `owl.ttl`.

## File layout

- `skos.ttl` — the five concept schemes above.
- `owl.ttl` — the `mlm:*` properties and classes.
- `ontology.ttl` — the combined file (the one the register tooling loads/publishes).

Source of definitions: <https://github.com/stac-extensions/mlm> (v1.5.2).
