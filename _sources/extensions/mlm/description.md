The STAC Machine Learning Model (MLM) extension describes machine learning models, their inputs and
outputs, training details, and runtime requirements on STAC Items and Collections. This block provides the
JSON Schema and the JSON-LD context that map the extension fields to the
[MLM ontology](bblocks://ogc.contrib.stac.extensions.mlm-ontology). It also provides reversible
[STAC Item to RDF transforms](README.md).

## Related STAC extensions

**None of the extensions below is universally required on every MLM Item.** Which definitions are
needed depends on the model's inputs, outputs and the metadata being supplied.
The viewer's dependency graph describes reuse between building blocks, not an unconditional requirement
to list every dependency in an Item's `stac_extensions`.

### Conditional input/output relationships

These extensions describe objects or structures directly referenced by MLM. A referenced object must
have an appropriate definition, but the applicable extension or STAC core representation depends on
the field and STAC version. Datacube belongs to this group alongside EO and Raster.

| Extension | When it applies | Connection to MLM |
| --- | --- | --- |
| [EO](bblocks://ogc.contrib.stac.extensions.eo) | When referenced bands are described using EO metadata. EO is not the only supported band representation; STAC 1.1 also defines common Band Objects. | Supplies spectral band names, common names and wavelength metadata for MLM `bands` references. |
| [Raster](bblocks://ogc.contrib.stac.extensions.raster) | When referenced bands use Raster metadata. It is not required merely because the model operates on raster data; the representation depends on the STAC/extension version. | Supplies band data types, nodata values and statistics. Source statistics need not equal the model's applied `value_scaling`. |
| [Datacube](bblocks://ogc.contrib.stac.extensions.datacube) | When non-empty MLM `variables` references are supplied, corresponding Datacube variable definitions are needed. Models without variable references do not require them. | Describes selected variables and their dimensions. Shared MLM SHACL resolves variable names and dimension references. |
| [Classification](bblocks://ogc.contrib.stac.extensions.classification) | When `classification:classes` metadata is supplied for an output. Not required for every model, or merely because a task is classification. | Describes output class values and labels. |
| [Processing](bblocks://ogc.contrib.stac.extensions.processing) | When MLM supplies pre/post-processing, derivation or custom scaling expressions. Reusing its Expression Object structure does not by itself require declaring the Processing extension on the Item. | Supplies the expression structure reused by MLM processing fields. |

### Complementary model, data and software metadata

These integrations add context rather than define the objects selected by MLM `bands` or `variables`.
They apply when the corresponding metadata is provided, not automatically to every model.

| Extension | When it applies | Connection to MLM |
| --- | --- | --- |
| [ML-AOI](bblocks://ogc.contrib.stac.extensions.ml-aoi) | When documenting training, validation or test areas of interest. | Describes areas associated with the model's training data. |
| [Application](bblocks://ogc.contrib.stac.extensions.application) | When documenting the software application that packages or executes the model. | Adds application metadata alongside the model description. |
| [VCS](bblocks://ogc.contrib.stac.extensions.vcs) | When documenting model/application source repositories or revisions. | Identifies version-control resources, including repository links. |
| [File Info](bblocks://ogc.contrib.stac.extensions.file) | When supplying sizes, checksums or other file metadata for model artifacts and associated files. | Describes the files carrying the model and related resources. |
| [Scientific Citation](bblocks://ogc.contrib.stac.extensions.scientific) | When supplying publications, citations or persistent identifiers. | Records scientific references associated with the model. |
| [Versioning Indicators](bblocks://ogc.contrib.stac.extensions.version) | When documenting revisions of the model's STAC resource. | Identifies versions and links between revisions. |
| [CF](bblocks://ogc.contrib.stac.extensions.cf) | When supplying Climate and Forecast metadata for climate variables. | Adds scientific variable descriptions; it is not required merely because a model uses Datacube. |

### Complete Example

In the [**Examples**](/bblock/ogc.contrib.stac.extensions.mlm/examples) tab, a pinned Resoterre U-Net for RDPS to HRDPS
climate variables downscaling
uses Datacube and all the complementary extensions above except CF to demonstrate own their interconnexions apply.

## Order matters

> In each `input` and `result` object, `shape[i]` is the size of the axis named
> `dim_order[i]`. The order of `bands` and `variables` matches the indices along the reserved `"bands"` and
> `"variables"` axes. A `value_scaling` array either has one broadcast entry or one entry per stacked element,
> in the same order. Arrays of `pre_processing_function` or `post_processing_function` expressions run
> sequentially.
> These positions are kept as ordered RDF lists. The SHACL shapes from the ontology block reject definitions
> whose positions no longer align. See
> [Order matters](bblocks://ogc.contrib.stac.extensions.mlm-ontology) for the full table of rules.
