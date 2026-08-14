
# STAC Core Ontology (Model)

`ogc.contrib.stac.core-ontology` *v0.1*

None

[*Status*](http://www.opengis.net/def/status): Stable

## Examples

### STAC Item (core fields)
#### turtle
```turtle
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/stac/> .

ex:item_20201211 a stac:Item ;
    stac:id       "20201211_223832_CS2" ;
    stac:datetime "2020-12-11T22:38:32.125000Z"^^xsd:dateTime ;
    stac:hasAsset ex:asset-visual , ex:asset-thumbnail ;
    stac:links    ex:link-collection , ex:link-root , ex:link-parent .

ex:asset-visual a stac:Asset ;
    stac:mediaType "image/tiff; application=geotiff; profile=cloud-optimized" .

ex:asset-thumbnail a stac:Asset ;
    stac:mediaType "image/jpeg" .

ex:link-collection a stac:Link ;
    stac:rel  "collection" ;
    stac:href "./collection.json"^^xsd:anyURI .

ex:link-root a stac:Link ;
    stac:rel  "root" ;
    stac:href "./collection.json"^^xsd:anyURI .

ex:link-parent a stac:Link ;
    stac:rel  "parent" ;
    stac:href "./collection.json"^^xsd:anyURI .

```


### STAC Collection (core fields)
#### turtle
```turtle
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix ex:   <https://example.org/stac/> .

ex:simple-collection a stac:Collection ;
    stac:id          "simple-collection" ;
    stac:description "A simple collection demonstrating core catalog fields with links to a couple of items" ;
    stac:license     "CC-BY-4.0" .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/core-ontology`

