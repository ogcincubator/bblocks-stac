
# STAC Electro-Optical Extension (Schema)

`ogc.contrib.stac.extensions.eo` *v0.1*

Electro-Optical (EO) Extension to the SpatioTemporal Asset Catalog (STAC) specification.

EO data is considered to be data that represents a snapshot of the Earth for a single date and time. It could consist of multiple spectral bands in any part of the electromagnetic spectrum. Examples of EO data include sensors with visible, short-wave and mid-wave IR bands (e.g., the OLI instrument on Landsat-8), long-wave IR bands (e.g. TIRS aboard Landsat-8).

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### A simple Collection demonstrating EO extension fields in a Collection.
#### json
```json
{
  "id": "eo-collection",
  "type": "Collection",
  "stac_extensions": [
    "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json"
  ],
  "stac_version": "1.0.0",
  "description": "A simple Collection demonstrating EO extension fields in a Collection.",
  "title": "Simple EO Collection",
  "extent": {
    "spatial": {
      "bbox": [
        [
          172.91173669923782,
          1.3438851951615003,
          172.95469614953714,
          1.3690476620161975
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2020-12-11T22:38:32.125Z",
          "2020-12-14T18:02:31.437Z"
        ]
      ]
    }
  },
  "license": "CC-BY-4.0",
  "summaries": {
    "platform": [
      "cool_sat1",
      "cool_sat2"
    ],
    "constellation": [
      "ion"
    ],
    "instruments": [
      "cool_sensor_v1",
      "cool_sensor_v2"
    ],
    "eo:cloud_cover": {
      "minimum": 0,
      "maximum": 50
    },
    "eo:bands": [
      {
        "name": "band1",
        "common_name": "blue",
        "center_wavelength": 0.47,
        "full_width_half_max": 0.07,
        "solar_illumination": 1959.66
      },
      {
        "name": "band2",
        "common_name": "green",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.08,
        "solar_illumination": 1823.24
      },
      {
        "name": "band3",
        "common_name": "red",
        "center_wavelength": 0.645,
        "full_width_half_max": 0.09,
        "solar_illumination": 1512.06
      },
      {
        "name": "band4",
        "common_name": "nir",
        "center_wavelength": 0.8,
        "full_width_half_max": 0.152,
        "solar_illumination": 1041.63
      }
    ]
  },
  "links": [
    {
      "rel": "root",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
    {
      "rel": "item",
      "href": "./item.json",
      "type": "application/geo+json",
      "title": "20201211_223832_CS2"
    }
  ],
  "item_assets": {
    "analytic": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
      ],
      "eo:bands": [
        {
          "name": "band1",
          "common_name": "blue",
          "center_wavelength": 0.47,
          "full_width_half_max": 0.7,
          "solar_illumination": 1959.66
        },
        {
          "name": "band2",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.08,
          "solar_illumination": 1823.24
        },
        {
          "name": "band3",
          "common_name": "red",
          "center_wavelength": 0.645,
          "full_width_half_max": 0.9,
          "solar_illumination": 1512.06
        },
        {
          "name": "band4",
          "common_name": "nir",
          "center_wavelength": 0.8,
          "full_width_half_max": 0.152,
          "solar_illumination": 1041.63
        }
      ]
    },
    "thumbnail": {
      "title": "Thumbnail",
      "type": "image/png",
      "roles": [
        "thumbnail"
      ]
    },
    "visual": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ],
      "eo:bands": [
        {
          "name": "band3",
          "common_name": "red",
          "center_wavelength": 0.645,
          "full_width_half_max": 0.09
        },
        {
          "name": "band2",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.08
        },
        {
          "name": "band1",
          "common_name": "blue",
          "center_wavelength": 0.47,
          "full_width_half_max": 0.07
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "id": "eo-collection",
  "type": "Collection",
  "stac_extensions": [
    "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json"
  ],
  "stac_version": "1.0.0",
  "description": "A simple Collection demonstrating EO extension fields in a Collection.",
  "title": "Simple EO Collection",
  "extent": {
    "spatial": {
      "bbox": [
        [
          172.91173669923782,
          1.3438851951615003,
          172.95469614953714,
          1.3690476620161975
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2020-12-11T22:38:32.125Z",
          "2020-12-14T18:02:31.437Z"
        ]
      ]
    }
  },
  "license": "CC-BY-4.0",
  "summaries": {
    "platform": [
      "cool_sat1",
      "cool_sat2"
    ],
    "constellation": [
      "ion"
    ],
    "instruments": [
      "cool_sensor_v1",
      "cool_sensor_v2"
    ],
    "eo:cloud_cover": {
      "minimum": 0,
      "maximum": 50
    },
    "eo:bands": [
      {
        "name": "band1",
        "common_name": "blue",
        "center_wavelength": 0.47,
        "full_width_half_max": 0.07,
        "solar_illumination": 1959.66
      },
      {
        "name": "band2",
        "common_name": "green",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.08,
        "solar_illumination": 1823.24
      },
      {
        "name": "band3",
        "common_name": "red",
        "center_wavelength": 0.645,
        "full_width_half_max": 0.09,
        "solar_illumination": 1512.06
      },
      {
        "name": "band4",
        "common_name": "nir",
        "center_wavelength": 0.8,
        "full_width_half_max": 0.152,
        "solar_illumination": 1041.63
      }
    ]
  },
  "links": [
    {
      "rel": "root",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
    {
      "rel": "item",
      "href": "./item.json",
      "type": "application/geo+json",
      "title": "20201211_223832_CS2"
    }
  ],
  "item_assets": {
    "analytic": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
      ],
      "eo:bands": [
        {
          "name": "band1",
          "common_name": "blue",
          "center_wavelength": 0.47,
          "full_width_half_max": 0.7,
          "solar_illumination": 1959.66
        },
        {
          "name": "band2",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.08,
          "solar_illumination": 1823.24
        },
        {
          "name": "band3",
          "common_name": "red",
          "center_wavelength": 0.645,
          "full_width_half_max": 0.9,
          "solar_illumination": 1512.06
        },
        {
          "name": "band4",
          "common_name": "nir",
          "center_wavelength": 0.8,
          "full_width_half_max": 0.152,
          "solar_illumination": 1041.63
        }
      ]
    },
    "thumbnail": {
      "title": "Thumbnail",
      "type": "image/png",
      "roles": [
        "thumbnail"
      ]
    },
    "visual": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ],
      "eo:bands": [
        {
          "name": "band3",
          "common_name": "red",
          "center_wavelength": 0.645,
          "full_width_half_max": 0.09
        },
        {
          "name": "band2",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.08
        },
        {
          "name": "band1",
          "common_name": "blue",
          "center_wavelength": 0.47,
          "full_width_half_max": 0.07
        }
      ]
    }
  },
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<https://example.com/stac/raster/example-1/eo-collection> a <https://example.com/stac/raster/example-1/Collection> ;
    rdfs:label "Simple EO Collection" ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/raster/example-1/collection.json> ],
        [ rdfs:label "20201211_223832_CS2" ;
            dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/raster/example-1/item.json> ] .


```


