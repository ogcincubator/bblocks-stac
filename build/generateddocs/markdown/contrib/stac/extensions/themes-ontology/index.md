
# STAC Themes Extension Ontology (Model)

`ogc.contrib.stac.extensions.themes-ontology` *v0.1*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### A STAC Item classified with a Themes concept
#### turtle
```turtle
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix thns:  <https://w3id.org/ogc/stac/themes/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/stac/> .

ex:item a stac:Item ;
    thns:schemes [
        a thns:Theme ;
        thns:scheme "https://www.eionet.europa.eu/gemet/en/inspire-theme/" ;
        thns:concepts [
            a thns:Concept ;
            thns:id "hb" ;
            thns:name "Habitats and biotopes" ;
            thns:description "Geographical areas characterized by specific ecological conditions, processes, structure, and life-support functions." ;
        ] ;
    ] .

```

## Sources

* [GitHub Repository](https://github.com/stac-extensions/themes)
* [JSON Schema (v1.0.0)](https://stac-extensions.github.io/themes/v1.0.0/schema.json)
* [README (Theme Object / Concept Object field tables)](https://github.com/stac-extensions/themes/blob/main/README.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/themes-ontology`

