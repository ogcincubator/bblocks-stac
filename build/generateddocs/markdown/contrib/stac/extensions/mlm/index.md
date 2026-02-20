
# STAC Machine Learning Model (Schema)

`ogc.contrib.stac.extensions.mlm` *v1.4.0*

STAC Machine Learning Model (MLM) Extension to describe ML models, their training details, and inference runtime requirements.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Collection of items contained in the Machine Learning Model examples.
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
    },
    {
      "href": "item_pytorch_geo_unet.json",
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
    },
    {
      "href": "item_pytorch_geo_unet.json",
      "rel": "item"
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

<https://example.com/stac/mlm/example-1/ml-model-examples> a <https://example.com/stac/mlm/example-1/Collection> ;
    dcterms:description "Collection of items contained in the Machine Learning Model examples." ;
    dcterms:extent [ ] ;
    dcterms:title "Machine Learning Model examples" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_pytorch_geo_unet.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_raster_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_and_raster_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_datacube_variables.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_multi_io.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_bands_expression.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_bands_summarized.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_basic.json> ] ;
    dcat:license "Apache-2.0" ;
    stac:hasExtension "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json" ;
    stac:version "1.0.0" .


```


### Demonstrate the basic use of MLM with no other extension cross-references.
#### json
```json
{
  "$comment": "Demonstrate the basic use of MLM with no other extension cross-references.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json"
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
  "$comment": "Demonstrate the basic use of MLM with no other extension cross-references.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json"
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

<https://example.com/stac/mlm/example-2/example-model> a geojson:Feature ;
    dcterms:description "Basic STAC Item with only the MLM extension and no other extension cross-references." ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-2/collection.json> ],
        [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-2/item_basic.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/mlm/v1.5.1/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    ns1:architecture "ResNet" ;
    ns1:input [ ] ;
    ns1:name "example-model" ;
    ns1:output [ ] ;
    ns1:tasks "classification" .


```


### Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.
#### json
```json
{
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "RBG+NDVI Bands Sentinel-2 Batch",
        "bands": [
          {
            "name": "B04"
          },
          {
            "name": "B03"
          },
          {
            "name": "B02"
          },
          {
            "name": "NDVI",
            "format": "rio-calc",
            "expression": "(B08 - B04) / (B08 + B04)"
          }
        ],
        "input": {
          "shape": [
            -1,
            4,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
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
          "segmentation",
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            2
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 1,
            "name": "vegetation",
            "title": "Vegetation",
            "description": "Pixels were vegetation is detected.",
            "color_hint": "00FF00",
            "nodata": false
          },
          {
            "value": 0,
            "name": "background",
            "title": "Non-Vegetation",
            "description": "Anything that is not classified as vegetation.",
            "color_hint": "000000",
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://example.com/model-rgb-ndvi.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A vegetation classification model trained on Sentinel-2 imagery and NDVI.",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "B02",
          "common_name": "blue",
          "description": "Blue (band 2)",
          "center_wavelength": 0.49,
          "full_width_half_max": 0.098
        },
        {
          "name": "B03",
          "common_name": "green",
          "description": "Green (band 3)",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B04",
          "common_name": "red",
          "description": "Red (band 4)",
          "center_wavelength": 0.665,
          "full_width_half_max": 0.038
        },
        {
          "name": "B08",
          "common_name": "nir",
          "description": "NIR 1 (band 8)",
          "center_wavelength": 0.842,
          "full_width_half_max": 0.145
        }
      ]
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
      "href": "./item_bands_expression.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "RBG+NDVI Bands Sentinel-2 Batch",
        "bands": [
          {
            "name": "B04"
          },
          {
            "name": "B03"
          },
          {
            "name": "B02"
          },
          {
            "name": "NDVI",
            "format": "rio-calc",
            "expression": "(B08 - B04) / (B08 + B04)"
          }
        ],
        "input": {
          "shape": [
            -1,
            4,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
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
          "segmentation",
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            2
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 1,
            "name": "vegetation",
            "title": "Vegetation",
            "description": "Pixels were vegetation is detected.",
            "color_hint": "00FF00",
            "nodata": false
          },
          {
            "value": 0,
            "name": "background",
            "title": "Non-Vegetation",
            "description": "Anything that is not classified as vegetation.",
            "color_hint": "000000",
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://example.com/model-rgb-ndvi.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A vegetation classification model trained on Sentinel-2 imagery and NDVI.",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "B02",
          "common_name": "blue",
          "description": "Blue (band 2)",
          "center_wavelength": 0.49,
          "full_width_half_max": 0.098
        },
        {
          "name": "B03",
          "common_name": "green",
          "description": "Green (band 3)",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B04",
          "common_name": "red",
          "description": "Red (band 4)",
          "center_wavelength": 0.665,
          "full_width_half_max": 0.038
        },
        {
          "name": "B08",
          "common_name": "nir",
          "description": "NIR 1 (band 8)",
          "center_wavelength": 0.842,
          "full_width_half_max": 0.145
        }
      ]
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
      "href": "./item_bands_expression.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <file:> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <mlm:> .
@prefix ns4: <ml-aoi:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-3/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns1:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns4:split "train" ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-3/collection.json> ],
        [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-3/item_bands_expression.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    ns3:accelerator "cuda" ;
    ns3:accelerator_constrained false ;
    ns3:accelerator_summary "Unknown" ;
    ns3:architecture "ResNet" ;
    ns3:batch_size_suggestion 256 ;
    ns3:framework "pytorch" ;
    ns3:framework_version "2.1.2+cu121" ;
    ns3:input [ ] ;
    ns3:memory_size 1 ;
    ns3:name "Resnet-18 Sentinel-2 ALL MOCO" ;
    ns3:output [ ] ;
    ns3:pretrained_source "EuroSat Sentinel-2" ;
    ns3:tasks "classification" ;
    ns3:total_parameters 11700000 .


```


### Demonstrate the use of MLM and DataCube variables description to characterize its inputs and outputs.
#### json
```json
{
  "$comment": "Demonstrate the use of MLM and DataCube variables description to characterize its inputs and outputs.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "UNet_ClimateDiffuse_ERA5_Downscaling",
  "collection": "ml-model-examples",
  "bbox": [
    233.6,
    54.2,
    297.5,
    22.6
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          233.6,
          54.2
        ],
        [
          297.5,
          54.2
        ],
        [
          297.5,
          22.6
        ],
        [
          233.6,
          22.6
        ],
        [
          233.6,
          54.2
        ]
      ]
    ]
  },
  "properties": {
    "description": "UNet model for coarse-to-fine downscaling as regression task of climate indices of ERA5 dataset.",
    "datetime": null,
    "start_datetime": "1940-01-01T00:00:00Z",
    "end_datetime": "2100-12-31T23:59:59Z",
    "mlm:name": "UNet ClimateDiffuse ERA5 Downscaling",
    "mlm:tasks": [
      "regression",
      "downscaling"
    ],
    "mlm:architecture": "U-Net",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu118",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:input": [
      {
        "name": "Coarse climate variables employed by the model downscaling regression. This model takes 2 'constant/spatial' variables and 3 'spatio-temporal' variables provided by ERA5 datacube.",
        "variables": [
          "land_sea_mask",
          "geopotential",
          "temperature_2m",
          "10m_u_component_of_wind",
          "10m_v_component_of_wind"
        ],
        "input": {
          "shape": [
            -1,
            5,
            128,
            256
          ],
          "dim_order": [
            "time",
            "variables",
            "lat",
            "lon"
          ],
          "data_type": "float32"
        },
        "norm_by_channel": false,
        "resize_type": null,
        "pre_processing_function": {
          "description": "Script that performs the relevant normalization and concatenation of variables for model input.",
          "format": "uri",
          "expression": {
            "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/DatasetUS.py",
            "type": "text/x-python"
          }
        }
      }
    ],
    "mlm:output": [
      {
        "name": "Fine climate variables predicted by the model. Only the 3 'spatio-temporal' variables are predicted.",
        "tasks": [
          "regression",
          "downscaling"
        ],
        "variables": [
          "temperature_2m",
          "10m_u_component_of_wind",
          "10m_v_component_of_wind"
        ],
        "result": {
          "shape": [
            -1,
            3,
            128,
            256
          ],
          "dim_order": [
            "time",
            "variables",
            "lat",
            "lon"
          ],
          "data_type": "float32"
        }
      }
    ],
    "cube:dimensions": {
      "time": {
        "type": "temporal",
        "extent": [
          "1940-01-01T00:00:00Z",
          "2100-12-31T23:59:59Z"
        ],
        "step": "P1H"
      },
      "lat": {
        "type": "spatial",
        "extent": [
          54.2,
          22.6
        ],
        "axis": "y"
      },
      "lon": {
        "type": "spatial",
        "extent": [
          233.6,
          297.5
        ],
        "axis": "x"
      }
    },
    "cube:variables": {
      "land_sea_mask": {
        "shortname": "lsm",
        "description": "Proportion of land-sea, where 1 indicates land and 0 indicates sea.",
        "type": "data",
        "data_type": "float32",
        "extent": [
          0,
          1
        ],
        "dimensions": [
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/172"
      },
      "geopotential": {
        "shortname": "z",
        "description": "This parameter is the geopotential, which is the potential energy per unit mass at a point in the atmosphere, expressed in metres squared per second squared (m² s⁻²). It is a measure of the height of a point in the atmosphere relative to sea level.",
        "type": "data",
        "data_type": "float32",
        "unit": "m² s-2",
        "dimensions": [
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/129"
      },
      "2m_temperature": {
        "description": "This parameter is the temperature of air at 2m above the surface of land, sea or in-land waters.",
        "type": "data",
        "data_type": "float32",
        "unit": "K",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/167"
      },
      "10m_u_component_of_wind": {
        "shortname": "10u",
        "description": "This parameter is the eastward component of the 10m wind. It is the horizontal speed of air moving towards the east, at a height of ten metres above the surface of the Earth, in metres per second.",
        "type": "data",
        "data_type": "float32",
        "unit": "m s-1",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/165"
      },
      "10m_v_component_of_wind": {
        "shortname": "10v",
        "description": "This parameter is the northward component of the 10m wind. It is the horizontal speed of air moving towards the north, at a height of ten metres above the surface of the Earth, in metres per second.",
        "type": "data",
        "data_type": "float32",
        "unit": "m s-1",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/166"
      }
    },
    "sci:publications": [
      {
        "doi": "10.48550/arXiv.2404.17752",
        "citation": "Robbie A. Watt, Laura A. Mansfield, Generative Diffusion-based Downscaling for Climate"
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://github.com/robbiewatt1/ClimateDiffuse/raw/refs/heads/main/Model_chpt/unet.pt",
      "title": "U-Net Pytorch weights checkpoint",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "file:size": 389657415
    },
    "model": {
      "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Network.py",
      "title": "Model implementation.",
      "description": "Source code to define the U-Net model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
    },
    "train-script": {
      "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/TrainUnet.py",
      "title": "Training script.",
      "description": "Script to run training of the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:training",
        "code",
        "metadata"
      ]
    }
  },
  "inference-script": {
    "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Inference.py",
    "title": "Inference script.",
    "description": "Script to run inference with the model.",
    "type": "text/x-python",
    "roles": [
      "mlm:inference",
      "code",
      "metadata"
    ]
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_datacube_variables.json",
      "type": "application/geo+json"
    },
    {
      "rel": "via",
      "href": "https://github.com/robbiewatt1/ClimateDiffuse",
      "type": "text/html"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.48550/arXiv.2404.17752",
      "type": "text/html"
    },
    {
      "rel": "code",
      "href": "https://github.com/robbiewatt1/ClimateDiffuse",
      "type": "text/html"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and DataCube variables description to characterize its inputs and outputs.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "UNet_ClimateDiffuse_ERA5_Downscaling",
  "collection": "ml-model-examples",
  "bbox": [
    233.6,
    54.2,
    297.5,
    22.6
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          233.6,
          54.2
        ],
        [
          297.5,
          54.2
        ],
        [
          297.5,
          22.6
        ],
        [
          233.6,
          22.6
        ],
        [
          233.6,
          54.2
        ]
      ]
    ]
  },
  "properties": {
    "description": "UNet model for coarse-to-fine downscaling as regression task of climate indices of ERA5 dataset.",
    "datetime": null,
    "start_datetime": "1940-01-01T00:00:00Z",
    "end_datetime": "2100-12-31T23:59:59Z",
    "mlm:name": "UNet ClimateDiffuse ERA5 Downscaling",
    "mlm:tasks": [
      "regression",
      "downscaling"
    ],
    "mlm:architecture": "U-Net",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu118",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:input": [
      {
        "name": "Coarse climate variables employed by the model downscaling regression. This model takes 2 'constant/spatial' variables and 3 'spatio-temporal' variables provided by ERA5 datacube.",
        "variables": [
          "land_sea_mask",
          "geopotential",
          "temperature_2m",
          "10m_u_component_of_wind",
          "10m_v_component_of_wind"
        ],
        "input": {
          "shape": [
            -1,
            5,
            128,
            256
          ],
          "dim_order": [
            "time",
            "variables",
            "lat",
            "lon"
          ],
          "data_type": "float32"
        },
        "norm_by_channel": false,
        "resize_type": null,
        "pre_processing_function": {
          "description": "Script that performs the relevant normalization and concatenation of variables for model input.",
          "format": "uri",
          "expression": {
            "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/DatasetUS.py",
            "type": "text/x-python"
          }
        }
      }
    ],
    "mlm:output": [
      {
        "name": "Fine climate variables predicted by the model. Only the 3 'spatio-temporal' variables are predicted.",
        "tasks": [
          "regression",
          "downscaling"
        ],
        "variables": [
          "temperature_2m",
          "10m_u_component_of_wind",
          "10m_v_component_of_wind"
        ],
        "result": {
          "shape": [
            -1,
            3,
            128,
            256
          ],
          "dim_order": [
            "time",
            "variables",
            "lat",
            "lon"
          ],
          "data_type": "float32"
        }
      }
    ],
    "cube:dimensions": {
      "time": {
        "type": "temporal",
        "extent": [
          "1940-01-01T00:00:00Z",
          "2100-12-31T23:59:59Z"
        ],
        "step": "P1H"
      },
      "lat": {
        "type": "spatial",
        "extent": [
          54.2,
          22.6
        ],
        "axis": "y"
      },
      "lon": {
        "type": "spatial",
        "extent": [
          233.6,
          297.5
        ],
        "axis": "x"
      }
    },
    "cube:variables": {
      "land_sea_mask": {
        "shortname": "lsm",
        "description": "Proportion of land-sea, where 1 indicates land and 0 indicates sea.",
        "type": "data",
        "data_type": "float32",
        "extent": [
          0,
          1
        ],
        "dimensions": [
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/172"
      },
      "geopotential": {
        "shortname": "z",
        "description": "This parameter is the geopotential, which is the potential energy per unit mass at a point in the atmosphere, expressed in metres squared per second squared (m\u00b2 s\u207b\u00b2). It is a measure of the height of a point in the atmosphere relative to sea level.",
        "type": "data",
        "data_type": "float32",
        "unit": "m\u00b2 s-2",
        "dimensions": [
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/129"
      },
      "2m_temperature": {
        "description": "This parameter is the temperature of air at 2m above the surface of land, sea or in-land waters.",
        "type": "data",
        "data_type": "float32",
        "unit": "K",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/167"
      },
      "10m_u_component_of_wind": {
        "shortname": "10u",
        "description": "This parameter is the eastward component of the 10m wind. It is the horizontal speed of air moving towards the east, at a height of ten metres above the surface of the Earth, in metres per second.",
        "type": "data",
        "data_type": "float32",
        "unit": "m s-1",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/165"
      },
      "10m_v_component_of_wind": {
        "shortname": "10v",
        "description": "This parameter is the northward component of the 10m wind. It is the horizontal speed of air moving towards the north, at a height of ten metres above the surface of the Earth, in metres per second.",
        "type": "data",
        "data_type": "float32",
        "unit": "m s-1",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/166"
      }
    },
    "sci:publications": [
      {
        "doi": "10.48550/arXiv.2404.17752",
        "citation": "Robbie A. Watt, Laura A. Mansfield, Generative Diffusion-based Downscaling for Climate"
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://github.com/robbiewatt1/ClimateDiffuse/raw/refs/heads/main/Model_chpt/unet.pt",
      "title": "U-Net Pytorch weights checkpoint",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "file:size": 389657415
    },
    "model": {
      "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Network.py",
      "title": "Model implementation.",
      "description": "Source code to define the U-Net model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
    },
    "train-script": {
      "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/TrainUnet.py",
      "title": "Training script.",
      "description": "Script to run training of the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:training",
        "code",
        "metadata"
      ]
    }
  },
  "inference-script": {
    "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Inference.py",
    "title": "Inference script.",
    "description": "Script to run inference with the model.",
    "type": "text/x-python",
    "roles": [
      "mlm:inference",
      "code",
      "metadata"
    ]
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_datacube_variables.json",
      "type": "application/geo+json"
    },
    {
      "rel": "via",
      "href": "https://github.com/robbiewatt1/ClimateDiffuse",
      "type": "text/html"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.48550/arXiv.2404.17752",
      "type": "text/html"
    },
    {
      "rel": "code",
      "href": "https://github.com/robbiewatt1/ClimateDiffuse",
      "type": "text/html"
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
@prefix ns3: <cube:> .
@prefix ns4: <sci:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-4/UNet_ClimateDiffuse_ERA5_Downscaling> a geojson:Feature ;
    ns3:dimensions [ dcterms:temporal [ a <https://example.com/stac/mlm/example-4/temporal> ;
                    dcterms:extent "1940-01-01T00:00:00Z",
                        "2100-12-31T23:59:59Z" ] ] ;
    ns3:variables [ ] ;
    dcterms:description "UNet model for coarse-to-fine downscaling as regression task of climate indices of ERA5 dataset." ;
    rdfs:seeAlso [ dcterms:type "text/html" ;
            ns2:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://github.com/robbiewatt1/ClimateDiffuse> ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-4/collection.json> ],
        [ dcterms:type "text/html" ;
            ns2:relation <http://www.iana.org/assignments/relation/code> ;
            oa:hasTarget <https://github.com/robbiewatt1/ClimateDiffuse> ],
        [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-4/item_datacube_variables.json> ],
        [ dcterms:type "text/html" ;
            ns2:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://doi.org/10.48550/arXiv.2404.17752> ] ;
    geojson:bbox ( 2.336e+02 5.42e+01 2.975e+02 2.26e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 2.336e+02 5.42e+01 ) ( 2.975e+02 5.42e+01 ) ( 2.975e+02 2.26e+01 ) ( 2.336e+02 2.26e+01 ) ( 2.336e+02 5.42e+01 ) ) ) ] ;
    stac:end_datetime "2100-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
        "https://stac-extensions.github.io/file/v2.1.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
        "https://stac-extensions.github.io/scientific/v1.0.0/schema.json" ;
    stac:start_datetime "1940-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    ns1:accelerator "cuda" ;
    ns1:accelerator_constrained false ;
    ns1:architecture "U-Net" ;
    ns1:framework "pytorch" ;
    ns1:framework_version "2.1.2+cu118" ;
    ns1:input [ ] ;
    ns1:name "UNet ClimateDiffuse ERA5 Downscaling" ;
    ns1:output [ ] ;
    ns1:tasks "downscaling",
        "regression" ;
    ns4:publications [ ] .


```


### Demonstrate the use of MLM with both EO and Raster extensions using complementary bands details to describe the Model Asset by band name reference.
#### json
```json
{
  "$comment": "Demonstrate the use of MLM with both EO and Raster extensions using complementary bands details to describe the Model Asset by band name reference.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
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
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "description": "Coastal aerosol (band 1)",
        "center_wavelength": 0.443,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "description": "Blue (band 2)",
        "center_wavelength": 0.49,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "description": "Green (band 3)",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "description": "Red (band 4)",
        "center_wavelength": 0.665,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "common_name": "rededge",
        "description": "Red edge 1 (band 5)",
        "center_wavelength": 0.704,
        "full_width_half_max": 0.019
      },
      {
        "name": "B06",
        "common_name": "rededge",
        "description": "Red edge 2 (band 6)",
        "center_wavelength": 0.74,
        "full_width_half_max": 0.018
      },
      {
        "name": "B07",
        "common_name": "rededge",
        "description": "Red edge 3 (band 7)",
        "center_wavelength": 0.783,
        "full_width_half_max": 0.028
      },
      {
        "name": "B08",
        "common_name": "nir",
        "description": "NIR 1 (band 8)",
        "center_wavelength": 0.842,
        "full_width_half_max": 0.145
      },
      {
        "name": "B8A",
        "common_name": "nir08",
        "description": "NIR 2 (band 8A)",
        "center_wavelength": 0.865,
        "full_width_half_max": 0.033
      },
      {
        "name": "B09",
        "common_name": "nir09",
        "description": "NIR 3 (band 9)",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "description": "SWIR - Cirrus (band 10)",
        "center_wavelength": 1.375,
        "full_width_half_max": 0.026
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "description": "SWIR 1 (band 11)",
        "center_wavelength": 1.61,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "description": "SWIR 2 (band 12)",
        "center_wavelength": 2.19,
        "full_width_half_max": 0.242
      }
    ],
    "raster:bands": [
      {
        "name": "B01",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B02",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B03",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B04",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B05",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B06",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B07",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B08",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B8A",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B09",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B10",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B11",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B12",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "coastal"
        },
        {
          "name": "blue"
        },
        {
          "name": "green"
        },
        {
          "name": "red"
        },
        {
          "name": "rededge1"
        },
        {
          "name": "rededge2"
        },
        {
          "name": "rededge3"
        },
        {
          "name": "nir"
        },
        {
          "name": "nir08"
        },
        {
          "name": "nir09"
        },
        {
          "name": "cirrus"
        },
        {
          "name": "swir16"
        },
        {
          "name": "swir22"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "code",
        "metadata"
      ]
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
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM with both EO and Raster extensions using complementary bands details to describe the Model Asset by band name reference.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
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
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "description": "Coastal aerosol (band 1)",
        "center_wavelength": 0.443,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "description": "Blue (band 2)",
        "center_wavelength": 0.49,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "description": "Green (band 3)",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "description": "Red (band 4)",
        "center_wavelength": 0.665,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "common_name": "rededge",
        "description": "Red edge 1 (band 5)",
        "center_wavelength": 0.704,
        "full_width_half_max": 0.019
      },
      {
        "name": "B06",
        "common_name": "rededge",
        "description": "Red edge 2 (band 6)",
        "center_wavelength": 0.74,
        "full_width_half_max": 0.018
      },
      {
        "name": "B07",
        "common_name": "rededge",
        "description": "Red edge 3 (band 7)",
        "center_wavelength": 0.783,
        "full_width_half_max": 0.028
      },
      {
        "name": "B08",
        "common_name": "nir",
        "description": "NIR 1 (band 8)",
        "center_wavelength": 0.842,
        "full_width_half_max": 0.145
      },
      {
        "name": "B8A",
        "common_name": "nir08",
        "description": "NIR 2 (band 8A)",
        "center_wavelength": 0.865,
        "full_width_half_max": 0.033
      },
      {
        "name": "B09",
        "common_name": "nir09",
        "description": "NIR 3 (band 9)",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "description": "SWIR - Cirrus (band 10)",
        "center_wavelength": 1.375,
        "full_width_half_max": 0.026
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "description": "SWIR 1 (band 11)",
        "center_wavelength": 1.61,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "description": "SWIR 2 (band 12)",
        "center_wavelength": 2.19,
        "full_width_half_max": 0.242
      }
    ],
    "raster:bands": [
      {
        "name": "B01",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B02",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B03",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B04",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B05",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B06",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B07",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B08",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B8A",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B09",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B10",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B11",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B12",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "coastal"
        },
        {
          "name": "blue"
        },
        {
          "name": "green"
        },
        {
          "name": "red"
        },
        {
          "name": "rededge1"
        },
        {
          "name": "rededge2"
        },
        {
          "name": "rededge3"
        },
        {
          "name": "nir"
        },
        {
          "name": "nir08"
        },
        {
          "name": "nir09"
        },
        {
          "name": "cirrus"
        },
        {
          "name": "swir16"
        },
        {
          "name": "swir22"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "code",
        "metadata"
      ]
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
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <mlm:> .
@prefix ns2: <ml-aoi:> .
@prefix ns3: <eo:> .
@prefix ns4: <file:> .
@prefix ns5: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix raster: <https://w3id.org/ogc/stac/raster/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-5/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns3:bands [ dcterms:description "NIR 3 (band 9)" ],
        [ dcterms:description "Coastal aerosol (band 1)" ],
        [ dcterms:description "NIR 2 (band 8A)" ],
        [ dcterms:description "Blue (band 2)" ],
        [ dcterms:description "Red edge 2 (band 6)" ],
        [ dcterms:description "Red (band 4)" ],
        [ dcterms:description "SWIR - Cirrus (band 10)" ],
        [ dcterms:description "Green (band 3)" ],
        [ dcterms:description "SWIR 2 (band 12)" ],
        [ dcterms:description "NIR 1 (band 8)" ],
        [ dcterms:description "Red edge 1 (band 5)" ],
        [ dcterms:description "Red edge 3 (band 7)" ],
        [ dcterms:description "SWIR 1 (band 11)" ] ;
    ns4:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns5:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-5/item_eo_bands.json> ],
        [ dcterms:type "application/json" ;
            ns5:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-5/collection.json> ],
        [ dcterms:type "application/json" ;
            ns5:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns2:split "train" ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    raster:bands [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B07" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 20 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B10" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 60 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B8A" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 20 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B01" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 60 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B12" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 20 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B11" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 20 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B03" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 10 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B08" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 10 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B02" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 10 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B06" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 20 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B05" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 20 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B09" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 60 ;
            raster:unit "m" ],
        [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B04" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 10 ;
            raster:unit "m" ] ;
    ns1:accelerator "cuda" ;
    ns1:accelerator_constrained false ;
    ns1:accelerator_summary "Unknown" ;
    ns1:architecture "ResNet" ;
    ns1:batch_size_suggestion 256 ;
    ns1:framework "pytorch" ;
    ns1:framework_version "2.1.2+cu121" ;
    ns1:input [ ] ;
    ns1:memory_size 1 ;
    ns1:name "Resnet-18 Sentinel-2 ALL MOCO" ;
    ns1:output [ ] ;
    ns1:pretrained_source "EuroSat Sentinel-2" ;
    ns1:tasks "classification" ;
    ns1:total_parameters 11700000 .


```


### Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.
#### json
```json
{
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "norm_by_channel": true,
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
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
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "B01",
          "common_name": "coastal",
          "description": "Coastal aerosol (band 1)",
          "center_wavelength": 0.443,
          "full_width_half_max": 0.027
        },
        {
          "name": "B02",
          "common_name": "blue",
          "description": "Blue (band 2)",
          "center_wavelength": 0.49,
          "full_width_half_max": 0.098
        },
        {
          "name": "B03",
          "common_name": "green",
          "description": "Green (band 3)",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B04",
          "common_name": "red",
          "description": "Red (band 4)",
          "center_wavelength": 0.665,
          "full_width_half_max": 0.038
        },
        {
          "name": "B05",
          "common_name": "rededge",
          "description": "Red edge 1 (band 5)",
          "center_wavelength": 0.704,
          "full_width_half_max": 0.019
        },
        {
          "name": "B06",
          "common_name": "rededge",
          "description": "Red edge 2 (band 6)",
          "center_wavelength": 0.74,
          "full_width_half_max": 0.018
        },
        {
          "name": "B07",
          "common_name": "rededge",
          "description": "Red edge 3 (band 7)",
          "center_wavelength": 0.783,
          "full_width_half_max": 0.028
        },
        {
          "name": "B08",
          "common_name": "nir",
          "description": "NIR 1 (band 8)",
          "center_wavelength": 0.842,
          "full_width_half_max": 0.145
        },
        {
          "name": "B8A",
          "common_name": "nir08",
          "description": "NIR 2 (band 8A)",
          "center_wavelength": 0.865,
          "full_width_half_max": 0.033
        },
        {
          "name": "B09",
          "common_name": "nir09",
          "description": "NIR 3 (band 9)",
          "center_wavelength": 0.945,
          "full_width_half_max": 0.026
        },
        {
          "name": "B10",
          "common_name": "cirrus",
          "description": "SWIR - Cirrus (band 10)",
          "center_wavelength": 1.375,
          "full_width_half_max": 0.026
        },
        {
          "name": "B11",
          "common_name": "swir16",
          "description": "SWIR 1 (band 11)",
          "center_wavelength": 1.61,
          "full_width_half_max": 0.143
        },
        {
          "name": "B12",
          "common_name": "swir22",
          "description": "SWIR 2 (band 12)",
          "center_wavelength": 2.19,
          "full_width_half_max": 0.242
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
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
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "norm_by_channel": true,
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
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
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "B01",
          "common_name": "coastal",
          "description": "Coastal aerosol (band 1)",
          "center_wavelength": 0.443,
          "full_width_half_max": 0.027
        },
        {
          "name": "B02",
          "common_name": "blue",
          "description": "Blue (band 2)",
          "center_wavelength": 0.49,
          "full_width_half_max": 0.098
        },
        {
          "name": "B03",
          "common_name": "green",
          "description": "Green (band 3)",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B04",
          "common_name": "red",
          "description": "Red (band 4)",
          "center_wavelength": 0.665,
          "full_width_half_max": 0.038
        },
        {
          "name": "B05",
          "common_name": "rededge",
          "description": "Red edge 1 (band 5)",
          "center_wavelength": 0.704,
          "full_width_half_max": 0.019
        },
        {
          "name": "B06",
          "common_name": "rededge",
          "description": "Red edge 2 (band 6)",
          "center_wavelength": 0.74,
          "full_width_half_max": 0.018
        },
        {
          "name": "B07",
          "common_name": "rededge",
          "description": "Red edge 3 (band 7)",
          "center_wavelength": 0.783,
          "full_width_half_max": 0.028
        },
        {
          "name": "B08",
          "common_name": "nir",
          "description": "NIR 1 (band 8)",
          "center_wavelength": 0.842,
          "full_width_half_max": 0.145
        },
        {
          "name": "B8A",
          "common_name": "nir08",
          "description": "NIR 2 (band 8A)",
          "center_wavelength": 0.865,
          "full_width_half_max": 0.033
        },
        {
          "name": "B09",
          "common_name": "nir09",
          "description": "NIR 3 (band 9)",
          "center_wavelength": 0.945,
          "full_width_half_max": 0.026
        },
        {
          "name": "B10",
          "common_name": "cirrus",
          "description": "SWIR - Cirrus (band 10)",
          "center_wavelength": 1.375,
          "full_width_half_max": 0.026
        },
        {
          "name": "B11",
          "common_name": "swir16",
          "description": "SWIR 1 (band 11)",
          "center_wavelength": 1.61,
          "full_width_half_max": 0.143
        },
        {
          "name": "B12",
          "common_name": "swir22",
          "description": "SWIR 2 (band 12)",
          "center_wavelength": 2.19,
          "full_width_half_max": 0.242
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
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
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
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
@prefix ns3: <ml-aoi:> .
@prefix ns4: <file:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-6/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns4:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-6/item_eo_bands.json> ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns3:split "train" ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-6/collection.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.5.1/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    ns1:accelerator "cuda" ;
    ns1:accelerator_constrained false ;
    ns1:accelerator_summary "Unknown" ;
    ns1:architecture "ResNet" ;
    ns1:batch_size_suggestion 256 ;
    ns1:framework "pytorch" ;
    ns1:framework_version "2.1.2+cu121" ;
    ns1:input [ ] ;
    ns1:memory_size 1 ;
    ns1:name "Resnet-18 Sentinel-2 ALL MOCO" ;
    ns1:output [ ] ;
    ns1:pretrained_source "EuroSat Sentinel-2" ;
    ns1:tasks "classification" ;
    ns1:total_parameters 11700000 .


```


### Demonstrate the use of MLM and EO for bands description, with EO bands summarized in the Item properties and referenced by name in the Model Asset.
#### json
```json
{
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands summarized in the Item properties and referenced by name in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
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
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "description": "Coastal aerosol (band 1)",
        "center_wavelength": 0.443,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "description": "Blue (band 2)",
        "center_wavelength": 0.49,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "description": "Green (band 3)",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "description": "Red (band 4)",
        "center_wavelength": 0.665,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "common_name": "rededge",
        "description": "Red edge 1 (band 5)",
        "center_wavelength": 0.704,
        "full_width_half_max": 0.019
      },
      {
        "name": "B06",
        "common_name": "rededge",
        "description": "Red edge 2 (band 6)",
        "center_wavelength": 0.74,
        "full_width_half_max": 0.018
      },
      {
        "name": "B07",
        "common_name": "rededge",
        "description": "Red edge 3 (band 7)",
        "center_wavelength": 0.783,
        "full_width_half_max": 0.028
      },
      {
        "name": "B08",
        "common_name": "nir",
        "description": "NIR 1 (band 8)",
        "center_wavelength": 0.842,
        "full_width_half_max": 0.145
      },
      {
        "name": "B8A",
        "common_name": "nir08",
        "description": "NIR 2 (band 8A)",
        "center_wavelength": 0.865,
        "full_width_half_max": 0.033
      },
      {
        "name": "B09",
        "common_name": "nir09",
        "description": "NIR 3 (band 9)",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "description": "SWIR - Cirrus (band 10)",
        "center_wavelength": 1.375,
        "full_width_half_max": 0.026
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "description": "SWIR 1 (band 11)",
        "center_wavelength": 1.61,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "description": "SWIR 2 (band 12)",
        "center_wavelength": 2.19,
        "full_width_half_max": 0.242
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "coastal"
        },
        {
          "name": "blue"
        },
        {
          "name": "green"
        },
        {
          "name": "red"
        },
        {
          "name": "rededge1"
        },
        {
          "name": "rededge2"
        },
        {
          "name": "rededge3"
        },
        {
          "name": "nir"
        },
        {
          "name": "nir08"
        },
        {
          "name": "nir09"
        },
        {
          "name": "cirrus"
        },
        {
          "name": "swir16"
        },
        {
          "name": "swir22"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "code",
        "metadata"
      ]
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
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands summarized in the Item properties and referenced by name in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
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
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "description": "Coastal aerosol (band 1)",
        "center_wavelength": 0.443,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "description": "Blue (band 2)",
        "center_wavelength": 0.49,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "description": "Green (band 3)",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "description": "Red (band 4)",
        "center_wavelength": 0.665,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "common_name": "rededge",
        "description": "Red edge 1 (band 5)",
        "center_wavelength": 0.704,
        "full_width_half_max": 0.019
      },
      {
        "name": "B06",
        "common_name": "rededge",
        "description": "Red edge 2 (band 6)",
        "center_wavelength": 0.74,
        "full_width_half_max": 0.018
      },
      {
        "name": "B07",
        "common_name": "rededge",
        "description": "Red edge 3 (band 7)",
        "center_wavelength": 0.783,
        "full_width_half_max": 0.028
      },
      {
        "name": "B08",
        "common_name": "nir",
        "description": "NIR 1 (band 8)",
        "center_wavelength": 0.842,
        "full_width_half_max": 0.145
      },
      {
        "name": "B8A",
        "common_name": "nir08",
        "description": "NIR 2 (band 8A)",
        "center_wavelength": 0.865,
        "full_width_half_max": 0.033
      },
      {
        "name": "B09",
        "common_name": "nir09",
        "description": "NIR 3 (band 9)",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "description": "SWIR - Cirrus (band 10)",
        "center_wavelength": 1.375,
        "full_width_half_max": 0.026
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "description": "SWIR 1 (band 11)",
        "center_wavelength": 1.61,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "description": "SWIR 2 (band 12)",
        "center_wavelength": 2.19,
        "full_width_half_max": 0.242
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "coastal"
        },
        {
          "name": "blue"
        },
        {
          "name": "green"
        },
        {
          "name": "red"
        },
        {
          "name": "rededge1"
        },
        {
          "name": "rededge2"
        },
        {
          "name": "rededge3"
        },
        {
          "name": "nir"
        },
        {
          "name": "nir08"
        },
        {
          "name": "nir09"
        },
        {
          "name": "cirrus"
        },
        {
          "name": "swir16"
        },
        {
          "name": "swir22"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "code",
        "metadata"
      ]
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
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <mlm:> .
@prefix ns2: <eo:> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix ns4: <ml-aoi:> .
@prefix ns5: <file:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-7/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns2:bands [ dcterms:description "Red edge 1 (band 5)" ],
        [ dcterms:description "SWIR 1 (band 11)" ],
        [ dcterms:description "SWIR - Cirrus (band 10)" ],
        [ dcterms:description "Green (band 3)" ],
        [ dcterms:description "NIR 1 (band 8)" ],
        [ dcterms:description "Red (band 4)" ],
        [ dcterms:description "NIR 3 (band 9)" ],
        [ dcterms:description "NIR 2 (band 8A)" ],
        [ dcterms:description "Red edge 3 (band 7)" ],
        [ dcterms:description "Blue (band 2)" ],
        [ dcterms:description "Coastal aerosol (band 1)" ],
        [ dcterms:description "Red edge 2 (band 6)" ],
        [ dcterms:description "SWIR 2 (band 12)" ] ;
    ns5:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns3:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns4:split "train" ],
        [ dcterms:type "application/geo+json" ;
            ns3:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-7/item_eo_bands.json> ],
        [ dcterms:type "application/json" ;
            ns3:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-7/collection.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.5.1/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    ns1:accelerator "cuda" ;
    ns1:accelerator_constrained false ;
    ns1:accelerator_summary "Unknown" ;
    ns1:architecture "ResNet" ;
    ns1:batch_size_suggestion 256 ;
    ns1:framework "pytorch" ;
    ns1:framework_version "2.1.2+cu121" ;
    ns1:input [ ] ;
    ns1:memory_size 1 ;
    ns1:name "Resnet-18 Sentinel-2 ALL MOCO" ;
    ns1:output [ ] ;
    ns1:pretrained_source "EuroSat Sentinel-2" ;
    ns1:tasks "classification" ;
    ns1:total_parameters 11700000 .


```


### Demonstrate the use of MLM with a mixture of inputs, some using EO bands, others without, and some with derived properties.
#### json
```json
{
  "$comment": "Demonstrate the use of MLM with a mixture of inputs, some using EO bands, others without, and some with derived properties.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "model-multi-input",
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
    "description": "Generic model that employs multiple input sources with different combination of bands, and some inputs without any band at all.",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "RGB",
        "bands": [
          "B04",
          "B03",
          "B02"
        ],
        "input": {
          "shape": [
            -1,
            3,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "uint16"
        },
        "value_scaling": null,
        "resize_type": null
      },
      {
        "description": "Compute NDVI from Sentinel-2 bands. The single 'NDVI' virtual band is then fed as 'bands' dimension to the model input.",
        "name": "NDVI",
        "bands": [
          "B04",
          "B08"
        ],
        "pre_processing_function": {
          "format": "gdal-calc",
          "expression": "(A - B) / (A + B)"
        },
        "input": {
          "shape": [
            -1,
            1,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "uint16"
        }
      },
      {
        "description": "Digital elevation model. Comes from another source than the Sentinel bands. Therefore, no 'bands' associated to it.",
        "name": "DEM",
        "bands": [],
        "input": {
          "shape": [
            -1,
            1,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "h",
            "y",
            "x"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "vegetation-segmentation",
        "tasks": [
          "semantic-segmentation"
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
            "name": "NON_VEGETATION",
            "description": "background pixels",
            "color_hint": null
          },
          {
            "value": 1,
            "name": "VEGETATION",
            "description": "pixels where vegetation was detected",
            "color_hint": [
              0,
              255,
              0
            ]
          }
        ],
        "post_processing_function": null
      },
      {
        "name": "inverse-mask",
        "tasks": [
          "semantic-segmentation"
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
            "name": "NON_VEGETATION",
            "description": "background pixels",
            "color_hint": [
              255,
              255,
              255
            ]
          },
          {
            "value": 1,
            "name": "VEGETATION",
            "description": "pixels where vegetation was detected",
            "color_hint": [
              0,
              0,
              0
            ]
          }
        ],
        "post_processing_function": {
          "format": "gdal-calc",
          "expression": "logical_not(A)"
        }
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet50_sentinel2_rgb_moco/blob/main/resnet50_sentinel2_rgb_moco.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-50 classification model trained on Sentinel-2 RGB imagery with torchgeo.",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "raster:bands": [
        {
          "name": "B02 - blue",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B03 - green",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B04 - red",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B08 - nir",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        }
      ]
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
      "href": "./item_multi_io.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM with a mixture of inputs, some using EO bands, others without, and some with derived properties.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "model-multi-input",
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
    "description": "Generic model that employs multiple input sources with different combination of bands, and some inputs without any band at all.",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "RGB",
        "bands": [
          "B04",
          "B03",
          "B02"
        ],
        "input": {
          "shape": [
            -1,
            3,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "uint16"
        },
        "value_scaling": null,
        "resize_type": null
      },
      {
        "description": "Compute NDVI from Sentinel-2 bands. The single 'NDVI' virtual band is then fed as 'bands' dimension to the model input.",
        "name": "NDVI",
        "bands": [
          "B04",
          "B08"
        ],
        "pre_processing_function": {
          "format": "gdal-calc",
          "expression": "(A - B) / (A + B)"
        },
        "input": {
          "shape": [
            -1,
            1,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "uint16"
        }
      },
      {
        "description": "Digital elevation model. Comes from another source than the Sentinel bands. Therefore, no 'bands' associated to it.",
        "name": "DEM",
        "bands": [],
        "input": {
          "shape": [
            -1,
            1,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "h",
            "y",
            "x"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "vegetation-segmentation",
        "tasks": [
          "semantic-segmentation"
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
            "name": "NON_VEGETATION",
            "description": "background pixels",
            "color_hint": null
          },
          {
            "value": 1,
            "name": "VEGETATION",
            "description": "pixels where vegetation was detected",
            "color_hint": [
              0,
              255,
              0
            ]
          }
        ],
        "post_processing_function": null
      },
      {
        "name": "inverse-mask",
        "tasks": [
          "semantic-segmentation"
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
            "name": "NON_VEGETATION",
            "description": "background pixels",
            "color_hint": [
              255,
              255,
              255
            ]
          },
          {
            "value": 1,
            "name": "VEGETATION",
            "description": "pixels where vegetation was detected",
            "color_hint": [
              0,
              0,
              0
            ]
          }
        ],
        "post_processing_function": {
          "format": "gdal-calc",
          "expression": "logical_not(A)"
        }
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet50_sentinel2_rgb_moco/blob/main/resnet50_sentinel2_rgb_moco.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-50 classification model trained on Sentinel-2 RGB imagery with torchgeo.",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "raster:bands": [
        {
          "name": "B02 - blue",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B03 - green",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B04 - red",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B08 - nir",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        }
      ]
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
      "href": "./item_multi_io.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
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
@prefix ns3: <ml-aoi:> .
@prefix ns4: <file:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-8/model-multi-input> a geojson:Feature ;
    ns4:size 43000000 ;
    dcterms:description "Generic model that employs multiple input sources with different combination of bands, and some inputs without any band at all." ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns3:split "train" ],
        [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-8/item_multi_io.json> ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-8/collection.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    ns1:accelerator "cuda" ;
    ns1:accelerator_constrained false ;
    ns1:accelerator_summary "Unknown" ;
    ns1:architecture "ResNet" ;
    ns1:batch_size_suggestion 256 ;
    ns1:framework "pytorch" ;
    ns1:framework_version "2.1.2+cu121" ;
    ns1:input [ dcterms:description "Digital elevation model. Comes from another source than the Sentinel bands. Therefore, no 'bands' associated to it." ],
        [ dcterms:description "Compute NDVI from Sentinel-2 bands. The single 'NDVI' virtual band is then fed as 'bands' dimension to the model input." ],
        [ ] ;
    ns1:memory_size 1 ;
    ns1:name "Resnet-18 Sentinel-2 ALL MOCO" ;
    ns1:output [ ],
        [ ] ;
    ns1:pretrained_source "EuroSat Sentinel-2" ;
    ns1:tasks "classification" ;
    ns1:total_parameters 11700000 .


```


### STAC item auto-generated using unet_mlm() in https://raw.githubusercontent.com/stac-extensions/mlm/refs/heads/main/stac_model/examples.py
#### json
```json
{
  "$comment": "STAC item auto-generated using unet_mlm() in https://raw.githubusercontent.com/stac-extensions/mlm/refs/heads/main/stac_model/examples.py",
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json"
  ],
  "id": "pytorch_geo_unet",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.88,
          37.13
        ],
        [
          -7.88,
          58.21
        ],
        [
          27.91,
          58.21
        ],
        [
          27.91,
          37.13
        ],
        [
          -7.88,
          37.13
        ]
      ]
    ]
  },
  "bbox": [
    -7.88,
    37.13,
    27.91,
    58.21
  ],
  "properties": {
    "description": "STAC item generated using unet_mlm() in stac_model/examples.py example. Specified in https://github.com/fieldsoftheworld/ftw-baselines First 4 S2 bands are for image t1 and last 4 bands are for image t2",
    "start_datetime": "2015-06-23T00:00:00Z",
    "end_datetime": "2024-08-27T23:59:59Z",
    "mlm:framework": "segmentation_models_pytorch.decoders.unet.model",
    "mlm:accelerator_constrained": false,
    "mlm:name": "U-Net_efficientnet-b3",
    "mlm:architecture": "segmentation_models_pytorch.decoders.unet.model.Unet",
    "mlm:tasks": [
      "semantic-segmentation"
    ],
    "mlm:input": [
      {
        "bands": [
          "B4",
          "B3",
          "B2",
          "B8",
          "B4",
          "B3",
          "B2",
          "B8"
        ],
        "variables": [],
        "name": "model_input",
        "input": {
          "shape": [
            -1,
            8,
            3,
            3
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 0,
            "stddev": 3000
          }
        ],
        "pre_processing_function": null
      }
    ],
    "mlm:output": [
      {
        "bands": [],
        "variables": [],
        "name": "model_output",
        "tasks": [
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            2
          ],
          "dim_order": [
            "batch",
            "classes"
          ],
          "data_type": "float32"
        },
        "classification:classes": [
          {
            "value": 0,
            "name": "class_0",
            "description": "Auto-generated class 0"
          },
          {
            "value": 1,
            "name": "class_1",
            "description": "Auto-generated class 1"
          }
        ],
        "post_processing_function": null
      }
    ],
    "mlm:total_parameters": 13160978,
    "mlm:pretrained": true,
    "datetime": null
  },
  "links": [
    {
      "rel": "cite-as",
      "href": "https://arxiv.org/abs/2409.16252",
      "type": "text/html",
      "title": "Publication for the training dataset of the model"
    },
    {
      "rel": "self",
      "href": "./item_pytorch_geo_unet.json",
      "type": "application/geo+json"
    },
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    }
  ],
  "assets": {
    "model": {
      "href": "https://huggingface.co/torchgeo/ftw/resolve/d2fdab6ea9d9cd38b491292cc9a5c8642533cef5/noncommercial/2-class/sentinel2_unet_effb3-bf010a31.pth",
      "type": "application/octet-stream; application=pytorch",
      "title": "U-Net_efficientnet-b3",
      "description": "A U-Net segmentation model with efficientnet-b3 encoder Weights are non-commercial.",
      "mlm:artifact_type": "torch.save",
      "eo:bands": [
        {
          "name": "B4"
        },
        {
          "name": "B3"
        },
        {
          "name": "B2"
        },
        {
          "name": "B8"
        },
        {
          "name": "B4"
        },
        {
          "name": "B3"
        },
        {
          "name": "B2"
        },
        {
          "name": "B8"
        }
      ],
      "roles": [
        "mlm:model",
        "mlm:weights",
        "data"
      ]
    },
    "source_code": {
      "href": "https://github.com/qubvel-org/segmentation_models.pytorch",
      "type": "text/html",
      "title": "Source code for U-Net_efficientnet-b3",
      "description": "GitHub repo of the pytorch model",
      "roles": [
        "mlm:source_code",
        "code"
      ]
    }
  },
  "collection": "ml-model-examples",
  "mlm:entrypoint": "segmentation_models_pytorch.decoders.unet.model.Unet"
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "STAC item auto-generated using unet_mlm() in https://raw.githubusercontent.com/stac-extensions/mlm/refs/heads/main/stac_model/examples.py",
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json"
  ],
  "id": "pytorch_geo_unet",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.88,
          37.13
        ],
        [
          -7.88,
          58.21
        ],
        [
          27.91,
          58.21
        ],
        [
          27.91,
          37.13
        ],
        [
          -7.88,
          37.13
        ]
      ]
    ]
  },
  "bbox": [
    -7.88,
    37.13,
    27.91,
    58.21
  ],
  "properties": {
    "description": "STAC item generated using unet_mlm() in stac_model/examples.py example. Specified in https://github.com/fieldsoftheworld/ftw-baselines First 4 S2 bands are for image t1 and last 4 bands are for image t2",
    "start_datetime": "2015-06-23T00:00:00Z",
    "end_datetime": "2024-08-27T23:59:59Z",
    "mlm:framework": "segmentation_models_pytorch.decoders.unet.model",
    "mlm:accelerator_constrained": false,
    "mlm:name": "U-Net_efficientnet-b3",
    "mlm:architecture": "segmentation_models_pytorch.decoders.unet.model.Unet",
    "mlm:tasks": [
      "semantic-segmentation"
    ],
    "mlm:input": [
      {
        "bands": [
          "B4",
          "B3",
          "B2",
          "B8",
          "B4",
          "B3",
          "B2",
          "B8"
        ],
        "variables": [],
        "name": "model_input",
        "input": {
          "shape": [
            -1,
            8,
            3,
            3
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 0,
            "stddev": 3000
          }
        ],
        "pre_processing_function": null
      }
    ],
    "mlm:output": [
      {
        "bands": [],
        "variables": [],
        "name": "model_output",
        "tasks": [
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            2
          ],
          "dim_order": [
            "batch",
            "classes"
          ],
          "data_type": "float32"
        },
        "classification:classes": [
          {
            "value": 0,
            "name": "class_0",
            "description": "Auto-generated class 0"
          },
          {
            "value": 1,
            "name": "class_1",
            "description": "Auto-generated class 1"
          }
        ],
        "post_processing_function": null
      }
    ],
    "mlm:total_parameters": 13160978,
    "mlm:pretrained": true,
    "datetime": null
  },
  "links": [
    {
      "rel": "cite-as",
      "href": "https://arxiv.org/abs/2409.16252",
      "type": "text/html",
      "title": "Publication for the training dataset of the model"
    },
    {
      "rel": "self",
      "href": "./item_pytorch_geo_unet.json",
      "type": "application/geo+json"
    },
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    }
  ],
  "assets": {
    "model": {
      "href": "https://huggingface.co/torchgeo/ftw/resolve/d2fdab6ea9d9cd38b491292cc9a5c8642533cef5/noncommercial/2-class/sentinel2_unet_effb3-bf010a31.pth",
      "type": "application/octet-stream; application=pytorch",
      "title": "U-Net_efficientnet-b3",
      "description": "A U-Net segmentation model with efficientnet-b3 encoder Weights are non-commercial.",
      "mlm:artifact_type": "torch.save",
      "eo:bands": [
        {
          "name": "B4"
        },
        {
          "name": "B3"
        },
        {
          "name": "B2"
        },
        {
          "name": "B8"
        },
        {
          "name": "B4"
        },
        {
          "name": "B3"
        },
        {
          "name": "B2"
        },
        {
          "name": "B8"
        }
      ],
      "roles": [
        "mlm:model",
        "mlm:weights",
        "data"
      ]
    },
    "source_code": {
      "href": "https://github.com/qubvel-org/segmentation_models.pytorch",
      "type": "text/html",
      "title": "Source code for U-Net_efficientnet-b3",
      "description": "GitHub repo of the pytorch model",
      "roles": [
        "mlm:source_code",
        "code"
      ]
    }
  },
  "collection": "ml-model-examples",
  "mlm:entrypoint": "segmentation_models_pytorch.decoders.unet.model.Unet"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <mlm:> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <classification:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-9/pytorch_geo_unet> a geojson:Feature ;
    dcterms:description "STAC item generated using unet_mlm() in stac_model/examples.py example. Specified in https://github.com/fieldsoftheworld/ftw-baselines First 4 S2 bands are for image t1 and last 4 bands are for image t2" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-9/collection.json> ],
        [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-9/item_pytorch_geo_unet.json> ],
        [ rdfs:label "Publication for the training dataset of the model" ;
            dcterms:type "text/html" ;
            ns2:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://arxiv.org/abs/2409.16252> ] ;
    geojson:bbox ( -7.88e+00 3.713e+01 2.791e+01 5.821e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88e+00 3.713e+01 ) ( -7.88e+00 5.821e+01 ) ( 2.791e+01 5.821e+01 ) ( 2.791e+01 3.713e+01 ) ( -7.88e+00 3.713e+01 ) ) ) ] ;
    stac:end_datetime "2024-08-27T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.5.1/schema.json" ;
    stac:start_datetime "2015-06-23T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    ns1:accelerator_constrained false ;
    ns1:architecture "segmentation_models_pytorch.decoders.unet.model.Unet" ;
    ns1:entrypoint "segmentation_models_pytorch.decoders.unet.model.Unet" ;
    ns1:framework "segmentation_models_pytorch.decoders.unet.model" ;
    ns1:input [ ] ;
    ns1:name "U-Net_efficientnet-b3" ;
    ns1:output [ ns3:classes [ dcterms:description "Auto-generated class 1" ],
                [ dcterms:description "Auto-generated class 0" ] ] ;
    ns1:pretrained true ;
    ns1:tasks "semantic-segmentation" ;
    ns1:total_parameters 13160978 .


