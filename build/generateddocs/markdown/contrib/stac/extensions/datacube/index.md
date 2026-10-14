
# STAC Datacube Extension (Schema)

`ogc.contrib.stac.extensions.datacube` *v2.3.0*

STAC Datacube Extension for Items, Collections and Assets.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Datacube item
#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json"
  ],
  "id": "datacube-123",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -122.308150179,
          37.488035566
        ],
        [
          -122.597502109,
          37.538869539
        ],
        [
          -122.576687533,
          37.613537207
        ],
        [
          -122.2880486,
          37.562818007
        ],
        [
          -122.308150179,
          37.488035566
        ]
      ]
    ]
  },
  "bbox": [
    -122.59750209,
    37.48803556,
    -122.2880486,
    37.613537207
  ],
  "properties": {
    "title": "Multi-dimensional data cube 123 in a STAC Item.",
    "datetime": "2016-05-03T13:21:30.040Z",
    "cube:dimensions": {
      "x": {
        "type": "spatial",
        "axis": "x",
        "extent": [
          -122.59750209,
          -122.2880486
        ],
        "reference_system": 4326
      },
      "y": {
        "type": "spatial",
        "axis": "y",
        "extent": [
          37.48803556,
          37.613537207
        ],
        "reference_system": 4326
      },
      "pressure_levels": {
        "type": "spatial",
        "axis": "z",
        "extent": [
          0,
          1000
        ],
        "step": 100,
        "unit": "Pa"
      },
      "metered_levels": {
        "type": "spatial",
        "axis": "z",
        "values": [
          0,
          10,
          25,
          50,
          100,
          1000
        ],
        "unit": "m"
      },
      "time": {
        "type": "temporal",
        "values": [
          "2016-05-03T13:21:30.040Z"
        ]
      },
      "spectral": {
        "type": "bands",
        "values": [
          "red",
          "green",
          "blue"
        ]
      }
    },
    "cube:variables": {
      "temp": {
        "dimensions": [
          "time",
          "y",
          "x",
          "pressure_levels"
        ],
        "type": "data",
        "nodata": "nan",
        "data_type": "float32"
      },
      "color": {
        "dimensions": [],
        "type": "auxiliary",
        "values": [
          "red",
          "green",
          "blue"
        ]
      }
    }
  },
  "assets": {
    "data": {
      "href": "http://cool-sat.com/catalog/datacube-123/data.nc",
      "type": "application/netcdf",
      "title": "netCDF Data cube"
    },
    "thumbnail": {
      "href": "http://cool-sat.com/catalog/datacube-123/thumbnail.png",
      "type": "image/png",
      "title": "Thumbnail"
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "http://cool-sat.com/catalog/datacube-123/item.json"
    }
  ]
}
```

#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json"
  ],
  "id": "datacube-123",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -122.308150179,
          37.488035566
        ],
        [
          -122.597502109,
          37.538869539
        ],
        [
          -122.576687533,
          37.613537207
        ],
        [
          -122.2880486,
          37.562818007
        ],
        [
          -122.308150179,
          37.488035566
        ]
      ]
    ]
  },
  "bbox": [
    -122.59750209,
    37.48803556,
    -122.2880486,
    37.613537207
  ],
  "properties": {
    "title": "Multi-dimensional data cube 123 in a STAC Item.",
    "datetime": "2016-05-03T13:21:30.040Z"
  },
  "assets": {
    "data": {
      "href": "http://cool-sat.com/catalog/datacube-123/data.nc",
      "type": "application/netcdf",
      "title": "netCDF Data cube",
      "cube:dimensions": {
        "x": {
          "type": "spatial",
          "axis": "x",
          "extent": [
            -122.59750209,
            -122.2880486
          ],
          "reference_system": 4326
        },
        "y": {
          "type": "spatial",
          "axis": "y",
          "extent": [
            37.48803556,
            37.613537207
          ],
          "reference_system": 4326
        },
        "pressure_levels": {
          "type": "spatial",
          "axis": "z",
          "extent": [
            0,
            1000
          ],
          "step": 100,
          "unit": "Pa"
        },
        "metered_levels": {
          "type": "spatial",
          "axis": "z",
          "values": [
            0,
            10,
            25,
            50,
            100,
            1000
          ],
          "unit": "m"
        },
        "time": {
          "type": "temporal",
          "values": [
            "2016-05-03T13:21:30.040Z"
          ]
        },
        "spectral": {
          "type": "bands",
          "values": [
            "red",
            "green",
            "blue"
          ]
        }
      },
      "cube:variables": {
        "temp": {
          "dimensions": [
            "time",
            "y",
            "x",
            "pressure_levels"
          ],
          "type": "data"
        },
        "color": {
          "dimensions": [],
          "type": "auxiliary",
          "values": [
            "red",
            "green",
            "blue"
          ]
        }
      }
    },
    "thumbnail": {
      "href": "http://cool-sat.com/catalog/datacube-123/thumbnail.png",
      "type": "image/png",
      "title": "Thumbnail"
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "http://cool-sat.com/catalog/datacube-123/item.json"
    }
  ]
}
```

