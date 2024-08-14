
# STAC Raster Extension (Schema)

`ogc.contrib.stac.extensions.raster` *v0.1*

An item can describe assets that are rasters of one or multiple bands with some information common to them all (raster size, projection) and also specific to each of them (data type, unit, number of bits used, nodata). A raster is often strongly linked with the georeferencing transform and coordinate system definition of all bands (using the projection extension). In many applications, it is interesting to have some metadata about the rasters in the asset (values statistics, value interpretation, transforms).

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example of Raster item - Sentinel2
#### json
```json
{
  "type": "Feature",
  "stac_version": "1.1.0-beta.1",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0-beta.1/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v2.0.0-beta.1/schema.json"
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
    "proj:code": "EPSG:32633",
    "sentinel:utm_zone": 33,
    "sentinel:latitude_band": "S",
    "sentinel:grid_square": "VB",
    "sentinel:sequence": "0",
    "sentinel:product_id": "S2B_MSIL2A_20210221T095029_N0214_R079_T33SVB_20210221T115149",
    "sentinel:data_coverage": 100,
    "eo:cloud_cover": 21.22
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
      "raster:spatial_resolution": 10,
      "bands": [
        {
          "name": "B04",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.6645,
          "eo:full_width_half_max": 0.038
        },
        {
          "name": "B03",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.045
        },
        {
          "name": "B02",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.4966,
          "eo:full_width_half_max": 0.098
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
      "bands": [
        {
          "name": "B04",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.6645,
          "eo:full_width_half_max": 0.038
        },
        {
          "name": "B03",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.045
        },
        {
          "name": "B02",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.4966,
          "eo:full_width_half_max": 0.098
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
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B01.tif",
      "title": "Band 1 (coastal) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 60,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 20567,
        "mean": 2339.4759595597,
        "stddev": 3026.6973619954,
        "valid_percent": 99.83
      },
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
      "eo:common_name": "coastal",
      "eo:center_wavelength": 0.4439,
      "eo:full_width_half_max": 0.027,
      "raster:spatial_resolution": 60,
      "raster:bits_per_sample": 15
    },
    "B02": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B02.tif",
      "title": "Band 2 (blue) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 19264,
        "mean": 2348.069117847,
        "stddev": 2916.5446249911,
        "valid_percent": 99.99
      },
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
      "eo:common_name": "blue",
      "eo:center_wavelength": 0.4966,
      "eo:full_width_half_max": 0.098,
      "raster:spatial_resolution": 10,
      "raster:bits_per_sample": 15
    },
    "B03": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B03.tif",
      "title": "Band 3 (green) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 18064,
        "mean": 2384.4680007438,
        "stddev": 2675.410513295,
        "valid_percent": 99.999
      },
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
      "eo:common_name": "green",
      "eo:center_wavelength": 0.56,
      "eo:full_width_half_max": 0.045,
      "raster:spatial_resolution": 10,
      "raster:bits_per_sample": 15
    },
    "B04": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B04.tif",
      "title": "Band 4 (red) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 17200,
        "mean": 2273.9667970732,
        "stddev": 2618.272802792,
        "valid_percent": 99.999
      },
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
      "eo:common_name": "red",
      "eo:center_wavelength": 0.6645,
      "eo:full_width_half_max": 0.038,
      "raster:spatial_resolution": 10,
      "raster:bits_per_sample": 15
    },
    "B05": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B05.tif",
      "title": "Band 5 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 16842,
        "mean": 2634.1490243416,
        "stddev": 2634.1490243416,
        "valid_percent": 99.999
      },
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
      "eo:center_wavelength": 0.7039,
      "eo:full_width_half_max": 0.019,
      "raster:spatial_resolution": 20,
      "raster:bits_per_sample": 15
    },
    "B06": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B06.tif",
      "title": "Band 6 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 16502,
        "mean": 3329.8844628619,
        "stddev": 2303.0096294469,
        "valid_percent": 99.999
      },
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
      "eo:center_wavelength": 0.7402,
      "eo:full_width_half_max": 0.018,
      "raster:spatial_resolution": 20,
      "raster:bits_per_sample": 15
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
      ],
      "raster:spatial_resolution": 20
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

#### jsonld
```jsonld
{
  "type": "Feature",
  "stac_version": "1.1.0-beta.1",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0-beta.1/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v2.0.0-beta.1/schema.json"
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
    "proj:code": "EPSG:32633",
    "sentinel:utm_zone": 33,
    "sentinel:latitude_band": "S",
    "sentinel:grid_square": "VB",
    "sentinel:sequence": "0",
    "sentinel:product_id": "S2B_MSIL2A_20210221T095029_N0214_R079_T33SVB_20210221T115149",
    "sentinel:data_coverage": 100,
    "eo:cloud_cover": 21.22
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
      "raster:spatial_resolution": 10,
      "bands": [
        {
          "name": "B04",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.6645,
          "eo:full_width_half_max": 0.038
        },
        {
          "name": "B03",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.045
        },
        {
          "name": "B02",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.4966,
          "eo:full_width_half_max": 0.098
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
      "bands": [
        {
          "name": "B04",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.6645,
          "eo:full_width_half_max": 0.038
        },
        {
          "name": "B03",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.045
        },
        {
          "name": "B02",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.4966,
          "eo:full_width_half_max": 0.098
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
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B01.tif",
      "title": "Band 1 (coastal) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 60,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 20567,
        "mean": 2339.4759595597,
        "stddev": 3026.6973619954,
        "valid_percent": 99.83
      },
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
      "eo:common_name": "coastal",
      "eo:center_wavelength": 0.4439,
      "eo:full_width_half_max": 0.027,
      "raster:spatial_resolution": 60,
      "raster:bits_per_sample": 15
    },
    "B02": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B02.tif",
      "title": "Band 2 (blue) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 19264,
        "mean": 2348.069117847,
        "stddev": 2916.5446249911,
        "valid_percent": 99.99
      },
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
      "eo:common_name": "blue",
      "eo:center_wavelength": 0.4966,
      "eo:full_width_half_max": 0.098,
      "raster:spatial_resolution": 10,
      "raster:bits_per_sample": 15
    },
    "B03": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B03.tif",
      "title": "Band 3 (green) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 18064,
        "mean": 2384.4680007438,
        "stddev": 2675.410513295,
        "valid_percent": 99.999
      },
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
      "eo:common_name": "green",
      "eo:center_wavelength": 0.56,
      "eo:full_width_half_max": 0.045,
      "raster:spatial_resolution": 10,
      "raster:bits_per_sample": 15
    },
    "B04": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B04.tif",
      "title": "Band 4 (red) BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 10,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 17200,
        "mean": 2273.9667970732,
        "stddev": 2618.272802792,
        "valid_percent": 99.999
      },
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
      "eo:common_name": "red",
      "eo:center_wavelength": 0.6645,
      "eo:full_width_half_max": 0.038,
      "raster:spatial_resolution": 10,
      "raster:bits_per_sample": 15
    },
    "B05": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B05.tif",
      "title": "Band 5 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 16842,
        "mean": 2634.1490243416,
        "stddev": 2634.1490243416,
        "valid_percent": 99.999
      },
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
      "eo:center_wavelength": 0.7039,
      "eo:full_width_half_max": 0.019,
      "raster:spatial_resolution": 20,
      "raster:bits_per_sample": 15
    },
    "B06": {
      "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B06.tif",
      "title": "Band 6 BOA reflectance",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": [
        "data"
      ],
      "gsd": 20,
      "data_type": "uint16",
      "nodata": 0,
      "statistics": {
        "minimum": 1,
        "maximum": 16502,
        "mean": 3329.8844628619,
        "stddev": 2303.0096294469,
        "valid_percent": 99.999
      },
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
      "eo:center_wavelength": 0.7402,
      "eo:full_width_half_max": 0.018,
      "raster:spatial_resolution": 20,
      "raster:bits_per_sample": 15
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
      ],
      "raster:spatial_resolution": 20
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

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <proj:> .
@prefix ns2: <eo:> .
@prefix ns3: <sentinel:> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix ns5: <view:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix raster: <https://w3id.org/ogc/stac/raster/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/raster/example-1/S2B_33SVB_20210221_0_L2A> a geojson:Feature ;
    ns2:cloud_cover 2.122e+01 ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/raster/example-1/sentinel-s2-l2a-cogs.json> ] ;
    geojson:bbox ( 1.386148e+01 3.695257e+01 1.511107e+01 3.794753e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.387638e+01 3.695257e+01 ) ( 1.386148e+01 3.794207e+01 ) ( 1.511107e+01 3.794753e+01 ) ( 1.510962e+01 3.695784e+01 ) ( 1.387638e+01 3.695257e+01 ) ) ) ] ;
    stac:assets <https://example.com/stac/raster/example-1/B01>,
        <https://example.com/stac/raster/example-1/B02>,
        <https://example.com/stac/raster/example-1/B03>,
        <https://example.com/stac/raster/example-1/B04>,
        <https://example.com/stac/raster/example-1/B05>,
        <https://example.com/stac/raster/example-1/B06>,
        <https://example.com/stac/raster/example-1/SCL>,
        <https://example.com/stac/raster/example-1/info>,
        <https://example.com/stac/raster/example-1/metadata>,
        <https://example.com/stac/raster/example-1/overview>,
        <https://example.com/stac/raster/example-1/thumbnail>,
        <https://example.com/stac/raster/example-1/visual> ;
    ns1:code "EPSG:32633" ;
    ns3:data_coverage 100 ;
    ns3:grid_square "VB" ;
    ns3:latitude_band "S" ;
    ns3:product_id "S2B_MSIL2A_20210221T095029_N0214_R079_T33SVB_20210221T115149" ;
    ns3:sequence "0" ;
    ns3:utm_zone 33 ;
    ns5:off_nadir 0 .

