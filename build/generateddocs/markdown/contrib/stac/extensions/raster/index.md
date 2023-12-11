
# STAC Forecast Extension (Schema)

`ogc.contrib.stac.extensions.raster` *v0.1*

This extension defines some high-level fields to get a basic understanding of weather forecast data. Some fields may also be applicable for climate forecast data, but it hasn't been written specifically for that domain.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example of Raster feature with Forecast extension
#### json
```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "1660262400-gefs.chem.t00z.a2d_0p25.f000",
  "properties": {
    "expires": "2022-08-12T00:00:00Z",
    "grib:discipline": "meteorological",
    "forecast:reference_datetime": "2022-08-12T00:00:00Z",
    "forecast:horizon": "PT0H",
    "processing:facility": "US-NCEP",
    "proj:epsg": null,
    "proj:projjson": {
      "$schema": "https://proj.org/schemas/v0.4/projjson.schema.json",
      "type": "GeographicCRS",
      "name": "Coordinate System imported from GRIB file",
      "datum": {
        "type": "GeodeticReferenceFrame",
        "name": "unnamed",
        "ellipsoid": {
          "name": "Sphere",
          "radius": 6371229
        }
      },
      "coordinate_system": {
        "subtype": "ellipsoidal",
        "axis": [
          {
            "name": "Latitude",
            "abbreviation": "lat",
            "direction": "north",
            "unit": "degree"
          },
          {
            "name": "Longitude",
            "abbreviation": "lon",
            "direction": "east",
            "unit": "degree"
          }
        ]
      }
    },
    "proj:shape": [
      1440,
      721
    ],
    "proj:transform": [
      0.25,
      0,
      -180.125,
      0,
      -0.25,
      90.125
    ],
    "datetime": "2022-08-12T00:00:00Z"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180.125,
          -90.125
        ],
        [
          179.875,
          -90.125
        ],
        [
          179.875,
          90.125
        ],
        [
          -180.125,
          90.125
        ],
        [
          -180.125,
          -90.125
        ]
      ]
    ]
  },
  "links": [
    {
      "rel": "collection",
      "href": "collection.json",
      "type": "application/json",
      "title": "NOAA Global Ensemble Forecast System (GEFS)"
    }
  ],
  "assets": {
    "grib2": {
      "href": "../tests/data-files/ncep/chem/gefs.chem.t00z.a2d_0p25.f000.grib2",
      "type": "application/wmo-GRIB2",
      "title": "GRIB2 file",
      "description": "The forecast data. Subsets of the data can be loaded using information from the associated index file.",
      "raster:bands": [
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0061231516301632,
            "maximum": 29.00252532959,
            "mean": 0.16919819447534,
            "stddev": 0.3764434353083
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.64043462276459,
            "maximum": 0.84214621782303,
            "mean": 0.76601473219048,
            "stddev": 0.036238526175545
          },
          "description": "Asymmetry Factor",
          "grib:element": "asysfk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.74945330619812,
            "maximum": 0.99926424026489,
            "mean": 0.94882971866408,
            "stddev": 0.03411827900738
          },
          "description": "Single Scattering Albedo",
          "grib:element": "ssalbk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0043960274197161,
            "maximum": 20.069881439209,
            "mean": 0.14160790555694,
            "stddev": 0.28359911907921
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0027195760048926,
            "maximum": 12.060523986816,
            "mean": 0.11106313425042,
            "stddev": 0.19478975993829
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0023061106912792,
            "maximum": 10.419253349304,
            "mean": 0.10488103820814,
            "stddev": 0.17622332473456
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0000031616805244994,
            "maximum": 3.1155025959015,
            "mean": 0.008855822054689,
            "stddev": 0.053499185481957
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0000030212595447665,
            "maximum": 2.8461494445801,
            "mean": 0.0081680120525493,
            "stddev": 0.049103679640117
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0000013180878113417,
            "maximum": 1.0072281360626,
            "mean": 0.04030248834866,
            "stddev": 0.056431185533878
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0000013180878113417,
            "maximum": 1.0072281360626,
            "mean": 0.04030248834866,
            "stddev": 0.056431185533878
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00060580234276131,
            "maximum": 4.025007724762,
            "mean": 0.020819146128007,
            "stddev": 0.055893246719568
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00060580234276131,
            "maximum": 4.025007724762,
            "mean": 0.020819146128007,
            "stddev": 0.055893246719568
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00052909186342731,
            "maximum": 10.38880443573,
            "mean": 0.034657705831735,
            "stddev": 0.12668759764327
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00051318010082468,
            "maximum": 10.030592918396,
            "mean": 0.034007718824436,
            "stddev": 0.12402715920299
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00014269040548243,
            "maximum": 1.6327264308929,
            "mean": 0.006424343336384,
            "stddev": 0.023662662901252
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.000034597389458213,
            "maximum": 0.34983298182487,
            "mean": 0.0015795669489139,
            "stddev": 0.0054900974371096
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0020731242839247,
            "maximum": 9.0323190689087,
            "mean": 0.097953657308747,
            "stddev": 0.16041500636699
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0011907988227904,
            "maximum": 4.9453902244568,
            "mean": 0.078425688122925,
            "stddev": 0.11565155095503
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00030365923885256,
            "maximum": 2.2889845371246,
            "mean": 0.05313892097441,
            "stddev": 0.071845546939689
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00007992128666956,
            "maximum": 0.78618425130844,
            "mean": 0.016158330569383,
            "stddev": 0.023989501072855
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 1.3996381831305e-8,
            "maximum": 309.77227783203,
            "mean": 0.41038999470455,
            "stddev": 4.0030611393966
          },
          "description": "Particulate matter (fine)",
          "unit": "10^-6g/m^3",
          "grib:element": "pmtf",
          "grib:short_name": "0-SFC"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 4.6261600772368e-8,
            "maximum": 57.208011627197,
            "mean": 3.1927213114378,
            "stddev": 4.2616933493912
          },
          "description": "Particulate matter (fine)",
          "unit": "10^-6g/m^3",
          "grib:element": "pmtf",
          "grib:short_name": "0-SFC"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00021699354692828,
            "maximum": 13193.625,
            "mean": 22.910594069461,
            "stddev": 41.772567854659
          },
          "description": "Particulate matter (coarse)",
          "unit": "10^-6g/m^3",
          "grib:element": "pmtc",
          "grib:short_name": "0-SFC"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00017043380648829,
            "maximum": 13191.577148438,
            "mean": 5.7616627017781,
            "stddev": 27.126657158214
          },
          "description": "Particulate matter (fine)",
          "unit": "10^-6g/m^3",
          "grib:element": "pmtf",
          "grib:short_name": "0-SFC"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 5.4072143029771e-7,
            "maximum": 0.0025077844038606,
            "mean": 0.000021760580395887,
            "stddev": 0.000048162056013382
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 3.7170894984229e-7,
            "maximum": 0.001863478217274,
            "mean": 0.0000093149012037263,
            "stddev": 0.000020545495128855
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 7.861409301313e-10,
            "maximum": 0.00054902862757444,
            "mean": 0.000001712380465595,
            "stddev": 0.0000098742292093661
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 2.2129525989456e-10,
            "maximum": 0.000041638519178377,
            "mean": 0.0000023144710131757,
            "stddev": 0.0000026636810432403
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 6.5196523735267e-9,
            "maximum": 0.0000842632871354,
            "mean": 3.0601876239339e-7,
            "stddev": 0.0000011748606985804
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 6.0665072965094e-8,
            "maximum": 0.0017742430791259,
            "mean": 0.0000031750432594164,
            "stddev": 0.000014052866691345
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        }
      ],
      "roles": [
        "data",
        "source"
      ]
    },
    "index": {
      "href": "../tests/data-files/ncep/chem/gefs.chem.t00z.a2d_0p25.f000.grib2.idx",
      "type": "text/plain",
      "title": "Index file",
      "description": "Contains information on each message within the GRIB2 file.",
      "roles": [
        "metadata",
        "index"
      ]
    }
  },
  "bbox": [
    -180.125,
    90.125,
    179.875,
    -90.125
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/timestamps/v1.0.0/schema.json"
  ],
  "collection": "noaa-gefs"
}
```