### An example demonstrating EO extension fields in a STAC item.
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "bbox": [
    172.91173669923782,
    1.3438851951615003,
    172.95469614953714,
    1.3690476620161975
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          172.91173669923782,
          1.3438851951615003
        ],
        [
          172.95469614953714,
          1.3438851951615003
        ],
        [
          172.95469614953714,
          1.3690476620161975
        ],
        [
          172.91173669923782,
          1.3690476620161975
        ],
        [
          172.91173669923782,
          1.3438851951615003
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32.125Z",
    "created": "2020-12-12T01:48:13.725Z",
    "updated": "2020-12-12T01:48:13.725Z",
    "platform": "cool_sat2",
    "instruments": [
      "cool_sensor_v1"
    ],
    "gsd": 0.66,
    "eo:cloud_cover": 1.2,
    "eo:snow_cover": 0
  },
  "collection": "eo-collection",
  "links": [
    {
      "rel": "root",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
    {
      "rel": "parent",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    }
  ],
  "assets": {
    "analytic": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
      ],
      "eo:bands": [
        {
          "name": "band1",
          "common_name": "blue",
          "center_wavelength": 0.47,
          "full_width_half_max": 0.07,
          "solar_illumination": 1959.66
        },
        {
          "name": "band2",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.08,
          "solar_illumination": 1823.24
        },
        {
          "name": "band3",
          "common_name": "red",
          "center_wavelength": 0.645,
          "full_width_half_max": 0.09,
          "solar_illumination": 1512.06
        },
        {
          "name": "band4",
          "common_name": "nir",
          "center_wavelength": 0.8,
          "full_width_half_max": 0.152,
          "solar_illumination": 1041.63
        }
      ]
    },
    "thumbnail": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg",
      "title": "Thumbnail",
      "type": "image/png",
      "roles": [
        "thumbnail"
      ]
    },
    "visual": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ],
      "eo:bands": [
        {
          "name": "band3",
          "common_name": "red",
          "center_wavelength": 0.645,
          "full_width_half_max": 0.09
        },
        {
          "name": "band2",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.08
        },
        {
          "name": "band1",
          "common_name": "blue",
          "center_wavelength": 0.47,
          "full_width_half_max": 0.07
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "bbox": [
    172.91173669923782,
    1.3438851951615003,
    172.95469614953714,
    1.3690476620161975
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          172.91173669923782,
          1.3438851951615003
        ],
        [
          172.95469614953714,
          1.3438851951615003
        ],
        [
          172.95469614953714,
          1.3690476620161975
        ],
        [
          172.91173669923782,
          1.3690476620161975
        ],
        [
          172.91173669923782,
          1.3438851951615003
        ]
      ]
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32.125Z",
    "created": "2020-12-12T01:48:13.725Z",
    "updated": "2020-12-12T01:48:13.725Z",
    "platform": "cool_sat2",
    "instruments": [
      "cool_sensor_v1"
    ],
    "gsd": 0.66,
    "eo:cloud_cover": 1.2,
    "eo:snow_cover": 0
  },
  "collection": "eo-collection",
  "links": [
    {
      "rel": "root",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
    {
      "rel": "parent",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    }
  ],
  "assets": {
    "analytic": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
      ],
      "eo:bands": [
        {
          "name": "band1",
          "common_name": "blue",
          "center_wavelength": 0.47,
          "full_width_half_max": 0.07,
          "solar_illumination": 1959.66
        },
        {
          "name": "band2",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.08,
          "solar_illumination": 1823.24
        },
        {
          "name": "band3",
          "common_name": "red",
          "center_wavelength": 0.645,
          "full_width_half_max": 0.09,
          "solar_illumination": 1512.06
        },
        {
          "name": "band4",
          "common_name": "nir",
          "center_wavelength": 0.8,
          "full_width_half_max": 0.152,
          "solar_illumination": 1041.63
        }
      ]
    },
    "thumbnail": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg",
      "title": "Thumbnail",
      "type": "image/png",
      "roles": [
        "thumbnail"
      ]
    },
    "visual": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ],
      "eo:bands": [
        {
          "name": "band3",
          "common_name": "red",
          "center_wavelength": 0.645,
          "full_width_half_max": 0.09
        },
        {
          "name": "band2",
          "common_name": "green",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.08
        },
        {
          "name": "band1",
          "common_name": "blue",
          "center_wavelength": 0.47,
          "full_width_half_max": 0.07
        }
      ]
    }
  },
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <eo:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/raster/example-1/20201211_223832_CS2> a geojson:Feature ;
    ns2:cloud_cover 1.2e+00 ;
    ns2:snow_cover 0 ;
    dcterms:created "2020-12-12T01:48:13.725Z" ;
    dcterms:modified "2020-12-12T01:48:13.725Z" ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/raster/example-1/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/raster/example-1/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/raster/example-1/collection.json> ] ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729117e+02 1.343885e+00 ) ( 1.729547e+02 1.343885e+00 ) ( 1.729547e+02 1.369048e+00 ) ( 1.729117e+02 1.369048e+00 ) ( 1.729117e+02 1.343885e+00 ) ) ) ] .


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
- $ref: https://stac-extensions.github.io/eo/v1.1.0/schema.json

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
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "geojson": "https://purl.org/geojson/vocab#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
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