<https://example.com/stac/raster/example-1/B01> rdfs:label "Band 1 (coastal) BOA reflectance" ;
    ns2:center_wavelength 4.439e-01 ;
    ns2:common_name "coastal" ;
    ns2:full_width_half_max 2.7e-02 ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B01.tif> ;
    raster:bits_per_sample 15 ;
    raster:spatial_resolution 60 ;
    ns1:shape 1830 ;
    ns1:transform -60,
        0,
        1,
        60,
        399960,
        4200000 .

<https://example.com/stac/raster/example-1/B02> rdfs:label "Band 2 (blue) BOA reflectance" ;
    ns2:center_wavelength 4.966e-01 ;
    ns2:common_name "blue" ;
    ns2:full_width_half_max 9.8e-02 ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B02.tif> ;
    raster:bits_per_sample 15 ;
    raster:spatial_resolution 10 ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 .

<https://example.com/stac/raster/example-1/B03> rdfs:label "Band 3 (green) BOA reflectance" ;
    ns2:center_wavelength 5.6e-01 ;
    ns2:common_name "green" ;
    ns2:full_width_half_max 4.5e-02 ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B03.tif> ;
    raster:bits_per_sample 15 ;
    raster:spatial_resolution 10 ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 .

<https://example.com/stac/raster/example-1/B04> rdfs:label "Band 4 (red) BOA reflectance" ;
    ns2:center_wavelength 6.645e-01 ;
    ns2:common_name "red" ;
    ns2:full_width_half_max 3.8e-02 ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B04.tif> ;
    raster:bits_per_sample 15 ;
    raster:spatial_resolution 10 ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 .

