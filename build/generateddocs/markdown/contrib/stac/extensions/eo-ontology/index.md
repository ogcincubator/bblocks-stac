
# STAC Electro-Optical Extension Ontology (Model)

`ogc.contrib.stac.extensions.eo-ontology` *v0.1*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Item band with a common name (Landsat-style red band)
#### turtle
```turtle
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix eo:   <https://w3id.org/ogc/stac/eo/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/stac/> .

ex:landsat-item a stac:Item ;
    eo:cloud_cover "12.5"^^xsd:double ;
    eo:snow_cover  "0"^^xsd:double .

ex:red-band
    eo:common_name          eo:red ;
    eo:center_wavelength    "0.655"^^xsd:double ;
    eo:full_width_half_max  "0.07"^^xsd:double .

```


### Common band name vocabulary member
#### turtle
```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix eo:   <https://w3id.org/ogc/stac/eo/> .

eo:red a skos:Concept ;
    skos:inScheme eo:CommonBandNameScheme ;
    skos:notation "red" ;
    skos:prefLabel "Red"@en ;
    skos:definition "Band range: 0.62 - 0.69µm."@en .

```

## Sources

* [GitHub Repository](https://github.com/stac-extensions/eo)
* [JSON Schema (v2.0.0)](https://stac-extensions.github.io/eo/v2.0.0/schema.json)
* [README (Common Band Names table)](https://github.com/stac-extensions/eo/blob/main/README.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/eo-ontology`

