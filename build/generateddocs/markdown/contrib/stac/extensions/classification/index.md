
# STAC Classification Extension (Schema)

`ogc.contrib.stac.extensions.classification` *v2.0.0*

STAC Classification Extension for STAC Items and STAC Collections.

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
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/classification/context.jsonld",
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
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<https://example.com/stac/classification/example-1/103001005D31F500> a <https://example.com/stac/classification/example-1/Collection> ;
    dcterms:description "103001005D31F500 ARD Tiles" ;
    dcterms:extent [ ] ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/classification/order_collections/5867496013686833273_root_collection.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/classification/10/120020223032/2016-10-08/103001005D31F500.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/classification/order_collections/5867496013686833273_root_collection.json> ] ;
    dcat:license "proprietary" ;
    stac:hasExtension "https://stac-extensions.github.io/classification/v2.0.0/schema.json",
        "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
        "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
        "https://stac-extensions.github.io/raster/v1.0.0/schema.json" ;
    stac:version "1.0.0" .


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
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/classification/context.jsonld",
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
@prefix ns1: <mlm:> .
@prefix ns2: <classification:> .
@prefix ns3: <ml-aoi:> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix ns5: <file:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix raster: <https://w3id.org/ogc/stac/raster/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/classification/example-1/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns5:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns4:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/classification/example-1/resnet-18_sentinel-2_all_moco_classification.json> ],
        [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns3:split "train" ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://crim-ca.github.io/mlm-extension/v1.0.0/schema.json",
        "https://stac-extensions.github.io/classification/v2.0.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    raster:bands [ raster:bits_per_sample 15 ;
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
            raster:name "B11" ;
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
            raster:name "B08" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 10 ;
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
            raster:name "B02" ;
            raster:nodata 0 ;
            raster:offset 0 ;
            raster:scale 1e-04 ;
            raster:spatial_resolution 10 ;
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
            raster:name "B06" ;
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
            raster:name "B07" ;
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
    ns1:output [ ns2:classes [ dcterms:description "Marks residential buildings with a bold red color." ;
                    dcterms:title "Residential Buildings" ],
                [ dcterms:description "Represents areas of annual crops with a bright yellow color." ;
                    dcterms:title "Annual Crop" ],
                [ dcterms:description "Depicts rivers and water bodies with a vivid cyan color." ;
                    dcterms:title "River" ],
                [ dcterms:description "Highlights industrial buildings with a vibrant purple color." ;
                    dcterms:title "Industrial Buildings" ],
                [ dcterms:description "Depicts forested areas with a deep green color." ;
                    dcterms:title "Forest" ],
                [ dcterms:description "Indicates areas of herbaceous vegetation with a green-yellow hue." ;
                    dcterms:title "Herbaceous Vegetation" ],
                [ dcterms:description "Illustrates pasture areas with a fresh lawn green color." ;
                    dcterms:title "Pasture" ],
                [ dcterms:description "Represents permanent crop areas with a dark green color." ;
                    dcterms:title "Permanent Crop" ],
                [ dcterms:description "Denotes highways and roads with a neutral gray color." ;
                    dcterms:title "Gray" ],
                [ dcterms:description "Indicates seas and lakes with a serene blue color." ;
                    dcterms:title "Sea and Lake" ] ] ;
    ns1:pretrained_source "EuroSat Sentinel-2" ;
    ns1:tasks "classification" ;
    ns1:total_parameters 11700000 .


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
- $ref: https://stac-extensions.github.io/classification/v2.0.0/schema.json
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/classification/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/classification/schema.yaml)


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
      "@context": {
        "logo": {
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
          }
        }
      },
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "rights": "dcat:rights",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/classification/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/classification)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/classification`

