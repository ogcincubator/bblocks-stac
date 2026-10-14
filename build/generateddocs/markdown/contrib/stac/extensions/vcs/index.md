
# STAC VCS Extension (Schema)

`ogc.contrib.stac.extensions.vcs` *v0.1.0*

STAC VCS Extension for describing version control system references.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC item with an application source repository link
#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/vcs/v0.1.0/schema.json"
  ],
  "id": "vcs-example",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "title": "VCS extension example"
  },
  "links": [
    {
      "rel": "self",
      "href": "https://stac-extensions.github.io/vcs/v0.1.0/examples/item.json",
      "type": "application/json"
    },
    {
      "rel": "vcs",
      "href": "https://github.com/stac-extensions/vcs.git",
      "title": "Git source repository",
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "abc1234",
      "vcs:tag": "v1.0.0"
    }
  ],
  "assets": {}
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/vcs/context.jsonld",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/vcs/v0.1.0/schema.json"
  ],
  "id": "vcs-example",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "title": "VCS extension example"
  },
  "links": [
    {
      "rel": "self",
      "href": "https://stac-extensions.github.io/vcs/v0.1.0/examples/item.json",
      "type": "application/json"
    },
    {
      "rel": "vcs",
      "href": "https://github.com/stac-extensions/vcs.git",
      "title": "Git source repository",
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "abc1234",
      "vcs:tag": "v1.0.0"
    }
  ],
  "assets": {}
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix vcs: <https://w3id.org/ogc/stac/vcs/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/vcs/item/vcs-example> a geojson:Feature ;
    dcterms:date "2025-01-01T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:title "VCS extension example" ;
    rdfs:seeAlso [ rdfs:label "Git source repository" ;
            ns1:relation <http://www.iana.org/assignments/relation/vcs> ;
            oa:hasTarget <https://github.com/stac-extensions/vcs.git> ;
            vcs:branch "main"^^xsd:string ;
            vcs:revision "abc1234"^^xsd:string ;
            vcs:tag "v1.0.0"^^xsd:string ;
            vcs:type "git"^^xsd:string ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://stac-extensions.github.io/vcs/v0.1.0/examples/item.json> ] ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/vcs/v0.1.0/schema.json" ;
    stac:version "1.1.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: VCS extension
description: STAC VCS Extension for Catalogs, Collections, Items, Assets and Links.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/vcs/v0.1.0/schema.json
x-jsonld-extra-terms:
  vcs:type:
    x-jsonld-id: https://w3id.org/ogc/stac/vcs/type
    x-jsonld-type: xsd:string
  vcs:branch:
    x-jsonld-id: https://w3id.org/ogc/stac/vcs/branch
    x-jsonld-type: xsd:string
  vcs:revision:
    x-jsonld-id: https://w3id.org/ogc/stac/vcs/revision
    x-jsonld-type: xsd:string
  vcs:tag:
    x-jsonld-id: https://w3id.org/ogc/stac/vcs/tag
    x-jsonld-type: xsd:string
x-jsonld-prefixes:
  vcs: https://w3id.org/ogc/stac/vcs/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/vcs/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/vcs/schema.yaml)


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
    "vcs:type": {
      "@id": "vcs:type",
      "@type": "xsd:string"
    },
    "vcs:branch": {
      "@id": "vcs:branch",
      "@type": "xsd:string"
    },
    "vcs:revision": {
      "@id": "vcs:revision",
      "@type": "xsd:string"
    },
    "vcs:tag": {
      "@id": "vcs:tag",
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
    "vcs": "https://w3id.org/ogc/stac/vcs/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/vcs/context.jsonld)

## Sources

* [STAC VCS Extension](https://github.com/stac-extensions/vcs/tree/v0.1.0)
* [STAC Application Extension](https://github.com/stac-extensions/application/tree/v0.1.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/vcs`

