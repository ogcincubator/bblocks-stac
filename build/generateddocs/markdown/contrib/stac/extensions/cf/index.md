
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
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<https://example.com/stac/cf/example-1/collection> rdfs:label "Collection with an Item" ;
    dcterms:description "A description" ;
    dcterms:extent [ ] ;
    dcterms:format "Collection" ;
    dcterms:license "Apache-2.0" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/cf/example-1/item.json> ] .


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

<https://example.com/stac/cf/example-2/item> dcterms:date "2020-12-11T22:38:32+00:00"^^xsd:dateTime ;
    dcterms:format "Feature" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/examples/item.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/cf/example-2/collection.json> ] ;
    geojson:bbox ( 1.729e+02 1.3e+00 173 1.4e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729e+02 1.3e+00 ) ( 173 1.3e+00 ) ( 173 1.4e+00 ) ( 1.729e+02 1.4e+00 ) ( 1.729e+02 1.3e+00 ) ) ) ] ;
    cf:parameter [ qudt:hasUnit "K" ;
            cf:name "sea_surface_temperature" ],
        [ qudt:hasUnit "K" ;
            cf:name "sea_ice_surface_temperature" ],
        [ qudt:hasUnit "m" ;
            cf:name "depth" ] ;
    stac:assets <https://example.com/stac/cf/example-2/sea_ice_surface_temperature>,
        <https://example.com/stac/cf/example-2/sea_surface_temperature> .

<https://example.com/stac/cf/example-2/sea_ice_surface_temperature> dcterms:format "application/netcdf" ;
    oa:hasTarget <https://example.com/examples/sea_ice_surface_temperature.nc> ;
    cf:parameter [ qudt:hasUnit "m" ;
            cf:name "depth" ],
        [ qudt:hasUnit "K" ;
            cf:name "sea_ice_surface_temperature" ] .

<https://example.com/stac/cf/example-2/sea_surface_temperature> dcterms:format "application/netcdf" ;
    oa:hasTarget <https://example.com/examples/sea_surface_temperature.nc> ;
    cf:parameter [ qudt:hasUnit "m" ;
            cf:name "depth" ],
        [ qudt:hasUnit "K" ;
            cf:name "sea_surface_temperature" ] .


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
    "type": "dct:format",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
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
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "type": "@type"
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
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
    "description": "dct:description",
    "license": "dct:license",
    "extent": "dct:extent",
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
    "assets": {
      "@id": "stac:assets",
      "@container": "@id",
      "@context": {
        "thumbnail": "stac:thumbnail",
        "overview": "stac:overview",
        "data": "stac:data",
        "metadata": "stac:metadata",
        "title": "dct:title",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      }
    },
    "media_type": "dct:format",
    "name": "cf:name",
    "unit": {
      "@id": "qudt:hasUnit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "cf": "https://w3id.org/ogc/stac/cf/",
    "qudt": "http://qudt.org/schema/qudt/",
    "geojson": "https://purl.org/geojson/vocab#",
    "stac": "https://w3id.org/ogc/stac/core/",
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

