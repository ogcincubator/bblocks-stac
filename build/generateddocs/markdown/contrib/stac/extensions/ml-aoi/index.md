
# STAC ML-AOI Extension (Schema)

`ogc.contrib.stac.extensions.ml-aoi` *v0.2.0*

STAC ML-AOI Extension for machine-learning training, validation and test areas of interest.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC ML-AOI training item
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/label/v1.0.1/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
    "https://stac-extensions.github.io/version/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "EuroSAT-subset-train-sample-42-class-Residential",
  "title": "EuroSAT subset train sample 42 class Residential",
  "description": "Annotated sample from the EuroSAT-subset-train collection.",
  "bbox": [
    -3.1472537450112785,
    51.531997746547134,
    -3.1380012709408427,
    51.53774085855159
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -3.1380012709408427,
          51.531997746547134
        ],
        [
          -3.1380012709408427,
          51.53774085855159
        ],
        [
          -3.1472537450112785,
          51.53774085855159
        ],
        [
          -3.1472537450112785,
          51.531997746547134
        ],
        [
          -3.1380012709408427,
          51.531997746547134
        ]
      ]
    ]
  },
  "assets": {
    "labels": {
      "title": "Labels for image Residential_1331 with Residential class",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/data/subset/ds/images/remote_sensing/otherDatasets/sentinel_2/label/Residential/Residential_1331.geojson",
      "type": "application/geo+json",
      "roles": [
        "data"
      ],
      "file:size": 749,
      "ml-aoi:role": "label"
    },
    "raster": {
      "title": "Raster Residential_1331 with Residential class",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/data/subset/ds/images/remote_sensing/otherDatasets/sentinel_2/tif/Residential/Residential_1331.tif",
      "type": "image/tiff; application=geotiff",
      "raster:bands": [
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        },
        {
          "nodata": 0,
          "unit": "m",
          "spatial_resolution": 10,
          "data_type": "uint16"
        }
      ],
      "roles": [
        "data"
      ],
      "file:size": 107244,
      "ml-aoi:role": "feature",
      "ml-aoi:reference-grid": true
    },
    "thumbnail": {
      "title": "Preview of Residential_1331.",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/data/subset/ds/images/remote_sensing/otherDatasets/sentinel_2/png/Residential/Residential_1331.png",
      "type": "image/png",
      "roles": [
        "thumbnail",
        "visual"
      ],
      "eo:bands": [
        {
          "name": "B04",
          "common_name": "red",
          "center_wavelength": 0.6645,
          "full_width_half_max": 0.038
        },
        {
          "name": "B03",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B02",
          "common_name": "blue",
          "center_wavelength": 0.4966,
          "full_width_half_max": 0.098
        }
      ],
      "file:size": 6984
    }
  },
  "collection": "EuroSAT-subset-train",
  "properties": {
    "datetime": "2023-12-19T16:11:19.208953+00:00",
    "license": "MIT",
    "version": "0.5.0",
    "label:properties": [
      "class"
    ],
    "label:tasks": [
      "segmentation",
      "classification"
    ],
    "label:type": "vector",
    "label:methods": [
      "manual"
    ],
    "label:description": "Land-cover area classification on Sentinel-2 image.",
    "label:classes": [
      {
        "name": "class",
        "classes": [
          "Residential",
          "7"
        ]
      }
    ],
    "label:overviews": [
      {
        "property_key": "class",
        "counts": [
          {
            "name": "Residential",
            "count": 1
          }
        ]
      }
    ],
    "ml-aoi:split": "train",
    "constellation": "sentinel-2",
    "instruments": [
      "msi"
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "center_wavelength": 0.4439,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "center_wavelength": 0.4966,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "center_wavelength": 0.6645,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "center_wavelength": 0.7039,
        "full_width_half_max": 0.019,
        "common_name": "rededge"
      },
      {
        "name": "B06",
        "center_wavelength": 0.7402,
        "full_width_half_max": 0.018,
        "common_name": "rededge"
      },
      {
        "name": "B07",
        "center_wavelength": 0.7825,
        "full_width_half_max": 0.028,
        "common_name": "rededge"
      },
      {
        "name": "B08",
        "common_name": "nir",
        "center_wavelength": 0.8351,
        "full_width_half_max": 0.145
      },
      {
        "name": "B08A",
        "center_wavelength": 0.8648,
        "full_width_half_max": 0.033,
        "common_name": "nir08"
      },
      {
        "name": "B09",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026,
        "common_name": "nir09"
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "center_wavelength": 1.3735,
        "full_width_half_max": 0.075
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "center_wavelength": 1.6137,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "center_wavelength": 2.22024,
        "full_width_half_max": 0.242
      }
    ],
    "view:off_nadir": 0,
    "gsd": 10
  },
  "links": [
    {
      "title": "Preview of Residential_1331.",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/data/subset/ds/images/remote_sensing/otherDatasets/sentinel_2/png/Residential/Residential_1331.png",
      "type": "image/png",
      "rel": "thumbnail"
    },
    {
      "title": "Raster Residential_1331 with Residential class",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/data/subset/ds/images/remote_sensing/otherDatasets/sentinel_2/tif/Residential/Residential_1331.tif",
      "type": "image/tiff; application=geotiff",
      "rel": "source",
      "label:assets": [
        "labels",
        "raster"
      ],
      "ml-aoi:role": "label"
    },
    {
      "title": "Raster Residential_1331 with Residential class",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/data/subset/ds/images/remote_sensing/otherDatasets/sentinel_2/tif/Residential/Residential_1331.tif",
      "type": "image/tiff; application=geotiff",
      "rel": "derived_from",
      "ml-aoi:role": "feature"
    },
    {
      "rel": "root",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "train"
    },
    {
      "rel": "collection",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "train"
    },
    {
      "rel": "self",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-42.json",
      "type": "application/geo+json"
    }
  ]
}

