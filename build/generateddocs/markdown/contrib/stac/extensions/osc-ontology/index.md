
# STAC Open Science Extension Ontology (Model)

`ogc.contrib.stac.extensions.osc-ontology` *v0.2*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### OSC product (matching the shape of stac-extensions/osc's product examples)
#### turtle
```turtle
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix osc:  <https://w3id.org/ogc/stac/osc/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/stac/> .

ex:product-collection a stac:Collection ;
    osc:type       osc:product-type ;
    osc:status     osc:ongoing ;
    osc:project    "Arctic Sea Ice Thickness"^^xsd:string ;
    osc:region     "Arctic"^^xsd:string ;
    osc:variables  "Sea ice thickness"^^xsd:string ;
    osc:missions   "CryoSat-2"^^xsd:string ;
    osc:experiment "cs2-retracker-v3"^^xsd:string .

```


### OSC project
#### turtle
```turtle
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix osc:  <https://w3id.org/ogc/stac/osc/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/stac/> .

ex:project-collection a stac:Collection ;
    osc:type      osc:project-type ;
    osc:status    osc:planned ;
    osc:region    "Agulhas"^^xsd:string ;
    osc:workflows "cs2-retracker-v3"^^xsd:string .

```

## Sources

* [GitHub Repository](https://github.com/stac-extensions/osc)
* [JSON Schema (v1.0.0)](https://stac-extensions.github.io/osc/v1.0.0/schema.json)
* [README (field table for project/product resources)](https://github.com/stac-extensions/osc/blob/main/README.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/osc-ontology`

