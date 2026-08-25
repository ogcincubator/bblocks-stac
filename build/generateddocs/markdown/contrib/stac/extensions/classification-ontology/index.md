
# STAC Classification Extension Ontology (Model)

`ogc.contrib.stac.extensions.classification-ontology` *v0.1*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Land-cover classes for a Sentinel-2 classification model output (EuroSAT classes)
#### turtle
```turtle
@prefix stac:           <https://w3id.org/ogc/stac/core/> .
@prefix classification: <https://w3id.org/ogc/stac/classification/> .
@prefix xsd:            <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:             <https://example.org/stac/> .

ex:resnet18-eurosat a stac:Item ;
    classification:classes
        [ a classification:Class ; classification:value 0 ; classification:name "AnnualCrop" ] ,
        [ a classification:Class ; classification:value 1 ; classification:name "Forest" ] ,
        [ a classification:Class ; classification:value 2 ; classification:name "HerbaceousVegetation" ] ,
        [ a classification:Class ; classification:value 3 ; classification:name "Highway" ] ,
        [ a classification:Class ; classification:value 4 ; classification:name "Industrial" ] ,
        [ a classification:Class ; classification:value 5 ; classification:name "Pasture" ] ,
        [ a classification:Class ; classification:value 6 ; classification:name "PermanentCrop" ] ,
        [ a classification:Class ; classification:value 7 ; classification:name "Residential" ] ,
        [ a classification:Class ; classification:value 8 ; classification:name "River" ] ,
        [ a classification:Class ; classification:value 9 ; classification:name "SeaLake" ] .

```


### Bitfield-encoded quality classes on a raster band
#### turtle
```turtle
@prefix stac:           <https://w3id.org/ogc/stac/core/> .
@prefix classification: <https://w3id.org/ogc/stac/classification/> .
@prefix xsd:            <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:             <https://example.org/stac/> .

ex:qa-band a stac:Asset ;
    classification:bitfields [
        a classification:BitField ;
        classification:offset "0"^^xsd:nonNegativeInteger ;
        classification:length "1"^^xsd:positiveInteger ;
        classification:name "cloud" ;
        classification:classes
            [ a classification:Class ; classification:value 0 ; classification:name "clear" ; classification:title "Clear" ] ,
            [ a classification:Class ; classification:value 1 ; classification:name "cloudy" ; classification:title "Cloudy" ] ;
    ] .

```

## Sources

* [GitHub Repository](https://github.com/stac-extensions/classification)
* [JSON Schema (v2.0.0)](https://stac-extensions.github.io/classification/v2.0.0/schema.json)
* [README (Class Object / Bit Field Object field tables)](https://github.com/stac-extensions/classification/blob/main/README.md)
* [Example: item-model-classes.json](https://github.com/stac-extensions/classification/raw/refs/heads/main/examples/item-model-classes.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/classification-ontology`