<https://example.com/stac/raster/example-1/B05> rdfs:label "Band 5 BOA reflectance" ;
    ns2:center_wavelength 7.039e-01 ;
    ns2:full_width_half_max 1.9e-02 ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B05.tif> ;
    raster:bits_per_sample 15 ;
    raster:spatial_resolution 20 ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 .

<https://example.com/stac/raster/example-1/B06> rdfs:label "Band 6 BOA reflectance" ;
    ns2:center_wavelength 7.402e-01 ;
    ns2:full_width_half_max 1.8e-02 ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/B06.tif> ;
    raster:bits_per_sample 15 ;
    raster:spatial_resolution 20 ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 .

<https://example.com/stac/raster/example-1/SCL> rdfs:label "Scene Classification Map (SCL)" ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/SCL.tif> ;
    raster:spatial_resolution 20 ;
    ns1:shape 5490 ;
    ns1:transform -20,
        0,
        1,
        20,
        399960,
        4200000 .

<https://example.com/stac/raster/example-1/info> a <https://example.com/stac/raster/example-1/application/json> ;
    rdfs:label "Original JSON metadata" ;
    oa:hasTarget <https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/S/VB/2021/2/21/0/tileInfo.json> .

<https://example.com/stac/raster/example-1/metadata> a <https://example.com/stac/raster/example-1/application/xml> ;
    rdfs:label "Original XML metadata" ;
    oa:hasTarget <https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/S/VB/2021/2/21/0/metadata.xml> .

<https://example.com/stac/raster/example-1/overview> rdfs:label "True color image" ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/L2A_PVI.tif> ;
    raster:spatial_resolution 10 ;
    ns1:shape 343 ;
    ns1:transform -320,
        0,
        1,
        320,
        399960,
        4200000 .

<https://example.com/stac/raster/example-1/thumbnail> a <https://example.com/stac/raster/example-1/image/png> ;
    rdfs:label "Thumbnail" ;
    oa:hasTarget <https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/S/VB/2021/2/21/0/preview.jpg> .

<https://example.com/stac/raster/example-1/visual> rdfs:label "True color image" ;
    oa:hasTarget <https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/S/VB/2021/2/S2B_33SVB_20210221_0_L2A/TCI.tif> ;
    ns1:shape 10980 ;
    ns1:transform -10,
        0,
        1,
        10,
        399960,
        4200000 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Forecast Extension
description: STAC Forecast Extension for STAC Items and STAC Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-v1-0-0/schema.yaml
- $ref: https://stac-extensions.github.io/raster/v2.0.0-beta.1/schema.json
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/schema.yaml)


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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/raster)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/raster`

