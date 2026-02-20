
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
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
  ],
  "type": "Collection",
  "id": "collection",
  "title": "Collection with an Item",
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
  "item_assets": {
    "sea_surface_temperature": {
      "type": "application/netcdf",
      "cf:parameter": [
        {
          "name": "sea_surface_temperature",
          "unit": "K"
        },
        {
          "name": "depth",
          "unit": "m"
        }
      ]
    },
    "sea_ice_surface_temperature": {
      "type": "application/netcdf",
      "cf:parameter": [
        {
          "name": "sea_ice_surface_temperature",
          "unit": "K"
        },
        {
          "name": "depth",
          "unit": "m"
        }
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "2015-06-23T00:00:00Z",
      "maximum": "2019-07-10T13:44:56Z"
    },
    "cf:parameter": [
      {
        "name": "sea_surface_temperature",
        "unit": "K"
      },
      {
        "name": "sea_ice_surface_temperature",
        "unit": "K"
      },
      {
        "name": "depth",
        "unit": "m"
      }
    ]
  },
  "links": [
    {
      "href": "https://example.com/examples/collection.json",
      "rel": "self"
    },
    {
      "href": "./item.json",
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
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
  ],
  "type": "Collection",
  "id": "collection",
  "title": "Collection with an Item",
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
  "item_assets": {
    "sea_surface_temperature": {
      "type": "application/netcdf",
      "cf:parameter": [
        {
          "name": "sea_surface_temperature",
          "unit": "K"
        },
        {
          "name": "depth",
          "unit": "m"
        }
      ]
    },
    "sea_ice_surface_temperature": {
      "type": "application/netcdf",
      "cf:parameter": [
        {
          "name": "sea_ice_surface_temperature",
          "unit": "K"
        },
        {
          "name": "depth",
          "unit": "m"
        }
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "2015-06-23T00:00:00Z",
      "maximum": "2019-07-10T13:44:56Z"
    },
    "cf:parameter": [
      {
        "name": "sea_surface_temperature",
        "unit": "K"
      },
      {
        "name": "sea_ice_surface_temperature",
        "unit": "K"
      },
      {
        "name": "depth",
        "unit": "m"
      }
    ]
  },
  "links": [
    {
      "href": "https://example.com/examples/collection.json",
      "rel": "self"
    },
    {
      "href": "./item.json",
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
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<https://example.com/stac/cf/example-1/collection> a <https://example.com/stac/cf/example-1/Collection> ;
    dcterms:description "A description" ;
    dcterms:extent [ ] ;
    dcterms:title "Collection with an Item" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/cf/example-1/item.json> ] ;
    dcat:license "Apache-2.0" ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json" ;
    stac:version "1.0.0" .


```


### An example demonstrating CF extension fields in a STAC item.
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
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
    "cf:parameter": [
      {
        "name": "sea_surface_temperature",
        "unit": "K"
      },
      {
        "name": "sea_ice_surface_temperature",
        "unit": "K"
      },
      {
        "name": "depth",
        "unit": "m"
      }
    ]
  },
  "links": [
    {
      "href": "https://example.com/examples/item.json",
      "rel": "self"
    },
    {
      "href": "./collection.json",
      "rel": "collection"
    },
    {
      "href": "./collection.json",
      "rel": "parent"
    },
    {
      "href": "./collection.json",
      "rel": "root"
    }
  ],
  "assets": {
    "sea_surface_temperature": {
      "href": "https://example.com/examples/sea_surface_temperature.nc",
      "type": "application/netcdf",
      "cf:parameter": [
        {
          "name": "sea_surface_temperature",
          "unit": "K"
        },
        {
          "name": "depth",
          "unit": "m"
        }
      ]
    },
    "sea_ice_surface_temperature": {
      "href": "https://example.com/examples/sea_ice_surface_temperature.nc",
      "type": "application/netcdf",
      "cf:parameter": [
        {
          "name": "sea_ice_surface_temperature",
          "unit": "K"
        },
        {
          "name": "depth",
          "unit": "m"
        }
      ]
    }
  },
  "collection": "collection"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
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
    "cf:parameter": [
      {
        "name": "sea_surface_temperature",
        "unit": "K"
      },
      {
        "name": "sea_ice_surface_temperature",
        "unit": "K"
      },
      {
        "name": "depth",
        "unit": "m"
      }
    ]
  },
  "links": [
    {
      "href": "https://example.com/examples/item.json",
      "rel": "self"
    },
    {
      "href": "./collection.json",
      "rel": "collection"
    },
    {
      "href": "./collection.json",
      "rel": "parent"
    },
    {
      "href": "./collection.json",
      "rel": "root"
    }
  ],
  "assets": {
    "sea_surface_temperature": {
      "href": "https://example.com/examples/sea_surface_temperature.nc",
      "type": "application/netcdf",
      "cf:parameter": [
        {
          "name": "sea_surface_temperature",
          "unit": "K"
        },
        {
          "name": "depth",
          "unit": "m"
        }
      ]
    },
    "sea_ice_surface_temperature": {
      "href": "https://example.com/examples/sea_ice_surface_temperature.nc",
      "type": "application/netcdf",
      "cf:parameter": [
        {
          "name": "sea_ice_surface_temperature",
          "unit": "K"
        },
        {
          "name": "depth",
          "unit": "m"
        }
      ]
    }
  },
  "collection": "collection"
}
```

#### ttl
```ttl
@prefix cf: <https://w3id.org/ogc/stac/cf/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/cf/example-2/item> a geojson:Feature ;
    dcterms:date "2020-12-11T22:38:32+00:00"^^xsd:dateTime ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/item.json> ] ;
    geojson:bbox ( 1.729e+02 1.3e+00 173 1.4e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729e+02 1.3e+00 ) ( 173 1.3e+00 ) ( 173 1.4e+00 ) ( 1.729e+02 1.4e+00 ) ( 1.729e+02 1.3e+00 ) ) ) ] ;
    cf:parameter [ qudt:hasUnit "m" ;
            cf:name "depth" ],
        [ qudt:hasUnit "K" ;
            cf:name "sea_ice_surface_temperature" ],
        [ qudt:hasUnit "K" ;
            cf:name "sea_surface_temperature" ] ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json" ;
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
    "assets": {
      "@context": {
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
    "keywords": {
      "@id": "dcat:keyword",
      "@container": "@set"
    },
    "license": "dcat:license",
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "start_datetime": {
      "@id": "stac:start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:end_datetime",
      "@type": "xsd:dateTime"
    },
    "providers": "stac:hasProvider",
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
    "title": {
      "@id": "dct:title",
      "@container": "@set"
    },
    "description": {
      "@id": "dct:description",
      "@container": "@set"
    },
    "name": "cf:name",
    "unit": {
      "@id": "qudt:hasUnit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
    },
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
    "created": "dct:created",
    "updated": "dct:modified",
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

