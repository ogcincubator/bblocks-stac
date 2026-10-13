# MLM STAC Item / RDF transforms

The Python transforms `item-to-rdf` and `rdf-to-item` convert **STAC Items**, not Collections or Catalogs.
They target MLM 1.6.0 using the official `stac-model` 0.7.0 package and require Python 3.11 or newer.

`item-to-rdf` accepts `application/geo+json` and produces Turtle or expanded JSON-LD.
`rdf-to-item` accepts the **reversible Item RDF profile** produced by the first transform and returns
STAC JSON. Their RDF media types carry the profile parameter
`profile="https://w3id.org/ogc/stac/mlm/serialization/"` to distinguish them from ordinary JSON-LD
uplift. This also prevents the postprocessor from applying the inverse transform to lossy,
automatically uplifted documentation snippets.

## Preservation guarantees

The transforms preserve JSON values, rather than whitespace or object-key ordering:

- Input/output order, tensor shapes and dimension order, channel references, scaling operations, and
  all other JSON arrays retain their order, duplicate entries, and empty-array representation.
- Explicit `null` remains distinguishable from an omitted field. This includes no required
  accelerator, no pretraining source, no resizing or scaling, no pre/post-processing, and nulls in
  other extension metadata. The upstream JSON schemas still determine where null is allowed.
- Asset dictionary keys, Datacube variable/dimension keys, empty objects, geometry, relative hrefs,
  and metadata from other extensions remain intact.
- Floating-point values round-trip without Turtle's default float formatting reducing their precision.
  The transform uses exact lexical `xsd:decimal` literals and reconstructs JSON floating-point numbers.

Known fields reuse the block's assembled context and local extension contexts: MLM, STAC Core,
EO, Raster, Datacube, Classification, Processing, Version, Scientific, File, ML-AOI, Application,
VCS, and the other locally available extension mappings. Unknown fields are retained under the
serialization vocabulary; no domain meaning is invented for them.

## RDF representation

The ordinary MLM context now maps ordered input/output, band/variable, task, and scaling arrays to
RDF lists. Query their members using `rdf:rest*/rdf:first`, not as unordered predicate objects.
The MLM ontology and SHACL paths reflect this representation.

The reversible profile adds small field descriptors to semantic RDF objects. They record each JSON
field's original key, predicate, and representation kind. **There is no hidden copy of the complete
source Item**: the inverse reads the current semantic values. For example, changing `mlm:name` in the
RDF changes the decoded model name.

Ordered predicates use RDF lists directly. For inherited predicates whose mappings are unordered,
the field descriptor supplies an ordered list of the **same value nodes**; the decoder checks that
its membership agrees with the semantic triples. This preserves order without redefining imported
vocabularies. Assets and Datacube definitions also retain their dictionary keys.

A field with explicit null has `serialization:kind "null"` and no semantic value triple. Null
elements in general arrays use `"null"^^rdf:JSON`. Neither is conflated with an omitted field.
The structural STAC `properties` object is retained as a separate object in this profile, rather
than erased by JSON-LD `@nest`; its MLM and Datacube fields share the same resource.

The supporting vocabulary is published as a resource of this block:
[serialization.ttl](../mlm-ontology/serialization.ttl). It is an implementation vocabulary, **not**
an addition to the upstream MLM JSON fields. Ordinary uplifted RDF cannot recover dropped nulls,
map keys, or original ordering and is rejected by the inverse rather than guessed into an Item.

## Validation

Both directions validate the original/reconstructed document with `stac-model`'s Pydantic models and
PySTAC's official STAC Core and declared extension JSON schemas. Model objects are used for validation
only: their serializers do not rewrite the source, reorder sets, insert defaults, or drop nulls.
Schema retrieval follows PySTAC's normal online/cache behavior.

`stac-model` 0.7.0's nested classification adapter rejects some schema-valid classification metadata
such as `title` and array-valued `color_hint`. Classification fields are excluded only from that
adapter's validation projection, not from the Item or RDF. Official JSON Schema validation remains
active for the complete document and its declared Classification extension.

Shared MLM SHACL adds variable-name resolution against Item/Asset Datacube definitions, variable
dimension resolution, and model-artifact role checks. Malformed lists, inconsistent field metadata,
duplicate map keys, cyclic structures, and missing or multiple Item roots are rejected explicitly.
Band-name cross-reference resolution is not yet covered by the shared SHACL rules; EO/Raster metadata
is nevertheless preserved and its declared schemas are validated.

Every forward transform verifies its inverse **after RDF serialization and parsing**. Automated tests
also cover both directions through the bblocks execution interface, Turtle/JSON-LD graph equivalence,
the pinned Resoterre U-Net, all upstream Item examples, and negative schema/SHACL cases.

## Running from a source checkout

Build the MLM block's assembled context first. The postprocessor supplies its path and the block's
source path through `transform_metadata.context`; executable dependencies are declared in
`transforms.yaml`. Use a Python 3.11+ postprocessor environment. A Python 3.10 Docker image cannot
install `stac-model` 0.7.0.

For direct execution in the `resoterre` conda environment:

```sh
UNET_ITEM=/path/to/unet_rdps_to_hrdps.json

conda run -n resoterre python _sources/extensions/mlm/transforms/item_rdf.py \
  to-rdf "$UNET_ITEM" /tmp/unet.ttl \
  --context build-local/annotated/contrib/stac/extensions/mlm/context.jsonld

conda run -n resoterre python _sources/extensions/mlm/transforms/item_rdf.py \
  to-item /tmp/unet.ttl /tmp/unet.json \
  --context build-local/annotated/contrib/stac/extensions/mlm/context.jsonld

conda run -n resoterre python -m unittest discover -s tests -p test_mlm_transforms.py
```

Use `--rdf-format jsonld` on both commands to select expanded JSON-LD instead of Turtle.
For the U-Net, use the original JSON from the pinned example reference. Tests fetch that exact
document: some postprocessor documentation renderers pass JSON through YAML and can turn scientific
notation such as `1e-05` into strings. The transforms operate on the original JSON, not that rendering.
