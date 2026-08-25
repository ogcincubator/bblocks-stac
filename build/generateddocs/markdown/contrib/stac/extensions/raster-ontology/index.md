
# STAC Raster Extension Ontology (Model)

`ogc.contrib.stac.extensions.raster-ontology` *v0.1*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Raster band with scale/offset (DN to reflectance conversion)
#### turtle
```turtle
@prefix raster: <https://w3id.org/ogc/stac/raster/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:     <https://example.org/stac/> .

ex:B4-band
    raster:scale  "0.0001"^^xsd:double ;
    raster:offset "0.0"^^xsd:double ;
    raster:sampling raster:area .

```


### Raster band histogram
#### turtle
```turtle
@prefix raster: <https://w3id.org/ogc/stac/raster/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:     <https://example.org/stac/> .

ex:B4-band raster:histogram [
    raster:count 10 ;
    raster:min "0.0"^^xsd:double ;
    raster:max "10000.0"^^xsd:double ;
    raster:buckets 4, 20, 100, 15, 8, 3, 2, 1, 1, 1 ;
] .

```

## Sources

* [GitHub Repository](https://github.com/stac-extensions/raster)
* [JSON Schema (v2.0.0)](https://stac-extensions.github.io/raster/v2.0.0/schema.json)
* [README (Raster Band Object field table and example)](https://github.com/stac-extensions/raster/blob/main/README.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/raster-ontology`

