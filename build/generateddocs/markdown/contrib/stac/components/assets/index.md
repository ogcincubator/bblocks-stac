
# Assets object (Schema)

`ogc.contrib.stac.components.assets` *v0.1*

Assets sub-schema reused in items and collections

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Core asset types
This is the simple item  asset example from the STAC specification.  

#### json
```json
{
  "assets": {
    "visual": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ]
    },
    "thumbnail": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg",
      "title": "Thumbnail",
      "type": "image/jpeg",
      "roles": [
        "thumbnail"
      ]
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/components/assets/context.jsonld",
  "assets": {
    "visual": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ]
    },
    "thumbnail": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg",
      "title": "Thumbnail",
      "type": "image/jpeg",
      "roles": [
        "thumbnail"
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix stac: <https://w3id.org/ogc/stac/core/> .

[] stac:hasAsset [ ] .


```


### Extended asset types
Includes asset types not defined by core

#### json
```json
{
  "assets": {
    "visual": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ]
    },
    "thumbnail": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg",
      "title": "Thumbnail",
      "type": "image/jpeg",
      "roles": [
        "thumbnail"
      ]
    },
    "model": {
      "href": "https://huggingface.co/example/model-card",
      "title": "Pytorch weights checkpoint",
      "description": "Example model.",
      "type": "text/html",
      "roles": [
        "mlm:model"
      ],
      "mlm:artifact_type": "torch.save"
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/components/assets/context.jsonld",
  "assets": {
    "visual": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ]
    },
    "thumbnail": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg",
      "title": "Thumbnail",
      "type": "image/jpeg",
      "roles": [
        "thumbnail"
      ]
    },
    "model": {
      "href": "https://huggingface.co/example/model-card",
      "title": "Pytorch weights checkpoint",
      "description": "Example model.",
      "type": "text/html",
      "roles": [
        "mlm:model"
      ],
      "mlm:artifact_type": "torch.save"
    }
  }
}
```

#### ttl
```ttl
@prefix stac: <https://w3id.org/ogc/stac/core/> .

[] stac:hasAsset [ ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: STAC Asset
type: object
description: This object represents a set of assets
properties:
  assets:
    $ref: '#/definitions/assets'
    x-jsonld-id: https://w3id.org/ogc/stac/core/hasAsset
    x-jsonld-container: '@set'
    x-jsonld-extra-terms:
      type: http://purl.org/dc/terms/format
      title: http://purl.org/dc/terms/title
      description: http://purl.org/dc/terms/description
      roles:
        x-jsonld-id: https://w3id.org/ogc/stac/core/roles
        x-jsonld-container: '@set'
definitions:
  assets:
    title: Asset links
    description: Links to assets
    type: object
    additionalProperties:
      $ref: '#/definitions/asset'
  asset:
    allOf:
    - type: object
      required:
      - href
      properties:
        href:
          title: Asset reference
          type: string
          format: iri-reference
          minLength: 1
        title:
          title: Asset title
          type: string
        description:
          title: Asset description
          type: string
        type:
          title: Asset type
          type: string
        roles:
          title: Asset roles
          type: array
          items:
            type: string
x-jsonld-prefixes:
  stac: https://w3id.org/ogc/stac/core/
  dct: http://purl.org/dc/terms/
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/components/assets/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/components/assets/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "assets": {
      "@context": {
        "type": "dct:format",
        "title": "dct:title",
        "description": "dct:description",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/components/assets/context.jsonld)

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/components/assets`

