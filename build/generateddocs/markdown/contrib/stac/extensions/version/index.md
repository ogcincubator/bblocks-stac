
# STAC Versioning Indicators Extension (Schema)

`ogc.contrib.stac.extensions.version` *v1.2.0*

STAC Versioning Indicators Extension for Items, Collections, Catalogs and Assets.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Versioning Indicators item
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/version/v1.2.0/schema.json"
  ],
  "id": "MERRAclim.2_5m_min_80s",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180,
          -90
        ],
        [
          180,
          -90
        ],
        [
          180,
          90
        ],
        [
          -180,
          90
        ],
        [
          -180,
          -90
        ]
      ]
    ]
  },
  "bbox": [
    -180,
    -90,
    180,
    90
  ],
  "properties": {
    "version": "1",
    "title": "MERRAclim. 2_5m_min_80s",
    "description": "MERRAclim Dataset. 19 global bioclimatic variables from the 1980s decade at 2.5 arcminutes resolution in GEOtiff format. The humidity version used is the min. The variables have been built using the same protocol as WorldClim with data from MERRA. Temperature layers (BIO1-BIO11) are in degree Celsius multiplied by 10, humidity layers (BIO12-BIO19) are in kg of water/kg of air multiplied by 100000.",
    "datetime": "1985-07-01T00:00:00Z"
  },
  "collection": "merraclim",
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/item.json"
    },
    {
      "rel": "collection",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/collection.json"
    },
    {
      "rel": "parent",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/collection.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/catalog.json"
    },
    {
      "rel": "latest-version",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v2/item.json"
    }
  ],
  "assets": {
    "primary": {
      "href": "https://datadryad.org/stash/downloads/file_stream/100467",
      "type": "application/zip",
      "title": "MERRAclim. 2_5m_min_80s"
    }
  }
}
```

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/version/v1.2.0/schema.json"
  ],
  "id": "merraclim",
  "type": "Collection",
  "title": "MERRAclim",
  "description": "A high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling.",
  "license": "CC0-1.0",
  "version": "1",
  "deprecated": true,
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
          "1980-01-01T00:00:00Z",
          "2009-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/collection.json"
    },
    {
      "rel": "item",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/item.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/catalog.json"
    },
    {
      "rel": "latest-version",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v2/collection.json"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/version/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/version/v1.2.0/schema.json"
  ],
  "id": "merraclim",
  "type": "Collection",
  "title": "MERRAclim",
  "description": "A high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling.",
  "license": "CC0-1.0",
  "version": "1",
  "deprecated": true,
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
          "1980-01-01T00:00:00Z",
          "2009-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/collection.json"
    },
    {
      "rel": "item",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/item.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/catalog.json"
    },
    {
      "rel": "latest-version",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v2/collection.json"
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
@prefix ver: <https://w3id.org/ogc/stac/version/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/version/collection/merraclim> a <https://example.com/stac/version/collection/Collection> ;
    dcterms:description "A high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling." ;
    dcterms:extent [ ] ;
    dcterms:title "MERRAclim" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v1/item.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://datadryad.org/resource/doi:10.5061/dryad.s2v81/catalog.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/latest-version> ;
            oa:hasTarget <https://datadryad.org/resource/doi:10.5061/dryad.s2v81/v2/collection.json> ] ;
    dcat:license "CC0-1.0" ;
    stac:hasExtension "https://stac-extensions.github.io/version/v1.2.0/schema.json" ;
    stac:version "1.0.0" ;
    ver:deprecated true ;
    ver:version "1"^^xsd:string .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Versioning Indicators extension
description: STAC Versioning Indicators Extension for STAC resources and assets.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/version/v1.2.0/schema.json
x-jsonld-extra-terms:
  version:
    x-jsonld-id: https://w3id.org/ogc/stac/version/version
    x-jsonld-type: xsd:string
  deprecated:
    x-jsonld-id: https://w3id.org/ogc/stac/version/deprecated
    x-jsonld-type: xsd:boolean
  experimental:
    x-jsonld-id: https://w3id.org/ogc/stac/version/experimental
    x-jsonld-type: xsd:boolean
  latest-version:
    x-jsonld-id: https://w3id.org/ogc/stac/version/latest-version
    x-jsonld-type: '@id'
  predecessor-version:
    x-jsonld-id: https://w3id.org/ogc/stac/version/predecessor-version
    x-jsonld-type: '@id'
  successor-version:
    x-jsonld-id: https://w3id.org/ogc/stac/version/successor-version
    x-jsonld-type: '@id'
  version-history:
    x-jsonld-id: https://w3id.org/ogc/stac/version/version-history
    x-jsonld-type: '@id'
  has-version:
    x-jsonld-id: https://w3id.org/ogc/stac/version/has-version
    x-jsonld-type: '@id'
  is-version-of:
    x-jsonld-id: https://w3id.org/ogc/stac/version/is-version-of
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  ver: https://w3id.org/ogc/stac/version/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/version/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/version/schema.yaml)


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
    "version": {
      "@id": "ver:version",
      "@type": "xsd:string"
    },
    "deprecated": {
      "@id": "ver:deprecated",
      "@type": "xsd:boolean"
    },
    "experimental": {
      "@id": "ver:experimental",
      "@type": "xsd:boolean"
    },
    "latest-version": {
      "@id": "ver:latest-version",
      "@type": "@id"
    },
    "predecessor-version": {
      "@id": "ver:predecessor-version",
      "@type": "@id"
    },
    "successor-version": {
      "@id": "ver:successor-version",
      "@type": "@id"
    },
    "version-history": {
      "@id": "ver:version-history",
      "@type": "@id"
    },
    "has-version": {
      "@id": "ver:has-version",
      "@type": "@id"
    },
    "is-version-of": {
      "@id": "ver:is-version-of",
      "@type": "@id"
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "ver": "https://w3id.org/ogc/stac/version/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/version/context.jsonld)

## Sources

* [STAC Versioning Indicators Extension](https://github.com/stac-extensions/version/tree/v1.2.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/version`

