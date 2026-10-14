
# STAC File Info Extension (Schema)

`ogc.contrib.stac.extensions.file` *v2.1.0*

STAC File Info Extension for Items, Collections, Catalogs and Assets.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC File Info item
#### json
```json
{
  "id": "S1A_EW_GRDM_1SSH_20181103T235855_20181103T235955_024430_02AD5D_5616",
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/file/v2.1.0/schema.json"
  ],
  "bbox": [
    -70.275032,
    -64.72924,
    -65.087479,
    -51.105831
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -67.071648,
          -64.72924
        ],
        [
          -65.087479,
          -56.674374
        ],
        [
          -68.033211,
          -51.105831
        ],
        [
          -70.275032,
          -59.805672
        ],
        [
          -67.071648,
          -64.72924
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2018-11-03T23:58:55Z"
  },
  "assets": {
    "noises": {
      "href": "./annotation/calibration/noise-s1a-ew-grd-hh-20181103t235855-20181103t235955-024430-02ad5d-001.xml",
      "title": "Calibration Schema",
      "type": "text/xml",
      "file:checksum": "90e40210a30d1711e81a4b11ef67b28744321659",
      "file:local_path": "S1A_EW_GRDM_1SSH_20181103T235855_20181103T235955_024430_02AD5D_5616.SAFE/annotation/calibration/noise-s1a-ew-grd-hh-20181103t235855-20181103t235955-024430-02ad5d-001.xml"
    },
    "calibrations": {
      "href": "./annotation/calibration/calibration-s1a-ew-grd-hh-20181103t235855-20181103t235955-024430-02ad5d-001.xml",
      "title": "Noise Schema",
      "type": "text/xml",
      "file:checksum": "90e402104fc5351af67db0b8f1746efe421a05e4",
      "file:local_path": "S1A_EW_GRDM_1SSH_20181103T235855_20181103T235955_024430_02AD5D_5616.SAFE/annotation/calibration/calibration-s1a-ew-grd-hh-20181103t235855-20181103t235955-024430-02ad5d-001.xml"
    },
    "products": {
      "href": "./annotation/s1a-ew-grd-hh-20181103t235855-20181103t235955-024430-02ad5d-001.xml",
      "title": "Product Schema",
      "type": "text/xml",
      "file:checksum": "90e402107a7f2588a85362b9beea2a12d4514d45"
    },
    "measurement": {
      "href": "./measurement/s1a-ew-grd-hh-20181103t235855-20181103t235955-024430-02ad5d-001.tiff",
      "title": "Measurements",
      "type": "image/tiff",
      "sar:polarizations": [
        "HH"
      ],
      "file:byte_order": "little-endian",
      "file:size": 209715200,
      "file:header_size": 4096,
      "file:checksum": "90e40210163700a8a6501eccd00b6d3b44ddaed0"
    },
    "thumbnail": {
      "href": "./preview/quick-look.png",
      "title": "Thumbnail",
      "type": "image/png",
      "file:byte_order": "big-endian",
      "file:size": 146484,
      "file:checksum": "90e40210f52acd32b09769d3b1871b420789456c"
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "https://example.com/collections/sentinel-1/items/S1A_EW_GRDM_1SSH_20181103T235855_20181103T235955_024430_02AD5D_5616"
    },
    {
      "rel": "parent",
      "href": "https://example.com/collections/sentinel-1",
      "file:checksum": "11146d97123fd2c02dec9a1b6d3b13136dbe600cf966"
    },
    {
      "rel": "root",
      "href": "https://example.com/collections",
      "file:checksum": "1114fa4b9d69fdddc7c1be7bed9440621400b383b43f"
    }
  ]
}
```

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/file/v2.1.0/schema.json"
  ],
  "id": "example",
  "type": "Collection",
  "title": "File Example",
  "description": "This examples shows how to use the file extension for collection assets.",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -180,
          -90,
          180,
          90
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2012-01-15T12:00:00Z",
          "2014-12-15T12:00:00Z"
        ]
      ]
    }
  },
  "license": "Apache-2.0",
  "links": [
    {
      "href": "https://example.com",
      "type": "text/html",
      "rel": "about"
    }
  ],
  "assets": {
    "thumbnail": {
      "href": "logo.png",
      "title": "A preview image for visualization.",
      "type": "image/png",
      "roles": [
        "thumbnail"
      ],
      "file:checksum": "90e4021044a8995dd50b6657a037a7839304535b",
      "file:size": 153600
    }
  }
}