#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json"
  ],
  "type": "Collection",
  "id": "daymet-hi-annual",
  "title": "Daymet Hawaii Annual",
  "description": "Daymet is a data product derived from a collection of algorithms and computer software designed to interpolate and extrapolate from daily meteorological observations to produce gridded estimates of daily weather parameters. Weather parameters generated include daily surfaces of minimum and maximum temperature, precipitation, vapor pressure, radiation, snow water equivalent, and day length produced on a 1 km x 1 km gridded surface. The motivation for producing Daymet is to provide measurements of near-surface meteorological conditions where no instrumentation exists. Having estimates of these surfaces is critical to understanding many processes in the terrestrial biogeochemical system.",
  "license": "proprietary",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -160.3056,
          17.9539,
          -154.772,
          23.5186
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1980-01-01T12:00:00Z",
          "2019-12-31T12:00:00Z"
        ]
      ]
    }
  },
  "links": [],
  "assets": {
    "data": {
      "href": "abfs://daymet-zarr/annual/hi.zarr",
      "title": "Annual Hawaii Daymet zarr root",
      "description": "The root of the annual Hawaii Daymet Zarr Group on Azure Blob Storage.",
      "roles": [
        "data",
        "zarr-root",
        "azure-blob-storge"
      ]
    }
  },
  "cube:dimensions": {
    "time": {
      "type": "temporal",
      "extent": [
        "1980:00:00T00:00:00Z",
        "2020:00:00T00:00:00Z"
      ],
      "description": "Annual",
      "step": "P1Y"
    },
    "x": {
      "type": "spatial",
      "axis": "x",
      "description": "North American Lambert Conformal Conic, 1KM grid.",
      "extent": [
        -622000,
        -5519250
      ],
      "step": 1000,
      "reference_system": "PROJCRS[\"undefined\",BASEGEOGCRS[\"undefined\",DATUM[\"undefined\",ELLIPSOID[\"undefined\",6378137,298.257223563,LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]]],PRIMEM[\"Greenwich\",0,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8901]]],CONVERSION[\"unknown\",METHOD[\"Lambert Conic Conformal (2SP)\",ID[\"EPSG\",9802]],PARAMETER[\"Latitude of 1st standard parallel\",25,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8823]],PARAMETER[\"Latitude of 2nd standard parallel\",60,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8824]],PARAMETER[\"Latitude of false origin\",42.5,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8821]],PARAMETER[\"Longitude of false origin\",-100,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8822]],PARAMETER[\"Easting at false origin\",0,LENGTHUNIT[\"metre\",1],ID[\"EPSG\",8826]],PARAMETER[\"Northing at false origin\",0,LENGTHUNIT[\"metre\",1],ID[\"EPSG\",8827]]],CS[Cartesian,2],AXIS[\"(E)\",east,ORDER[1],LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]],AXIS[\"(N)\",north,ORDER[2],LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]]]"
    },
    "y": {
      "type": "spatial",
      "axis": "y",
      "description": "North American Lambert Conformal Conic, 1KM grid.",
      "extent": [
        -5802250,
        -39000
      ],
      "step": 1000,
      "reference_system": "PROJCRS[\"undefined\",BASEGEOGCRS[\"undefined\",DATUM[\"undefined\",ELLIPSOID[\"undefined\",6378137,298.257223563,LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]]],PRIMEM[\"Greenwich\",0,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8901]]],CONVERSION[\"unknown\",METHOD[\"Lambert Conic Conformal (2SP)\",ID[\"EPSG\",9802]],PARAMETER[\"Latitude of 1st standard parallel\",25,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8823]],PARAMETER[\"Latitude of 2nd standard parallel\",60,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8824]],PARAMETER[\"Latitude of false origin\",42.5,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8821]],PARAMETER[\"Longitude of false origin\",-100,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8822]],PARAMETER[\"Easting at false origin\",0,LENGTHUNIT[\"metre\",1],ID[\"EPSG\",8826]],PARAMETER[\"Northing at false origin\",0,LENGTHUNIT[\"metre\",1],ID[\"EPSG\",8827]]],CS[Cartesian,2],AXIS[\"(E)\",east,ORDER[1],LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]],AXIS[\"(N)\",north,ORDER[2],LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]]]"
    },
    "nv": {
      "type": "count",
      "description": "Size of time_bnds.",
      "values": [
        0,
        1
      ]
    }
  },
  "cube:variables": {
    "lat": {
      "type": "auxiliary",
      "extent": [
        17.960035,
        23.512327
      ],
      "description": "latitude coordinate",
      "unit": "degrees_north",
      "dimensions": [
        "y",
        "x"
      ]
    },
    "lon": {
      "type": "auxiliary",
      "extent": [
        -160.29884,
        -154.77806
      ],
      "description": "longitude coordinate",
      "unit": "degrees_east",
      "dimensions": [
        "y",
        "x"
      ]
    },
    "prcp": {
      "type": "data",
      "description": "The total accumulated precipitation over the monthly period of the daily total precipitation. Sum of all forms of precipitation converted to a water-equivalent depth.",
      "extent": [
        0,
        null
      ],
      "unit": "mm",
      "dimensions": [
        "time",
        "y",
        "x"
      ]
    },
    "swe": {
      "type": "data",
      "description": "The average of the daily snow water equivalent (the amount of water contained within the snowpack) in kilograms per square meter over the monthly period.",
      "extent": [
        0,
        null
      ],
      "unit": "kg/m2",
      "dimensions": [
        "time",
        "y",
        "x"
      ]
    },
    "tmin": {
      "type": "data",
      "description": "The average minimum temperature for a daily period over the entire monthly period.",
      "unit": "degrees C",
      "dimensions": [
        "time",
        "y",
        "x"
      ]
    },
    "tmax": {
      "type": "data",
      "description": "The average maximum temperature for a daily period over the entire monthly period.",
      "unit": "degrees C",
      "dimensions": [
        "time",
        "y",
        "x"
      ]
    },
    "vp": {
      "type": "data",
      "description": "The average of the daily average partial pressure of water vapor over the monthly period.",
      "unit": "Pa",
      "dimensions": [
        "time",
        "y",
        "x"
      ]
    },
    "time_bnds": {
      "type": "auxiliary",
      "description": "",
      "dimensions": [
        "time",
        "nv"
      ]
    },
    "lambert_conformal_conic": {
      "type": "auxiliary",
      "description": "Lambert Conformal Conic.",
      "values": [
        -32767
      ],
      "dimensions": []
    }
  }
}
```

#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json"
  ],
  "id": "vector-datacube",
  "type": "Feature",
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [
        [
          [
            -122.40863800048828,
            37.60280825923639
          ],
          [
            -122.35301971435545,
            37.60280825923639
          ],
          [
            -122.35301971435545,
            37.641694203264265
          ],
          [
            -122.40863800048828,
            37.641694203264265
          ],
          [
            -122.40863800048828,
            37.60280825923639
          ]
        ]
      ],
      [
        [
          [
            -122.51575469970703,
            37.50373410549169
          ],
          [
            -122.48313903808594,
            37.50373410549169
          ],
          [
            -122.48313903808594,
            37.52443079581378
          ],
          [
            -122.51575469970703,
            37.52443079581378
          ],
          [
            -122.51575469970703,
            37.50373410549169
          ]
        ]
      ],
      [
        [
          [
            -122.26203918457031,
            37.69726847113855
          ],
          [
            -122.19577789306639,
            37.69726847113855
          ],
          [
            -122.19577789306639,
            37.747507619675595
          ],
          [
            -122.26203918457031,
            37.747507619675595
          ],
          [
            -122.26203918457031,
            37.69726847113855
          ]
        ]
      ],
      [
        [
          [
            -122.13415145874025,
            37.65175228874552
          ],
          [
            -122.10994720458984,
            37.65175228874552
          ],
          [
            -122.10994720458984,
            37.66765215806202
          ],
          [
            -122.13415145874025,
            37.66765215806202
          ],
          [
            -122.13415145874025,
            37.65175228874552
          ]
        ]
      ]
    ]
  },
  "bbox": [
    -122.51575469970703,
    37.50373410549169,
    -122.10994720458984,
    37.747507619675595
  ],
  "properties": {
    "title": "Multi-dimensional vector data cube in a STAC Item.",
    "start_datetime": "2016-01-01T00:00:00Z",
    "datetime": "2017-01-01T00:00:00Z",
    "end_datetime": "2018-01-01T00:00:00Z",
    "cube:dimensions": {
      "vector": {
        "type": "geometry",
        "bbox": [
          -122.51575469970703,
          37.50373410549169,
          -122.10994720458984,
          37.747507619675595
        ],
        "values": [
          "POLYGON ((-122.40863800048828 37.60280825923639, -122.35301971435545 37.60280825923639, -122.35301971435545 37.641694203264265, -122.40863800048828 37.641694203264265, -122.40863800048828 37.60280825923639))",
          "POLYGON ((-122.51575469970703 37.50373410549169, -122.48313903808594 37.50373410549169, -122.48313903808594 37.52443079581378, -122.51575469970703 37.52443079581378, -122.51575469970703 37.50373410549169))",
          "POLYGON ((-122.26203918457031 37.69726847113855, -122.19577789306639 37.69726847113855, -122.19577789306639 37.747507619675595, -122.26203918457031 37.747507619675595, -122.26203918457031 37.69726847113855))",
          "POLYGON ((-122.13415145874025 37.65175228874552, -122.10994720458984 37.65175228874552, -122.10994720458984 37.66765215806202, -122.13415145874025 37.66765215806202, -122.13415145874025 37.65175228874552))"
        ],
        "geometry_types": [
          "Polygon"
        ],
        "reference_system": 4326
      },
      "t": {
        "type": "temporal",
        "values": [
          "2016-01-01T00:00:00Z",
          "2017-01-01T00:00:00Z",
          "2018-01-01T00:00:00Z"
        ]
      },
      "stats": {
        "type": "statistics",
        "values": [
          "min",
          "max",
          "mean"
        ]
      }
    }
  },
  "assets": {
    "data": {
      "href": "http://cool-sat.com/catalog/datacube/data.nc",
      "type": "application/netcdf",
      "title": "netCDF Data cube"
    },
    "thumbnail": {
      "href": "http://cool-sat.com/catalog/datacube/thumbnail.png",
      "type": "image/png",
      "title": "Thumbnail"
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "http://cool-sat.com/catalog/datacube/vector.json"
    }
  ]
}
```

