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

`mlm:input` and `mlm:output` link a STAC Item or Collection to its `mlm:ModelInput` and
`mlm:ModelOutput` descriptions. Within those descriptions, `mlm:bands` contains ordered names or
references to the corresponding STAC Asset band metadata. Those referenced band definitions may use
STAC common metadata and the EO and Raster extension fields. Likewise, `mlm:variables` contains
ordered keys into the applicable Datacube `cube:variables` map; those variable definitions may refer
to `cube:dimensions`. These are reference relationships, not `owl:equivalentProperty` relationships:
the MLM fields identify which bands or variables the model consumes or produces, while the other
extensions describe those data objects.

## Interaction graph

The following graph shows the intended traversal through an MLM resource and the related STAC
extensions. A string in `mlm:bands` or `mlm:variables` is a name lookup; an object entry is
represented by `mlm:BandVariableReference`.

```text
STAC Item / Collection
├── mlm:name, mlm:architecture, mlm:tasks, mlm:framework, ...
├── mlm:input ───────────────► mlm:ModelInput
│                              ├── mlm:io_name / mlm:io_description
│                              ├── mlm:bands ───────► STAC Asset band metadata
│                              │                       ├── STAC common band fields
│                              │                       ├── eo:common_name, eo:center_wavelength
│                              │                       └── raster:* band fields
│                              ├── mlm:variables ───► cube:variables entry
│                              │                       └── cube:dimensions
│                              ├── mlm:input_structure
│                              ├── mlm:value_scaling ─► mlm:ValueScaling
│                              ├── mlm:resize_type
│                              └── mlm:pre_processing_function
├── mlm:output ──────────────► mlm:ModelOutput
│                              ├── mlm:io_name / mlm:io_description
│                              ├── mlm:bands / mlm:variables
│                              ├── mlm:result ──────► mlm:ResultStructure
│                              ├── classification:classes
│                              └── mlm:post_processing_function
├── mlm:model_asset ─────────► stac:Asset
│                              ├── roles contains "mlm:model"
│                              ├── mlm:artifact_type
│                              └── mlm:entrypoint ──► asset with "code" role
├── application:* ───────────► STAC Application metadata
└── vcs link ────────────────► VCS repository metadata
```

## Relationship reference

| Subject | Predicate | Object | Meaning and source |
| --- | --- | --- | --- |
| `mlm:ModelInput` | `mlm:io_name` | string | Name of the model input. |
| `mlm:ModelInput` | `mlm:io_description` | string | Description of the model input. |
| `mlm:ModelInput` | `mlm:bands` | string or `mlm:BandVariableReference` | Ordered input band names or explicit references. |
| `mlm:ModelInput` | `mlm:variables` | string or `mlm:BandVariableReference` | Ordered input variable names or explicit references. |
| `mlm:ModelInput` | `mlm:input_structure` | `mlm:InputStructure` | Expected input tensor shape, order, and data type. |
| `mlm:ModelInput` | `mlm:value_scaling` | `mlm:ValueScaling` | Ordered transformations applied to input values. |
| `mlm:ModelInput` | `mlm:resize_type` | SKOS concept | Spatial resizing method applied to the input. |
| `mlm:ModelInput` | `mlm:pre_processing_function` | Processing expression | Transformation applied before model inference. |
| `mlm:ModelOutput` | `mlm:io_name` | string | Name of the model output. |
| `mlm:ModelOutput` | `mlm:io_description` | string | Description of the model output. |
| `mlm:ModelOutput` | `mlm:bands` | string or `mlm:BandVariableReference` | Ordered output band names or explicit references. |
| `mlm:ModelOutput` | `mlm:variables` | string or `mlm:BandVariableReference` | Ordered output variable names or explicit references. |
| `mlm:ModelOutput` | `mlm:result` | `mlm:ResultStructure` | Produced tensor shape, order, and data type. |
| `mlm:ModelOutput` | `classification:classes` | classification classes | Classification labels reused from the Classification extension. |
| `mlm:ModelOutput` | `mlm:post_processing_function` | Processing expression | Transformation applied after model inference. |
| `mlm:BandVariableReference` | `mlm:reference_name` | string | Name used to resolve a band or variable. |
| `mlm:BandVariableReference` | `mlm:reference_format` | string | Format used to interpret the derivation expression. |
| `mlm:BandVariableReference` | `mlm:reference_expression` | JSON value | Optional derivation expression, interpreted using `mlm:reference_format`. |
| `mlm:InputStructure` / `mlm:ResultStructure` | `mlm:shape` | ordered integers | Tensor dimension sizes. |
| `mlm:InputStructure` / `mlm:ResultStructure` | `mlm:dim_order` | ordered strings | Names and order of tensor dimensions, including `bands` or `variables`. |
| `mlm:InputStructure` / `mlm:ResultStructure` | `mlm:data_type` | string | Tensor data type. |
| `mlm:ValueScaling` | `mlm:scaling_type` | SKOS concept | Scaling operation selected from the MLM value-scaling scheme. |
| `mlm:ValueScaling` | `mlm:minimum`, `mlm:maximum`, `mlm:mean`, `mlm:stddev`, `mlm:scaling_value` | number | Parameters for the selected scaling operation. For `offset` and `scale`, `mlm:scaling_value` is the fixed amount added or multiplier applied. |
| STAC Item/Collection | `mlm:input` | `mlm:ModelInput` | Model input specification defined by MLM. |
| STAC Item/Collection | `mlm:output` | `mlm:ModelOutput` | Model output specification defined by MLM. |
| STAC Item/Collection | `mlm:name`, `mlm:architecture`, `mlm:tasks`, `mlm:framework`, etc. | model metadata | Model identity, task, framework, accelerator, and artifact metadata defined by MLM. |
| STAC Item/Collection | `mlm:model_asset` | `stac:Asset` | Asset carrying the `mlm:model` role and model artifact metadata. |
| STAC Item/Collection | `cube:variables` | variable map | Datacube descriptions selected by `mlm:variables`; variables may refer to `cube:dimensions`. |
| STAC Item/Collection | `application:*` | application metadata | Application extension describes the executable/software resource. |
| STAC Asset | `eo:*` / `raster:*` | band metadata | Description of the referenced band, supplied by EO/Raster extensions. |
| STAC Link | `vcs:*` | repository metadata | VCS extension identifies the source repository for an application or other resource. |

