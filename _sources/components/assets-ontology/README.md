# STAC Asset Component Ontology

This building block defines the **ontology** (RDF vocabulary) for the STAC **Asset Object** component
used by Items and Collections (`_sources/components/assets`).

## Purpose

To provide Linked Data support for the Asset Object by giving its one field with no existing reusable
term — `roles` — a resolvable vocabulary, so that STAC data mapped through the assets component's
JSON-LD context can be interpreted as RDF.

## Scope

The Asset Object has five fields. Four are already fully covered by reuse and mint nothing new here:

- `href` → JSON-LD `@id` (the asset's own identity, not a predicate)
- `title` → `dct:title` (reused)
- `description` → `dct:description` (reused)
- `type` → `dct:format` (reused; an IANA media type)

Only `roles` needed a term of its own: `assets:roles`.

`stac:Asset` and `stac:hasAsset` are defined by the STAC **core** ontology (`core-ontology` block) and are
reused as this property's domain/range context, not redefined here.

## SKOS vs. OWL

`roles` draws its recommended values from the STAC specification's own best-practices documentation
("Asset Roles"), but that list is explicitly **not closed** — an asset may carry other, custom roles. It
is therefore modeled the same way as `mlm:framework`: a `skos:ConceptScheme`
(`assets:AssetRoleScheme`) marked non-exhaustive, in `skos.ttl`. `assets:roles` itself, the property that
carries these values, is plain OWL — see `owl.ttl`.

## A note on `stac:roles`

The assets component's `context.jsonld` previously mapped the JSON `roles` key to `stac:roles` — a term
that was never actually defined in the STAC core ontology (the same class of dangling-reference bug found
elsewhere in this register, e.g. the pre-fix `osc`/`themes` context). This block fixes that by minting
`assets:roles` and repointing the context at it, rather than adding an undefined term to `core-ontology`
(kept out of scope here — `roles` is specifically an Asset Object concern).

## File layout

- `skos.ttl` — `assets:AssetRoleScheme` and its members.
- `owl.ttl` — `assets:roles`.
- `ontology.ttl` — the combined file (the one the register tooling loads/publishes).

Source of definitions: <https://github.com/radiantearth/stac-spec> — `commons/assets.md` (Asset Object
field table) and `best-practices.md` (Asset Roles table).
