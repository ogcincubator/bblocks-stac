This building block defines the RDF vocabulary (OWL classes and properties, SKOS concept schemes, and SHACL
shapes) for the fields introduced by the [STAC Machine Learning Model (MLM) extension](https://github.com/stac-extensions/mlm).
It is bound to the MLM JSON Schema by the
[STAC Machine Learning Model](bblocks://ogc.contrib.stac.extensions.mlm) block's JSON-LD context. See the
[ontology README](README.md) for the interaction graph and the full relationship reference.

## Order matters

> [!IMPORTANT]
> Several MLM arrays are **positional**: the index of an element carries meaning. Reordering them changes
> which data feeds which tensor channel, or which operation runs first, even when every value is individually
> valid. These arrays are mapped to ordered RDF lists (`rdf:List`), never to unordered multi-valued
> properties. Traverse their members with `rdf:rest*/rdf:first`.

| Field | What the position means | Validation |
| --- | --- | --- |
| `shape` / `dim_order` (in `input` and `result`) | `shape[i]` is the size of the axis named `dim_order[i]`; the sequence is the tensor memory layout expected by the framework (e.g. channels-first versus channels-last). | **SHACL error** when lengths differ, when a size is `0` or below `-1`, or when a dimension name repeats. |
| `bands` | Item `i` describes index `i` of the reserved `"bands"` axis in `dim_order`. Processing expressions may also refer to these bands positionally (e.g. `A`, `B` in `gdal-calc`). | **SHACL error** when a non-empty list has no `"bands"` axis (or the reverse), or when the list length differs from that axis size (unless the size is `-1` or a processing function changes the stacked size). |
| `variables` | Item `i` describes index `i` of the reserved `"variables"` axis in `dim_order`. | Same checks as `bands`, with the `"variables"` axis. |
| `value_scaling` | Either one entry broadcast to every stacked element, or entry `i` applies to element `i` of the stacked `bands` / `variables` / `channel` axis. | **SHACL error** when more than one entry is provided and the count matches no known size on those axes. |
| `pre_processing_function` / `post_processing_function` | When an array of expressions is provided, they run sequentially in array order, each result feeding the next. | Preserved by the JSON literal; documentation only. |
| `mlm:input` / `mlm:output` | Can correspond to the positional arguments and results of the model inference call. | Order preserved; documentation only. |
| `mlm:tasks` | No semantic order. | Order preserved only for round-trip fidelity. |
| `classification:classes` | No semantic order; classes are identified by their `value`. | Modeled as a set. |

The JSON Schema already rejects some of these cases on its own (for example a non-empty `bands` without a
`"bands"` axis, or repeated `dim_order` names). The SHACL shapes repeat those checks so that RDF data that
did not originate from validated JSON is held to the same rules. They also add the position-alignment checks
that JSON Schema cannot express.