> [!IMPORTANT]
> **Order matters.** `bands`, `variables`, `shape`, `dim_order`, `value_scaling`, and arrays of processing
> expressions are positional. `shape[i]` is the size of the axis named `dim_order[i]`, and the order of
> `bands` and `variables` defines the indices along the reserved `"bands"` and `"variables"` axes.
> `value_scaling` entry `i` applies to stacked element `i`, unless it has one broadcast entry. Processing
> expression arrays run sequentially. Reordering any of these arrays changes the model contract.
> See [Order matters](description.md#order-matters) for the full table and the checks that enforce it.

The `bands` and `variables` arrays preserve model channel/variable order through RDF lists. MLM
`input`, `output`, `tasks`, `value_scaling`, `shape`, and `dim_order` arrays are also RDF lists. Table and
diagram relationships to their members are traversed using `rdf:rest*/rdf:first` after the field predicate.
When present, the corresponding `mlm:dim_order` list uses `bands` and/or `variables` to identify those tensor
axes.
The ontology does not assert that `mlm:bands` is equivalent to `eo:bands` or `raster:bands`:
those extensions describe the referenced STAC data, whereas MLM selects the data used by the model.

The JSON field names and the RDF predicate names must not be confused. At Item/Collection level, the
MLM JSON property is `mlm:name`; inside an `input` or `output` object, the JSON member is simply
`name` (without an `mlm:` prefix). The JSON-LD context maps the nested member to the distinct RDF
predicate `mlm:io_name`, while the top-level property maps to `mlm:name`. Similarly, nested
`description`, `input`, `type`, and `value` members map to `mlm:io_description`,
`mlm:input_structure`, `mlm:scaling_type`, and `mlm:scaling_value`. This preserves the distinct
concepts in RDF while keeping the JSON serialization aligned with the MLM schema. No fictitious JSON
property named `mlm:name` is introduced inside a nested object.

## Cross-resource SHACL validation

The ontology includes SHACL constraints for relationships that the MLM JSON Schema cannot validate
because they depend on multiple resources or on ordered RDF structures:

- each `mlm:variables` reference on an input or output must resolve to a key in the enclosing
  Item or attached Asset Datacube `cube:variables` map;
- each dimension named by a Datacube variable must resolve to a key in that resource's
  `cube:dimensions` map;
- an asset carrying `mlm:artifact_type` must also carry the STAC `mlm:model` asset role;
- `shape` and `dim_order` must have the same length, have sizes greater than 0 or equal to -1, and use
  unique dimension names;
- the reserved `"bands"` / `"variables"` axis must be present if and only if the corresponding list is
  non-empty;
- the `bands` / `variables` list length must equal that axis size, unless the size is -1 or a
  pre/post-processing function changes the stacked size;
- `value_scaling` must have one broadcast entry or one entry per stacked `bands` / `variables` /
  `channel` element;
- nested MLM input/output structures and band/variable reference objects receive their applicable
  field-level shape checks.

The schema-specific context preserves Datacube JSON map keys as
`mlm:datacube_variable_name` and `mlm:datacube_dimension_name` so those references remain
available to SHACL without changing the standalone Datacube block. These predicates are uplift
implementation terms, not replacements for Datacube's `cube:variables` or `cube:dimensions`
properties. Band-name resolution is intentionally not asserted here because the current STAC EO and
Raster RDF mappings do not provide one authoritative, interoperable RDF predicate for every form of
asset band name.

The [MLM schema block transforms](../mlm/README.md) additionally provide a reversible Item RDF profile
that preserves explicit nulls, extension metadata, dictionary keys, and array order. Its structural
serialization vocabulary is separate from the upstream MLM fields.

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

Source of definitions: <https://github.com/stac-extensions/mlm> (v1.6.0).
