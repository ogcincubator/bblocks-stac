
# STAC Machine Learning Model Extension Ontology (Model)

`ogc.contrib.stac.extensions.mlm-ontology` *v0.2*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### ResNet-18 Sentinel-2 scene classifier (model identity and framework)
#### turtle
```turtle
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix mlm:  <https://w3id.org/ogc/stac/mlm/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/stac/> .

ex:resnet18-eurosat a stac:Item ;
    mlm:name             "ResNet-18 Sentinel-2 Classifier"^^xsd:string ;
    mlm:architecture     "ResNet-18"^^xsd:string ;
    mlm:tasks            ( mlm:scene-classification ) ;
    mlm:framework        "PyTorch"^^xsd:string ;
    mlm:framework_version "2.1.2"^^xsd:string ;
    mlm:total_parameters 11700000 ;
    mlm:accelerator      mlm:cuda ;
    mlm:input ( [
        mlm:io_name "13 Band Sentinel-2 Batch" ;
        mlm:input_structure [
            mlm:shape ( -1 13 64 64 ) ;
            mlm:dim_order ( "batch" "channel" "height" "width" ) ;
            mlm:data_type "float32"^^xsd:string ;
        ]
    ] ) ;
    mlm:output ( [
        mlm:io_name "classification" ;
        mlm:tasks ( mlm:scene-classification ) ;
        mlm:result [
            mlm:shape ( -1 10 ) ;
            mlm:dim_order ( "batch" "class" ) ;
            mlm:data_type "float32"^^xsd:string ;
        ]
    ] ) .

```


### Value scaling (min-max normalization on a ModelInput)
#### turtle
```turtle
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:  <https://example.org/stac/> .

ex:input1
    mlm:io_name "13 Band Sentinel-2 Batch" ;
    mlm:input_structure [
        mlm:shape ( -1 13 64 64 ) ;
        mlm:dim_order ( "batch" "channel" "height" "width" ) ;
        mlm:data_type "float32"^^xsd:string ;
    ] ;
    mlm:value_scaling ( [
        mlm:scaling_type mlm:min-max ;
        mlm:minimum "0.0"^^xsd:double ;
        mlm:maximum "10000.0"^^xsd:double ;
    ] ) .

```

## Sources

* [GitHub Repository](https://github.com/stac-extensions/mlm)
* [JSON Schema (v1.6.0)](https://stac-extensions.github.io/mlm/v1.6.0/schema.json)
* [README (field descriptions and example)](https://github.com/stac-extensions/mlm/blob/main/README.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/mlm-ontology`

