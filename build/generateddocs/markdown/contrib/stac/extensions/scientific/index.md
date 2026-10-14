
# STAC Scientific Citation Extension (Schema)

`ogc.contrib.stac.extensions.scientific` *v1.0.0*

STAC Scientific Citation Extension for Items, Collections and Assets.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Scientific Citation item
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "id": "MERRAclim.2_5m_min_80s",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180,
          -90
        ],
        [
          180,
          -90
        ],
        [
          180,
          90
        ],
        [
          -180,
          90
        ],
        [
          -180,
          -90
        ]
      ]
    ]
  },
  "bbox": [
    -180,
    -90,
    180,
    90
  ],
  "properties": {
    "title": "MERRAclim. 2_5m_min_80s",
    "description": "MERRAclim Dataset. 19 global bioclimatic variables from the 1980s decade at 2.5 arcminutes resolution in GEOtiff format. The humidity version used is the min. The variables have been built using the same protocol as WorldClim with data from MERRA. Temperature layers (BIO1-BIO11) are in degree Celsius multiplied by 10, humidity layers (BIO12-BIO19) are in kg of water/kg of air multiplied by 100000.",
    "datetime": "1985-07-01T00:00:00Z",
    "start_datetime": "1980-01-01T00:00:00Z",
    "end_datetime": "1989-12-31T23:59:59Z",
    "sci:doi": "10.5061/dryad.s2v81.2/27.2",
    "sci:publications": [
      {
        "doi": "10.5061/dryad.s2v81.2",
        "citation": "Vega GC, Pertierra LR, Olalla-Tárraga MÁ (2017) Data from: MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Dryad Digital Repository."
      },
      {
        "doi": "10.1038/sdata.2017.78",
        "citation": "Vega GC, Pertierra LR, Olalla-Tárraga MÁ (2017) MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Scientific Data 4: 170078."
      }
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/item.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/catalog.json"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.5061/dryad.s2v81.2/27.2"
    }
  ],
  "assets": {
    "primary": {
      "href": "https://datadryad.org/stash/downloads/file_stream/100467",
      "type": "application/zip",
      "title": "MERRAclim. 2_5m_min_80s"
    }
  }
}

```

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "id": "MERRAclim",
  "title": "MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling.",
  "description": "Species Distribution Models (SDMs) combine information on the geographic occurrence of species with environmental layers to estimate distributional ranges and have been extensively implemented to answer a wide array of applied ecological questions. Unfortunately, most global datasets available to parameterize SDMs consist of spatially interpolated climate surfaces obtained from ground weather station data and have omitted the Antarctic continent, a landmass covering c. 20% of the Southern Hemisphere and increasingly showing biological effects of global change. Here we introduce MERRAclim, a global set of satellite-based bioclimatic variables including Antarctica for the first time. MERRAclim consists of three datasets of 19 bioclimatic variables that have been built for each of the last three decades (1980s, 1990s and 2000s) using hourly data of 2 m temperature and specific humidity. We provide MERRAclim at three spatial resolutions (10 arc-minutes, 5 arc-minutes and 2.5 arc-minutes). These reanalysed data are comparable to widely used datasets based on ground station interpolations, but allow extending their geographical reach and SDM building in previously uncovered regions of the globe.",
  "type": "Collection",
  "keywords": [
    "bioclimatic",
    "MERRAclim",
    "macroecology",
    "biogeography"
  ],
  "license": "CC0-1.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -180,
          -90,
          180,
          90
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1980-01-01T00:00:00Z",
          "2009-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "sci:doi": "10.5061/dryad.s2v81.2",
  "sci:citation": "Vega GC, Pertierra LR, Olalla-Tárraga MÁ (2017) Data from: MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Dryad Digital Repository.",
  "sci:publications": [
    {
      "doi": "10.1038/sdata.2017.78",
      "citation": "Vega GC, Pertierra LR, Olalla-Tárraga MÁ (2017) MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Scientific Data 4: 170078."
    }
  ],
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "item",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/item.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.5061/dryad.s2v81.2"
    }
  ]
}

```

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "id": "MERRAclim",
  "title": "MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling.",
  "description": "Species Distribution Models (SDMs) combine information on the geographic occurrence of species with environmental layers to estimate distributional ranges and have been extensively implemented to answer a wide array of applied ecological questions. Unfortunately, most global datasets available to parameterize SDMs consist of spatially interpolated climate surfaces obtained from ground weather station data and have omitted the Antarctic continent, a landmass covering c. 20% of the Southern Hemisphere and increasingly showing biological effects of global change. Here we introduce MERRAclim, a global set of satellite-based bioclimatic variables including Antarctica for the first time. MERRAclim consists of three datasets of 19 bioclimatic variables that have been built for each of the last three decades (1980s, 1990s and 2000s) using hourly data of 2 m temperature and specific humidity. We provide MERRAclim at three spatial resolutions (10 arc-minutes, 5 arc-minutes and 2.5 arc-minutes). These reanalysed data are comparable to widely used datasets based on ground station interpolations, but allow extending their geographical reach and SDM building in previously uncovered regions of the globe.",
  "type": "Collection",
  "keywords": [
    "bioclimatic",
    "MERRAclim",
    "macroecology",
    "biogeography"
  ],
  "license": "CC0-1.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -180,
          -90,
          180,
          90
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1980-01-01T00:00:00Z",
          "2009-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "assets": {
    "test": {
      "href": "example.xml",
      "type": "application/xml",
      "sci:doi": "10.5061/dryad.s2v81.2"
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "item",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/item.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.5061/dryad.s2v81.2"
    }
  ]
}

