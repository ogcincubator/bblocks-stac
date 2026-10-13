The STAC Machine Learning Model (MLM) extension describes machine learning models, their inputs and
outputs, training details, and runtime requirements on STAC Items and Collections. This block provides the
JSON Schema and the JSON-LD context that map the extension fields to the
[MLM ontology](bblocks://ogc.contrib.stac.extensions.mlm-ontology). It also provides reversible
[STAC Item to RDF transforms](README.md).

> [!IMPORTANT]
> **Order matters.** In each `input` and `result` object, `shape[i]` is the size of the axis named
> `dim_order[i]`. The order of `bands` and `variables` matches the indices along the reserved `"bands"` and
> `"variables"` axes. A `value_scaling` array either has one broadcast entry or one entry per stacked element,
> in the same order. Arrays of `pre_processing_function` or `post_processing_function` expressions run
> sequentially.
> These positions are kept as ordered RDF lists. The SHACL shapes from the ontology block reject definitions
> whose positions no longer align. See
> [Order matters](bblocks://ogc.contrib.stac.extensions.mlm-ontology) for the full table of rules.
