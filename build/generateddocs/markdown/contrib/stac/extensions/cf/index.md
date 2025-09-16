
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
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <http://stacspec.org/ontology/core#> .

<https://example.com/stac/cf/example-1/collection> a <https://example.com/stac/cf/example-1/Collection> ;
    rdfs:label "Collection with an Item" ;
    stac:description "A description" ;
    stac:extent [ ] ;
    stac:license "Apache-2.0" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/cf/example-1/item.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/collection.json> ] .


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
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <cf:> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <https://w3id.org/ogc/stac/core/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <http://stacspec.org/ontology/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/cf/example-2/item> a geojson:Feature ;
    ns1:parameter [ ],
        [ ],
        [ ] ;
    stac:datetime "2020-12-11T22:38:32+00:00"^^xsd:dateTime ;
    rdfs:seeAlso [ ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ],
        [ ns2:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ],
        [ ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/item.json> ],
        [ ns2:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ] ;
    geojson:bbox ( 1.729e+02 1.3e+00 173 1.4e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729e+02 1.3e+00 ) ( 173 1.3e+00 ) ( 173 1.4e+00 ) ( 1.729e+02 1.4e+00 ) ( 1.729e+02 1.3e+00 ) ) ) ] ;
    ns3:assets <https://example.com/stac/cf/example-2/sea_ice_surface_temperature>,
        <https://example.com/stac/cf/example-2/sea_surface_temperature> .

<https://example.com/stac/cf/example-2/sea_ice_surface_temperature> a <https://example.com/stac/cf/example-2/application/netcdf> ;
    ns1:parameter [ ],
        [ ] ;
    oa:hasTarget <https://example.com/examples/sea_ice_surface_temperature.nc> .

<https://example.com/stac/cf/example-2/sea_surface_temperature> a <https://example.com/stac/cf/example-2/application/netcdf> ;
    ns1:parameter [ ],
        [ ] ;
    oa:hasTarget <https://example.com/examples/sea_surface_temperature.nc> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CF Extension
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-v1-0-0/schema.yaml
- $ref: https://stac-extensions.github.io/cf/v0.2.0/schema.json
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "rel": {
      "@context": {
        "@base": "http://www.iana.org/assignments/relation/"
      },
      "@id": "http://www.iana.org/assignments/relation",
      "@type": "@id"
    },
    "type": "@type",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "id": "@id",
    "properties": "@nest",
    "geometry": "geojson:geometry",
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
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
    "links": {
      "@context": {
        "type": "dct:type"
      },
      "@id": "rdfs:seeAlso"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "uriTemplate": {
      "@type": "xsd:string",
      "@id": "oa:hasTarget"
    },
    "description": "stac:description",
    "license": "stac:license",
    "extent": "stac:extent",
    "datetime": {
      "@id": "stac:datetime",
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
    "assets": {
      "@id": "https://w3id.org/ogc/stac/core/assets",
      "@container": "@id"
    },
    "media_type": "stac:mediaType",
    "themes": {
      "@id": "thns:schemes",
      "@container": "@set"
    },
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
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "geojson": "https://purl.org/geojson/vocab#",
    "stac": "http://stacspec.org/ontology/core#",
    "geo": "http://www.opengis.net/ont/geosparql#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
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

