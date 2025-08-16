
# STAC Machine Learning Model (Schema)

`ogc.contrib.stac.extensions.mlm` *v0.1*

STAC Machine Learning Model (MLM) Extension to describe ML models, their training details, and inference runtime requirements.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Collection
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json"
  ],
  "type": "Collection",
  "id": "ml-model-examples",
  "title": "Machine Learning Model examples",
  "description": "Collection of items contained in the Machine Learning Model examples.",
  "license": "Apache-2.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -7.882190080512502,
          37.13739173208318,
          27.911651652899923,
          58.21798141355221
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1900-01-01T00:00:00Z",
          "9999-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "item_assets": {
    "weights": {
      "title": "model weights",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "1900-01-01T00:00:00Z",
      "maximum": "9999-12-31T23:59:59Z"
    }
  },
  "links": [
    {
      "href": "collection.json",
      "rel": "self"
    },
    {
      "href": "item_basic.json",
      "rel": "item"
    },
    {
      "href": "item_bands_expression.json",
      "rel": "item"
    },
    {
      "href": "item_datacube_variables.json",
      "rel": "item"
    },
    {
      "href": "item_eo_bands.json",
      "rel": "item"
    },
    {
      "href": "item_eo_and_raster_bands.json",
      "rel": "item"
    },
    {
      "href": "item_eo_bands_summarized.json",
      "rel": "item"
    },
    {
      "href": "item_raster_bands.json",
      "rel": "item"
    },
    {
      "href": "item_multi_io.json",
      "rel": "item"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json"
  ],
  "type": "Collection",
  "id": "ml-model-examples",
  "title": "Machine Learning Model examples",
  "description": "Collection of items contained in the Machine Learning Model examples.",
  "license": "Apache-2.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -7.882190080512502,
          37.13739173208318,
          27.911651652899923,
          58.21798141355221
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1900-01-01T00:00:00Z",
          "9999-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "item_assets": {
    "weights": {
      "title": "model weights",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "1900-01-01T00:00:00Z",
      "maximum": "9999-12-31T23:59:59Z"
    }
  },
  "links": [
    {
      "href": "collection.json",
      "rel": "self"
    },
    {
      "href": "item_basic.json",
      "rel": "item"
    },
    {
      "href": "item_bands_expression.json",
      "rel": "item"
    },
    {
      "href": "item_datacube_variables.json",
      "rel": "item"
    },
    {
      "href": "item_eo_bands.json",
      "rel": "item"
    },
    {
      "href": "item_eo_and_raster_bands.json",
      "rel": "item"
    },
    {
      "href": "item_eo_bands_summarized.json",
      "rel": "item"
    },
    {
      "href": "item_raster_bands.json",
      "rel": "item"
    },
    {
      "href": "item_multi_io.json",
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

<https://example.com/stac/mlm/example-1/ml-model-examples> a <https://example.com/stac/mlm/example-1/Collection> ;
    rdfs:label "Machine Learning Model examples" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_multi_io.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_and_raster_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_bands_expression.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_basic.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_bands_summarized.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_raster_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_datacube_variables.json> ] .


```


### Item Basic
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.4.0/schema.json"
  ],
  "type": "Feature",
  "id": "example-model",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Basic STAC Item with only the MLM extension and no other extension cross-references.",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "example-model",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:input": [
      {
        "name": "Model with RGB input that does not refer to any band.",
        "bands": [],
        "input": {
          "shape": [
            -1,
            3,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "channel",
            "height",
            "width"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            1
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "uint8"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "BACKGROUND",
            "description": "Background non-city.",
            "color_hint": [
              0,
              0,
              0
            ]
          },
          {
            "value": 1,
            "name": "CITY",
            "description": "A city is detected.",
            "color_hint": [
              0,
              0,
              255
            ]
          }
        ]
      }
    ]
  },
  "assets": {
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
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_basic.json",
      "type": "application/geo+json"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.4.0/schema.json"
  ],
  "type": "Feature",
  "id": "example-model",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Basic STAC Item with only the MLM extension and no other extension cross-references.",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "example-model",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:input": [
      {
        "name": "Model with RGB input that does not refer to any band.",
        "bands": [],
        "input": {
          "shape": [
            -1,
            3,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "channel",
            "height",
            "width"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            1
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "uint8"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "BACKGROUND",
            "description": "Background non-city.",
            "color_hint": [
              0,
              0,
              0
            ]
          },
          {
            "value": 1,
            "name": "CITY",
            "description": "A city is detected.",
            "color_hint": [
              0,
              0,
              255
            ]
          }
        ]
      }
    ]
  },
  "assets": {
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
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_basic.json",
      "type": "application/geo+json"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <mlm:> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-1/example-model> a geojson:Feature ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/collection.json> ],
        [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_basic.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:assets <https://example.com/stac/mlm/example-1/model> ;
    ns1:architecture "ResNet" ;
    ns1:input [ ] ;
    ns1:name "example-model" ;
    ns1:output [ ] ;
    ns1:tasks "classification" .

<https://example.com/stac/mlm/example-1/model> a <https://example.com/stac/mlm/example-1/text/html> ;
    rdfs:label "Pytorch weights checkpoint" ;
    oa:hasTarget <https://huggingface.co/example/model-card> ;
    ns1:artifact_type "torch.save" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: MLM extension
description: STAC MLM for STAC Items and STAC Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-v1-0-0/schema.yaml
- $ref: https://stac-extensions.github.io/mlm/v1.4.0/schema.json
x-jsonld-extra-terms:
  raster:bands:
    x-jsonld-id: https://w3id.org/ogc/stac/raster/bands
    x-jsonld-context:
      '@vocab': https://w3id.org/ogc/stac/raster/
  raster:range:
    x-jsonld-id: https://w3id.org/ogc/stac/raster/range
    x-jsonld-container: '@list'
x-jsonld-prefixes:
  raster: https://w3id.org/ogc/stac/raster/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/schema.yaml)


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
    "assets": {
      "@id": "stac:assets",
      "@container": "@id"
    },
    "raster:bands": {
      "@id": "raster:bands",
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/raster/"
      }
    },
    "raster:range": {
      "@id": "raster:range",
      "@container": "@list"
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "raster": "https://w3id.org/ogc/stac/raster/",
    "geojson": "https://purl.org/geojson/vocab#",
    "stac": "https://w3id.org/ogc/stac/core/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/mlm)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/mlm`