```

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "id": "MERRAclim",
  "title": "MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling.",
  "description": "Species Distribution Models (SDMs) combine information on the geographic occurrence of species with environmental layers to estimate distributional ranges and have been extensively implemented to answer a wide array of applied ecological questions. Unfortunately, most global datasets available to parameterize SDMs consist of spatially interpolated climate surfaces obtained from ground weather station data and have omitted the Antarctic continent, a landmass covering c. 20% of the Southern Hemisphere and increasingly showing biological effects of global change. Here we introduce MERRAclim, a global set of satellite-based bioclimatic variables including Antarctica for the first time. MERRAclim consists of three datasets of 19 bioclimatic variables that have been built for each of the last three decades (1980s, 1990s and 2000s) using hourly data of 2 m temperature and specific humidity. We provide MERRAclim at three spatial resolutions (10 arc-minutes, 5 arc-minutes and 2.5 arc-minutes). These reanalysed data are comparable to widely used datasets based on ground station interpolations, but allow extending their geographical reach and SDM building in previously uncovered regions of the globe.",
  "type": "Collection",
  "keywords": [
    "bioclimatic",
    "MERRAclim",
    "macroecology",
    "biogeography"
  ],
  "license": "CC0-1.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -180,
          -90,
          180,
          90
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1980-01-01T00:00:00Z",
          "2009-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "item_assets": {
    "primary": {
      "type": "application/zip",
      "title": "MERRAclim. 2_5m_min_80s",
      "sci:doi": "10.5061/dryad.s2v81.2"
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "item",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/item.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.5061/dryad.s2v81.2"
    }
  ]
}

```

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "id": "MERRAclim",
  "title": "MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling.",
  "description": "Species Distribution Models (SDMs) combine information on the geographic occurrence of species with environmental layers to estimate distributional ranges and have been extensively implemented to answer a wide array of applied ecological questions. Unfortunately, most global datasets available to parameterize SDMs consist of spatially interpolated climate surfaces obtained from ground weather station data and have omitted the Antarctic continent, a landmass covering c. 20% of the Southern Hemisphere and increasingly showing biological effects of global change. Here we introduce MERRAclim, a global set of satellite-based bioclimatic variables including Antarctica for the first time. MERRAclim consists of three datasets of 19 bioclimatic variables that have been built for each of the last three decades (1980s, 1990s and 2000s) using hourly data of 2 m temperature and specific humidity. We provide MERRAclim at three spatial resolutions (10 arc-minutes, 5 arc-minutes and 2.5 arc-minutes). These reanalysed data are comparable to widely used datasets based on ground station interpolations, but allow extending their geographical reach and SDM building in previously uncovered regions of the globe.",
  "type": "Collection",
  "keywords": [
    "bioclimatic",
    "MERRAclim",
    "macroecology",
    "biogeography"
  ],
  "license": "CC0-1.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -180,
          -90,
          180,
          90
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1980-01-01T00:00:00Z",
          "2009-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "summaries": {
    "sci:doi": [
      "10.5061/dryad.s2v81.2/27.2"
    ],
    "sci:publications": [
      {
        "doi": "10.5061/dryad.s2v81.2",
        "citation": "Vega GC, Pertierra LR, Olalla-Tárraga MÁ (2017) Data from: MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Dryad Digital Repository."
      },
      {
        "doi": "10.1038/sdata.2017.78",
        "citation": "Vega GC, Pertierra LR, Olalla-Tárraga MÁ (2017) MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Scientific Data 4: 170078."
      }
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "item",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/item.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.5061/dryad.s2v81.2"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/scientific/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "id": "MERRAclim",
  "title": "MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling.",
  "description": "Species Distribution Models (SDMs) combine information on the geographic occurrence of species with environmental layers to estimate distributional ranges and have been extensively implemented to answer a wide array of applied ecological questions. Unfortunately, most global datasets available to parameterize SDMs consist of spatially interpolated climate surfaces obtained from ground weather station data and have omitted the Antarctic continent, a landmass covering c. 20% of the Southern Hemisphere and increasingly showing biological effects of global change. Here we introduce MERRAclim, a global set of satellite-based bioclimatic variables including Antarctica for the first time. MERRAclim consists of three datasets of 19 bioclimatic variables that have been built for each of the last three decades (1980s, 1990s and 2000s) using hourly data of 2\u2009m temperature and specific humidity. We provide MERRAclim at three spatial resolutions (10 arc-minutes, 5 arc-minutes and 2.5 arc-minutes). These reanalysed data are comparable to widely used datasets based on ground station interpolations, but allow extending their geographical reach and SDM building in previously uncovered regions of the globe.",
  "type": "Collection",
  "keywords": [
    "bioclimatic",
    "MERRAclim",
    "macroecology",
    "biogeography"
  ],
  "license": "CC0-1.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -180,
          -90,
          180,
          90
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1980-01-01T00:00:00Z",
          "2009-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "summaries": {
    "sci:doi": [
      "10.5061/dryad.s2v81.2/27.2"
    ],
    "sci:publications": [
      {
        "doi": "10.5061/dryad.s2v81.2",
        "citation": "Vega GC, Pertierra LR, Olalla-T\u00e1rraga M\u00c1 (2017) Data from: MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Dryad Digital Repository."
      },
      {
        "doi": "10.1038/sdata.2017.78",
        "citation": "Vega GC, Pertierra LR, Olalla-T\u00e1rraga M\u00c1 (2017) MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling. Scientific Data 4: 170078."
      }
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "item",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/item.json"
    },
    {
      "rel": "root",
      "href": "https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.5061/dryad.s2v81.2"
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

<https://example.com/stac/scientific/collection-summaries/MERRAclim> a <https://example.com/stac/scientific/collection-summaries/Collection> ;
    dcterms:description "Species Distribution Models (SDMs) combine information on the geographic occurrence of species with environmental layers to estimate distributional ranges and have been extensively implemented to answer a wide array of applied ecological questions. Unfortunately, most global datasets available to parameterize SDMs consist of spatially interpolated climate surfaces obtained from ground weather station data and have omitted the Antarctic continent, a landmass covering c. 20% of the Southern Hemisphere and increasingly showing biological effects of global change. Here we introduce MERRAclim, a global set of satellite-based bioclimatic variables including Antarctica for the first time. MERRAclim consists of three datasets of 19 bioclimatic variables that have been built for each of the last three decades (1980s, 1990s and 2000s) using hourly data of 2 m temperature and specific humidity. We provide MERRAclim at three spatial resolutions (10 arc-minutes, 5 arc-minutes and 2.5 arc-minutes). These reanalysed data are comparable to widely used datasets based on ground station interpolations, but allow extending their geographical reach and SDM building in previously uncovered regions of the globe." ;
    dcterms:extent [ ] ;
    dcterms:title "MERRAclim, a high-resolution global dataset of remotely sensed bioclimatic variables for ecological modelling." ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://datadryad.org/resource/doi:10.5061/dryad.s2v81/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://doi.org/10.5061/dryad.s2v81.2> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://datadryad.org/resource/doi:10.5061/dryad.s2v81/item.json> ] ;
    dcat:keyword "MERRAclim",
        "bioclimatic",
        "biogeography",
        "macroecology" ;
    dcat:license "CC0-1.0" ;
    stac:hasExtension "https://stac-extensions.github.io/scientific/v1.0.0/schema.json" ;
    stac:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Scientific Citation extension
description: STAC Scientific Citation Extension for Items and Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/scientific/v1.0.0/schema.json
x-jsonld-extra-terms:
  sci:doi:
    x-jsonld-id: https://w3id.org/ogc/stac/scientific/doi
    x-jsonld-type: xsd:string
  sci:citation:
    x-jsonld-id: https://w3id.org/ogc/stac/scientific/citation
    x-jsonld-type: xsd:string
  sci:publications:
    x-jsonld-id: https://w3id.org/ogc/stac/scientific/publications
    x-jsonld-type: '@json'
x-jsonld-prefixes:
  sci: https://w3id.org/ogc/stac/scientific/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/scientific/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/scientific/schema.yaml)


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
    "sci:doi": {
      "@id": "sci:doi",
      "@type": "xsd:string"
    },
    "sci:citation": {
      "@id": "sci:citation",
      "@type": "xsd:string"
    },
    "sci:publications": {
      "@id": "sci:publications",
      "@type": "@json"
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "sci": "https://w3id.org/ogc/stac/scientific/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/scientific/context.jsonld)

## Sources

* [STAC Scientific Citation Extension](https://github.com/stac-extensions/scientific/tree/v1.0.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/scientific`