```

#### json
```json
{
  "id": "examples",
  "stac_extensions": [
    "https://stac-extensions.github.io/file/v2.1.0/schema.json"
  ],
  "type": "Catalog",
  "title": "Example Catalog",
  "stac_version": "1.0.0",
  "description": "This catalog is a simple demonstration of an example catalog that is used to organize a hierarchy of collections and their items.",
  "links": [
    {
      "rel": "root",
      "href": "./catalog.json",
      "type": "application/json"
    },
    {
      "rel": "item",
      "href": "./some-item.json",
      "type": "application/json",
      "title": "Some item",
      "file:size": 8675309
    },
    {
      "rel": "self",
      "href": "https://raw.githubusercontent.com/radiantearth/stac-spec/v1.0.0/examples/catalog.json",
      "type": "application/json"
    }
  ]
}


```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/file/context.jsonld",
  "id": "examples",
  "stac_extensions": [
    "https://stac-extensions.github.io/file/v2.1.0/schema.json"
  ],
  "type": "Catalog",
  "title": "Example Catalog",
  "stac_version": "1.0.0",
  "description": "This catalog is a simple demonstration of an example catalog that is used to organize a hierarchy of collections and their items.",
  "links": [
    {
      "rel": "root",
      "href": "./catalog.json",
      "type": "application/json"
    },
    {
      "rel": "item",
      "href": "./some-item.json",
      "type": "application/json",
      "title": "Some item",
      "file:size": 8675309
    },
    {
      "rel": "self",
      "href": "https://raw.githubusercontent.com/radiantearth/stac-spec/v1.0.0/examples/catalog.json",
      "type": "application/json"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix file: <https://w3id.org/ogc/stac/file/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/file/catalog/examples> a <https://example.com/stac/file/catalog/Catalog> ;
    dcterms:description "This catalog is a simple demonstration of an example catalog that is used to organize a hierarchy of collections and their items." ;
    dcterms:title "Example Catalog" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/file/catalog/catalog.json> ],
        [ rdfs:label "Some item" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/file/catalog/some-item.json> ;
            file:size "8675309"^^xsd:nonNegativeInteger ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://raw.githubusercontent.com/radiantearth/stac-spec/v1.0.0/examples/catalog.json> ] ;
    stac:hasExtension "https://stac-extensions.github.io/file/v2.1.0/schema.json" ;
    stac:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: File Info extension
description: STAC File Info Extension for Items, Collections, Catalogs and Assets.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
  - type: object
    required:
    - id
    - type
    - stac_version
    - description
    - links
    properties:
      id:
        type: string
      type:
        const: Catalog
      stac_version:
        type: string
      description:
        type: string
      links:
        type: array
- $ref: https://stac-extensions.github.io/file/v2.1.0/schema.json
x-jsonld-extra-terms:
  file:byte_order:
    x-jsonld-id: https://w3id.org/ogc/stac/file/byte_order
    x-jsonld-type: xsd:string
  file:checksum:
    x-jsonld-id: https://w3id.org/ogc/stac/file/checksum
    x-jsonld-type: xsd:string
  file:header_size:
    x-jsonld-id: https://w3id.org/ogc/stac/file/header_size
    x-jsonld-type: xsd:nonNegativeInteger
  file:size:
    x-jsonld-id: https://w3id.org/ogc/stac/file/size
    x-jsonld-type: xsd:nonNegativeInteger
  file:values:
    x-jsonld-id: https://w3id.org/ogc/stac/file/values
    x-jsonld-type: '@json'
  file:local_path:
    x-jsonld-id: https://w3id.org/ogc/stac/file/local_path
    x-jsonld-type: xsd:string
x-jsonld-prefixes:
  file: https://w3id.org/ogc/stac/file/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/file/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/file/schema.yaml)


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
      "@id": "dcat:keyword",
      "@container": "@set"
    },
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
    "created": "dct:created",
    "updated": "dct:modified",
    "license": "dcat:license",
    "providers": "stac:hasProvider",
    "assets": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/assets/",
        "href": "@id",
        "type": "dct:format",
        "roles": {
          "@id": "stac:hasAssetroles",
          "@type": "xsd:string",
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
    "file:byte_order": {
      "@id": "file:byte_order",
      "@type": "xsd:string"
    },
    "file:checksum": {
      "@id": "file:checksum",
      "@type": "xsd:string"
    },
    "file:header_size": {
      "@id": "file:header_size",
      "@type": "xsd:nonNegativeInteger"
    },
    "file:size": {
      "@id": "file:size",
      "@type": "xsd:nonNegativeInteger"
    },
    "file:values": {
      "@id": "file:values",
      "@type": "@json"
    },
    "file:local_path": {
      "@id": "file:local_path",
      "@type": "xsd:string"
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "file": "https://w3id.org/ogc/stac/file/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/file/context.jsonld)

## Sources

* [STAC File Info Extension](https://github.com/stac-extensions/file/tree/v2.1.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/file`