#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json"
  ],
  "type": "Collection",
  "id": "Sentinel2-L1C",
  "title": "Sentinel-2: MultiSpectral Instrument, Level-1C",
  "description": "Multi-dimensional Sentinel-2 data cube in a STAC collection.",
  "license": "proprietary",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -180,
          -56,
          180,
          83
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2015-06-23T00:00:00Z",
          "2019-07-10T13:44:56Z"
        ]
      ]
    }
  },
  "cube:dimensions": {
    "x": {
      "type": "spatial",
      "axis": "x",
      "extent": [
        -180,
        180
      ],
      "reference_system": 3857
    },
    "y": {
      "type": "spatial",
      "axis": "y",
      "extent": [
        -56,
        83
      ],
      "reference_system": 3857
    },
    "time": {
      "type": "temporal",
      "extent": [
        "2015-06-23T00:00:00Z",
        "2019-07-10T13:44:56Z"
      ],
      "step": "P5D"
    },
    "spectral": {
      "type": "bands",
      "values": [
        "B1",
        "B2",
        "B3",
        "B4",
        "B5",
        "B6",
        "B7",
        "B8",
        "B8A",
        "B9",
        "B10",
        "B11",
        "B12",
        "QA10",
        "QA20",
        "QA60"
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "2015-06-23T00:00:00Z",
      "maximum": "2019-07-10T13:44:56Z"
    },
    "gsd": [
      10,
      30,
      60
    ],
    "eo:platform": [
      "sentinel-2a",
      "sentinel-2b"
    ],
    "eo:constellation": [
      "sentinel-2"
    ],
    "eo:instrument": [
      "msi"
    ],
    "proj:epsg": [
      3857
    ],
    "eo:bands": [
      [
        {
          "name": "B1",
          "common_name": "coastal",
          "center_wavelength": 4.439
        },
        {
          "name": "B2",
          "common_name": "blue",
          "center_wavelength": 4.966
        },
        {
          "name": "B3",
          "common_name": "green",
          "center_wavelength": 5.6
        },
        {
          "name": "B4",
          "common_name": "red",
          "center_wavelength": 6.645
        },
        {
          "name": "B5",
          "center_wavelength": 7.039
        },
        {
          "name": "B6",
          "center_wavelength": 7.402
        },
        {
          "name": "B7",
          "center_wavelength": 7.825
        },
        {
          "name": "B8",
          "common_name": "nir",
          "center_wavelength": 8.351
        },
        {
          "name": "B8A",
          "center_wavelength": 8.648
        },
        {
          "name": "B9",
          "center_wavelength": 9.45
        },
        {
          "name": "B10",
          "center_wavelength": 1.3735
        },
        {
          "name": "B11",
          "common_name": "swir16",
          "center_wavelength": 1.6137
        },
        {
          "name": "B12",
          "common_name": "swir22",
          "center_wavelength": 2.2024
        }
      ]
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://example.sentinel2-hub.com/stac/example-collection.json"
    },
    {
      "rel": "license",
      "href": "https://scihub.copernicus.eu/twiki/pub/SciHubWebPortal/TermsConditions/Sentinel_Data_Terms_and_Conditions.pdf",
      "title": "Legal notice on the use of Copernicus Sentinel Data and Service Information"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/datacube/context.jsonld",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json"
  ],
  "type": "Collection",
  "id": "Sentinel2-L1C",
  "title": "Sentinel-2: MultiSpectral Instrument, Level-1C",
  "description": "Multi-dimensional Sentinel-2 data cube in a STAC collection.",
  "license": "proprietary",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -180,
          -56,
          180,
          83
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2015-06-23T00:00:00Z",
          "2019-07-10T13:44:56Z"
        ]
      ]
    }
  },
  "cube:dimensions": {
    "x": {
      "type": "spatial",
      "axis": "x",
      "extent": [
        -180,
        180
      ],
      "reference_system": 3857
    },
    "y": {
      "type": "spatial",
      "axis": "y",
      "extent": [
        -56,
        83
      ],
      "reference_system": 3857
    },
    "time": {
      "type": "temporal",
      "extent": [
        "2015-06-23T00:00:00Z",
        "2019-07-10T13:44:56Z"
      ],
      "step": "P5D"
    },
    "spectral": {
      "type": "bands",
      "values": [
        "B1",
        "B2",
        "B3",
        "B4",
        "B5",
        "B6",
        "B7",
        "B8",
        "B8A",
        "B9",
        "B10",
        "B11",
        "B12",
        "QA10",
        "QA20",
        "QA60"
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "2015-06-23T00:00:00Z",
      "maximum": "2019-07-10T13:44:56Z"
    },
    "gsd": [
      10,
      30,
      60
    ],
    "eo:platform": [
      "sentinel-2a",
      "sentinel-2b"
    ],
    "eo:constellation": [
      "sentinel-2"
    ],
    "eo:instrument": [
      "msi"
    ],
    "proj:epsg": [
      3857
    ],
    "eo:bands": [
      [
        {
          "name": "B1",
          "common_name": "coastal",
          "center_wavelength": 4.439
        },
        {
          "name": "B2",
          "common_name": "blue",
          "center_wavelength": 4.966
        },
        {
          "name": "B3",
          "common_name": "green",
          "center_wavelength": 5.6
        },
        {
          "name": "B4",
          "common_name": "red",
          "center_wavelength": 6.645
        },
        {
          "name": "B5",
          "center_wavelength": 7.039
        },
        {
          "name": "B6",
          "center_wavelength": 7.402
        },
        {
          "name": "B7",
          "center_wavelength": 7.825
        },
        {
          "name": "B8",
          "common_name": "nir",
          "center_wavelength": 8.351
        },
        {
          "name": "B8A",
          "center_wavelength": 8.648
        },
        {
          "name": "B9",
          "center_wavelength": 9.45
        },
        {
          "name": "B10",
          "center_wavelength": 1.3735
        },
        {
          "name": "B11",
          "common_name": "swir16",
          "center_wavelength": 1.6137
        },
        {
          "name": "B12",
          "common_name": "swir22",
          "center_wavelength": 2.2024
        }
      ]
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://example.sentinel2-hub.com/stac/example-collection.json"
    },
    {
      "rel": "license",
      "href": "https://scihub.copernicus.eu/twiki/pub/SciHubWebPortal/TermsConditions/Sentinel_Data_Terms_and_Conditions.pdf",
      "title": "Legal notice on the use of Copernicus Sentinel Data and Service Information"
    }
  ]
}
```

#### ttl
```ttl
@prefix cube: <https://w3id.org/ogc/stac/datacube/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/datacube/collection/Sentinel2-L1C> a <https://example.com/stac/datacube/collection/Collection> ;
    dcterms:description "Multi-dimensional Sentinel-2 data cube in a STAC collection." ;
    dcterms:extent [ ] ;
    dcterms:title "Sentinel-2: MultiSpectral Instrument, Level-1C" ;
    rdfs:seeAlso [ rdfs:label "Legal notice on the use of Copernicus Sentinel Data and Service Information" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://scihub.copernicus.eu/twiki/pub/SciHubWebPortal/TermsConditions/Sentinel_Data_Terms_and_Conditions.pdf> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.sentinel2-hub.com/stac/example-collection.json> ] ;
    dcat:license "proprietary" ;
    stac:hasExtension "https://stac-extensions.github.io/datacube/v2.3.0/schema.json" ;
    stac:version "1.1.0" ;
    cube:dimensions [ cube:axis "y" ;
            cube:extent ( -56 83 ) ;
            cube:reference_system 3857 ;
            cube:type "spatial" ],
        [ cube:extent ( "2015-06-23T00:00:00Z" "2019-07-10T13:44:56Z" ) ;
            cube:step "P5D" ;
            cube:type "temporal" ],
        [ cube:axis "x" ;
            cube:extent ( -180 180 ) ;
            cube:reference_system 3857 ;
            cube:type "spatial" ],
        [ cube:type "bands" ;
            cube:values ( "B1" "B2" "B3" "B4" "B5" "B6" "B7" "B8" "B8A" "B9" "B10" "B11" "B12" "QA10" "QA20" "QA60" ) ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Datacube extension
description: STAC Datacube Extension for Items and Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/datacube/v2.3.0/schema.json
x-jsonld-extra-terms:
  cube:dimensions:
    x-jsonld-id: https://w3id.org/ogc/stac/datacube/dimensions
    x-jsonld-container: '@index'
    x-jsonld-context:
      type: https://w3id.org/ogc/stac/datacube/type
      axis: https://w3id.org/ogc/stac/datacube/axis
      axes:
        '@id': https://w3id.org/ogc/stac/datacube/axes
        '@container': '@set'
      description: https://w3id.org/ogc/stac/datacube/description
      extent:
        '@id': https://w3id.org/ogc/stac/datacube/extent
        '@container': '@list'
      values:
        '@id': https://w3id.org/ogc/stac/datacube/values
        '@container': '@list'
      step: https://w3id.org/ogc/stac/datacube/step
      unit: https://w3id.org/ogc/stac/datacube/unit
      reference_system: https://w3id.org/ogc/stac/datacube/reference_system
      bbox:
        '@id': https://w3id.org/ogc/stac/datacube/bbox
        '@container': '@list'
      geometry_types:
        '@id': https://w3id.org/ogc/stac/datacube/geometry_types
        '@container': '@set'
  cube:variables:
    x-jsonld-id: https://w3id.org/ogc/stac/datacube/variables
    x-jsonld-container: '@index'
    x-jsonld-context:
      dimensions:
        '@id': https://w3id.org/ogc/stac/datacube/dimensions
        '@container': '@set'
      type: https://w3id.org/ogc/stac/datacube/type
      description: https://w3id.org/ogc/stac/datacube/description
      extent:
        '@id': https://w3id.org/ogc/stac/datacube/extent
        '@container': '@list'
      values:
        '@id': https://w3id.org/ogc/stac/datacube/values
        '@container': '@list'
      unit: https://w3id.org/ogc/stac/datacube/unit
      nodata: https://w3id.org/ogc/stac/datacube/nodata
      data_type: https://w3id.org/ogc/stac/datacube/data_type
x-jsonld-prefixes:
  cube: https://w3id.org/ogc/stac/datacube/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/datacube/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/datacube/schema.yaml)


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
    "cube:dimensions": {
      "@id": "cube:dimensions",
      "@container": "@index",
      "@context": {
        "type": "cube:type",
        "axis": "cube:axis",
        "axes": {
          "@id": "cube:axes",
          "@container": "@set"
        },
        "description": "cube:description",
        "extent": {
          "@id": "cube:extent",
          "@container": "@list"
        },
        "values": {
          "@id": "cube:values",
          "@container": "@list"
        },
        "step": "cube:step",
        "unit": "cube:unit",
        "reference_system": "cube:reference_system",
        "bbox": {
          "@id": "cube:bbox",
          "@container": "@list"
        },
        "geometry_types": {
          "@id": "cube:geometry_types",
          "@container": "@set"
        }
      }
    },
    "cube:variables": {
      "@id": "cube:variables",
      "@container": "@index",
      "@context": {
        "dimensions": {
          "@id": "cube:dimensions",
          "@container": "@set"
        },
        "type": "cube:type",
        "description": "cube:description",
        "extent": {
          "@id": "cube:extent",
          "@container": "@list"
        },
        "values": {
          "@id": "cube:values",
          "@container": "@list"
        },
        "unit": "cube:unit",
        "nodata": "cube:nodata",
        "data_type": "cube:data_type"
      }
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "cube": "https://w3id.org/ogc/stac/datacube/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/datacube/context.jsonld)

## Sources

* [STAC Datacube Extension](https://github.com/stac-extensions/datacube/tree/v2.3.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/datacube`

