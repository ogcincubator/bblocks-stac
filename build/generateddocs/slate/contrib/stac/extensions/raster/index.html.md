---
title: STAC Raster Extension (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>STAC Raster Extension</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: STAC Raster Extension (Schema)
---


# STAC Raster Extension `ogc.contrib.stac.extensions.raster`

An item can describe assets that are rasters of one or multiple bands with some information common to them all (raster size, projection) and also specific to each of them (data type, unit, number of bits used, nodata). A raster is often strongly linked with the georeferencing transform and coordinate system definition of all bands (using the projection extension). In many applications, it is interesting to have some metadata about the rasters in the asset (values statistics, value interpretation, transforms).

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/ogcincubator/bblocks-stac/blob/master/build/tests/contrib/stac/extensions/raster/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example of Raster item - Sentinel2



```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json"
  ],
  "id": "S2B_33SVB_20210221_0_L2A",
  "bbox": [
    13.86148243891681,
    36.95257399124932,
    15.111074610520053,
    37.94752813015372
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          13.876381589019879,
          36.95257399124932
        ],
        [
          13.86148243891681,
          37.942072015005024
        ],
        [
          15.111074610520053,
          37.94752813015372
        ],
        [
          15.109620666835209,
          36.95783951241028
        ],
        [
          13.876381589019879,
          36.95257399124932
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2021-02-21T10:00:17Z",
    "platform": "sentinel-2b",
    "constellation": "sentinel-2",
    "instruments": [
      "msi"
    ],
    "gsd": 10,
    "view:off_nadir": 0,
    "proj:epsg": 32633,
    "sentinel:utm_zone": 33,
    "sentinel:latitude_band": "S",
    "sentinel:grid_square": "VB",
    "sentinel:sequence": "0",
    "sentinel:product_id": "S2B_MSIL2A_20210221T095029_N0214_R079_T33SVB_20210221T115149",
    "sentinel:data_coverage": 100,
    "eo:cloud_cover": 21.22,
    "sentinel:valid_cloud_cover": true
  },
  "collection": "sentinel-s2-l2a-cogs",
  "assets": {
    "thumbnail": {
      "title": "Thumbnail",
      "type": "image/png",
      "roles": [
        "thumbnail"
      ],
      "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/S/VB/2021/2/21/0/preview.jpg"
    },
    "overview": {
      "title": "True color image",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "overview"
      ],
      "gsd": 10,
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
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/L2A_PVI.tif",
      "proj:shape": [
        343,
        343
      ],
      "proj:transform": [
        320,
        0,
        399960,
        0,
        -320,
        4200000,
        0,
        0,
        1
      ]
    },
    "info": {
      "title": "Original JSON metadata",
      "type": "application/json",
      "roles": [
        "metadata"
      ],
      "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/S/VB/2021/2/21/0/tileInfo.json"
    },
    "metadata": {
      "title": "Original XML metadata",
      "type": "application/xml",
      "roles": [
        "metadata"
      ],
      "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/S/VB/2021/2/21/0/metadata.xml"
    },
    "visual": {
      "title": "True color image",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "overview"
      ],
      "gsd": 10,
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
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/TCI.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ]
    },
    "B01": {
      "title": "Band 1 (coastal) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 60,
      "eo:bands": [
        {
          "name": "B01",
          "common_name": "coastal",
          "center_wavelength": 0.4439,
          "full_width_half_max": 0.027
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B01.tif",
      "proj:shape": [
        1830,
        1830
      ],
      "proj:transform": [
        60,
        0,
        399960,
        0,
        -60,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 60,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 20567,
            "mean": 2339.4759595597,
            "stddev": 3026.6973619954,
            "valid_percent": 99.83
          }
        }
      ]
    },
    "B02": {
      "title": "Band 2 (blue) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "eo:bands": [
        {
          "name": "B02",
          "common_name": "blue",
          "center_wavelength": 0.4966,
          "full_width_half_max": 0.098
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B02.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 10,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 19264,
            "mean": 2348.069117847,
            "stddev": 2916.5446249911,
            "valid_percent": 99.99
          }
        }
      ]
    },
    "B03": {
      "title": "Band 3 (green) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "eo:bands": [
        {
          "name": "B03",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B03.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 10,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 18064,
            "mean": 2384.4680007438,
            "stddev": 2675.410513295,
            "valid_percent": 99.999
          }
        }
      ]
    },
    "B04": {
      "title": "Band 4 (red) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "eo:bands": [
        {
          "name": "B04",
          "common_name": "red",
          "center_wavelength": 0.6645,
          "full_width_half_max": 0.038
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B04.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 10,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 17200,
            "mean": 2273.9667970732,
            "stddev": 2618.272802792,
            "valid_percent": 99.999
          }
        }
      ]
    },
    "B05": {
      "title": "Band 5 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B05",
          "center_wavelength": 0.7039,
          "full_width_half_max": 0.019
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B05.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 20,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 16842,
            "mean": 2634.1490243416,
            "stddev": 2634.1490243416,
            "valid_percent": 99.999
          }
        }
      ]
    },
    "B06": {
      "title": "Band 6 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B06",
          "center_wavelength": 0.7402,
          "full_width_half_max": 0.018
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B06.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 20,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 16502,
            "mean": 3329.8844628619,
            "stddev": 2303.0096294469,
            "valid_percent": 99.999
          }
        }
      ]
    },
    "B07": {
      "title": "Band 7 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B07",
          "center_wavelength": 0.7825,
          "full_width_half_max": 0.028
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B07.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    },
    "B08": {
      "title": "Band 8 (nir) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "eo:bands": [
        {
          "name": "B08",
          "common_name": "nir",
          "center_wavelength": 0.8351,
          "full_width_half_max": 0.145
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B08.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ]
    },
    "B8A": {
      "title": "Band 8A BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B8A",
          "center_wavelength": 0.8648,
          "full_width_half_max": 0.033
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B8A.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    },
    "B09": {
      "title": "Band 9 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 60,
      "eo:bands": [
        {
          "name": "B09",
          "center_wavelength": 0.945,
          "full_width_half_max": 0.026
        }
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 60,
          "bits_per_sample": 15,
          "nodata": "nan"
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B09.tif",
      "proj:shape": [
        1830,
        1830
      ],
      "proj:transform": [
        60,
        0,
        399960,
        0,
        -60,
        4200000,
        0,
        0,
        1
      ]
    },
    "B11": {
      "title": "Band 11 (swir16) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B11",
          "common_name": "swir16",
          "center_wavelength": 1.6137,
          "full_width_half_max": 0.143
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B11.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    },
    "B12": {
      "title": "Band 12 (swir22) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B12",
          "common_name": "swir22",
          "center_wavelength": 2.22024,
          "full_width_half_max": 0.242
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B12.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    },
    "AOT": {
      "title": "Aerosol Optical Thickness (AOT)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/AOT.tif",
      "proj:shape": [
        1830,
        1830
      ],
      "proj:transform": [
        60,
        0,
        399960,
        0,
        -60,
        4200000,
        0,
        0,
        1
      ]
    },
    "WVP": {
      "title": "Water Vapour (WVP)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/WVP.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ]
    },
    "SCL": {
      "title": "Scene Classification Map (SCL)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/SCL.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    }
  },
  "virtual:assets": {
    "SIR": {
      "title": "Shortwave Infra-red",
      "raster:range": [
        0,
        10000
      ],
      "href": [
        "#B12",
        "#B8A",
        "#B04"
      ]
    }
  },
  "links": [
    {
      "type": "application/json",
      "rel": "collection",
      "href": "sentinel-s2-l2a-cogs.json"
    }
  ]
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/raster/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fextensions%2Fraster%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json"
  ],
  "id": "S2B_33SVB_20210221_0_L2A",
  "bbox": [
    13.86148243891681,
    36.95257399124932,
    15.111074610520053,
    37.94752813015372
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          13.876381589019879,
          36.95257399124932
        ],
        [
          13.86148243891681,
          37.942072015005024
        ],
        [
          15.111074610520053,
          37.94752813015372
        ],
        [
          15.109620666835209,
          36.95783951241028
        ],
        [
          13.876381589019879,
          36.95257399124932
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2021-02-21T10:00:17Z",
    "platform": "sentinel-2b",
    "constellation": "sentinel-2",
    "instruments": [
      "msi"
    ],
    "gsd": 10,
    "view:off_nadir": 0,
    "proj:epsg": 32633,
    "sentinel:utm_zone": 33,
    "sentinel:latitude_band": "S",
    "sentinel:grid_square": "VB",
    "sentinel:sequence": "0",
    "sentinel:product_id": "S2B_MSIL2A_20210221T095029_N0214_R079_T33SVB_20210221T115149",
    "sentinel:data_coverage": 100,
    "eo:cloud_cover": 21.22,
    "sentinel:valid_cloud_cover": true
  },
  "collection": "sentinel-s2-l2a-cogs",
  "assets": {
    "thumbnail": {
      "title": "Thumbnail",
      "type": "image/png",
      "roles": [
        "thumbnail"
      ],
      "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/S/VB/2021/2/21/0/preview.jpg"
    },
    "overview": {
      "title": "True color image",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "overview"
      ],
      "gsd": 10,
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
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/L2A_PVI.tif",
      "proj:shape": [
        343,
        343
      ],
      "proj:transform": [
        320,
        0,
        399960,
        0,
        -320,
        4200000,
        0,
        0,
        1
      ]
    },
    "info": {
      "title": "Original JSON metadata",
      "type": "application/json",
      "roles": [
        "metadata"
      ],
      "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/S/VB/2021/2/21/0/tileInfo.json"
    },
    "metadata": {
      "title": "Original XML metadata",
      "type": "application/xml",
      "roles": [
        "metadata"
      ],
      "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/S/VB/2021/2/21/0/metadata.xml"
    },
    "visual": {
      "title": "True color image",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "overview"
      ],
      "gsd": 10,
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
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/TCI.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ]
    },
    "B01": {
      "title": "Band 1 (coastal) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 60,
      "eo:bands": [
        {
          "name": "B01",
          "common_name": "coastal",
          "center_wavelength": 0.4439,
          "full_width_half_max": 0.027
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B01.tif",
      "proj:shape": [
        1830,
        1830
      ],
      "proj:transform": [
        60,
        0,
        399960,
        0,
        -60,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 60,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 20567,
            "mean": 2339.4759595597,
            "stddev": 3026.6973619954,
            "valid_percent": 99.83
          }
        }
      ]
    },
    "B02": {
      "title": "Band 2 (blue) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "eo:bands": [
        {
          "name": "B02",
          "common_name": "blue",
          "center_wavelength": 0.4966,
          "full_width_half_max": 0.098
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B02.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 10,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 19264,
            "mean": 2348.069117847,
            "stddev": 2916.5446249911,
            "valid_percent": 99.99
          }
        }
      ]
    },
    "B03": {
      "title": "Band 3 (green) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "eo:bands": [
        {
          "name": "B03",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B03.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 10,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 18064,
            "mean": 2384.4680007438,
            "stddev": 2675.410513295,
            "valid_percent": 99.999
          }
        }
      ]
    },
    "B04": {
      "title": "Band 4 (red) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "eo:bands": [
        {
          "name": "B04",
          "common_name": "red",
          "center_wavelength": 0.6645,
          "full_width_half_max": 0.038
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B04.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 10,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 17200,
            "mean": 2273.9667970732,
            "stddev": 2618.272802792,
            "valid_percent": 99.999
          }
        }
      ]
    },
    "B05": {
      "title": "Band 5 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B05",
          "center_wavelength": 0.7039,
          "full_width_half_max": 0.019
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B05.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 20,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 16842,
            "mean": 2634.1490243416,
            "stddev": 2634.1490243416,
            "valid_percent": 99.999
          }
        }
      ]
    },
    "B06": {
      "title": "Band 6 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B06",
          "center_wavelength": 0.7402,
          "full_width_half_max": 0.018
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B06.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 20,
          "bits_per_sample": 15,
          "nodata": 0,
          "statistics": {
            "minimum": 1,
            "maximum": 16502,
            "mean": 3329.8844628619,
            "stddev": 2303.0096294469,
            "valid_percent": 99.999
          }
        }
      ]
    },
    "B07": {
      "title": "Band 7 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B07",
          "center_wavelength": 0.7825,
          "full_width_half_max": 0.028
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B07.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    },
    "B08": {
      "title": "Band 8 (nir) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "eo:bands": [
        {
          "name": "B08",
          "common_name": "nir",
          "center_wavelength": 0.8351,
          "full_width_half_max": 0.145
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B08.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ]
    },
    "B8A": {
      "title": "Band 8A BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B8A",
          "center_wavelength": 0.8648,
          "full_width_half_max": 0.033
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B8A.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    },
    "B09": {
      "title": "Band 9 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 60,
      "eo:bands": [
        {
          "name": "B09",
          "center_wavelength": 0.945,
          "full_width_half_max": 0.026
        }
      ],
      "raster:bands": [
        {
          "data_type": "uint16",
          "spatial_resolution": 60,
          "bits_per_sample": 15,
          "nodata": "nan"
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B09.tif",
      "proj:shape": [
        1830,
        1830
      ],
      "proj:transform": [
        60,
        0,
        399960,
        0,
        -60,
        4200000,
        0,
        0,
        1
      ]
    },
    "B11": {
      "title": "Band 11 (swir16) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B11",
          "common_name": "swir16",
          "center_wavelength": 1.6137,
          "full_width_half_max": 0.143
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B11.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    },
    "B12": {
      "title": "Band 12 (swir22) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "eo:bands": [
        {
          "name": "B12",
          "common_name": "swir22",
          "center_wavelength": 2.22024,
          "full_width_half_max": 0.242
        }
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B12.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    },
    "AOT": {
      "title": "Aerosol Optical Thickness (AOT)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/AOT.tif",
      "proj:shape": [
        1830,
        1830
      ],
      "proj:transform": [
        60,
        0,
        399960,
        0,
        -60,
        4200000,
        0,
        0,
        1
      ]
    },
    "WVP": {
      "title": "Water Vapour (WVP)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/WVP.tif",
      "proj:shape": [
        10980,
        10980
      ],
      "proj:transform": [
        10,
        0,
        399960,
        0,
        -10,
        4200000,
        0,
        0,
        1
      ]
    },
    "SCL": {
      "title": "Scene Classification Map (SCL)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/SCL.tif",
      "proj:shape": [
        5490,
        5490
      ],
      "proj:transform": [
        20,
        0,
        399960,
        0,
        -20,
        4200000,
        0,
        0,
        1
      ]
    }
  },
  "virtual:assets": {
    "SIR": {
      "title": "Shortwave Infra-red",
      "raster:range": [
        0,
        10000
      ],
      "href": [
        "#B12",
        "#B8A",
        "#B04"
      ]
    }
  },
  "links": [
    {
      "type": "application/json",
      "rel": "collection",
      "href": "sentinel-s2-l2a-cogs.json"
    }
  ],
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/raster/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fextensions%2Fraster%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix dct: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <proj:> .
@prefix ns2: <eo:> .
@prefix ns3: <sentinel:> .
@prefix ns4: <virtual:> .
@prefix ns5: <view:> .
@prefix ns6: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix raster: <urn:stac:extensions/raster#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <urn:stac:vocab#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/S2B_33SVB_20210221_0_L2A> a geojson:Feature ;
    ns2:cloud_cover 2.122e+01 ;
    rdfs:seeAlso [ dct:type "application/json" ;
            ns6:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <file:///github/workspace/sentinel-s2-l2a-cogs.json> ] ;
    geojson:bbox ( 1.386148e+01 3.695257e+01 1.511107e+01 3.794753e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.387638e+01 3.695257e+01 ) ( 1.386148e+01 3.794207e+01 ) ( 1.511107e+01 3.794753e+01 ) ( 1.510962e+01 3.695784e+01 ) ( 1.387638e+01 3.695257e+01 ) ) ) ] ;
    ns1:epsg 32633 ;
    ns3:data_coverage 100 ;
    ns3:grid_square "VB" ;
    ns3:latitude_band "S" ;
    ns3:product_id "S2B_MSIL2A_20210221T095029_N0214_R079_T33SVB_20210221T115149" ;
    ns3:sequence "0" ;
    ns3:utm_zone 33 ;
    ns3:valid_cloud_cover true ;
    stac:assets <file:///github/workspace/AOT>,
        <file:///github/workspace/B01>,
        <file:///github/workspace/B02>,
        <file:///github/workspace/B03>,
        <file:///github/workspace/B04>,
        <file:///github/workspace/B05>,
        <file:///github/workspace/B06>,
        <file:///github/workspace/B07>,
        <file:///github/workspace/B08>,
        <file:///github/workspace/B09>,
        <file:///github/workspace/B11>,
        <file:///github/workspace/B12>,
        <file:///github/workspace/B8A>,
        <file:///github/workspace/SCL>,
        <file:///github/workspace/WVP>,
        <file:///github/workspace/info>,
        <file:///github/workspace/metadata>,
        <file:///github/workspace/overview>,
        <file:///github/workspace/thumbnail>,
        <file:///github/workspace/visual> ;
    ns5:off_nadir 0 ;
    ns4:assets [ ] .

<file:///github/workspace/AOT> rdfs:label "Aerosol Optical Thickness (AOT)" ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/AOT.tif> ;
    ns1:shape 1830 ;
    ns1:transform -60,
        0,
        1,
        60,
        399960,
        4200000 .

<file:///github/workspace/B01> rdfs:label "Band 1 (coastal) BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B01.tif> ;
    ns1:shape 1830 ;
    ns1:transform -60,
        0,
        1,
        60,
        399960,
        4200000 ;
    raster:bands [ <rasterrasterrasterrasterbits_per_sample> 15 ;
            <rasterrasterrasterrasterdata_type> "uint16" ;
            <rasterrasterrasterrasternodata> 0 ;
            <rasterrasterrasterrasterspatial_resolution> 60 ;
            <rasterrasterrasterrasterstatistics> [ <rasterrasterrasterrastermaximum> 20567 ;
                    <rasterrasterrasterrastermean> 2.339476e+03 ;
                    <rasterrasterrasterrasterminimum> 1 ;
                    <rasterrasterrasterrasterstddev> 3.026697e+03 ;
                    <rasterrasterrasterrastervalid_percent> 9.983e+01 ] ] .

<file:///github/workspace/B02> rdfs:label "Band 2 (blue) BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B02.tif> ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 ;
    raster:bands [ <rasterrasterrasterrasterbits_per_sample> 15 ;
            <rasterrasterrasterrasterdata_type> "uint16" ;
            <rasterrasterrasterrasternodata> 0 ;
            <rasterrasterrasterrasterspatial_resolution> 10 ;
            <rasterrasterrasterrasterstatistics> [ <rasterrasterrasterrastermaximum> 19264 ;
                    <rasterrasterrasterrastermean> 2.348069e+03 ;
                    <rasterrasterrasterrasterminimum> 1 ;
                    <rasterrasterrasterrasterstddev> 2.916545e+03 ;
                    <rasterrasterrasterrastervalid_percent> 9.999e+01 ] ] .

<file:///github/workspace/B03> rdfs:label "Band 3 (green) BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B03.tif> ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 ;
    raster:bands [ <rasterrasterrasterrasterbits_per_sample> 15 ;
            <rasterrasterrasterrasterdata_type> "uint16" ;
            <rasterrasterrasterrasternodata> 0 ;
            <rasterrasterrasterrasterspatial_resolution> 10 ;
            <rasterrasterrasterrasterstatistics> [ <rasterrasterrasterrastermaximum> 18064 ;
                    <rasterrasterrasterrastermean> 2.384468e+03 ;
                    <rasterrasterrasterrasterminimum> 1 ;
                    <rasterrasterrasterrasterstddev> 2.675411e+03 ;
                    <rasterrasterrasterrastervalid_percent> 9.9999e+01 ] ] .

<file:///github/workspace/B04> rdfs:label "Band 4 (red) BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B04.tif> ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 ;
    raster:bands [ <rasterrasterrasterrasterbits_per_sample> 15 ;
            <rasterrasterrasterrasterdata_type> "uint16" ;
            <rasterrasterrasterrasternodata> 0 ;
            <rasterrasterrasterrasterspatial_resolution> 10 ;
            <rasterrasterrasterrasterstatistics> [ <rasterrasterrasterrastermaximum> 17200 ;
                    <rasterrasterrasterrastermean> 2.273967e+03 ;
                    <rasterrasterrasterrasterminimum> 1 ;
                    <rasterrasterrasterrasterstddev> 2.618273e+03 ;
                    <rasterrasterrasterrastervalid_percent> 9.9999e+01 ] ] .

<file:///github/workspace/B05> rdfs:label "Band 5 BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B05.tif> ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 ;
    raster:bands [ <rasterrasterrasterrasterbits_per_sample> 15 ;
            <rasterrasterrasterrasterdata_type> "uint16" ;
            <rasterrasterrasterrasternodata> 0 ;
            <rasterrasterrasterrasterspatial_resolution> 20 ;
            <rasterrasterrasterrasterstatistics> [ <rasterrasterrasterrastermaximum> 16842 ;
                    <rasterrasterrasterrastermean> 2.634149e+03 ;
                    <rasterrasterrasterrasterminimum> 1 ;
                    <rasterrasterrasterrasterstddev> 2.634149e+03 ;
                    <rasterrasterrasterrastervalid_percent> 9.9999e+01 ] ] .

<file:///github/workspace/B06> rdfs:label "Band 6 BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B06.tif> ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 ;
    raster:bands [ <rasterrasterrasterrasterbits_per_sample> 15 ;
            <rasterrasterrasterrasterdata_type> "uint16" ;
            <rasterrasterrasterrasternodata> 0 ;
            <rasterrasterrasterrasterspatial_resolution> 20 ;
            <rasterrasterrasterrasterstatistics> [ <rasterrasterrasterrastermaximum> 16502 ;
                    <rasterrasterrasterrastermean> 3.329884e+03 ;
                    <rasterrasterrasterrasterminimum> 1 ;
                    <rasterrasterrasterrasterstddev> 2.30301e+03 ;
                    <rasterrasterrasterrastervalid_percent> 9.9999e+01 ] ] .

<file:///github/workspace/B07> rdfs:label "Band 7 BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B07.tif> ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 .

<file:///github/workspace/B08> rdfs:label "Band 8 (nir) BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B08.tif> ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 .

<file:///github/workspace/B09> rdfs:label "Band 9 BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B09.tif> ;
    ns1:shape 1830 ;
    ns1:transform -60,
        0,
        1,
        60,
        399960,
        4200000 ;
    raster:bands [ <rasterrasterrasterrasterbits_per_sample> 15 ;
            <rasterrasterrasterrasterdata_type> "uint16" ;
            <rasterrasterrasterrasternodata> "nan" ;
            <rasterrasterrasterrasterspatial_resolution> 60 ] .

<file:///github/workspace/B11> rdfs:label "Band 11 (swir16) BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B11.tif> ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 .

<file:///github/workspace/B12> rdfs:label "Band 12 (swir22) BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B12.tif> ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 .

<file:///github/workspace/B8A> rdfs:label "Band 8A BOA reflectance" ;
    ns2:bands [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B8A.tif> ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 .

<file:///github/workspace/SCL> rdfs:label "Scene Classification Map (SCL)" ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/SCL.tif> ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 .

<file:///github/workspace/WVP> rdfs:label "Water Vapour (WVP)" ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/WVP.tif> ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 .

<file:///github/workspace/info> a <file:///github/workspace/application/json> ;
    rdfs:label "Original JSON metadata" ;
    oa:hasTarget <https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/S/VB/2021/2/21/0/tileInfo.json> .

<file:///github/workspace/metadata> a <file:///github/workspace/application/xml> ;
    rdfs:label "Original XML metadata" ;
    oa:hasTarget <https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/S/VB/2021/2/21/0/metadata.xml> .

<file:///github/workspace/overview> rdfs:label "True color image" ;
    ns2:bands [ ],
        [ ],
        [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/L2A_PVI.tif> ;
    ns1:shape 343 ;
    ns1:transform -320,
        0,
        1,
        320,
        399960,
        4200000 .

<file:///github/workspace/thumbnail> a <file:///github/workspace/image/png> ;
    rdfs:label "Thumbnail" ;
    oa:hasTarget <https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/S/VB/2021/2/21/0/preview.jpg> .

<file:///github/workspace/visual> rdfs:label "True color image" ;
    ns2:bands [ ],
        [ ],
        [ ] ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/TCI.tif> ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/raster/example_1_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
title: Forecast Extension
description: STAC Forecast Extension for STAC Items and STAC Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/raster/v1.1.0/schema.json
x-jsonld-extra-terms:
  raster:bands:
    x-jsonld-id: urn:stac:extensions/raster#bands
    x-jsonld-context:
      '@vocab': rasterrasterrasterraster
  raster:range:
    x-jsonld-id: urn:stac:extensions/raster#range
    x-jsonld-container: '@list'
x-jsonld-prefixes:
  raster: urn:stac:extensions/raster#

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fextensions%2Fraster%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/schema.yaml" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/schema.json" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/schema.json</a>


# JSON-LD Context

```json--ldContext
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
    "geometry": {
      "@context": {},
      "@id": "geojson:geometry"
    },
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
        "@vocab": "rasterrasterrasterraster"
      }
    },
    "raster:range": {
      "@id": "raster:range",
      "@container": "@list"
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "raster": "urn:stac:extensions/raster#",
    "geojson": "https://purl.org/geojson/vocab#",
    "stac": "urn:stac:vocab#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fextensions%2Fraster%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/context.jsonld" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/context.jsonld</a>

# References

* [GitHub Repository](https://github.com/stac-extensions/raster)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/bblocks-stac" target="_blank">https://github.com/ogcincubator/bblocks-stac</a>
* Path:
<code><a href="https://github.com/ogcincubator/bblocks-stac/blob/HEAD/_sources/extensions/raster" target="_blank">_sources/extensions/raster</a></code>

