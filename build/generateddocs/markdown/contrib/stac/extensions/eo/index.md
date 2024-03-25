
# STAC Electro-Optical Extension (Schema)

`ogc.contrib.stac.extensions.eo` *v0.1*

Electro-Optical (EO) Extension to the SpatioTemporal Asset Catalog (STAC) specification.

EO data is considered to be data that represents a snapshot of the Earth for a single date and time. It could consist of multiple spectral bands in any part of the electromagnetic spectrum. Examples of EO data include sensors with visible, short-wave and mid-wave IR bands (e.g., the OLI instrument on Landsat-8), long-wave IR bands (e.g. TIRS aboard Landsat-8).

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example of Electro-Optical using projection extension
#### json
```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "proj-example",
  "properties": {
    "datetime": "2018-10-01T01:08:32.033000Z",
    "proj:epsg": 32614,
    "proj:wkt2": "PROJCS[\"WGS 84 / UTM zone 14N\",GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]],UNIT[\"metre\",1,AUTHORITY[\"EPSG\",\"9001\"]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"latitude_of_origin\",0],PARAMETER[\"central_meridian\",-99],PARAMETER[\"scale_factor\",0.9996],PARAMETER[\"false_easting\",500000],PARAMETER[\"false_northing\",0],AUTHORITY[\"EPSG\",\"32614\"],AXIS[\"Easting\",EAST],AXIS[\"Northing\",NORTH]]",
    "proj:projjson": {
      "$schema": "https://proj.org/schemas/v0.2/projjson.schema.json",
      "type": "ProjectedCRS",
      "name": "WGS 84 / UTM zone 14N",
      "base_crs": {
        "name": "WGS 84",
        "datum": {
          "type": "GeodeticReferenceFrame",
          "name": "World Geodetic System 1984",
          "ellipsoid": {
            "name": "WGS 84",
            "semi_major_axis": 6378137,
            "inverse_flattening": 298.257223563
          }
        },
        "coordinate_system": {
          "subtype": "ellipsoidal",
          "axis": [
            {
              "name": "Geodetic latitude",
              "abbreviation": "Lat",
              "direction": "north",
              "unit": "degree"
            },
            {
              "name": "Geodetic longitude",
              "abbreviation": "Lon",
              "direction": "east",
              "unit": "degree"
            }
          ]
        },
        "id": {
          "authority": "EPSG",
          "code": 4326
        }
      },
      "conversion": {
        "name": "UTM zone 14N",
        "method": {
          "name": "Transverse Mercator",
          "id": {
            "authority": "EPSG",
            "code": 9807
          }
        },
        "parameters": [
          {
            "name": "Latitude of natural origin",
            "value": 0,
            "unit": "degree",
            "id": {
              "authority": "EPSG",
              "code": 8801
            }
          },
          {
            "name": "Longitude of natural origin",
            "value": -99,
            "unit": "degree",
            "id": {
              "authority": "EPSG",
              "code": 8802
            }
          },
          {
            "name": "Scale factor at natural origin",
            "value": 0.9996,
            "unit": "unity",
            "id": {
              "authority": "EPSG",
              "code": 8805
            }
          },
          {
            "name": "False easting",
            "value": 500000,
            "unit": "metre",
            "id": {
              "authority": "EPSG",
              "code": 8806
            }
          },
          {
            "name": "False northing",
            "value": 0,
            "unit": "metre",
            "id": {
              "authority": "EPSG",
              "code": 8807
            }
          }
        ]
      },
      "coordinate_system": {
        "subtype": "Cartesian",
        "axis": [
          {
            "name": "Easting",
            "abbreviation": "E",
            "direction": "east",
            "unit": "metre"
          },
          {
            "name": "Northing",
            "abbreviation": "N",
            "direction": "north",
            "unit": "metre"
          }
        ]
      },
      "area": "World - N hemisphere - 102°W to 96°W - by country",
      "bbox": {
        "south_latitude": 0,
        "west_longitude": -102,
        "north_latitude": 84,
        "east_longitude": -96
      },
      "id": {
        "authority": "EPSG",
        "code": 32614
      }
    },
    "proj:geometry": {
      "coordinates": [
        [
          [
            169200,
            3712800
          ],
          [
            403200,
            3712800
          ],
          [
            403200,
            3951000
          ],
          [
            169200,
            3951000
          ],
          [
            169200,
            3712800
          ]
        ]
      ],
      "type": "Polygon"
    },
    "proj:bbox": [
      169200,
      3712800,
      403200,
      3951000
    ],
    "proj:centroid": {
      "lat": 34.595302781575604,
      "lon": -101.34448382627504
    },
    "proj:shape": [
      8391,
      8311
    ],
    "proj:transform": [
      30,
      0,
      224985,
      0,
      -30,
      6790215,
      0,
      0,
      1
    ]
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          152.52758,
          60.63437
        ],
        [
          149.1755,
          61.19016
        ],
        [
          148.13933,
          59.51584
        ],
        [
          151.33786,
          58.97792
        ],
        [
          152.52758,
          60.63437
        ]
      ]
    ]
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Example Catalog"
    },
    {
      "rel": "parent",
      "href": "../collection.json",
      "type": "application/json",
      "title": "Collection of Extension Items"
    },
    {
      "rel": "collection",
      "href": "../collection.json",
      "type": "application/json",
      "title": "Collection of Extension Items"
    }
  ],
  "assets": {
    "B1": {
      "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/107/018/LC08_L1TP_107018_20181001_20181001_01_RT/LC08_L1TP_107018_20181001_20181001_01_RT_B1.TIF",
      "type": "image/tiff; application=geotiff",
      "title": "Band 1 (coastal)",
      "eo:bands": [
        {
          "name": "B1",
          "common_name": "coastal",
          "center_wavelength": 0.44,
          "full_width_half_max": 0.02
        }
      ]
    },
    "B8": {
      "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/107/018/LC08_L1TP_107018_20181001_20181001_01_RT/LC08_L1TP_107018_20181001_20181001_01_RT_B8.TIF",
      "type": "image/tiff; application=geotiff",
      "title": "Band 8 (panchromatic)",
      "eo:bands": [
        {
          "name": "B8",
          "center_wavelength": 0.59,
          "full_width_half_max": 0.18
        }
      ],
      "proj:shape": [
        16781,
        16621
      ],
      "proj:transform": [
        15,
        0,
        224992.5,
        0,
        -15,
        6790207.5,
        0,
        0,
        1
      ]
    }
  },
  "bbox": [
    148.13933,
    59.51584,
    152.52758,
    60.63437
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json"
  ],
  "collection": "landsat-8-l1"
}

```