```

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
    "https://stac-extensions.github.io/stats/v0.2.0/schema.json",
    "https://stac-extensions.github.io/version/v1.0.0/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json"
  ],
  "type": "Collection",
  "id": "EuroSAT-subset-train",
  "title": "EuroSAT subset train",
  "description": "EuroSAT dataset with labeled annotations for land-cover classification and associated imagery. This collection represents the samples part of the train split set for training machine learning algorithms.",
  "version": "0.5.0",
  "experimental": true,
  "license": "MIT",
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
          "2015-06-27T10:25:31.456Z",
          "2017-06-14T00:00:00Z"
        ]
      ]
    }
  },
  "summaries": {
    "sci:doi": [
      "10.1109/JSTARS.2019.2918242"
    ],
    "sci:citation": [
      "Eurosat: A novel dataset and deep learning benchmark for land use and land cover classification. Patrick Helber, Benjamin Bischke, Andreas Dengel, Damian Borth. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2019."
    ],
    "sci:publications": [
      {
        "doi": "10.1109/IGARSS.2018.8519248",
        "citation": "Introducing EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification. Patrick Helber, Benjamin Bischke, Andreas Dengel. 2018 IEEE International Geoscience and Remote Sensing Symposium, 2018."
      }
    ],
    "ml-aoi:split": [
      "train"
    ],
    "constellation": [
      "sentinel-2"
    ],
    "instruments": [
      "msi"
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "center_wavelength": 0.4439,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "center_wavelength": 0.4966,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "center_wavelength": 0.6645,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "center_wavelength": 0.7039,
        "full_width_half_max": 0.019,
        "common_name": "rededge"
      },
      {
        "name": "B06",
        "center_wavelength": 0.7402,
        "full_width_half_max": 0.018,
        "common_name": "rededge"
      },
      {
        "name": "B07",
        "center_wavelength": 0.7825,
        "full_width_half_max": 0.028,
        "common_name": "rededge"
      },
      {
        "name": "B08",
        "common_name": "nir",
        "center_wavelength": 0.8351,
        "full_width_half_max": 0.145
      },
      {
        "name": "B08A",
        "center_wavelength": 0.8648,
        "full_width_half_max": 0.033,
        "common_name": "nir08"
      },
      {
        "name": "B09",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026,
        "common_name": "nir09"
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "center_wavelength": 1.3735,
        "full_width_half_max": 0.075
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "center_wavelength": 1.6137,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "center_wavelength": 2.22024,
        "full_width_half_max": 0.242
      }
    ],
    "view:off_nadir": [
      0
    ],
    "gsd": [
      10
    ]
  },
  "assets": {
    "source": {
      "href": "https://github.com/phelber/EuroSAT/",
      "type": "text/html",
      "roles": [
        "data",
        "source",
        "scientific",
        "citation"
      ],
      "title": "GitHub repository",
      "description": "Source GitHub repository of the EuroSAT dataset.",
      "sci:doi": "10.1109/JSTARS.2019.2918242"
    },
    "paper": {
      "href": "https://www.researchgate.net/publication/319463676",
      "type": "text/html",
      "roles": [
        "paper",
        "scientific",
        "citation"
      ],
      "title": "Scientific Paper",
      "description": "ResearchGate page with embedded PDF of the scientific paper supporting the dataset.",
      "sci:doi": "10.1109/JSTARS.2019.2918242"
    },
    "thumbnail": {
      "href": "https://raw.githubusercontent.com/phelber/EuroSAT/master/eurosat_overview_small.jpg",
      "type": "image/jpeg",
      "roles": [
        "thumbnail",
        "overview"
      ],
      "description": "Preview of dataset samples.",
      "sci:doi": "10.1109/JSTARS.2019.2918242"
    },
    "license": {
      "href": "https://raw.githubusercontent.com/phelber/EuroSAT/master/LICENSE",
      "type": "text/plain",
      "roles": [
        "legal",
        "license"
      ],
      "title": "License",
      "description": "License contents associated to the EuroSAT dataset.",
      "sci:doi": "10.1109/JSTARS.2019.2918242"
    }
  },
  "stats:items": {
    "count": 60
  },
  "links": [
    {
      "rel": "cite-as",
      "href": "https://arxiv.org/abs/1709.00029",
      "type": "text/html",
      "title": "EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification"
    },
    {
      "rel": "license",
      "href": "https://raw.githubusercontent.com/phelber/EuroSAT/master/LICENSE",
      "type": "text/html",
      "title": "EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-0.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-1.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-2.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-3.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-4.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-5.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-6.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-7.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-8.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-9.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-10.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-11.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-12.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-13.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-14.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-15.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-16.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-17.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-18.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-19.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-20.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-21.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-22.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-23.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-24.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-25.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-26.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-27.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-28.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-29.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-30.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-31.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-32.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-33.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-34.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-35.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-36.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-37.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-38.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-39.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-40.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-41.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-42.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-43.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-44.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-45.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-46.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-47.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-48.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-49.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-50.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-51.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-52.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-53.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-54.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-55.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-56.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-57.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-58.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-59.json",
      "type": "application/geo+json"
    },
    {
      "rel": "root",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/catalog.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "train"
    },
    {
      "rel": "collection",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "train"
    },
    {
      "rel": "related",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/test/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "test"
    },
    {
      "rel": "related",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/validate/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "validate"
    },
    {
      "rel": "parent",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/catalog.json",
      "type": "application/json",
      "title": "STAC Catalog"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/ml-aoi/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
    "https://stac-extensions.github.io/stats/v0.2.0/schema.json",
    "https://stac-extensions.github.io/version/v1.0.0/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json"
  ],
  "type": "Collection",
  "id": "EuroSAT-subset-train",
  "title": "EuroSAT subset train",
  "description": "EuroSAT dataset with labeled annotations for land-cover classification and associated imagery. This collection represents the samples part of the train split set for training machine learning algorithms.",
  "version": "0.5.0",
  "experimental": true,
  "license": "MIT",
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
          "2015-06-27T10:25:31.456Z",
          "2017-06-14T00:00:00Z"
        ]
      ]
    }
  },
  "summaries": {
    "sci:doi": [
      "10.1109/JSTARS.2019.2918242"
    ],
    "sci:citation": [
      "Eurosat: A novel dataset and deep learning benchmark for land use and land cover classification. Patrick Helber, Benjamin Bischke, Andreas Dengel, Damian Borth. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2019."
    ],
    "sci:publications": [
      {
        "doi": "10.1109/IGARSS.2018.8519248",
        "citation": "Introducing EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification. Patrick Helber, Benjamin Bischke, Andreas Dengel. 2018 IEEE International Geoscience and Remote Sensing Symposium, 2018."
      }
    ],
    "ml-aoi:split": [
      "train"
    ],
    "constellation": [
      "sentinel-2"
    ],
    "instruments": [
      "msi"
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "center_wavelength": 0.4439,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "center_wavelength": 0.4966,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "center_wavelength": 0.6645,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "center_wavelength": 0.7039,
        "full_width_half_max": 0.019,
        "common_name": "rededge"
      },
      {
        "name": "B06",
        "center_wavelength": 0.7402,
        "full_width_half_max": 0.018,
        "common_name": "rededge"
      },
      {
        "name": "B07",
        "center_wavelength": 0.7825,
        "full_width_half_max": 0.028,
        "common_name": "rededge"
      },
      {
        "name": "B08",
        "common_name": "nir",
        "center_wavelength": 0.8351,
        "full_width_half_max": 0.145
      },
      {
        "name": "B08A",
        "center_wavelength": 0.8648,
        "full_width_half_max": 0.033,
        "common_name": "nir08"
      },
      {
        "name": "B09",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026,
        "common_name": "nir09"
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "center_wavelength": 1.3735,
        "full_width_half_max": 0.075
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "center_wavelength": 1.6137,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "center_wavelength": 2.22024,
        "full_width_half_max": 0.242
      }
    ],
    "view:off_nadir": [
      0
    ],
    "gsd": [
      10
    ]
  },
  "assets": {
    "source": {
      "href": "https://github.com/phelber/EuroSAT/",
      "type": "text/html",
      "roles": [
        "data",
        "source",
        "scientific",
        "citation"
      ],
      "title": "GitHub repository",
      "description": "Source GitHub repository of the EuroSAT dataset.",
      "sci:doi": "10.1109/JSTARS.2019.2918242"
    },
    "paper": {
      "href": "https://www.researchgate.net/publication/319463676",
      "type": "text/html",
      "roles": [
        "paper",
        "scientific",
        "citation"
      ],
      "title": "Scientific Paper",
      "description": "ResearchGate page with embedded PDF of the scientific paper supporting the dataset.",
      "sci:doi": "10.1109/JSTARS.2019.2918242"
    },
    "thumbnail": {
      "href": "https://raw.githubusercontent.com/phelber/EuroSAT/master/eurosat_overview_small.jpg",
      "type": "image/jpeg",
      "roles": [
        "thumbnail",
        "overview"
      ],
      "description": "Preview of dataset samples.",
      "sci:doi": "10.1109/JSTARS.2019.2918242"
    },
    "license": {
      "href": "https://raw.githubusercontent.com/phelber/EuroSAT/master/LICENSE",
      "type": "text/plain",
      "roles": [
        "legal",
        "license"
      ],
      "title": "License",
      "description": "License contents associated to the EuroSAT dataset.",
      "sci:doi": "10.1109/JSTARS.2019.2918242"
    }
  },
  "stats:items": {
    "count": 60
  },
  "links": [
    {
      "rel": "cite-as",
      "href": "https://arxiv.org/abs/1709.00029",
      "type": "text/html",
      "title": "EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification"
    },
    {
      "rel": "license",
      "href": "https://raw.githubusercontent.com/phelber/EuroSAT/master/LICENSE",
      "type": "text/html",
      "title": "EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-0.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-1.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-2.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-3.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-4.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-5.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-6.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-7.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-8.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-9.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-10.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-11.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-12.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-13.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-14.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-15.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-16.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-17.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-18.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-19.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-20.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-21.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-22.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-23.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-24.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-25.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-26.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-27.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-28.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-29.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-30.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-31.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-32.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-33.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-34.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-35.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-36.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-37.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-38.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-39.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-40.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-41.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-42.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-43.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-44.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-45.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-46.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-47.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-48.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-49.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-50.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-51.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-52.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-53.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-54.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-55.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-56.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-57.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-58.json",
      "type": "application/geo+json"
    },
    {
      "rel": "item",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-59.json",
      "type": "application/geo+json"
    },
    {
      "rel": "root",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/catalog.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "train"
    },
    {
      "rel": "collection",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "train"
    },
    {
      "rel": "related",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/test/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "test"
    },
    {
      "rel": "related",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/validate/collection.json",
      "type": "application/json",
      "title": "EuroSAT STAC Collection with samples from 'train' split.",
      "ml-aoi:split": "validate"
    },
    {
      "rel": "parent",
      "href": "https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/catalog.json",
      "type": "application/json",
      "title": "STAC Catalog"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ml-aoi: <https://w3id.org/ogc/stac/ml-aoi/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <stats:> .
@prefix ns3: <https://w3id.org/ogc/stac/assets/> .
@prefix ns4: <sci:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/ml-aoi/collection/EuroSAT-subset-train> a <https://example.com/stac/ml-aoi/collection/Collection> ;
    dcterms:description "EuroSAT dataset with labeled annotations for land-cover classification and associated imagery. This collection represents the samples part of the train split set for training machine learning algorithms." ;
    dcterms:extent [ ] ;
    dcterms:title "EuroSAT subset train" ;
    rdfs:seeAlso [ rdfs:label "EuroSAT STAC Collection with samples from 'train' split." ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/validate/collection.json> ;
            ml-aoi:split "validate"^^xsd:string ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-57.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-14.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/catalog.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-46.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-32.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-25.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-58.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-22.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-41.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-7.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-11.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-44.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-36.json> ],
        [ rdfs:label "EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://raw.githubusercontent.com/phelber/EuroSAT/master/LICENSE> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-12.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-20.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-55.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-52.json> ],
        [ rdfs:label "EuroSAT STAC Collection with samples from 'train' split." ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/test/collection.json> ;
            ml-aoi:split "test"^^xsd:string ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-47.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-33.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-34.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-24.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-53.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-42.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-30.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-45.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-59.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-13.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-27.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-9.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-48.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-18.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-49.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-31.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-6.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-1.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-8.json> ],
        [ rdfs:label "EuroSAT STAC Collection with samples from 'train' split." ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/collection.json> ;
            ml-aoi:split "train"^^xsd:string ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-19.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-56.json> ],
        [ rdfs:label "EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://arxiv.org/abs/1709.00029> ],
        [ rdfs:label "STAC Catalog" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/catalog.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-51.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-37.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-16.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-17.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-3.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-29.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-28.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-54.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-39.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-21.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-15.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-26.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-50.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-2.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-38.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-4.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-5.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-43.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-10.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-40.json> ],
        [ rdfs:label "EuroSAT STAC Collection with samples from 'train' split." ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/collection.json> ;
            ml-aoi:split "train"^^xsd:string ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-0.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-35.json> ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://raw.githubusercontent.com/ai-extensions/stac-data-loader/0.5.0/data/EuroSAT/stac/subset/train/item-23.json> ] ;
    dcat:license "MIT" ;
    stac:hasAsset [ dcat:license <https://raw.githubusercontent.com/phelber/EuroSAT/master/LICENSE> ;
            ns3:paper <https://www.researchgate.net/publication/319463676> ;
            ns3:source <https://github.com/phelber/EuroSAT/> ;
            ns3:thumbnail <https://raw.githubusercontent.com/phelber/EuroSAT/master/eurosat_overview_small.jpg> ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
        "https://stac-extensions.github.io/stats/v0.2.0/schema.json",
        "https://stac-extensions.github.io/version/v1.0.0/schema.json",
        "https://stac-extensions.github.io/view/v1.0.0/schema.json" ;
    stac:version "1.0.0" ;
    ns2:items [ ] .

<https://github.com/phelber/EuroSAT/> dcterms:description "Source GitHub repository of the EuroSAT dataset." ;
    dcterms:format "text/html" ;
    dcterms:title "GitHub repository" ;
    stac:hasAssetroles "citation"^^xsd:string,
        "data"^^xsd:string,
        "scientific"^^xsd:string,
        "source"^^xsd:string ;
    ns4:doi "10.1109/JSTARS.2019.2918242" .

<https://raw.githubusercontent.com/phelber/EuroSAT/master/eurosat_overview_small.jpg> dcterms:description "Preview of dataset samples." ;
    dcterms:format "image/jpeg" ;
    stac:hasAssetroles "overview"^^xsd:string,
        "thumbnail"^^xsd:string ;
    ns4:doi "10.1109/JSTARS.2019.2918242" .

<https://www.researchgate.net/publication/319463676> dcterms:description "ResearchGate page with embedded PDF of the scientific paper supporting the dataset." ;
    dcterms:format "text/html" ;
    dcterms:title "Scientific Paper" ;
    stac:hasAssetroles "citation"^^xsd:string,
        "paper"^^xsd:string,
        "scientific"^^xsd:string ;
    ns4:doi "10.1109/JSTARS.2019.2918242" .

<https://raw.githubusercontent.com/phelber/EuroSAT/master/LICENSE> dcterms:description "License contents associated to the EuroSAT dataset." ;
    dcterms:format "text/plain" ;
    dcterms:title "License" ;
    stac:hasAssetroles "legal"^^xsd:string,
        "license"^^xsd:string ;
    ns4:doi "10.1109/JSTARS.2019.2918242" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ML-AOI extension
description: STAC ML-AOI Extension for machine-learning areas of interest.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json
x-jsonld-extra-terms:
  ml-aoi:split:
    x-jsonld-id: https://w3id.org/ogc/stac/ml-aoi/split
    x-jsonld-type: xsd:string
  ml-aoi:role:
    x-jsonld-id: https://w3id.org/ogc/stac/ml-aoi/role
    x-jsonld-type: xsd:string
  ml-aoi:reference-grid:
    x-jsonld-id: https://w3id.org/ogc/stac/ml-aoi/reference-grid
    x-jsonld-type: xsd:boolean
  ml-aoi:resampling-method:
    x-jsonld-id: https://w3id.org/ogc/stac/ml-aoi/resampling-method
    x-jsonld-type: xsd:string
x-jsonld-prefixes:
  ml-aoi: https://w3id.org/ogc/stac/ml-aoi/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/ml-aoi/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/ml-aoi/schema.yaml)


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
    "ml-aoi:split": {
      "@id": "ml-aoi:split",
      "@type": "xsd:string"
    },
    "ml-aoi:role": {
      "@id": "ml-aoi:role",
      "@type": "xsd:string"
    },
    "ml-aoi:reference-grid": {
      "@id": "ml-aoi:reference-grid",
      "@type": "xsd:boolean"
    },
    "ml-aoi:resampling-method": {
      "@id": "ml-aoi:resampling-method",
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
    "ml-aoi": "https://w3id.org/ogc/stac/ml-aoi/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/ml-aoi/context.jsonld)

## Sources

* [STAC ML-AOI Extension](https://github.com/stac-extensions/ml-aoi/tree/v0.2.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/ml-aoi`

