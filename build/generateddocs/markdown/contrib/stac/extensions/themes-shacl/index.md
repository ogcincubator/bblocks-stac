
# STAC Themes Extension with SHACL semantic uplift step (Schema)

`ogc.contrib.stac.extensions.themes-shacl` *v0.1*

Themes Extension to the SpatioTemporal Asset Catalog (STAC) specification.
A knowledge organization system used to classify the resource (controlled vocabularies / keywords)

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### A simple Collection demonstrating Themes extension fields in a Collection.
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json"
  ],
  "type": "Collection",
  "id": "collection",
  "title": "A title",
  "description": "A description",
  "license": "Apache-2.0",
  "themes": [
    {
      "concepts": [
        {
          "id": "dobson",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson"
        },
        {
          "id": "brewer",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_brewer"
        },
        {
          "id": "vassey",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_vassey"
        },
        {
          "id": "pion",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_pion"
        },
        {
          "id": "microtops",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_microtops"
        },
        {
          "id": "spectral",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_spectral"
        },
        {
          "id": "hoelper",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_hoelper"
        },
        {
          "id": "saoz",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_saoz"
        },
        {
          "id": "filter",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter"
        }
      ],
      "scheme": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode"
    },
    {
      "concepts": [
        {
          "id": "atmosphericComposition",
          "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_atmosphericComposition"
        },
        {
          "id": "pollution",
          "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_pollution"
        },
        {
          "id": "observationPlatform",
          "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_observationPlatform"
        },
        {
          "id": "rocketSounding",
          "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_rocketSounding"
        }
      ],
      "scheme": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          172.9,
          1.3,
          173,
          1.4
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2015-06-23T00:00:00Z",
          null
        ]
      ]
    }
  },
  "links": [
    {
      "href": "https://example.com/examples/collection.json",
      "rel": "self"
    },
    {
      "href": "https://example.com/examples/item.json",
      "rel": "item"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/themes-shacl/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json"
  ],
  "type": "Collection",
  "id": "collection",
  "title": "A title",
  "description": "A description",
  "license": "Apache-2.0",
  "themes": [
    {
      "concepts": [
        {
          "id": "dobson",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson"
        },
        {
          "id": "brewer",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_brewer"
        },
        {
          "id": "vassey",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_vassey"
        },
        {
          "id": "pion",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_pion"
        },
        {
          "id": "microtops",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_microtops"
        },
        {
          "id": "spectral",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_spectral"
        },
        {
          "id": "hoelper",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_hoelper"
        },
        {
          "id": "saoz",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_saoz"
        },
        {
          "id": "filter",
          "url": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter"
        }
      ],
      "scheme": "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode"
    },
    {
      "concepts": [
        {
          "id": "atmosphericComposition",
          "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_atmosphericComposition"
        },
        {
          "id": "pollution",
          "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_pollution"
        },
        {
          "id": "observationPlatform",
          "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_observationPlatform"
        },
        {
          "id": "rocketSounding",
          "url": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_rocketSounding"
        }
      ],
      "scheme": "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          172.9,
          1.3,
          173,
          1.4
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2015-06-23T00:00:00Z",
          null
        ]
      ]
    }
  },
  "links": [
    {
      "href": "https://example.com/examples/collection.json",
      "rel": "self"
    },
    {
      "href": "https://example.com/examples/item.json",
      "rel": "item"
    }
  ]
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/ogc/stac/assets/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/themes/example-1/collection> dcterms:description "A description" ;
    dcterms:extent [ :spatial [ geojson:bbox ( ( 1.729e+02 1.3e+00 173 1.4e+00 ) ) ] ;
            :temporal [ :interval "2015-06-23T00:00:00Z" ] ] ;
    dcterms:format "Collection" ;
    dcterms:title "A title" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/examples/item.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/collection.json> ] ;
    dcat:license "Apache-2.0" ;
    stac:hasExtension "https://stac-extensions.github.io/themes/v1.0.0/schema.json" ;
    stac:version "1.0.0" ;
    rec:themes [ thns:concepts <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_brewer>,
                <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson>,
                <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter>,
                <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_hoelper>,
                <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_microtops>,
                <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_pion>,
                <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_saoz>,
                <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_spectral>,
                <https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_vassey> ;
            thns:scheme "https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode" ],
        [ thns:concepts <https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_atmosphericComposition>,
                <https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_observationPlatform>,
                <https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_pollution>,
                <https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_rocketSounding> ;
            thns:scheme "https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode" ] .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_brewer> thns:id "brewer" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_dobson> thns:id "dobson" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_filter> thns:id "filter" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_hoelper> thns:id "hoelper" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_microtops> thns:id "microtops" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_pion> thns:id "pion" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_saoz> thns:id "saoz" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_spectral> thns:id "spectral" .

<https://geo.woudc.org/codelists.xml#WOUDC_InstrumentCode_vassey> thns:id "vassey" .

<https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_atmosphericComposition> thns:id "atmosphericComposition" .

