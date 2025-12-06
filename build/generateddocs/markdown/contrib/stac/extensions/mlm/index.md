
# STAC Machine Learning Model (Schema)

`ogc.contrib.stac.extensions.mlm` *v1.4.0*

STAC Machine Learning Model (MLM) Extension to describe ML models, their training details, and inference runtime requirements.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Item Basic
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.0/schema.json"
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
    "https://stac-extensions.github.io/mlm/v1.5.0/schema.json"
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
@prefix : <https://w3id.org/ogc/stac/assets/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <mlm:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-1/example-model> dcterms:description "Basic STAC Item with only the MLM extension and no other extension cross-references." ;
    dcterms:format "Feature" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/collection.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_basic.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    :collection "ml-model-examples" ;
    :end_datetime "9999-12-31T23:59:59Z" ;
    :start_datetime "1900-01-01T00:00:00Z" ;
    stac:hasAsset [ :model [ dcterms:description "Example model." ;
                    dcterms:format "text/html" ;
                    dcterms:title "Pytorch weights checkpoint" ;
                    oa:hasTarget <https://huggingface.co/example/model-card> ;
                    stac:roles "mlm:model" ;
                    ns2:artifact_type "torch.save" ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/mlm/v1.5.0/schema.json" ;
    stac:version "1.0.0" ;
    ns2:architecture "ResNet" ;
    ns2:input [ :input [ :data_type "float32" ;
                    :dim_order "batch",
                        "channel",
                        "height",
                        "width" ;
                    :shape -1,
                        3,
                        64 ] ;
            :name "Model with RGB input that does not refer to any band." ] ;
    ns2:name "example-model" ;
    ns2:output [ :classification_classes [ dcterms:description "A city is detected." ;
                    :color_hint 0,
                        255 ;
                    :name "CITY" ;
                    :value 1 ],
                [ dcterms:description "Background non-city." ;
                    :color_hint 0 ;
                    :name "BACKGROUND" ;
                    :value 0 ] ;
            :name "classification" ;
            :result [ :data_type "uint8" ;
                    :dim_order "batch",
                        "class" ;
                    :shape -1,
                        1 ] ;
            :tasks "classification" ] ;
    ns2:tasks "classification" .


```


### Item Raster Bands
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.0/schema.json"
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
    "https://stac-extensions.github.io/mlm/v1.5.0/schema.json"
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
@prefix : <https://w3id.org/ogc/stac/assets/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <mlm:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-1/example-model> dcterms:description "Basic STAC Item with only the MLM extension and no other extension cross-references." ;
    dcterms:format "Feature" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/collection.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_basic.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    :collection "ml-model-examples" ;
    :end_datetime "9999-12-31T23:59:59Z" ;
    :start_datetime "1900-01-01T00:00:00Z" ;
    stac:hasAsset [ :model [ dcterms:description "Example model." ;
                    dcterms:format "text/html" ;
                    dcterms:title "Pytorch weights checkpoint" ;
                    oa:hasTarget <https://huggingface.co/example/model-card> ;
                    stac:roles "mlm:model" ;
                    ns2:artifact_type "torch.save" ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/mlm/v1.5.0/schema.json" ;
    stac:version "1.0.0" ;
    ns2:architecture "ResNet" ;
    ns2:input [ :input [ :data_type "float32" ;
                    :dim_order "batch",
                        "channel",
                        "height",
                        "width" ;
                    :shape -1,
                        3,
                        64 ] ;
            :name "Model with RGB input that does not refer to any band." ] ;
    ns2:name "example-model" ;
    ns2:output [ :classification_classes [ dcterms:description "Background non-city." ;
                    :color_hint 0 ;
                    :name "BACKGROUND" ;
                    :value 0 ],
                [ dcterms:description "A city is detected." ;
                    :color_hint 0,
                        255 ;
                    :name "CITY" ;
                    :value 1 ] ;
            :name "classification" ;
            :result [ :data_type "uint8" ;
                    :dim_order "batch",
                        "class" ;
                    :shape -1,
                        1 ] ;
            :tasks "classification" ] ;
    ns2:tasks "classification" .


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
- $ref: https://stac-extensions.github.io/mlm/v1.5.0/schema.json
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
    "stac_extensions": "stac:hasExtension",
    "type": "dct:format",
    "id": "@id",
    "extent": {
      "@context": {
        "spatial": {},
        "temporal": {
          "@context": {
            "interval": {}
          }
        }
      },
      "@id": "dct:extent"
    },
    "item_assets": {
      "@context": {
        "type": "@type"
      }
    },
    "links": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "anchor": {},
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "method": {},
        "headers": {},
        "body": {}
      },
      "@id": "rdfs:seeAlso"
    },
    "summaries": {
      "@context": {
        "minimum": {},
        "maximum": {}
      }
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
    "roles": {
      "@id": "stac:roles",
      "@container": "@set"
    },
    "bands": {
      "@context": {
        "name": {}
      }
    },
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "start_datetime": {},
    "end_datetime": {},
    "created": "dct:created",
    "updated": "dct:modified",
    "data_type": {},
    "nodata": {},
    "statistics": {
      "@context": {
        "minimum": {},
        "maximum": {},
        "mean": {},
        "stddev": {},
        "count": {},
        "valid_percent": {}
      }
    },
    "unit": {},
    "platform": {},
    "instruments": {},
    "constellation": {},
    "mission": {},
    "gsd": {},
    "license": "dcat:license",
    "providers": {
      "@context": {
        "name": {},
        "url": {}
      }
    },
    "@vocab": "https://w3id.org/ogc/stac/assets/",
    "assets": {
      "@context": {
        "raster:bands": {
          "@context": {
            "name": {}
          }
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
        "type": "@type",
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        },
        "geometries": {}
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
    "time": {
      "@context": {
        "date": {},
        "timestamp": {},
        "interval": {},
        "resolution": {}
      },
      "@id": "dct:temporal"
    },
    "linkTemplates": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
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
    "collection": {},
    "language": {
      "@context": {
        "code": {},
        "name": {},
        "alternate": {},
        "dir": {}
      },
      "@id": "rec:language"
    },
    "languages": {
      "@context": {
        "code": {},
        "name": {},
        "alternate": {},
        "dir": {}
      },
      "@container": "@set",
      "@id": "rec:languages"
    },
    "resourceLanguages": {
      "@context": {
        "code": {},
        "name": {},
        "alternate": {},
        "dir": {}
      },
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
      "@context": {
        "identifier": {},
        "name": {},
        "position": {},
        "organization": {},
        "logo": {
          "@context": {
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "anchor": {},
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          }
        },
        "phones": {
          "@context": {
            "value": {}
          }
        },
        "emails": {
          "@context": {
            "value": {}
          }
        },
        "addresses": {
          "@context": {
            "deliveryPoint": {},
            "city": {},
            "administrativeArea": {},
            "postalCode": {},
            "country": {}
          }
        },
        "hoursOfService": {},
        "contactInstructions": {}
      },
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "rights": "dcat:rights",
    "mlm:name": {},
    "mlm:architecture": {},
    "mlm:tasks": {},
    "mlm:framework": {},
    "mlm:framework_version": {},
    "mlm:memory_size": {},
    "mlm:total_parameters": {},
    "mlm:pretrained": {},
    "mlm:pretrained_source": {},
    "mlm:batch_size_suggestion": {},
    "mlm:accelerator": {},
    "mlm:accelerator_constrained": {},
    "mlm:accelerator_summary": {},
    "mlm:accelerator_count": {},
    "mlm:input": {
      "@context": {
        "name": {},
        "bands": {
          "@context": {
            "format": {},
            "expression": {}
          }
        },
        "variables": {
          "@context": {
            "format": {},
            "expression": {}
          }
        },
        "input": {
          "@context": {
            "shape": {},
            "dim_order": {}
          }
        },
        "value_scaling": {
          "@context": {
            "minimum": {},
            "maximum": {},
            "mean": {},
            "stddev": {},
            "value": {},
            "format": {},
            "expression": {}
          }
        },
        "resize_type": {},
        "pre_processing_function": {
          "@context": {
            "format": {},
            "expression": {}
          }
        }
      }
    },
    "mlm:output": {
      "@context": {
        "name": {},
        "tasks": {},
        "result": {
          "@context": {
            "shape": {},
            "dim_order": {}
          }
        },
        "bands": {
          "@context": {
            "format": {},
            "expression": {}
          }
        },
        "variables": {
          "@context": {
            "format": {},
            "expression": {}
          }
        },
        "classification:classes": {
          "@context": {
            "value": {},
            "color_hint": {}
          }
        },
        "post_processing_function": {
          "@context": {
            "format": {},
            "expression": {}
          }
        }
      }
    },
    "mlm:hyperparameters": {},
    "mlm:artifact_type": {},
    "mlm:compile_method": {},
    "mlm:entrypoint": {},
    "eo:bands": {},
    "cube:variables": {},
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
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "raster": "https://w3id.org/ogc/stac/raster/",
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