#### jsonld
```jsonld
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "proj-example",
  "properties": {
    "datetime": "2018-10-01T01:08:32.033000Z",
    "proj:epsg": 32614,
    "proj:wkt2": "PROJCS[\"WGS 84 / UTM zone 14N\",GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]],UNIT[\"metre\",1,AUTHORITY[\"EPSG\",\"9001\"]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"latitude_of_origin\",0],PARAMETER[\"central_meridian\",-99],PARAMETER[\"scale_factor\",0.9996],PARAMETER[\"false_easting\",500000],PARAMETER[\"false_northing\",0],AUTHORITY[\"EPSG\",\"32614\"],AXIS[\"Easting\",EAST],AXIS[\"Northing\",NORTH]]",
    "proj:projjson": {
      "$schema": "https://proj.org/schemas/v0.2/projjson.schema.json",
      "type": "ProjectedCRS",
      "name": "WGS 84 / UTM zone 14N",
      "base_crs": {
        "name": "WGS 84",
        "datum": {
          "type": "GeodeticReferenceFrame",
          "name": "World Geodetic System 1984",
          "ellipsoid": {
            "name": "WGS 84",
            "semi_major_axis": 6378137,
            "inverse_flattening": 298.257223563
          }
        },
        "coordinate_system": {
          "subtype": "ellipsoidal",
          "axis": [
            {
              "name": "Geodetic latitude",
              "abbreviation": "Lat",
              "direction": "north",
              "unit": "degree"
            },
            {
              "name": "Geodetic longitude",
              "abbreviation": "Lon",
              "direction": "east",
              "unit": "degree"
            }
          ]
        },
        "id": {
          "authority": "EPSG",
          "code": 4326
        }
      },
      "conversion": {
        "name": "UTM zone 14N",
        "method": {
          "name": "Transverse Mercator",
          "id": {
            "authority": "EPSG",
            "code": 9807
          }
        },
        "parameters": [
          {
            "name": "Latitude of natural origin",
            "value": 0,
            "unit": "degree",
            "id": {
              "authority": "EPSG",
              "code": 8801
            }
          },
          {
            "name": "Longitude of natural origin",
            "value": -99,
            "unit": "degree",
            "id": {
              "authority": "EPSG",
              "code": 8802
            }
          },
          {
            "name": "Scale factor at natural origin",
            "value": 0.9996,
            "unit": "unity",
            "id": {
              "authority": "EPSG",
              "code": 8805
            }
          },
          {
            "name": "False easting",
            "value": 500000,
            "unit": "metre",
            "id": {
              "authority": "EPSG",
              "code": 8806
            }
          },
          {
            "name": "False northing",
            "value": 0,
            "unit": "metre",
            "id": {
              "authority": "EPSG",
              "code": 8807
            }
          }
        ]
      },
      "coordinate_system": {
        "subtype": "Cartesian",
        "axis": [
          {
            "name": "Easting",
            "abbreviation": "E",
            "direction": "east",
            "unit": "metre"
          },
          {
            "name": "Northing",
            "abbreviation": "N",
            "direction": "north",
            "unit": "metre"
          }
        ]
      },
      "area": "World - N hemisphere - 102\u00b0W to 96\u00b0W - by country",
      "bbox": {
        "south_latitude": 0,
        "west_longitude": -102,
        "north_latitude": 84,
        "east_longitude": -96
      },
      "id": {
        "authority": "EPSG",
        "code": 32614
      }
    },
    "proj:geometry": {
      "coordinates": [
        [
          [
            169200,
            3712800
          ],
          [
            403200,
            3712800
          ],
          [
            403200,
            3951000
          ],
          [
            169200,
            3951000
          ],
          [
            169200,
            3712800
          ]
        ]
      ],
      "type": "Polygon"
    },
    "proj:bbox": [
      169200,
      3712800,
      403200,
      3951000
    ],
    "proj:centroid": {
      "lat": 34.595302781575604,
      "lon": -101.34448382627504
    },
    "proj:shape": [
      8391,
      8311
    ],
    "proj:transform": [
      30,
      0,
      224985,
      0,
      -30,
      6790215,
      0,
      0,
      1
    ]
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          152.52758,
          60.63437
        ],
        [
          149.1755,
          61.19016
        ],
        [
          148.13933,
          59.51584
        ],
        [
          151.33786,
          58.97792
        ],
        [
          152.52758,
          60.63437
        ]
      ]
    ]
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Example Catalog"
    },
    {
      "rel": "parent",
      "href": "../collection.json",
      "type": "application/json",
      "title": "Collection of Extension Items"
    },
    {
      "rel": "collection",
      "href": "../collection.json",
      "type": "application/json",
      "title": "Collection of Extension Items"
    }
  ],
  "assets": {
    "B1": {
      "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/107/018/LC08_L1TP_107018_20181001_20181001_01_RT/LC08_L1TP_107018_20181001_20181001_01_RT_B1.TIF",
      "type": "image/tiff; application=geotiff",
      "title": "Band 1 (coastal)",
      "eo:bands": [
        {
          "name": "B1",
          "common_name": "coastal",
          "center_wavelength": 0.44,
          "full_width_half_max": 0.02
        }
      ]
    },
    "B8": {
      "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/107/018/LC08_L1TP_107018_20181001_20181001_01_RT/LC08_L1TP_107018_20181001_20181001_01_RT_B8.TIF",
      "type": "image/tiff; application=geotiff",
      "title": "Band 8 (panchromatic)",
      "eo:bands": [
        {
          "name": "B8",
          "center_wavelength": 0.59,
          "full_width_half_max": 0.18
        }
      ],
      "proj:shape": [
        16781,
        16621
      ],
      "proj:transform": [
        15,
        0,
        224992.5,
        0,
        -15,
        6790207.5,
        0,
        0,
        1
      ]
    }
  },
  "bbox": [
    148.13933,
    59.51584,
    152.52758,
    60.63437
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json"
  ],
  "collection": "landsat-8-l1",
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld"
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <proj:> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/raster/example-1/proj-example> a geojson:Feature ;
    geojson:bbox ( 1.481393e+02 5.951584e+01 1.525276e+02 6.063437e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.525276e+02 6.063437e+01 ) ( 1.491755e+02 6.119016e+01 ) ( 1.481393e+02 5.951584e+01 ) ( 1.513379e+02 5.897792e+01 ) ( 1.525276e+02 6.063437e+01 ) ) ) ] ;
    ns1:bbox 169200,
        403200,
        3712800,
        3951000 ;
    ns1:centroid [ ] ;
    ns1:epsg 32614 ;
    ns1:geometry [ a geojson:Polygon ] ;
    ns1:projjson [ a <https://example.com/stac/raster/example-1/ProjectedCRS> ;
            geojson:bbox ( [ ] ) ] ;
    ns1:shape 8311,
        8391 ;
    ns1:transform -30,
        0,
        1,
        30,
        224985,
        6790215 ;
    ns1:wkt2 "PROJCS[\"WGS 84 / UTM zone 14N\",GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.01745329251994328,AUTHORITY[\"EPSG\",\"9122\"]],AUTHORITY[\"EPSG\",\"4326\"]],UNIT[\"metre\",1,AUTHORITY[\"EPSG\",\"9001\"]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"latitude_of_origin\",0],PARAMETER[\"central_meridian\",-99],PARAMETER[\"scale_factor\",0.9996],PARAMETER[\"false_easting\",500000],PARAMETER[\"false_northing\",0],AUTHORITY[\"EPSG\",\"32614\"],AXIS[\"Easting\",EAST],AXIS[\"Northing\",NORTH]]" .


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
- $ref: https://stac-extensions.github.io/raster/v1.1.0/schema.json

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.yaml)


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
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/eo)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/eo`