<https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_observationPlatform> thns:id "observationPlatform" .

<https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_pollution> thns:id "pollution" .

<https://wis.wmo.int/2012/codelists/WMOCodeLists.xml#WMO_CategoryCode_rocketSounding> thns:id "rocketSounding" .


```


### An example demonstrating Themes extension fields in a STAC item.
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "example",
  "bbox": [
    172.9,
    1.3,
    173,
    1.4
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          5.6287,
          44.2673
        ],
        [
          5.5996,
          44.1958
        ],
        [
          5.57633,
          44.13603
        ],
        [
          4.25061,
          44.15852
        ],
        [
          4.27204,
          45.14675
        ],
        [
          5.66762,
          45.12267
        ],
        [
          5.6287,
          44.2673
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2022-06-16T10:36:31.024Z",
    "themes": [
      {
        "concepts": [
          {
            "id": "geonames::2976077",
            "name": "Forêt de Saou"
          },
          {
            "id": "geonames::11071625",
            "name": "Auvergne-Rhône-Alpes"
          },
          {
            "id": "geonames::3017382",
            "name": "France"
          }
        ],
        "scheme": "https://www.geonames.org"
      },
      {
        "concepts": [
          {
            "id": "wiki::Summer",
            "name": "Summer"
          },
          {
            "id": "wiki::Syncline",
            "name": "Syncline"
          }
        ],
        "scheme": "https://en.wikipedia.org"
      }
    ]
  },
  "links": [
    {
      "href": "https://example.com/examples/item.json",
      "rel": "self"
    }
  ],
  "assets": {
    "data": {
      "href": "./example.file",
      "type": "text/plain"
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/themes-shacl/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "example",
  "bbox": [
    172.9,
    1.3,
    173,
    1.4
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          5.6287,
          44.2673
        ],
        [
          5.5996,
          44.1958
        ],
        [
          5.57633,
          44.13603
        ],
        [
          4.25061,
          44.15852
        ],
        [
          4.27204,
          45.14675
        ],
        [
          5.66762,
          45.12267
        ],
        [
          5.6287,
          44.2673
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2022-06-16T10:36:31.024Z",
    "themes": [
      {
        "concepts": [
          {
            "id": "geonames::2976077",
            "name": "For\u00eat de Saou"
          },
          {
            "id": "geonames::11071625",
            "name": "Auvergne-Rh\u00f4ne-Alpes"
          },
          {
            "id": "geonames::3017382",
            "name": "France"
          }
        ],
        "scheme": "https://www.geonames.org"
      },
      {
        "concepts": [
          {
            "id": "wiki::Summer",
            "name": "Summer"
          },
          {
            "id": "wiki::Syncline",
            "name": "Syncline"
          }
        ],
        "scheme": "https://en.wikipedia.org"
      }
    ]
  },
  "links": [
    {
      "href": "https://example.com/examples/item.json",
      "rel": "self"
    }
  ],
  "assets": {
    "data": {
      "href": "./example.file",
      "type": "text/plain"
    }
  }
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/ogc/stac/assets/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/themes/example-2/example> dcterms:date "2022-06-16T10:36:31.024000+00:00"^^xsd:dateTime ;
    dcterms:format "Feature" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/item.json> ] ;
    geojson:bbox ( 1.729e+02 1.3e+00 173 1.4e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 5.6287e+00 4.42673e+01 ) ( 5.5996e+00 4.41958e+01 ) ( 5.57633e+00 4.413603e+01 ) ( 4.25061e+00 4.415852e+01 ) ( 4.27204e+00 4.514675e+01 ) ( 5.66762e+00 4.512267e+01 ) ( 5.6287e+00 4.42673e+01 ) ) ) ] ;
    stac:hasAsset [ :data [ dcterms:format "text/plain" ;
                    oa:hasTarget <https://example.com/stac/themes/example-2/example.file> ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/themes/v1.0.0/schema.json" ;
    stac:version "1.0.0" ;
    rec:themes [ thns:concepts [ :name "Syncline" ;
                    thns:id "wiki::Syncline" ],
                [ :name "Summer" ;
                    thns:id "wiki::Summer" ] ;
            thns:scheme "https://en.wikipedia.org" ],
        [ thns:concepts [ :name "France" ;
                    thns:id "geonames::3017382" ],
                [ :name "Auvergne-Rhône-Alpes" ;
                    thns:id "geonames::11071625" ],
                [ :name "Forêt de Saou" ;
                    thns:id "geonames::2976077" ] ;
            thns:scheme "https://www.geonames.org" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Themes Extension
description: STAC Themes for STAC Items and STAC Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/themes/v1.0.0/schema.json
x-jsonld-extra-terms:
  themes:
    x-jsonld-id: https://w3id.org/ogc/stac/themes/schemes
    x-jsonld-container: '@set'
  concepts:
    x-jsonld-id: https://w3id.org/ogc/stac/themes/concepts
    x-jsonld-container: '@set'
    x-jsonld-context:
      name: https://w3id.org/ogc/stac/themes/name
      id: https://w3id.org/ogc/stac/themes/id
      url: '@id'
  scheme: https://w3id.org/ogc/stac/themes/scheme
x-jsonld-prefixes:
  thns: https://w3id.org/ogc/stac/themes/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/themes-shacl/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/themes-shacl/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "stac_extensions": "stac:hasExtension",
    "type": "dct:format",
    "id": "@id",
    "extent": {
      "@context": {
        "spatial": {},
        "temporal": {
          "@context": {
            "interval": {}
          }
        }
      },
      "@id": "dct:extent"
    },
    "item_assets": {
      "@context": {
        "type": "@type"
      }
    },
    "links": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "anchor": {},
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "method": {},
        "headers": {},
        "body": {}
      },
      "@id": "rdfs:seeAlso"
    },
    "summaries": {
      "@context": {
        "minimum": {},
        "maximum": {}
      }
    },
    "title": {
      "@id": "dct:title",
      "@container": "@set"
    },
    "description": {
      "@id": "dct:description",
      "@container": "@set"
    },
    "keywords": {
      "@id": "dcat:keyword",
      "@container": "@set"
    },
    "roles": {
      "@id": "stac:roles",
      "@container": "@set"
    },
    "bands": {
      "@context": {
        "name": {}
      }
    },
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "start_datetime": {},
    "end_datetime": {},
    "created": "dct:created",
    "updated": "dct:modified",
    "data_type": {},
    "nodata": {},
    "statistics": {
      "@context": {
        "minimum": {},
        "maximum": {},
        "mean": {},
        "stddev": {},
        "count": {},
        "valid_percent": {}
      }
    },
    "unit": {},
    "platform": {},
    "instruments": {},
    "constellation": {},
    "mission": {},
    "gsd": {},
    "license": "dcat:license",
    "providers": {
      "@context": {
        "name": {},
        "url": {}
      }
    },
    "@vocab": "https://w3id.org/ogc/stac/assets/",
    "assets": {
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac_version": "stac:version",
    "media_type": "dct:format",
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "properties": "@nest",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        },
        "geometries": {}
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "time": {
      "@context": {
        "date": {},
        "timestamp": {},
        "interval": {},
        "resolution": {}
      },
      "@id": "dct:temporal"
    },
    "linkTemplates": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "uriTemplate": {
          "@type": "xsd:string",
          "@id": "rec:uriTemplate"
        },
        "varBase": "rec:varBase",
        "variables": {
          "@id": "rec:hasVariable",
          "@container": "@index",
          "@index": "dct:identifier"
        }
      },
      "@id": "rec:hasLinkTemplate"
    },
    "collection": {},
    "language": {
      "@context": {
        "code": {},
        "name": {},
        "alternate": {},
        "dir": {}
      },
      "@id": "rec:language"
    },
    "languages": {
      "@context": {
        "code": {},
        "name": {},
        "alternate": {},
        "dir": {}
      },
      "@container": "@set",
      "@id": "rec:languages"
    },
    "resourceLanguages": {
      "@context": {
        "code": {},
        "name": {},
        "alternate": {},
        "dir": {}
      },
      "@container": "@set",
      "@id": "rec:resourceLanguages"
    },
    "externalIds": {
      "@context": {
        "scheme": "rec:scheme",
        "value": "rec:id"
      },
      "@container": "@set",
      "@id": "rec:scopedIdentifier"
    },
    "themes": {
      "@context": {
        "concepts": {
          "@context": {
            "id": "thns:id",
            "url": "@id"
          },
          "@id": "thns:concepts",
          "@container": "@set"
        }
      },
      "@container": "@set",
      "@id": "rec:themes"
    },
    "formats": {
      "@context": {
        "name": "rec:name",
        "mediaType": "rec:mediaType"
      },
      "@container": "@set",
      "@id": "rec:format",
      "@type": "@id"
    },
    "contacts": {
      "@context": {
        "identifier": {},
        "name": {},
        "position": {},
        "organization": {},
        "logo": {
          "@context": {
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "anchor": {},
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          }
        },
        "phones": {
          "@context": {
            "value": {}
          }
        },
        "emails": {
          "@context": {
            "value": {}
          }
        },
        "addresses": {
          "@context": {
            "deliveryPoint": {},
            "city": {},
            "administrativeArea": {},
            "postalCode": {},
            "country": {}
          }
        },
        "hoursOfService": {},
        "contactInstructions": {}
      },
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "rights": "dcat:rights",
    "concepts": {
      "@id": "thns:concepts",
      "@container": "@set",
      "@context": {
        "name": "thns:name",
        "id": "thns:id",
        "url": "@id"
      }
    },
    "scheme": "thns:scheme",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "geojson": "https://purl.org/geojson/vocab#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "w3ctime": "http://www.w3.org/2006/time#",
    "dctype": "http://purl.org/dc/dcmitype/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/themes-shacl/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/themes)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/themes-shacl`

