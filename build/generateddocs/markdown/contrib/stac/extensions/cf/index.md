
# STAC CF Extension (Schema)

`ogc.contrib.stac.extensions.cf` *v0.2.0*

CF Extension to the SpatioTemporal Asset Catalog (STAC) specification. Allows to provide the Standard Name Table based on the CF metadata convention.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### A simple Collection demonstrating CF extension fields in a Collection.
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.3.0/schema.json"
  ],
  "type": "Collection",
  "id": "collection",
  "title": "A title",
  "description": "A description",
  "license": "Apache-2.0",
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
  "assets": {
    "example": {
      "href": "https://example.com/examples/file.xyz"
    }
  },
  "item_assets": {
    "data": {
      "roles": [
        "data"
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "2015-06-23T00:00:00Z",
      "maximum": "2019-07-10T13:44:56Z"
    },
    "cube:dimensions": {
      "time_interval1": {
        "type": "temporal",
        "description": "time interval that cell_methods is applied over",
        "values": [
          -24
        ],
        "unit": "h"
      },
      "vertical_dimension1": {
        "type": "spatial",
        "axis": "z",
        "cf:standard_name": "height",
        "description": "Height above ground level",
        "unit": "m",
        "values": [
          10
        ]
      },
      "time_interval2": {
        "type": "temporal",
        "description": "time interval that cell_methods is applied over",
        "values": [
          -60
        ],
        "unit": "min"
      },
      "vertical_dimension2": {
        "type": "spatial",
        "axis": "z",
        "cf:standard_name": "height",
        "description": "Air pressure",
        "unit": "hPa",
        "values": [
          500
        ]
      }
    },
    "cube:variables": {
      "sea_surface_temperature": {
        "type": "data",
        "cf:standard_name": "sea_surface_temperature",
        "description": "Average temperature on sea surface for preceding 24 hours",
        "unit": "K",
        "cf:cell_methods": [
          "mean"
        ],
        "dimensions": [
          "time_interval1"
        ]
      },
      "wind_speed_at_10m": {
        "type": "data",
        "cf:standard_name": "wind_speed",
        "description": "minimum wind speed in 1 hour at 10 m agl",
        "unit": "kt",
        "cf:cell_methods": [
          null,
          "minimum"
        ],
        "dimensions": [
          "vertical_dimension1",
          "time_interval2"
        ]
      },
      "temp_at_500hPa": {
        "type": "data",
        "cf:standard_name": "air_temperature",
        "description": "air temperature at 500 hPa",
        "unit": "degC",
        "dimensions": [
          "vertical_dimension2"
        ]
      }
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
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.3.0/schema.json"
  ],
  "type": "Collection",
  "id": "collection",
  "title": "A title",
  "description": "A description",
  "license": "Apache-2.0",
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
  "assets": {
    "example": {
      "href": "https://example.com/examples/file.xyz"
    }
  },
  "item_assets": {
    "data": {
      "roles": [
        "data"
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "2015-06-23T00:00:00Z",
      "maximum": "2019-07-10T13:44:56Z"
    },
    "cube:dimensions": {
      "time_interval1": {
        "type": "temporal",
        "description": "time interval that cell_methods is applied over",
        "values": [
          -24
        ],
        "unit": "h"
      },
      "vertical_dimension1": {
        "type": "spatial",
        "axis": "z",
        "cf:standard_name": "height",
        "description": "Height above ground level",
        "unit": "m",
        "values": [
          10
        ]
      },
      "time_interval2": {
        "type": "temporal",
        "description": "time interval that cell_methods is applied over",
        "values": [
          -60
        ],
        "unit": "min"
      },
      "vertical_dimension2": {
        "type": "spatial",
        "axis": "z",
        "cf:standard_name": "height",
        "description": "Air pressure",
        "unit": "hPa",
        "values": [
          500
        ]
      }
    },
    "cube:variables": {
      "sea_surface_temperature": {
        "type": "data",
        "cf:standard_name": "sea_surface_temperature",
        "description": "Average temperature on sea surface for preceding 24 hours",
        "unit": "K",
        "cf:cell_methods": [
          "mean"
        ],
        "dimensions": [
          "time_interval1"
        ]
      },
      "wind_speed_at_10m": {
        "type": "data",
        "cf:standard_name": "wind_speed",
        "description": "minimum wind speed in 1 hour at 10 m agl",
        "unit": "kt",
        "cf:cell_methods": [
          null,
          "minimum"
        ],
        "dimensions": [
          "vertical_dimension1",
          "time_interval2"
        ]
      },
      "temp_at_500hPa": {
        "type": "data",
        "cf:standard_name": "air_temperature",
        "description": "air temperature at 500 hPa",
        "unit": "degC",
        "dimensions": [
          "vertical_dimension2"
        ]
      }
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
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <https://w3id.org/ogc/stac/assets/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<https://example.com/stac/cf/example-1/collection> a <https://example.com/stac/cf/example-1/Collection> ;
    dcterms:description "A description" ;
    dcterms:extent [ ] ;
    dcterms:title "A title" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/examples/item.json> ] ;
    dcat:license "Apache-2.0" ;
    stac:hasAsset [ ns2:example [ oa:hasTarget <https://example.com/examples/file.xyz> ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.3.0/schema.json" ;
    stac:version "1.0.0" .


```


### An example demonstrating CF extension fields in a STAC item.
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.3.0/schema.json"
  ],
  "type": "Feature",
  "id": "item",
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
          172.9,
          1.3
        ],
        [
          173,
          1.3
        ],
        [
          173,
          1.4
        ],
        [
          172.9,
          1.4
        ],
        [
          172.9,
          1.3
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32Z",
    "cube:dimensions": {
      "time_interval1": {
        "type": "temporal",
        "description": "time interval that cell_methods is applied over",
        "values": [
          -24
        ],
        "unit": "h"
      },
      "vertical_dimension1": {
        "type": "spatial",
        "axis": "z",
        "cf:standard_name": "height",
        "description": "Height above ground level",
        "unit": "m",
        "values": [
          10
        ]
      },
      "time_interval2": {
        "type": "temporal",
        "description": "time interval that cell_methods is applied over",
        "values": [
          -60
        ],
        "unit": "min"
      },
      "vertical_dimension2": {
        "type": "spatial",
        "axis": "z",
        "cf:standard_name": "height",
        "description": "Air pressure",
        "unit": "hPa",
        "values": [
          500
        ]
      }
    },
    "cube:variables": {
      "sea_surface_temperature": {
        "type": "data",
        "cf:standard_name": "sea_surface_temperature",
        "description": "Average temperature on sea surface for preceding 24 hours",
        "unit": "K",
        "cf:cell_methods": [
          "mean"
        ],
        "dimensions": [
          "time_interval1"
        ]
      },
      "wind_speed_at_10m": {
        "type": "data",
        "cf:standard_name": "wind_speed",
        "description": "minimum wind speed in 1 hour at 10 m agl",
        "unit": "kt",
        "cf:cell_methods": [
          null,
          "minimum"
        ],
        "dimensions": [
          "vertical_dimension1",
          "time_interval2"
        ]
      },
      "temp_at_500hPa": {
        "type": "data",
        "cf:standard_name": "air_temperature",
        "description": "air temperature at 500 hPa",
        "unit": "degC",
        "dimensions": [
          "vertical_dimension2"
        ]
      }
    }
  },
  "links": [
    {
      "href": "https://example.com/examples/item.json",
      "rel": "self"
    }
  ],
  "assets": {
    "data": {
      "href": "https://example.com/examples/file.xyz"
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.3.0/schema.json"
  ],
  "type": "Feature",
  "id": "item",
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
          172.9,
          1.3
        ],
        [
          173,
          1.3
        ],
        [
          173,
          1.4
        ],
        [
          172.9,
          1.4
        ],
        [
          172.9,
          1.3
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32Z",
    "cube:dimensions": {
      "time_interval1": {
        "type": "temporal",
        "description": "time interval that cell_methods is applied over",
        "values": [
          -24
        ],
        "unit": "h"
      },
      "vertical_dimension1": {
        "type": "spatial",
        "axis": "z",
        "cf:standard_name": "height",
        "description": "Height above ground level",
        "unit": "m",
        "values": [
          10
        ]
      },
      "time_interval2": {
        "type": "temporal",
        "description": "time interval that cell_methods is applied over",
        "values": [
          -60
        ],
        "unit": "min"
      },
      "vertical_dimension2": {
        "type": "spatial",
        "axis": "z",
        "cf:standard_name": "height",
        "description": "Air pressure",
        "unit": "hPa",
        "values": [
          500
        ]
      }
    },
    "cube:variables": {
      "sea_surface_temperature": {
        "type": "data",
        "cf:standard_name": "sea_surface_temperature",
        "description": "Average temperature on sea surface for preceding 24 hours",
        "unit": "K",
        "cf:cell_methods": [
          "mean"
        ],
        "dimensions": [
          "time_interval1"
        ]
      },
      "wind_speed_at_10m": {
        "type": "data",
        "cf:standard_name": "wind_speed",
        "description": "minimum wind speed in 1 hour at 10 m agl",
        "unit": "kt",
        "cf:cell_methods": [
          null,
          "minimum"
        ],
        "dimensions": [
          "vertical_dimension1",
          "time_interval2"
        ]
      },
      "temp_at_500hPa": {
        "type": "data",
        "cf:standard_name": "air_temperature",
        "description": "air temperature at 500 hPa",
        "unit": "degC",
        "dimensions": [
          "vertical_dimension2"
        ]
      }
    }
  },
  "links": [
    {
      "href": "https://example.com/examples/item.json",
      "rel": "self"
    }
  ],
  "assets": {
    "data": {
      "href": "https://example.com/examples/file.xyz"
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <cube:> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <https://w3id.org/ogc/stac/assets/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/cf/example-2/item> a geojson:Feature ;
    ns1:dimensions [ ] ;
    ns1:variables [ ] ;
    dcterms:date "2020-12-11T22:38:32+00:00"^^xsd:dateTime ;
    rdfs:seeAlso [ ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/item.json> ] ;
    geojson:bbox ( 1.729e+02 1.3e+00 173 1.4e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729e+02 1.3e+00 ) ( 173 1.3e+00 ) ( 173 1.4e+00 ) ( 1.729e+02 1.4e+00 ) ( 1.729e+02 1.3e+00 ) ) ) ] ;
    stac:hasAsset [ ns3:data [ oa:hasTarget <https://example.com/examples/file.xyz> ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.3.0/schema.json" ;
    stac:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CF Extension
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/cf/v0.2.0/schema.json
x-jsonld-extra-terms:
  name: https://w3id.org/ogc/stac/cf/name
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/hasUnit
    x-jsonld-context:
      '@base': http://qudt.org/vocab/unit/
x-jsonld-prefixes:
  cf: https://w3id.org/ogc/stac/cf/
  qudt: http://qudt.org/schema/qudt/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "stac_extensions": "stac:hasExtension",
    "type": "@type",
    "id": "@id",
    "extent": "dct:extent",
    "links": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
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
      "@container": "@set",
      "@id": "dcat:keyword"
    },
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "license": "dcat:license",
    "assets": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/assets/",
        "type": "dct:format",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      },
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
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
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
    "time": "dct:temporal",
    "linkTemplates": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:format",
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
    "name": "cf:name",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "cf": "https://w3id.org/ogc/stac/cf/",
    "qudt": "http://qudt.org/schema/qudt/",
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
    "thns": "https://w3id.org/ogc/stac/themes/",
    "language": "rec:language",
    "languages": {
      "@container": "@set",
      "@id": "rec:languages"
    },
    "resourceLanguages": {
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
        },
        "scheme": "thns:scheme"
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
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "rights": "dcat:rights",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/cf)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/cf`

