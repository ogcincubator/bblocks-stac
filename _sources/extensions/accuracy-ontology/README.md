# STAC Accuracy Extension Ontology

This building block defines the **ontology** (RDF vocabulary) for the elements introduced by the
[STAC Accuracy extension](https://github.com/stac-extensions/accuracy).

## Purpose

To provide Linked Data support for the STAC Accuracy extension by giving each `accuracy:*` field a
resolvable term with a definition, so that STAC data mapped through the extension's JSON-LD context can
be interpreted as RDF.

## Scope

Describes **only** the elements the Accuracy extension itself adds:

- `accuracy:geometric_x_bias`, `accuracy:geometric_y_bias` — geometric bias estimates
- `accuracy:geometric_x_stddev`, `accuracy:geometric_y_stddev` — geometric standard deviations
- `accuracy:geometric_rmse` — radial root mean square error, in meters
- `accuracy:measurement_relative`, `accuracy:measurement_absolute` — measurement uncertainty

STAC Item, Collection and Asset — and their core fields — are defined by the STAC **core** vocabulary and
are **reused, not redefined**, here. The Accuracy schema block inherits them via its
`bblocks://ogc.contrib.stac.item` and `bblocks://ogc.contrib.stac.collection` imports.

## File layout

- `owl.ttl` — the `accuracy:*` datatype properties (OWL component).
- `skos.ttl` — intentionally empty. The extension defines no enumerated/controlled values, so there is no
  SKOS component to mint. Kept as a placeholder for layout consistency with sibling ontology blocks and as
  the obvious place to add one if a future extension version introduces an enumeration.
- `ontology.ttl` — the combined file (the one the register tooling loads/publishes), currently equal to
  `owl.ttl`.

Source of definitions: <https://github.com/stac-extensions/accuracy> (v1.0.0-beta.1).
