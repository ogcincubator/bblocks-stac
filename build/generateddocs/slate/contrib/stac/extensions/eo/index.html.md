---
title: STAC Electro-Optical Extension (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>STAC Electro-Optical Extension</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: STAC Electro-Optical Extension (Schema)
---


# STAC Electro-Optical Extension `ogc.contrib.stac.extensions.eo`

Electro-Optical (EO) Extension to the SpatioTemporal Asset Catalog (STAC) specification.

EO data is considered to be data that represents a snapshot of the Earth for a single date and time. It could consist of multiple spectral bands in any part of the electromagnetic spectrum. Examples of EO data include sensors with visible, short-wave and mid-wave IR bands (e.g., the OLI instrument on Landsat-8), long-wave IR bands (e.g. TIRS aboard Landsat-8).

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="warning">
Validation for this building block has <strong><a href="https://github.com/ogcincubator/bblocks-stac/blob/master/build/tests/contrib/stac/extensions/eo/" target="_blank">failed</a></strong>
</aside>

# Examples

## Example of Electro-Optical using projection extension



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

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/eo/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fextensions%2Feo%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




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

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/eo/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fextensions%2Feo%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <proj:> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/raster/example-1/proj-example> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Collection of Extension Items" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/raster/collection.json> ],
        [ rdfs:label "Example Catalog" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/catalog.json> ],
        [ rdfs:label "Collection of Extension Items" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/raster/collection.json> ] ;
    geojson:bbox ( 1.481393e+02 5.951584e+01 1.525276e+02 6.063437e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.525276e+02 6.063437e+01 ) ( 1.491755e+02 6.119016e+01 ) ( 1.481393e+02 5.951584e+01 ) ( 1.513379e+02 5.897792e+01 ) ( 1.525276e+02 6.063437e+01 ) ) ) ] ;
    ns1:bbox 169200,
        403200,
        3712800,
        3951000 ;
    ns1:centroid [ ] ;
    ns1:epsg 32614 ;
    ns1:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 169200 3712800 ) ( 403200 3712800 ) ( 403200 3951000 ) ( 169200 3951000 ) ( 169200 3712800 ) ) ) ] ;
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

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/eo/example_1_1.ttl">Open in new window</a>
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
- $ref: https://stac-extensions.github.io/eo/v1.1.0/schema.json

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fextensions%2Feo%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.yaml" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.json" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
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
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {},
      "@id": "geojson:geometry"
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
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fextensions%2Feo%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld</a>

# References

* [GitHub Repository](https://github.com/stac-extensions/eo)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/bblocks-stac" target="_blank">https://github.com/ogcincubator/bblocks-stac</a>
* Path:
<code><a href="https://github.com/ogcincubator/bblocks-stac/blob/HEAD/_sources/extensions/eo" target="_blank">_sources/extensions/eo</a></code>