```


### Demonstrate the use of MLM and Raster for bands description, with Raster bands directly in the Model Asset.
#### json
```json
{
  "$comment": "Demonstrate the use of MLM and Raster for bands description, with Raster bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "value_scaling": null,
        "resize_type": null,
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
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
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "raster:bands": [
        {
          "name": "B01",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B02",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B03",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B04",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B05",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B06",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B07",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B08",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B8A",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B09",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B10",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B11",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B12",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
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
      "href": "./item_raster_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and Raster for bands description, with Raster bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "value_scaling": null,
        "resize_type": null,
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
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
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "raster:bands": [
        {
          "name": "B01",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B02",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B03",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B04",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B05",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B06",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B07",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B08",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B8A",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B09",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B10",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B11",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B12",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
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
      "href": "./item_raster_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
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
@prefix ns3: <file:> .
@prefix ns4: <ml-aoi:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-10/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns3:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-10/item_raster_bands.json> ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns4:split "train" ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-10/collection.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.5.1/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    ns1:accelerator "cuda" ;
    ns1:accelerator_constrained false ;
    ns1:accelerator_summary "Unknown" ;
    ns1:architecture "ResNet" ;
    ns1:batch_size_suggestion 256 ;
    ns1:framework "pytorch" ;
    ns1:framework_version "2.1.2+cu121" ;
    ns1:input [ ] ;
    ns1:memory_size 1 ;
    ns1:name "Resnet-18 Sentinel-2 ALL MOCO" ;
    ns1:output [ ] ;
    ns1:pretrained_source "EuroSat Sentinel-2" ;
    ns1:tasks "classification" ;
    ns1:total_parameters 11700000 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: MLM extension 1.5.1
description: STAC MLM for STAC Items and STAC Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/mlm/v1.5.1/schema.json
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
    "assets": {
      "@context": {
        "type": "dct:format",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac_version": "stac:version",
    "keywords": {
      "@id": "dcat:keyword",
      "@container": "@set"
    },
    "license": "dcat:license",
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
    "providers": "stac:hasProvider",
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
    "title": {
      "@id": "dct:title",
      "@container": "@set"
    },
    "description": {
      "@id": "dct:description",
      "@container": "@set"
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
    "created": "dct:created",
    "updated": "dct:modified",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/mlm)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/mlm`

