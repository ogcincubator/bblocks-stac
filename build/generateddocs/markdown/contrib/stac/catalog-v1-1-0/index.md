
# STAC Catalog (v1.1.0) (Schema)

`ogc.contrib.stac.catalog-v1-1-0` *v1.1.0*

A SpatioTemporal Asset Catalogs (STAC) catalog, version 1.1.0.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Catalog v1.1.0
Ref to STAC example using version (1.1.0)
#### json
```json
{
  "id": "examples",
  "type": "Catalog",
  "title": "Example Catalog",
  "stac_version": "1.1.0",
  "description": "This catalog is a simple demonstration of an example catalog that is used to organize a hierarchy of collections and their items.",
  "links": [
    {
      "rel": "root",
      "href": "./catalog.json",
      "type": "application/json"
    },
    {
      "rel": "child",
      "href": "./extensions-collection/collection.json",
      "type": "application/json",
      "title": "Collection Demonstrating STAC Extensions"
    },
    {
      "rel": "child",
      "href": "./collection-only/collection.json",
      "type": "application/json",
      "title": "Collection with no items (standalone)"
    },
    {
      "rel": "child",
      "href": "./collection-only/collection-with-schemas.json",
      "type": "application/json",
      "title": "Collection with no items (standalone with JSON Schemas)"
    },
    {
      "rel": "item",
      "href": "./collectionless-item.json",
      "type": "application/json",
      "title": "Item that does not have a collection (not recommended, but allowed by the spec)"
    },
    {
      "rel": "self",
      "href": "https://raw.githubusercontent.com/radiantearth/stac-spec/v1.1.0/examples/catalog.json",
      "type": "application/json"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog-v1-1-0/context.jsonld",
  "id": "examples",
  "type": "Catalog",
  "title": "Example Catalog",
  "stac_version": "1.1.0",
  "description": "This catalog is a simple demonstration of an example catalog that is used to organize a hierarchy of collections and their items.",
  "links": [
    {
      "rel": "root",
      "href": "./catalog.json",
      "type": "application/json"
    },
    {
      "rel": "child",
      "href": "./extensions-collection/collection.json",
      "type": "application/json",
      "title": "Collection Demonstrating STAC Extensions"
    },
    {
      "rel": "child",
      "href": "./collection-only/collection.json",
      "type": "application/json",
      "title": "Collection with no items (standalone)"
    },
    {
      "rel": "child",
      "href": "./collection-only/collection-with-schemas.json",
      "type": "application/json",
      "title": "Collection with no items (standalone with JSON Schemas)"
    },
    {
      "rel": "item",
      "href": "./collectionless-item.json",
      "type": "application/json",
      "title": "Item that does not have a collection (not recommended, but allowed by the spec)"
    },
    {
      "rel": "self",
      "href": "https://raw.githubusercontent.com/radiantearth/stac-spec/v1.1.0/examples/catalog.json",
      "type": "application/json"
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
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<https://example.com/stac/example1/examples> a stac:Catalog ;
    dcterms:description "This catalog is a simple demonstration of an example catalog that is used to organize a hierarchy of collections and their items." ;
    dcterms:title "Example Catalog" ;
    rdfs:seeAlso [ rdfs:label "Item that does not have a collection (not recommended, but allowed by the spec)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/example1/collectionless-item.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/example1/catalog.json> ],
        [ rdfs:label "Collection Demonstrating STAC Extensions" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/extensions-collection/collection.json> ],
        [ rdfs:label "Collection with no items (standalone)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/collection-only/collection.json> ],
        [ rdfs:label "Collection with no items (standalone with JSON Schemas)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/collection-only/collection-with-schemas.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://raw.githubusercontent.com/radiantearth/stac-spec/v1.1.0/examples/catalog.json> ] ;
    stac:version "1.1.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: STAC Catalog V1.1.0
allOf:
- $ref: https://schemas.stacspec.org/v1.1.0/catalog-spec/json-schema/catalog.json
- $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog/schema.yaml
- type: object
  properties:
    stac_version:
      title: STAC version
      type: string
      const: 1.1.0
  required:
  - stac_version
x-bblocks-metadata:
  itemIdentifier: ogc.contrib.stac.catalog-v1-1-0
  register: https://ogcincubator.github.io/bblocks-stac/build/register.json
  version: 1.1.0
  dateOfLastChange: '2026-11-25'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog-v1-1-0/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog-v1-1-0/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "stac_version": "stac:version",
    "stac_extensions": "stac:hasExtension",
    "type": "@type",
    "id": "@id",
    "links": {
      "@context": {
        "href": {
          "@id": "oa:hasTarget",
          "@type": "@id"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "title": "rdfs:label",
        "hreflang": "dct:language",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "title": "dct:title",
    "description": "dct:description",
    "keywords": "dct:subject",
    "Catalog": "stac:Catalog",
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog-v1-1-0/context.jsonld)

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/catalog-v1-1-0`

