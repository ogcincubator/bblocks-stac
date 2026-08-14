
# STAC Processing Extension Ontology (Model)

`ogc.contrib.stac.extensions.processes-ontology` *v0.2*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Item with processing metadata (Sentinel-1 GRD)
#### turtle
```turtle
@prefix stac:       <https://w3id.org/ogc/stac/core/> .
@prefix processing: <https://w3id.org/ogc/stac/processing/> .
@prefix xsd:        <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf:        <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex:         <https://example.org/stac/> .

ex:S1A_IW_GRDH_1SDV_20160822T182823 a stac:Item ;
    processing:lineage  "GRD Post Processing" ;
    processing:level    "L1" ;
    processing:facility "Copernicus S1 Core Ground Segment - DPA" ;
    processing:datetime "2016-08-23T00:30:33Z"^^xsd:dateTime ;
    processing:software "{\"Sentinel-1 IPF\":\"002.71\"}"^^rdf:JSON .

```


### STAC Collection with processing metadata (Sentinel-2 L2A)
#### turtle
```turtle
@prefix stac:       <https://w3id.org/ogc/stac/core/> .
@prefix processing: <https://w3id.org/ogc/stac/processing/> .
@prefix rdf:        <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex:         <https://example.org/stac/> .

ex:Sentinel2-L2A a stac:Collection ;
    processing:lineage  "Generation of Level-2A User Product" ;
    processing:level    "L2A" ;
    processing:facility "Copernicus S2 Processing and Archiving Facility" ;
    processing:version  "02.06" ;
    processing:software "{\"Sentinel-2 Toolbox\":\"8.0.0\"}"^^rdf:JSON .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/processes-ontology`

