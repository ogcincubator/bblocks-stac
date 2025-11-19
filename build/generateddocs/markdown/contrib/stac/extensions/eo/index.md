
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
    "https://stac-extensions.github.io/eo/v2.0.0/schema.json"
  ],
  "stac_version": "1.1.0",
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
    "bands": [
      {
        "name": "band1",
        "eo:common_name": "blue",
        "eo:center_wavelength": 0.47,
        "eo:full_width_half_max": 0.07,
        "eo:solar_illumination": 1959.66
      },
      {
        "name": "band2",
        "eo:common_name": "green",
        "eo:center_wavelength": 0.56,
        "eo:full_width_half_max": 0.08,
        "eo:solar_illumination": 1823.24
      },
      {
        "name": "band3",
        "eo:common_name": "red",
        "eo:center_wavelength": 0.645,
        "eo:full_width_half_max": 0.09,
        "eo:solar_illumination": 1512.06
      },
      {
        "name": "band4",
        "eo:common_name": "nir",
        "eo:center_wavelength": 0.8,
        "eo:full_width_half_max": 0.152,
        "eo:solar_illumination": 1041.63
      }
    ]
  },
  "item_assets": {
    "analytic": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
      ],
      "bands": [
        {
          "name": "band1",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.47,
          "eo:full_width_half_max": 0.7,
          "eo:solar_illumination": 1959.66
        },
        {
          "name": "band2",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.08,
          "eo:solar_illumination": 1823.24
        },
        {
          "name": "band3",
          "common_name": "red",
          "eo:center_wavelength": 0.645,
          "eo:full_width_half_max": 0.9,
          "eo:solar_illumination": 1512.06
        },
        {
          "name": "band4",
          "eo:common_name": "nir",
          "eo:center_wavelength": 0.8,
          "eo:full_width_half_max": 0.152,
          "eo:solar_illumination": 1041.63
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
      "bands": [
        {
          "name": "band3",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.645,
          "eo:full_width_half_max": 0.09
        },
        {
          "name": "band2",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.08
        },
        {
          "name": "band1",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.47,
          "eo:full_width_half_max": 0.07
        }
      ]
    }
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
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld",
  "id": "eo-collection",
  "type": "Collection",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0/schema.json"
  ],
  "stac_version": "1.1.0",
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
    "bands": [
      {
        "name": "band1",
        "eo:common_name": "blue",
        "eo:center_wavelength": 0.47,
        "eo:full_width_half_max": 0.07,
        "eo:solar_illumination": 1959.66
      },
      {
        "name": "band2",
        "eo:common_name": "green",
        "eo:center_wavelength": 0.56,
        "eo:full_width_half_max": 0.08,
        "eo:solar_illumination": 1823.24
      },
      {
        "name": "band3",
        "eo:common_name": "red",
        "eo:center_wavelength": 0.645,
        "eo:full_width_half_max": 0.09,
        "eo:solar_illumination": 1512.06
      },
      {
        "name": "band4",
        "eo:common_name": "nir",
        "eo:center_wavelength": 0.8,
        "eo:full_width_half_max": 0.152,
        "eo:solar_illumination": 1041.63
      }
    ]
  },
  "item_assets": {
    "analytic": {
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
      ],
      "bands": [
        {
          "name": "band1",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.47,
          "eo:full_width_half_max": 0.7,
          "eo:solar_illumination": 1959.66
        },
        {
          "name": "band2",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.08,
          "eo:solar_illumination": 1823.24
        },
        {
          "name": "band3",
          "common_name": "red",
          "eo:center_wavelength": 0.645,
          "eo:full_width_half_max": 0.9,
          "eo:solar_illumination": 1512.06
        },
        {
          "name": "band4",
          "eo:common_name": "nir",
          "eo:center_wavelength": 0.8,
          "eo:full_width_half_max": 0.152,
          "eo:solar_illumination": 1041.63
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
      "bands": [
        {
          "name": "band3",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.645,
          "eo:full_width_half_max": 0.09
        },
        {
          "name": "band2",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.08
        },
        {
          "name": "band1",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.47,
          "eo:full_width_half_max": 0.07
        }
      ]
    }
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

<https://example.com/stac/eo/example-1/eo-collection> a <https://example.com/stac/eo/example-1/Collection> ;
    dcterms:description "A simple Collection demonstrating EO extension fields in a Collection." ;
    dcterms:extent [ ] ;
    dcterms:title "Simple EO Collection" ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:format "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/eo/example-1/collection.json> ],
        [ rdfs:label "20201211_223832_CS2" ;
            dcterms:format "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/eo/example-1/item.json> ] ;
    dcat:license "CC-BY-4.0" ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v2.0.0/schema.json" ;
    stac:version "1.1.0" .


```


### An example demonstrating EO extension fields in a STAC item.
#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "collection": "eo-collection",
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
  "assets": {
    "analytic": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
      ],
      "eo:cloud_cover": 1.2,
      "bands": [
        {
          "name": "band1",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.47,
          "eo:full_width_half_max": 0.07,
          "eo:solar_illumination": 1959.66
        },
        {
          "name": "band2",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.08,
          "eo:solar_illumination": 1823.24
        },
        {
          "name": "band3",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.645,
          "eo:full_width_half_max": 0.09,
          "eo:solar_illumination": 1512.06
        },
        {
          "name": "band4",
          "eo:common_name": "nir",
          "eo:center_wavelength": 0.8,
          "eo:full_width_half_max": 0.152,
          "eo:solar_illumination": 1041.63
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
      "bands": [
        {
          "name": "band3",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.645,
          "eo:full_width_half_max": 0.09
        },
        {
          "name": "band2",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.08
        },
        {
          "name": "band1",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.47,
          "eo:full_width_half_max": 0.07
        }
      ]
    }
  },
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
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "collection": "eo-collection",
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
  "assets": {
    "analytic": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
      ],
      "eo:cloud_cover": 1.2,
      "bands": [
        {
          "name": "band1",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.47,
          "eo:full_width_half_max": 0.07,
          "eo:solar_illumination": 1959.66
        },
        {
          "name": "band2",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.08,
          "eo:solar_illumination": 1823.24
        },
        {
          "name": "band3",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.645,
          "eo:full_width_half_max": 0.09,
          "eo:solar_illumination": 1512.06
        },
        {
          "name": "band4",
          "eo:common_name": "nir",
          "eo:center_wavelength": 0.8,
          "eo:full_width_half_max": 0.152,
          "eo:solar_illumination": 1041.63
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
      "bands": [
        {
          "name": "band3",
          "eo:common_name": "red",
          "eo:center_wavelength": 0.645,
          "eo:full_width_half_max": 0.09
        },
        {
          "name": "band2",
          "eo:common_name": "green",
          "eo:center_wavelength": 0.56,
          "eo:full_width_half_max": 0.08
        },
        {
          "name": "band1",
          "eo:common_name": "blue",
          "eo:center_wavelength": 0.47,
          "eo:full_width_half_max": 0.07
        }
      ]
    }
  },
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
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix eo: <https://w3id.org/ogc/stac/eo/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/eo/example-2/20201211_223832_CS2> a geojson:Feature ;
    dcterms:created "2020-12-12T01:48:13.725Z" ;
    dcterms:date "2020-12-11T22:38:32.125000+00:00"^^xsd:dateTime ;
    dcterms:modified "2020-12-12T01:48:13.725Z" ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:format "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/eo/example-2/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:format "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/eo/example-2/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:format "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/eo/example-2/collection.json> ] ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729117e+02 1.343885e+00 ) ( 1.729547e+02 1.343885e+00 ) ( 1.729547e+02 1.369048e+00 ) ( 1.729117e+02 1.369048e+00 ) ( 1.729117e+02 1.343885e+00 ) ) ) ] ;
    stac:assets <https://example.com/stac/eo/example-2/analytic>,
        <https://example.com/stac/eo/example-2/thumbnail>,
        <https://example.com/stac/eo/example-2/visual> ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v2.0.0/schema.json" ;
    stac:version "1.1.0" ;
    eo:cloud_cover 1.2e+00 ;
    eo:snow_cover 0 .

<https://example.com/stac/eo/example-2/analytic> dcterms:format "image/tiff; application=geotiff; profile=cloud-optimized" ;
    dcterms:title "4-Band Analytic" ;
    oa:hasTarget <https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif> ;
    stac:roles "data" ;
    eo:cloud_cover 1.2e+00 .

<https://example.com/stac/eo/example-2/thumbnail> dcterms:format "image/png" ;
    dcterms:title "Thumbnail" ;
    oa:hasTarget <https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg> ;
    stac:roles "thumbnail" .

<https://example.com/stac/eo/example-2/visual> dcterms:format "image/tiff; application=geotiff; profile=cloud-optimized" ;
    dcterms:title "3-Band Visual" ;
    oa:hasTarget <https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif> ;
    stac:roles "visual" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Electro-Optical Extension
description: STAC Electro-Optical Extension for STAC Items and STAC Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-v1-0-0/schema.yaml
- $ref: https://stac-extensions.github.io/eo/v2.0.0/schema.json
x-jsonld-extra-terms:
  eo:bands:
    x-jsonld-id: https://w3id.org/ogc/stac/eo/bands
    x-jsonld-context:
      '@vocab': https://w3id.org/ogc/stac/eo/
x-jsonld-prefixes:
  eo: https://w3id.org/ogc/stac/eo/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "links": {
      "@context": {
        "type": "dct:format",
        "title": "rdfs:label"
      },
      "@id": "rdfs:seeAlso"
    },
    "stac_version": "stac:version",
    "stac_extensions": "stac:hasExtension",
    "id": "@id",
    "type": "@type",
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
    "license": "dcat:license",
    "extent": "dct:extent",
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
    "assets": {
      "@id": "stac:assets",
      "@container": "@id",
      "@context": {
        "thumbnail": "stac:thumbnail",
        "overview": "stac:overview",
        "data": "stac:data",
        "metadata": "stac:metadata",
        "type": "dct:format",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      }
    },
    "providers": "stac:hasProvider",
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
    "geometry": "geojson:geometry",
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
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "created": "dct:created",
    "updated": "dct:modified",
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
      "@container": "@set",
      "@id": "rec:themes"
    },
    "formats": {
      "@container": "@set",
      "@id": "rec:format",
      "@type": "@id"
    },
    "contacts": {
      "@context": {
        "type": "dct:type",
        "title": "rdfs:label"
      },
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "rights": "dcat:rights",
    "linkTemplates": {
      "@context": {
        "type": "dct:format",
        "title": "rdfs:label",
        "uriTemplate": {
          "@type": "xsd:string",
          "@id": "rec:uriTemplate"
        },
        "varBase": "rec:varBase",
        "variables": {
          "@id": "rec:hasVariable",
          "@container": "@index",
          "@index": "dct:identifier",
          "@type": "@json"
        }
      },
      "@id": "rec:hasLinkTemplate"
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
    "length": "dct:extent",
    "eo:bands": {
      "@id": "eo:bands",
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/eo/"
      }
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "eo": "https://w3id.org/ogc/stac/eo/",
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

