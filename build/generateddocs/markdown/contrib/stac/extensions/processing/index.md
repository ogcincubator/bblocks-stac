
# STAC Processing Extension (Schema)

`ogc.contrib.stac.extensions.processing` *v0.1*

STAC Processing Extension for STAC Items and STAC Collections.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Collection
#### json
```json
{
  "type": "Collection",
  "id": "103001005D31F500",
  "stac_version": "1.0.0",
  "description": "103001005D31F500 ARD Tiles",
  "links": [
    {
      "rel": "root",
      "href": "../order_collections/5867496013686833273_root_collection.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../order_collections/5867496013686833273_root_collection.json",
      "type": "application/json"
    },
    {
      "rel": "item",
      "href": "../10/120020223032/2016-10-08/103001005D31F500.json",
      "type": "application/json"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -122.43409303549794,
          37.76425505192271,
          -122.37337588954041,
          37.812440528660765
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2016-10-08 19:25:32Z",
          "2016-10-08 19:25:32Z"
        ]
      ]
    }
  },
  "item_assets": {
    "cloud-mask-raster": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Cloud/Cloud Shadow Coverage Raster",
      "description": "thematic raster, 0 -> no data, 1 -> clear, 2 -> cloud, 3 -> cloud shadow",
      "proj:shape": [
        2176,
        2176
      ],
      "eo:bands": [
        {
          "name": "BAND_CM",
          "description": "Clouds/Cloud Shadows Mask"
        }
      ],
      "raster:bands": [
        {
          "classification:classes": [
            {
              "value": 0,
              "name": "nodata",
              "description": "NoData",
              "nodata": true
            },
            {
              "value": 1,
              "name": "clear",
              "description": "Clear of clouds or shadows"
            },
            {
              "value": 2,
              "name": "cloud",
              "description": "Clouds",
              "color_hint": "B8D0EC"
            },
            {
              "value": 3,
              "name": "cloud_shadow",
              "description": "Cloud shadows",
              "color_hint": "9C9EA0"
            }
          ]
        }
      ]
    },
    "visual": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Visual (RGB) Image",
      "proj:shape": [
        17408,
        17408
      ],
      "eo:bands": [
        {
          "name": "BAND_R",
          "common_name": "red",
          "description": "Red"
        },
        {
          "name": "BAND_G",
          "common_name": "green",
          "description": "Green"
        },
        {
          "name": "BAND_B",
          "common_name": "blue",
          "description": "Blue"
        }
      ]
    }
  },
  "license": "proprietary",
  "stac_extensions": [
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.0.0/schema.json",
    "https://stac-extensions.github.io/classification/v2.0.0/schema.json"
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/context.jsonld",
  "type": "Collection",
  "id": "103001005D31F500",
  "stac_version": "1.0.0",
  "description": "103001005D31F500 ARD Tiles",
  "links": [
    {
      "rel": "root",
      "href": "../order_collections/5867496013686833273_root_collection.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../order_collections/5867496013686833273_root_collection.json",
      "type": "application/json"
    },
    {
      "rel": "item",
      "href": "../10/120020223032/2016-10-08/103001005D31F500.json",
      "type": "application/json"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -122.43409303549794,
          37.76425505192271,
          -122.37337588954041,
          37.812440528660765
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2016-10-08 19:25:32Z",
          "2016-10-08 19:25:32Z"
        ]
      ]
    }
  },
  "item_assets": {
    "cloud-mask-raster": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Cloud/Cloud Shadow Coverage Raster",
      "description": "thematic raster, 0 -> no data, 1 -> clear, 2 -> cloud, 3 -> cloud shadow",
      "proj:shape": [
        2176,
        2176
      ],
      "eo:bands": [
        {
          "name": "BAND_CM",
          "description": "Clouds/Cloud Shadows Mask"
        }
      ],
      "raster:bands": [
        {
          "classification:classes": [
            {
              "value": 0,
              "name": "nodata",
              "description": "NoData",
              "nodata": true
            },
            {
              "value": 1,
              "name": "clear",
              "description": "Clear of clouds or shadows"
            },
            {
              "value": 2,
              "name": "cloud",
              "description": "Clouds",
              "color_hint": "B8D0EC"
            },
            {
              "value": 3,
              "name": "cloud_shadow",
              "description": "Cloud shadows",
              "color_hint": "9C9EA0"
            }
          ]
        }
      ]
    },
    "visual": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Visual (RGB) Image",
      "proj:shape": [
        17408,
        17408
      ],
      "eo:bands": [
        {
          "name": "BAND_R",
          "common_name": "red",
          "description": "Red"
        },
        {
          "name": "BAND_G",
          "common_name": "green",
          "description": "Green"
        },
        {
          "name": "BAND_B",
          "common_name": "blue",
          "description": "Blue"
        }
      ]
    }
  },
  "license": "proprietary",
  "stac_extensions": [
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.0.0/schema.json",
    "https://stac-extensions.github.io/classification/v2.0.0/schema.json"
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<https://example.com/stac/classification/example-1/103001005D31F500> a <https://example.com/stac/classification/example-1/Collection> ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/classification/10/120020223032/2016-10-08/103001005D31F500.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/classification/order_collections/5867496013686833273_root_collection.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/classification/order_collections/5867496013686833273_root_collection.json> ] .


```


