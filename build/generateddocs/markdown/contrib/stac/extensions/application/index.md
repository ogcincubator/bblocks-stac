
# STAC Application Extension (Schema)

`ogc.contrib.stac.extensions.application` *v0.1.0*

STAC Application Extension for describing software applications in Items, Collections and Catalogs.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Application item
#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/application/v0.1.0/schema.json"
  ],
  "id": "esa-cci-permafrost",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "datetime": "2025-03-17T14:30:23Z",
    "type": "workflow",
    "title": "ESA CCI permafrost",
    "description": "cube generation workflow for esa-cci-permafrost",
    "application:container": "Jupyter Notebook",
    "application:languages": [
      "Python"
    ]
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Open Science Catalog"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Workflows"
    },
    {
      "rel": "self",
      "href": "https://esa-earthcode.github.io/open-science-catalog-metadata/workflows/esa-cci-permafrost/record.json",
      "type": "application/json"
    },
    {
      "rel": "related",
      "href": "../../projects/deep-earth-system-data-lab/collection.json",
      "type": "application/json",
      "title": "Project: DeepESDL"
    },
    {
      "rel": "child",
      "href": "../../experiments/esa-cci-permafrost/record.json",
      "type": "application/json",
      "title": "ESA CCI permafrost"
    },
    {
      "rel": "related",
      "href": "../../themes/cryosphere/catalog.json",
      "type": "application/json",
      "title": "Theme: Cryosphere"
    },
    {
      "rel": "vcs",
      "title": "Git source repository",
      "href": "https://github.com/deepesdl/cube-gen.git",
      "vcs:type": "git",
      "vcs:branch": "main"
    },
    {
      "rel": "application",
      "title": "Jupyter Notebook: Create CCI Permafrost cube",
      "href": "https://github.com/deepesdl/cube-gen/blob/main/Permafrost/Create-CCI-Permafrost-cube-EarthCODE.ipynb",
      "file:local_path": "Permafrost/Create-CCI-Permafrost-cube-EarthCODE.ipynb",
      "type": "application/x-ipynb+json",
      "application:container": "Jupyter Notebook",
      "application:languages": [
        "Python"
      ],
      "jupyter:kernel": {
        "name": "deepesdl-xcube-1.8.3",
        "pythonVersion": "3.11",
        "envFile": "https://github.com/deepesdl/cube-gen/blob/main/Permafrost/environment.yml"
      }
    },
    {
      "rel": "example",
      "title": "Cube generation script",
      "href": "https://github.com/deepesdl/cube-gen/blob/main/Permafrost/cube.py",
      "type": "text/x-python",
      "application:entrypoint": "generate_cube",
      "application:languages": [
        "Python"
      ]
    },
    {
      "rel": "application-platform",
      "title": "DeepESDL platform",
      "href": "https://deep.earthsystemdatalab.net/",
      "type": "text/html"
    },
    {
      "rel": "related",
      "href": "https://deep.earthsystemdatalab.net/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdeepesdl%2Fcube-gen&urlpath=lab%2Ftree%2Fcube-gen%2FPermafrost%2FCreate-CCI-Permafrost-cube-EarthCODE.ipynb&branch=main",
      "title": "Open notebook on the DeepESDL platform"
    }
  ],
  "assets": {}
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/application/context.jsonld",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/application/v0.1.0/schema.json"
  ],
  "id": "esa-cci-permafrost",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "datetime": "2025-03-17T14:30:23Z",
    "type": "workflow",
    "title": "ESA CCI permafrost",
    "description": "cube generation workflow for esa-cci-permafrost",
    "application:container": "Jupyter Notebook",
    "application:languages": [
      "Python"
    ]
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Open Science Catalog"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Workflows"
    },
    {
      "rel": "self",
      "href": "https://esa-earthcode.github.io/open-science-catalog-metadata/workflows/esa-cci-permafrost/record.json",
      "type": "application/json"
    },
    {
      "rel": "related",
      "href": "../../projects/deep-earth-system-data-lab/collection.json",
      "type": "application/json",
      "title": "Project: DeepESDL"
    },
    {
      "rel": "child",
      "href": "../../experiments/esa-cci-permafrost/record.json",
      "type": "application/json",
      "title": "ESA CCI permafrost"
    },
    {
      "rel": "related",
      "href": "../../themes/cryosphere/catalog.json",
      "type": "application/json",
      "title": "Theme: Cryosphere"
    },
    {
      "rel": "vcs",
      "title": "Git source repository",
      "href": "https://github.com/deepesdl/cube-gen.git",
      "vcs:type": "git",
      "vcs:branch": "main"
    },
    {
      "rel": "application",
      "title": "Jupyter Notebook: Create CCI Permafrost cube",
      "href": "https://github.com/deepesdl/cube-gen/blob/main/Permafrost/Create-CCI-Permafrost-cube-EarthCODE.ipynb",
      "file:local_path": "Permafrost/Create-CCI-Permafrost-cube-EarthCODE.ipynb",
      "type": "application/x-ipynb+json",
      "application:container": "Jupyter Notebook",
      "application:languages": [
        "Python"
      ],
      "jupyter:kernel": {
        "name": "deepesdl-xcube-1.8.3",
        "pythonVersion": "3.11",
        "envFile": "https://github.com/deepesdl/cube-gen/blob/main/Permafrost/environment.yml"
      }
    },
    {
      "rel": "example",
      "title": "Cube generation script",
      "href": "https://github.com/deepesdl/cube-gen/blob/main/Permafrost/cube.py",
      "type": "text/x-python",
      "application:entrypoint": "generate_cube",
      "application:languages": [
        "Python"
      ]
    },
    {
      "rel": "application-platform",
      "title": "DeepESDL platform",
      "href": "https://deep.earthsystemdatalab.net/",
      "type": "text/html"
    },
    {
      "rel": "related",
      "href": "https://deep.earthsystemdatalab.net/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdeepesdl%2Fcube-gen&urlpath=lab%2Ftree%2Fcube-gen%2FPermafrost%2FCreate-CCI-Permafrost-cube-EarthCODE.ipynb&branch=main",
      "title": "Open notebook on the DeepESDL platform"
    }
  ],
  "assets": {}
}
```

#### ttl
```ttl
@prefix application: <https://w3id.org/ogc/stac/application/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <jupyter:> .
@prefix ns3: <file:> .
@prefix ns4: <vcs:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/application/item/esa-cci-permafrost> a <https://example.com/stac/application/item/workflow>,
        geojson:Feature ;
    dcterms:date "2025-03-17T14:30:23+00:00"^^xsd:dateTime ;
    dcterms:description "cube generation workflow for esa-cci-permafrost" ;
    dcterms:title "ESA CCI permafrost" ;
    rdfs:seeAlso [ rdfs:label "Workflows" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/application/catalog.json> ],
        [ rdfs:label "Theme: Cryosphere" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/themes/cryosphere/catalog.json> ],
        [ rdfs:label "Cube generation script" ;
            dcterms:type "text/x-python" ;
            ns1:relation <http://www.iana.org/assignments/relation/example> ;
            oa:hasTarget <https://github.com/deepesdl/cube-gen/blob/main/Permafrost/cube.py> ;
            application:entrypoint "generate_cube"^^xsd:string ;
            application:languages "Python"^^xsd:string ],
        [ rdfs:label "Open Science Catalog" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/catalog.json> ],
        [ rdfs:label "ESA CCI permafrost" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/experiments/esa-cci-permafrost/record.json> ],
        [ rdfs:label "Git source repository" ;
            ns1:relation <http://www.iana.org/assignments/relation/vcs> ;
            oa:hasTarget <https://github.com/deepesdl/cube-gen.git> ;
            ns4:branch "main" ;
            ns4:type "git" ],
        [ rdfs:label "Open notebook on the DeepESDL platform" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://deep.earthsystemdatalab.net/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdeepesdl%2Fcube-gen&urlpath=lab%2Ftree%2Fcube-gen%2FPermafrost%2FCreate-CCI-Permafrost-cube-EarthCODE.ipynb&branch=main> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://esa-earthcode.github.io/open-science-catalog-metadata/workflows/esa-cci-permafrost/record.json> ],
        [ rdfs:label "Jupyter Notebook: Create CCI Permafrost cube" ;
            ns3:local_path "Permafrost/Create-CCI-Permafrost-cube-EarthCODE.ipynb" ;
            dcterms:type "application/x-ipynb+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/application> ;
            oa:hasTarget <https://github.com/deepesdl/cube-gen/blob/main/Permafrost/Create-CCI-Permafrost-cube-EarthCODE.ipynb> ;
            application:container "Jupyter Notebook"^^xsd:string ;
            application:languages "Python"^^xsd:string ;
            ns2:kernel [ ] ],
        [ rdfs:label "DeepESDL platform" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/application-platform> ;
            oa:hasTarget <https://deep.earthsystemdatalab.net/> ],
        [ rdfs:label "Project: DeepESDL" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/projects/deep-earth-system-data-lab/collection.json> ] ;
    application:container "Jupyter Notebook"^^xsd:string ;
    application:languages "Python"^^xsd:string ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/application/v0.1.0/schema.json" ;
    stac:version "1.1.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Application extension
description: STAC Application Extension for Items, Collections and Catalogs.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/application/v0.1.0/schema.json
x-jsonld-extra-terms:
  application:container:
    x-jsonld-id: https://w3id.org/ogc/stac/application/container
    x-jsonld-type: xsd:string
  application:entrypoint:
    x-jsonld-id: https://w3id.org/ogc/stac/application/entrypoint
    x-jsonld-type: xsd:string
  application:languages:
    x-jsonld-id: https://w3id.org/ogc/stac/application/languages
    x-jsonld-container: '@set'
    x-jsonld-type: xsd:string
x-jsonld-prefixes:
  application: https://w3id.org/ogc/stac/application/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/application/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/application/schema.yaml)


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
    "application:container": {
      "@id": "application:container",
      "@type": "xsd:string"
    },
    "application:entrypoint": {
      "@id": "application:entrypoint",
      "@type": "xsd:string"
    },
    "application:languages": {
      "@id": "application:languages",
      "@container": "@set",
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
    "application": "https://w3id.org/ogc/stac/application/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/application/context.jsonld)

## Sources

* [STAC Application Extension](https://github.com/stac-extensions/application/tree/v0.1.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/application`

