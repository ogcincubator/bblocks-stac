
# STAC Collection (v1.0.0) (Schema)

`ogc.contrib.stac.collection-v1-0-0` *v1.0.0*

A SpatioTemporal Asset Catalogs (STAC) collection.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example STAC Collection
STAC no longer publishes v1.0.0 examples - to be explored.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: STAC Collection V1.0.0
allOf:
- $ref: https://schemas.stacspec.org/v1.0.0/collection-spec/json-schema/collection.json
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-features/build/annotated/api/features/v1/schemas/collection/schema.yaml
- type: object
  properties:
    links:
      type: array
      items:
        $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml
      x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
x-jsonld-extra-terms:
  stac_version: https://w3id.org/ogc/stac/core/version
  stac_extensions: https://w3id.org/ogc/stac/core/hasExtension
  id: '@id'
  title: http://purl.org/dc/terms/title
  type: '@type'
  description: http://purl.org/dc/terms/description
  keywords: http://purl.org/dc/terms/subject
  license: http://purl.org/dc/terms/license
  extent: http://purl.org/dc/terms/extent
  datetime:
    x-jsonld-id: http://purl.org/dc/terms/date
    x-jsonld-type: xsd:dateTime
  start_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/start_datetime
    x-jsonld-type: xsd:dateTime
  end_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/end_datetime
    x-jsonld-type: xsd:dateTime
  assets:
    x-jsonld-id: https://w3id.org/ogc/stac/core/hasAsset
    x-jsonld-container: '@set'
    x-jsonld-context:
      thumbnail:
        '@id': https://w3id.org/ogc/stac/core/thumbnail
      overview: https://w3id.org/ogc/stac/core/overview
      data: https://w3id.org/ogc/stac/core/data
      metadata: https://w3id.org/ogc/stac/core/metadata
      type: http://purl.org/dc/terms/format
      title: http://purl.org/dc/terms/title
      roles:
        '@id': https://w3id.org/ogc/stac/core/roles
        '@container': '@set'
  providers: https://w3id.org/ogc/stac/core/hasProvider
  media_type: http://purl.org/dc/terms/format
x-jsonld-prefixes:
  stac: https://w3id.org/ogc/stac/core/
  dct: http://purl.org/dc/terms/
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml)


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
    "type": "dct:type",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "links": "rdfs:seeAlso",
    "stac_version": "stac:version",
    "stac_extensions": "stac:hasExtension",
    "id": "@id",
    "description": "dct:description",
    "keywords": "dct:subject",
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
      "@id": "stac:hasAsset",
      "@container": "@set",
      "@context": {
        "thumbnail": "stac:thumbnail",
        "overview": "stac:overview",
        "data": "stac:data",
        "metadata": "stac:metadata",
        "type": "dct:format",
        "title": "dct:title",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      }
    },
    "providers": "stac:hasProvider",
    "media_type": "dct:format",
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/context.jsonld)

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/collection-v1-0-0`