### Item Model Classes
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://crim-ca.github.io/mlm-extension/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
    "https://stac-extensions.github.io/classification/v2.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
            "channel",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "norm_type": null,
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
        "classification:classes": [
          {
            "value": 0,
            "name": "AnnualCrop",
            "color_hint": "FFFF00",
            "nodata": false,
            "title": "Annual Crop",
            "description": "Represents areas of annual crops with a bright yellow color."
          },
          {
            "value": 1,
            "name": "Forest",
            "color_hint": "008000",
            "nodata": false,
            "title": "Forest",
            "description": "Depicts forested areas with a deep green color."
          },
          {
            "value": 2,
            "name": "HerbaceousVegetation",
            "color_hint": "ADFF2F",
            "nodata": false,
            "title": "Herbaceous Vegetation",
            "description": "Indicates areas of herbaceous vegetation with a green-yellow hue."
          },
          {
            "value": 3,
            "name": "Highway",
            "color_hint": "808080",
            "nodata": false,
            "title": "Gray",
            "description": "Denotes highways and roads with a neutral gray color."
          },
          {
            "value": 4,
            "name": "Industrial",
            "color_hint": "800080",
            "nodata": false,
            "title": "Industrial Buildings",
            "description": "Highlights industrial buildings with a vibrant purple color."
          },
          {
            "value": 5,
            "name": "Pasture",
            "color_hint": "7CFC00",
            "nodata": false,
            "title": "Pasture",
            "description": "Illustrates pasture areas with a fresh lawn green color."
          },
          {
            "value": 6,
            "name": "PermanentCrop",
            "color_hint": "006400",
            "nodata": false,
            "title": "Permanent Crop",
            "description": "Represents permanent crop areas with a dark green color."
          },
          {
            "value": 7,
            "name": "Residential",
            "color_hint": "FF0000",
            "nodata": false,
            "title": "Residential Buildings",
            "description": "Marks residential buildings with a bold red color."
          },
          {
            "value": 8,
            "name": "River",
            "color_hint": "00FFFF",
            "nodata": false,
            "title": "River",
            "description": "Depicts rivers and water bodies with a vivid cyan color."
          },
          {
            "value": 9,
            "name": "SeaLake",
            "color_hint": "0000FF",
            "nodata": false,
            "title": "Sea and Lake",
            "description": "Indicates seas and lakes with a serene blue color."
          }
        ],
        "post_processing_function": null
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
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:model",
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "resnet-18_sentinel-2_all_moco_classification.json",
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
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://crim-ca.github.io/mlm-extension/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
    "https://stac-extensions.github.io/classification/v2.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
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
            "channel",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "norm_type": null,
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
        "classification:classes": [
          {
            "value": 0,
            "name": "AnnualCrop",
            "color_hint": "FFFF00",
            "nodata": false,
            "title": "Annual Crop",
            "description": "Represents areas of annual crops with a bright yellow color."
          },
          {
            "value": 1,
            "name": "Forest",
            "color_hint": "008000",
            "nodata": false,
            "title": "Forest",
            "description": "Depicts forested areas with a deep green color."
          },
          {
            "value": 2,
            "name": "HerbaceousVegetation",
            "color_hint": "ADFF2F",
            "nodata": false,
            "title": "Herbaceous Vegetation",
            "description": "Indicates areas of herbaceous vegetation with a green-yellow hue."
          },
          {
            "value": 3,
            "name": "Highway",
            "color_hint": "808080",
            "nodata": false,
            "title": "Gray",
            "description": "Denotes highways and roads with a neutral gray color."
          },
          {
            "value": 4,
            "name": "Industrial",
            "color_hint": "800080",
            "nodata": false,
            "title": "Industrial Buildings",
            "description": "Highlights industrial buildings with a vibrant purple color."
          },
          {
            "value": 5,
            "name": "Pasture",
            "color_hint": "7CFC00",
            "nodata": false,
            "title": "Pasture",
            "description": "Illustrates pasture areas with a fresh lawn green color."
          },
          {
            "value": 6,
            "name": "PermanentCrop",
            "color_hint": "006400",
            "nodata": false,
            "title": "Permanent Crop",
            "description": "Represents permanent crop areas with a dark green color."
          },
          {
            "value": 7,
            "name": "Residential",
            "color_hint": "FF0000",
            "nodata": false,
            "title": "Residential Buildings",
            "description": "Marks residential buildings with a bold red color."
          },
          {
            "value": 8,
            "name": "River",
            "color_hint": "00FFFF",
            "nodata": false,
            "title": "River",
            "description": "Depicts rivers and water bodies with a vivid cyan color."
          },
          {
            "value": 9,
            "name": "SeaLake",
            "color_hint": "0000FF",
            "nodata": false,
            "title": "Sea and Lake",
            "description": "Indicates seas and lakes with a serene blue color."
          }
        ],
        "post_processing_function": null
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
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:model",
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "resnet-18_sentinel-2_all_moco_classification.json",
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
@prefix ns1: <classification:> .
@prefix ns2: <file:> .
@prefix ns3: <mlm:> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix ns5: <ml-aoi:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix raster: <https://w3id.org/ogc/stac/raster/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/classification/example-1/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns2:size 43000000 ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns5:split "train" ],
        [ dcterms:type "application/geo+json" ;
            ns4:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/classification/example-1/resnet-18_sentinel-2_all_moco_classification.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:assets <https://example.com/stac/classification/example-1/source_code>,
        <https://example.com/stac/classification/example-1/weights> ;
    raster:bands [ raster:bits_per_sample 15 ;
            raster:data_type "uint16" ;
            raster:name "B08" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 10 ;
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
            raster:name "B04" ;
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
            raster:name "B10" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 60 ;
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
            raster:name "B03" ;
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
            raster:name "B09" ;
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
            raster:name "B07" ;
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
            raster:name "B12" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 20 ;
            raster:unit "m" ] ;
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
    ns3:output [ ns1:classes [ rdfs:label "Forest" ],
                [ rdfs:label "Residential Buildings" ],
                [ rdfs:label "Industrial Buildings" ],
                [ rdfs:label "Permanent Crop" ],
                [ rdfs:label "Pasture" ],
                [ rdfs:label "Sea and Lake" ],
                [ rdfs:label "Herbaceous Vegetation" ],
                [ rdfs:label "River" ],
                [ rdfs:label "Gray" ],
                [ rdfs:label "Annual Crop" ] ] ;
    ns3:pretrained_source "EuroSat Sentinel-2" ;
    ns3:tasks "classification" ;
    ns3:total_parameters 11700000 .

<https://example.com/stac/classification/example-1/source_code> a <https://example.com/stac/classification/example-1/text/x-python> ;
    rdfs:label "Model implementation." ;
    oa:hasTarget <https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> .

<https://example.com/stac/classification/example-1/weights> rdfs:label "Pytorch weights checkpoint" ;
    oa:hasTarget <https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> .


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
- $ref: https://stac-extensions.github.io/processing/v1.2.0/schema.json
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/schema.yaml)


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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/processing)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/processing`