#### jsonld
```jsonld
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "1660262400-gefs.chem.t00z.a2d_0p25.f000",
  "properties": {
    "expires": "2022-08-12T00:00:00Z",
    "grib:discipline": "meteorological",
    "forecast:reference_datetime": "2022-08-12T00:00:00Z",
    "forecast:horizon": "PT0H",
    "processing:facility": "US-NCEP",
    "proj:epsg": null,
    "proj:projjson": {
      "$schema": "https://proj.org/schemas/v0.4/projjson.schema.json",
      "type": "GeographicCRS",
      "name": "Coordinate System imported from GRIB file",
      "datum": {
        "type": "GeodeticReferenceFrame",
        "name": "unnamed",
        "ellipsoid": {
          "name": "Sphere",
          "radius": 6371229
        }
      },
      "coordinate_system": {
        "subtype": "ellipsoidal",
        "axis": [
          {
            "name": "Latitude",
            "abbreviation": "lat",
            "direction": "north",
            "unit": "degree"
          },
          {
            "name": "Longitude",
            "abbreviation": "lon",
            "direction": "east",
            "unit": "degree"
          }
        ]
      }
    },
    "proj:shape": [
      1440,
      721
    ],
    "proj:transform": [
      0.25,
      0,
      -180.125,
      0,
      -0.25,
      90.125
    ],
    "datetime": "2022-08-12T00:00:00Z"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180.125,
          -90.125
        ],
        [
          179.875,
          -90.125
        ],
        [
          179.875,
          90.125
        ],
        [
          -180.125,
          90.125
        ],
        [
          -180.125,
          -90.125
        ]
      ]
    ]
  },
  "links": [
    {
      "rel": "collection",
      "href": "collection.json",
      "type": "application/json",
      "title": "NOAA Global Ensemble Forecast System (GEFS)"
    }
  ],
  "assets": {
    "grib2": {
      "href": "../tests/data-files/ncep/chem/gefs.chem.t00z.a2d_0p25.f000.grib2",
      "type": "application/wmo-GRIB2",
      "title": "GRIB2 file",
      "description": "The forecast data. Subsets of the data can be loaded using information from the associated index file.",
      "raster:bands": [
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0061231516301632,
            "maximum": 29.00252532959,
            "mean": 0.16919819447534,
            "stddev": 0.3764434353083
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.64043462276459,
            "maximum": 0.84214621782303,
            "mean": 0.76601473219048,
            "stddev": 0.036238526175545
          },
          "description": "Asymmetry Factor",
          "grib:element": "asysfk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.74945330619812,
            "maximum": 0.99926424026489,
            "mean": 0.94882971866408,
            "stddev": 0.03411827900738
          },
          "description": "Single Scattering Albedo",
          "grib:element": "ssalbk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0043960274197161,
            "maximum": 20.069881439209,
            "mean": 0.14160790555694,
            "stddev": 0.28359911907921
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0027195760048926,
            "maximum": 12.060523986816,
            "mean": 0.11106313425042,
            "stddev": 0.19478975993829
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0023061106912792,
            "maximum": 10.419253349304,
            "mean": 0.10488103820814,
            "stddev": 0.17622332473456
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 3.1616805244994e-06,
            "maximum": 3.1155025959015,
            "mean": 0.008855822054689,
            "stddev": 0.053499185481957
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 3.0212595447665e-06,
            "maximum": 2.8461494445801,
            "mean": 0.0081680120525493,
            "stddev": 0.049103679640117
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 1.3180878113417e-06,
            "maximum": 1.0072281360626,
            "mean": 0.04030248834866,
            "stddev": 0.056431185533878
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 1.3180878113417e-06,
            "maximum": 1.0072281360626,
            "mean": 0.04030248834866,
            "stddev": 0.056431185533878
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00060580234276131,
            "maximum": 4.025007724762,
            "mean": 0.020819146128007,
            "stddev": 0.055893246719568
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00060580234276131,
            "maximum": 4.025007724762,
            "mean": 0.020819146128007,
            "stddev": 0.055893246719568
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00052909186342731,
            "maximum": 10.38880443573,
            "mean": 0.034657705831735,
            "stddev": 0.12668759764327
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00051318010082468,
            "maximum": 10.030592918396,
            "mean": 0.034007718824436,
            "stddev": 0.12402715920299
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00014269040548243,
            "maximum": 1.6327264308929,
            "mean": 0.006424343336384,
            "stddev": 0.023662662901252
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 3.4597389458213e-05,
            "maximum": 0.34983298182487,
            "mean": 0.0015795669489139,
            "stddev": 0.0054900974371096
          },
          "description": "Scattering Aerosol Optical Thickness",
          "grib:element": "sctaotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0020731242839247,
            "maximum": 9.0323190689087,
            "mean": 0.097953657308747,
            "stddev": 0.16041500636699
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.0011907988227904,
            "maximum": 4.9453902244568,
            "mean": 0.078425688122925,
            "stddev": 0.11565155095503
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00030365923885256,
            "maximum": 2.2889845371246,
            "mean": 0.05313892097441,
            "stddev": 0.071845546939689
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 7.992128666956e-05,
            "maximum": 0.78618425130844,
            "mean": 0.016158330569383,
            "stddev": 0.023989501072855
          },
          "description": "Atmosphere Optical Thickness",
          "grib:element": "aotk",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 1.3996381831305e-08,
            "maximum": 309.77227783203,
            "mean": 0.41038999470455,
            "stddev": 4.0030611393966
          },
          "description": "Particulate matter (fine)",
          "unit": "10^-6g/m^3",
          "grib:element": "pmtf",
          "grib:short_name": "0-SFC"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 4.6261600772368e-08,
            "maximum": 57.208011627197,
            "mean": 3.1927213114378,
            "stddev": 4.2616933493912
          },
          "description": "Particulate matter (fine)",
          "unit": "10^-6g/m^3",
          "grib:element": "pmtf",
          "grib:short_name": "0-SFC"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00021699354692828,
            "maximum": 13193.625,
            "mean": 22.910594069461,
            "stddev": 41.772567854659
          },
          "description": "Particulate matter (coarse)",
          "unit": "10^-6g/m^3",
          "grib:element": "pmtc",
          "grib:short_name": "0-SFC"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 0.00017043380648829,
            "maximum": 13191.577148438,
            "mean": 5.7616627017781,
            "stddev": 27.126657158214
          },
          "description": "Particulate matter (fine)",
          "unit": "10^-6g/m^3",
          "grib:element": "pmtf",
          "grib:short_name": "0-SFC"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 5.4072143029771e-07,
            "maximum": 0.0025077844038606,
            "mean": 2.1760580395887e-05,
            "stddev": 4.8162056013382e-05
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 3.7170894984229e-07,
            "maximum": 0.001863478217274,
            "mean": 9.3149012037263e-06,
            "stddev": 2.0545495128855e-05
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 7.861409301313e-10,
            "maximum": 0.00054902862757444,
            "mean": 1.712380465595e-06,
            "stddev": 9.8742292093661e-06
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 2.2129525989456e-10,
            "maximum": 4.1638519178377e-05,
            "mean": 2.3144710131757e-06,
            "stddev": 2.6636810432403e-06
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 6.5196523735267e-09,
            "maximum": 8.42632871354e-05,
            "mean": 3.0601876239339e-07,
            "stddev": 1.1748606985804e-06
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        },
        {
          "data_type": "float64",
          "statistics": {
            "minimum": 6.0665072965094e-08,
            "maximum": 0.0017742430791259,
            "mean": 3.1750432594164e-06,
            "stddev": 1.4052866691345e-05
          },
          "description": "Column-Integrated Mass Density",
          "unit": "kg/(m^2)",
          "grib:element": "colmd",
          "grib:short_name": "0-EATM"
        }
      ],
      "roles": [
        "data",
        "source"
      ]
    },
    "index": {
      "href": "../tests/data-files/ncep/chem/gefs.chem.t00z.a2d_0p25.f000.grib2.idx",
      "type": "text/plain",
      "title": "Index file",
      "description": "Contains information on each message within the GRIB2 file.",
      "roles": [
        "metadata",
        "index"
      ]
    }
  },
  "bbox": [
    -180.125,
    90.125,
    179.875,
    -90.125
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/timestamps/v1.0.0/schema.json"
  ],
  "collection": "noaa-gefs",
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/context.jsonld"
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <grib:> .
@prefix ns2: <proj:> .
@prefix ns3: <forecast:> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix ns5: <processing:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/1.1/schema/qudt#> .
@prefix raster: <urn:stac:extensions/raster#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix stac: <urn:stac:vocab#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/raster/example-1/1660262400-gefs.chem.t00z.a2d_0p25.f000> a geojson:Feature ;
    ns3:horizon "PT0H" ;
    ns3:reference_datetime "2022-08-12T00:00:00Z" ;
    ns1:discipline "meteorological" ;
    rdfs:seeAlso [ rdfs:label "NOAA Global Ensemble Forecast System (GEFS)" ;
            dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/raster/example-1/collection.json> ] ;
    geojson:bbox ( -1.80125e+02 9.0125e+01 1.79875e+02 -9.0125e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( "[[-180.125, -90.125], [179.875, -90.125], [179.875, 90.125], [-180.125, 90.125], [-180.125, -90.125]]" ) ] ;
    ns5:facility "US-NCEP" ;
    ns2:projjson [ a <https://example.com/stac/raster/example-1/GeographicCRS> ] ;
    ns2:shape 721,
        1440 ;
    ns2:transform -1.80125e+02,
        -2.5e-01,
        0,
        2.5e-01,
        9.0125e+01 ;
    stac:extensions "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
        "https://stac-extensions.github.io/timestamps/v1.0.0/schema.json" ;
    stac:hasAsset <https://example.com/stac/raster/example-1/grib2>,
        <https://example.com/stac/raster/example-1/index> ;
    stac:version "1.0.0" .

<https://example.com/stac/raster/example-1/grib2> dcterms:description "The forecast data. Subsets of the data can be loaded using information from the associated index file." ;
    dcterms:format "application/wmo-GRIB2" ;
    dcterms:title "GRIB2 file" ;
    dcat:downloadURL <https://example.com/stac/raster/tests/data-files/ncep/chem/gefs.chem.t00z.a2d_0p25.f000.grib2> ;
    raster:bands [ ns1:short_name "0-EATM" ;
            dcterms:description "Scattering Aerosol Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/sctaotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Column-Integrated Mass Density" ;
            qudt:unit "kg/(m^2)" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/colmd> ],
        [ ns1:short_name "0-SFC" ;
            dcterms:description "Particulate matter (coarse)" ;
            qudt:unit "10^-6g/m^3" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/pmtc> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Scattering Aerosol Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/sctaotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Column-Integrated Mass Density" ;
            qudt:unit "kg/(m^2)" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/colmd> ],
        [ ns1:short_name "0-SFC" ;
            dcterms:description "Particulate matter (fine)" ;
            qudt:unit "10^-6g/m^3" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/pmtf> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Asymmetry Factor" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/asysfk> ],
        [ ns1:short_name "0-SFC" ;
            dcterms:description "Particulate matter (fine)" ;
            qudt:unit "10^-6g/m^3" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/pmtf> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Scattering Aerosol Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/sctaotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Single Scattering Albedo" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/ssalbk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Column-Integrated Mass Density" ;
            qudt:unit "kg/(m^2)" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/colmd> ],
        [ ns1:short_name "0-SFC" ;
            dcterms:description "Particulate matter (fine)" ;
            qudt:unit "10^-6g/m^3" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/pmtf> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Column-Integrated Mass Density" ;
            qudt:unit "kg/(m^2)" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/colmd> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Scattering Aerosol Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/sctaotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Column-Integrated Mass Density" ;
            qudt:unit "kg/(m^2)" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/colmd> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Scattering Aerosol Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/sctaotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Scattering Aerosol Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/sctaotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Atmosphere Optical Thickness" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/aotk> ],
        [ ns1:short_name "0-EATM" ;
            dcterms:description "Column-Integrated Mass Density" ;
            qudt:unit "kg/(m^2)" ;
            sosa:observedProperty <http://w3id.org/ogc/dev/stac-examples/bands/colmd> ] .

<https://example.com/stac/raster/example-1/index> dcterms:description "Contains information on each message within the GRIB2 file." ;
    dcterms:format "text/plain" ;
    dcterms:title "Index file" ;
    dcat:downloadURL <https://example.com/stac/raster/tests/data-files/ncep/chem/gefs.chem.t00z.a2d_0p25.f000.grib2.idx> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Forecast Extension
description: STAC Forecast Extension for STAC Items and STAC Collections.
allOf:
- anyOf:
  - $ref: ../../collection/schema.yaml
  - $ref: ../../item/schema.yaml
- $ref: https://stac-extensions.github.io/raster/v1.1.0/schema.json#
x-jsonld-extra-terms:
  raster:bands:
    x-jsonld-id: urn:stac:extensions/raster#bands
    x-jsonld-context:
      aotk: http://vocab.nerc.ac.uk/standard_name/atmosphere_optical_thickness_due_to_ambient_aerosol_particles/
      grib:element:
        '@id': http://www.w3.org/ns/sosa/observedProperty
        '@type': '@id'
        '@context':
          '@base': http://w3id.org/ogc/dev/stac-examples/bands/
      unit: http://qudt.org/1.1/schema/qudt#unit
x-jsonld-prefixes:
  raster: urn:stac:extensions/raster#
  sosa: http://www.w3.org/ns/sosa/
  qudt: http://qudt.org/1.1/schema/qudt#
  stac: urn:stac:vocab#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "links": {
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
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "stac_version": "stac:version",
    "stac_extensions": "stac:extensions",
    "description": "dct:description",
    "license": "dct:license",
    "keywords": "dct:subject",
    "extent": "dct:extent",
    "assets": {
      "@id": "stac:hasAsset",
      "@container": "@id",
      "@context": {
        "href": {
          "@id": "dcat:downloadURL",
          "@type": "@id"
        },
        "title": "dct:title",
        "type": "dct:format"
      }
    },
    "type": "@type",
    "id": "@id",
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
    "raster:bands": {
      "@id": "raster:bands",
      "@context": {
        "aotk": "http://vocab.nerc.ac.uk/standard_name/atmosphere_optical_thickness_due_to_ambient_aerosol_particles/",
        "grib:element": {
          "@id": "sosa:observedProperty",
          "@type": "@id",
          "@context": {
            "@base": "http://w3id.org/ogc/dev/stac-examples/bands/"
          }
        },
        "unit": "qudt:unit"
      }
    },
    "stac": "urn:stac:vocab#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "raster": "urn:stac:extensions/raster#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "qudt": "http://qudt.org/1.1/schema/qudt#",
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/raster/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/forecast)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/raster`

