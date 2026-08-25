
# STAC Accuracy Extension Ontology (Model)

`ogc.contrib.stac.extensions.accuracy-ontology` *v0.1*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Item with geometric and measurement accuracy
#### turtle
```turtle
@prefix stac:     <https://w3id.org/ogc/stac/core/> .
@prefix accuracy: <https://w3id.org/ogc/stac/accuracy/> .
@prefix xsd:      <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:       <https://example.org/stac/> .

ex:S2A_MSIL2A_item a stac:Item ;
    accuracy:geometric_x_bias      "0.5"^^xsd:double ;
    accuracy:geometric_y_bias      "0.3"^^xsd:double ;
    accuracy:geometric_x_stddev    "1.1"^^xsd:double ;
    accuracy:geometric_y_stddev    "1.0"^^xsd:double ;
    accuracy:geometric_rmse        "1.2"^^xsd:double ;
    accuracy:measurement_absolute  "0.15"^^xsd:double .

```


### STAC Collection with relative measurement accuracy
#### turtle
```turtle
@prefix stac:     <https://w3id.org/ogc/stac/core/> .
@prefix accuracy: <https://w3id.org/ogc/stac/accuracy/> .
@prefix xsd:      <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:       <https://example.org/stac/> .

ex:collection a stac:Collection ;
    accuracy:measurement_relative "0.02"^^xsd:double .

```

## Sources

* [GitHub Repository](https://github.com/stac-extensions/accuracy)
* [JSON Schema (v1.0.0-beta.1)](https://stac-extensions.github.io/accuracy/v1.0.0-beta.1/schema.json)
* [README (field table and units)](https://github.com/stac-extensions/accuracy/blob/main/README.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/accuracy-ontology`

