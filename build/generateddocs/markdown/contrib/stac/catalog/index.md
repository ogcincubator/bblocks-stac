
# STAC Catalog (Schema)

`ogc.contrib.stac.catalog` *v1.1.0*

A SpatioTemporal Asset Catalogs (STAC) catalog.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Catalog v1.1.0
Ref to STAC example from current version (1.1.0)
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
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog/context.jsonld",
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
    rdfs:seeAlso [ rdfs:label "Collection with no items (standalone)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/collection-only/collection.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://raw.githubusercontent.com/radiantearth/stac-spec/v1.1.0/examples/catalog.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/example1/catalog.json> ],
        [ rdfs:label "Collection Demonstrating STAC Extensions" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/extensions-collection/collection.json> ],
        [ rdfs:label "Collection with no items (standalone with JSON Schemas)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/collection-only/collection-with-schemas.json> ],
        [ rdfs:label "Item that does not have a collection (not recommended, but allowed by the spec)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/example1/collectionless-item.json> ] ;
    stac:version "1.1.0" .


```


### STAC Catalog v1.0.0
Ref to STAC example using version (1.0.0)
#### json
```json
{
  "id": "examples",
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
      "title": "Collection with no items (standalone)"
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
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog/context.jsonld",
  "id": "examples",
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
      "title": "Collection with no items (standalone)"
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
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<https://example.com/stac/example1/examples> a stac:Catalog ;
    dcterms:description "This catalog is a simple demonstration of an example catalog that is used to organize a hierarchy of collections and their items." ;
    dcterms:title "Example Catalog" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/example1/catalog.json> ],
        [ rdfs:label "Collection with no items (standalone)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/example1/collectionless-item.json> ],
        [ rdfs:label "Collection with no items (standalone with JSON Schemas)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/collection-only/collection-with-schemas.json> ],
        [ rdfs:label "Collection Demonstrating STAC Extensions" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/extensions-collection/collection.json> ],
        [ rdfs:label "Collection with no items (standalone)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/example1/collection-only/collection.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://raw.githubusercontent.com/radiantearth/stac-spec/v1.0.0/examples/catalog.json> ] ;
    stac:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: STAC Catalog Specification
description: This object represents Catalogs in a SpatioTemporal Asset Catalog (adapted
  from official specs)
allOf:
- $ref: '#/definitions/catalog'
- $ref: https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/json-schema/common.json
definitions:
  catalog:
    title: STAC Catalog
    description: These are the fields specific to a STAC Catalog.
    type: object
    $comment: title and description are validated through the common metadata. stac_version
      is required by the version-specific building blocks.
    required:
    - type
    - id
    - description
    - links
    properties:
      stac_extensions:
        title: STAC extensions
        type: array
        uniqueItems: true
        items:
          title: Reference to a JSON Schema
          type: string
          format: iri
        x-jsonld-id: https://w3id.org/ogc/stac/core/hasExtension
      type:
        title: Type of STAC entity
        const: Catalog
        x-jsonld-id: '@type'
      id:
        title: Identifier
        type: string
        minLength: 1
        x-jsonld-id: '@id'
      links:
        type: array
        items:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
x-jsonld-extra-terms:
  stac_version: https://w3id.org/ogc/stac/core/version
  Catalog: https://w3id.org/ogc/stac/core/Catalog
  title: http://purl.org/dc/terms/title
  description: http://purl.org/dc/terms/description
  keywords: http://purl.org/dc/terms/subject
x-jsonld-prefixes:
  stac: https://w3id.org/ogc/stac/core/
  dct: http://purl.org/dc/terms/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
x-bblocks-metadata:
  itemIdentifier: ogc.contrib.stac.catalog
  register: https://ogcincubator.github.io/bblocks-stac/build/register.json
  version: 1.1.0
  dateOfLastChange: '2026-11-25'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "stac_extensions": "stac:hasExtension",
    "type": "@type",
    "id": "@id",
    "links": {
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
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "title": "dct:title",
    "description": "dct:description",
    "keywords": "dct:subject",
    "stac_version": "stac:version",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/catalog/context.jsonld)

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)
* [STAC Catalog Specification](https://github.com/radiantearth/stac-spec/blob/master/catalog-spec/catalog-spec.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/catalog`

