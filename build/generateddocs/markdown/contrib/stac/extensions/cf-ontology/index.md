
# STAC CF Extension Ontology (Model)

`ogc.contrib.stac.extensions.cf-ontology` *v0.1*

None

[*Status*](http://www.opengis.net/def/status): Stable

## Examples

### STAC Item with CF parameters
#### turtle
```turtle
@prefix cf:   <https://w3id.org/ogc/stac/cf/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix ex:   <https://example.org/stac/> .

ex:item a stac:Item ;
    cf:parameter
        [ a cf:Object ; cf:name "sea_surface_temperature"     ; qudt:hasUnit unit:K ] ,
        [ a cf:Object ; cf:name "sea_ice_surface_temperature" ; qudt:hasUnit unit:K ] ,
        [ a cf:Object ; cf:name "depth"                       ; qudt:hasUnit unit:M ] .

```


### STAC Collection with CF parameters (summaries)
#### turtle
```turtle
@prefix cf:   <https://w3id.org/ogc/stac/cf/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix ex:   <https://example.org/stac/> .

ex:collection a stac:Collection ;
    cf:parameter
        [ a cf:Object ; cf:name "sea_surface_temperature"     ; qudt:hasUnit unit:K ] ,
        [ a cf:Object ; cf:name "sea_ice_surface_temperature" ; qudt:hasUnit unit:K ] ,
        [ a cf:Object ; cf:name "depth"                       ; qudt:hasUnit unit:M ] .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/cf-ontology`

