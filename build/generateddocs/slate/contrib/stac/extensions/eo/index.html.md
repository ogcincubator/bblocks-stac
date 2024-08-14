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

<aside class="success">
This building block is <strong><a href="https://github.com/ogcincubator/bblocks-stac/blob/master/build/tests/contrib/stac/extensions/eo/" target="_blank">valid</a></strong>
</aside>

# Examples

## A simple Collection demonstrating EO extension fields in a Collection.



```json
{
  "id": "eo-collection",
  "type": "Collection",
  "stac_extensions": [
    "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json",
    "https://stac-extensions.github.io/eo/v2.0.0-beta.1/schema.json"
  ],
  "stac_version": "1.1.0-beta.1",
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

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/eo/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fextensions%2Feo%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "id": "eo-collection",
  "type": "Collection",
  "stac_extensions": [
    "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json",
    "https://stac-extensions.github.io/eo/v2.0.0-beta.1/schema.json"
  ],
  "stac_version": "1.1.0-beta.1",
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
  ],
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
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<https://example.com/stac/eo/example-1/eo-collection> a <https://example.com/stac/eo/example-1/Collection> ;
    rdfs:label "Simple EO Collection" ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/eo/example-1/collection.json> ],
        [ rdfs:label "20201211_223832_CS2" ;
            dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/eo/example-1/item.json> ] .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/eo/example_1_1.ttl">Open in new window</a>
</blockquote>



## An example demonstrating EO extension fields in a STAC item.



```json
{
  "stac_version": "1.1.0-beta.1",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0-beta.1/schema.json"
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

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/eo/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fextensions%2Feo%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "stac_version": "1.1.0-beta.1",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0-beta.1/schema.json"
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
  ],
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/eo/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fextensions%2Feo%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
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
    dcterms:modified "2020-12-12T01:48:13.725Z" ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/eo/example-2/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/eo/example-2/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/eo/example-2/collection.json> ] ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729117e+02 1.343885e+00 ) ( 1.729547e+02 1.343885e+00 ) ( 1.729547e+02 1.369048e+00 ) ( 1.729117e+02 1.369048e+00 ) ( 1.729117e+02 1.343885e+00 ) ) ) ] ;
    stac:assets <https://example.com/stac/eo/example-2/analytic>,
        <https://example.com/stac/eo/example-2/thumbnail>,
        <https://example.com/stac/eo/example-2/visual> ;
    eo:cloud_cover 1.2e+00 ;
    eo:snow_cover 0 .

<https://example.com/stac/eo/example-2/analytic> rdfs:label "4-Band Analytic" ;
    oa:hasTarget <https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif> ;
    eo:cloud_cover 1.2e+00 .

<https://example.com/stac/eo/example-2/thumbnail> a <https://example.com/stac/eo/example-2/image/png> ;
    rdfs:label "Thumbnail" ;
    oa:hasTarget <https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg> .

<https://example.com/stac/eo/example-2/visual> rdfs:label "3-Band Visual" ;
    oa:hasTarget <https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif> .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/extensions/eo/example_2_1.ttl">Open in new window</a>
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
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-v1-0-0/schema.yaml
- $ref: https://stac-extensions.github.io/eo/v2.0.0-beta.1/schema.json
x-jsonld-extra-terms:
  eo:bands:
    x-jsonld-id: https://w3id.org/ogc/stac/eo/bands
    x-jsonld-context:
      '@vocab': https://w3id.org/ogc/stac/eo/
x-jsonld-prefixes:
  eo: https://w3id.org/ogc/stac/eo/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fextensions%2Feo%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.yaml" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.json" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/eo/schema.json</a>


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
    "eo:bands": {
      "@id": "eo:bands",
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/eo/"
      }
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "eo": "https://w3id.org/ogc/stac/eo/",
    "geojson": "https://purl.org/geojson/vocab#",
    "stac": "https://w3id.org/ogc/stac/core/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
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

