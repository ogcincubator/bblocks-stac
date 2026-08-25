
# STAC Asset Component Ontology (Model)

`ogc.contrib.stac.components.assets-ontology` *v0.1*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### A thumbnail asset
#### turtle
```turtle
@prefix stac:   <https://w3id.org/ogc/stac/core/> .
@prefix assets: <https://w3id.org/ogc/stac/assets/> .
@prefix dct:    <http://purl.org/dc/terms/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:     <https://example.org/stac/assets/> .

ex:thumb a stac:Asset ;
    dct:title "Thumbnail image" ;
    dct:format "image/png" ;
    assets:roles "thumbnail"^^xsd:string .

```


### A data asset with a custom role alongside a recommended one
#### turtle
```turtle
@prefix stac:   <https://w3id.org/ogc/stac/core/> .
@prefix assets: <https://w3id.org/ogc/stac/assets/> .
@prefix dct:    <http://purl.org/dc/terms/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:     <https://example.org/stac/assets/> .

ex:B04 a stac:Asset ;
    dct:title "Band 4 (red)" ;
    dct:format "image/tiff; application=geotiff; profile=cloud-optimized" ;
    assets:roles "data"^^xsd:string, "reflectance"^^xsd:string .

```

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)
* [Asset Object field table](https://github.com/radiantearth/stac-spec/blob/master/commons/assets.md)
* [Best Practices — Asset Roles](https://github.com/radiantearth/stac-spec/blob/master/best-practices.md#asset-roles)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/components/assets-ontology`

