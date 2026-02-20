
# STAC Collection (Schema)

`ogc.contrib.stac.collection` *v1.1.0*

A SpatioTemporal Asset Catalogs (STAC) collection.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC Collection v1.1.0
Ref to STAC example from current version (1.1.0)
#### json
```json
{
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json"
  ],
  "id": "sentinel-2",
  "title": "Sentinel-2 MSI: MultiSpectral Instrument, Level-1C",
  "description": "Sentinel-2 is a wide-swath, high-resolution, multi-spectral\nimaging mission supporting Copernicus Land Monitoring studies,\nincluding the monitoring of vegetation, soil and water cover,\nas well as observation of inland waterways and coastal areas.\n\nThe Sentinel-2 data contain 13 UINT16 spectral bands representing\nTOA reflectance scaled by 10000. See the [Sentinel-2 User Handbook](https://sentinel.esa.int/documents/247904/685211/Sentinel-2_User_Handbook)\nfor details. In addition, three QA bands are present where one\n(QA60) is a bitmask band with cloud mask information. For more\ndetails, [see the full explanation of how cloud masks are computed.](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-1c/cloud-masks)\n\nEach Sentinel-2 product (zip archive) may contain multiple\ngranules. Each granule becomes a separate Earth Engine asset.\nEE asset ids for Sentinel-2 assets have the following format:\nCOPERNICUS/S2/20151128T002653_20151128T102149_T56MNN. Here the\nfirst numeric part represents the sensing date and time, the\nsecond numeric part represents the product generation date and\ntime, and the final 6-character string is a unique granule identifier\nindicating its UTM grid reference (see [MGRS](https://en.wikipedia.org/wiki/Military_Grid_Reference_System)).\n\nFor more details on Sentinel-2 radiometric resoltuon, [see this page](https://earth.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/radiometric).\n",
  "license": "other",
  "keywords": [
    "copernicus",
    "esa",
    "eu",
    "msi",
    "radiance",
    "sentinel"
  ],
  "providers": [
    {
      "name": "European Union/ESA/Copernicus",
      "roles": [
        "producer",
        "licensor"
      ],
      "url": "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi"
    }
  ],
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
          null
        ]
      ]
    }
  },
  "assets": {
    "metadata_iso_19139": {
      "roles": [
        "metadata",
        "iso-19139"
      ],
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/sentinel-2-iso-19139.xml",
      "title": "ISO 19139 metadata",
      "type": "application/vnd.iso.19139+xml"
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "2015-06-23T00:00:00Z",
      "maximum": "2019-07-10T13:44:56Z"
    },
    "platform": [
      "sentinel-2a",
      "sentinel-2b"
    ],
    "constellation": [
      "sentinel-2"
    ],
    "instruments": [
      "msi"
    ],
    "view:off_nadir": {
      "minimum": 0,
      "maximum": 100
    },
    "view:sun_elevation": {
      "minimum": 6.78,
      "maximum": 89.9
    },
    "gsd": [
      10,
      30,
      60
    ],
    "proj:code": [
      "EPSG:32601",
      "EPSG:32602",
      "EPSG:32603",
      "EPSG:32604",
      "EPSG:32605",
      "EPSG:32606",
      "EPSG:32607",
      "EPSG:32608",
      "EPSG:32609",
      "EPSG:32610",
      "EPSG:32611",
      "EPSG:32612",
      "EPSG:32613",
      "EPSG:32614",
      "EPSG:32615",
      "EPSG:32616",
      "EPSG:32617",
      "EPSG:32618",
      "EPSG:32619",
      "EPSG:32620",
      "EPSG:32621",
      "EPSG:32622",
      "EPSG:32623",
      "EPSG:32624",
      "EPSG:32625",
      "EPSG:32626",
      "EPSG:32627",
      "EPSG:32628",
      "EPSG:32629",
      "EPSG:32630",
      "EPSG:32631",
      "EPSG:32632",
      "EPSG:32633",
      "EPSG:32634",
      "EPSG:32635",
      "EPSG:32636",
      "EPSG:32637",
      "EPSG:32638",
      "EPSG:32639",
      "EPSG:32640",
      "EPSG:32641",
      "EPSG:32642",
      "EPSG:32643",
      "EPSG:32644",
      "EPSG:32645",
      "EPSG:32646",
      "EPSG:32647",
      "EPSG:32648",
      "EPSG:32649",
      "EPSG:32650",
      "EPSG:32651",
      "EPSG:32652",
      "EPSG:32653",
      "EPSG:32654",
      "EPSG:32655",
      "EPSG:32656",
      "EPSG:32657",
      "EPSG:32658",
      "EPSG:32659",
      "EPSG:32660"
    ],
    "bands": [
      {
        "name": "B1",
        "eo:common_name": "coastal",
        "eo:center_wavelength": 0.4439
      },
      {
        "name": "B2",
        "eo:common_name": "blue",
        "eo:center_wavelength": 0.4966
      },
      {
        "name": "B3",
        "eo:common_name": "green",
        "eo:center_wavelength": 0.56
      },
      {
        "name": "B4",
        "eo:common_name": "red",
        "eo:center_wavelength": 0.6645
      },
      {
        "name": "B5",
        "eo:center_wavelength": 0.7039
      },
      {
        "name": "B6",
        "eo:center_wavelength": 0.7402
      },
      {
        "name": "B7",
        "eo:center_wavelength": 0.7825
      },
      {
        "name": "B8",
        "eo:common_name": "nir",
        "eo:center_wavelength": 0.8351
      },
      {
        "name": "B8A",
        "eo:center_wavelength": 0.8648
      },
      {
        "name": "B9",
        "eo:center_wavelength": 0.945
      },
      {
        "name": "B10",
        "eo:center_wavelength": 1.3735
      },
      {
        "name": "B11",
        "eo:common_name": "swir16",
        "eo:center_wavelength": 1.6137
      },
      {
        "name": "B12",
        "eo:common_name": "swir22",
        "eo:center_wavelength": 2.2024
      }
    ]
  },
  "links": [
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Example Catalog"
    },
    {
      "rel": "root",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Example Catalog"
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
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/context.jsonld",
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v2.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json"
  ],
  "id": "sentinel-2",
  "title": "Sentinel-2 MSI: MultiSpectral Instrument, Level-1C",
  "description": "Sentinel-2 is a wide-swath, high-resolution, multi-spectral\nimaging mission supporting Copernicus Land Monitoring studies,\nincluding the monitoring of vegetation, soil and water cover,\nas well as observation of inland waterways and coastal areas.\n\nThe Sentinel-2 data contain 13 UINT16 spectral bands representing\nTOA reflectance scaled by 10000. See the [Sentinel-2 User Handbook](https://sentinel.esa.int/documents/247904/685211/Sentinel-2_User_Handbook)\nfor details. In addition, three QA bands are present where one\n(QA60) is a bitmask band with cloud mask information. For more\ndetails, [see the full explanation of how cloud masks are computed.](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-1c/cloud-masks)\n\nEach Sentinel-2 product (zip archive) may contain multiple\ngranules. Each granule becomes a separate Earth Engine asset.\nEE asset ids for Sentinel-2 assets have the following format:\nCOPERNICUS/S2/20151128T002653_20151128T102149_T56MNN. Here the\nfirst numeric part represents the sensing date and time, the\nsecond numeric part represents the product generation date and\ntime, and the final 6-character string is a unique granule identifier\nindicating its UTM grid reference (see [MGRS](https://en.wikipedia.org/wiki/Military_Grid_Reference_System)).\n\nFor more details on Sentinel-2 radiometric resoltuon, [see this page](https://earth.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/radiometric).\n",
  "license": "other",
  "keywords": [
    "copernicus",
    "esa",
    "eu",
    "msi",
    "radiance",
    "sentinel"
  ],
  "providers": [
    {
      "name": "European Union/ESA/Copernicus",
      "roles": [
        "producer",
        "licensor"
      ],
      "url": "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi"
    }
  ],
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
          null
        ]
      ]
    }
  },
  "assets": {
    "metadata_iso_19139": {
      "roles": [
        "metadata",
        "iso-19139"
      ],
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/sentinel-2-iso-19139.xml",
      "title": "ISO 19139 metadata",
      "type": "application/vnd.iso.19139+xml"
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "2015-06-23T00:00:00Z",
      "maximum": "2019-07-10T13:44:56Z"
    },
    "platform": [
      "sentinel-2a",
      "sentinel-2b"
    ],
    "constellation": [
      "sentinel-2"
    ],
    "instruments": [
      "msi"
    ],
    "view:off_nadir": {
      "minimum": 0,
      "maximum": 100
    },
    "view:sun_elevation": {
      "minimum": 6.78,
      "maximum": 89.9
    },
    "gsd": [
      10,
      30,
      60
    ],
    "proj:code": [
      "EPSG:32601",
      "EPSG:32602",
      "EPSG:32603",
      "EPSG:32604",
      "EPSG:32605",
      "EPSG:32606",
      "EPSG:32607",
      "EPSG:32608",
      "EPSG:32609",
      "EPSG:32610",
      "EPSG:32611",
      "EPSG:32612",
      "EPSG:32613",
      "EPSG:32614",
      "EPSG:32615",
      "EPSG:32616",
      "EPSG:32617",
      "EPSG:32618",
      "EPSG:32619",
      "EPSG:32620",
      "EPSG:32621",
      "EPSG:32622",
      "EPSG:32623",
      "EPSG:32624",
      "EPSG:32625",
      "EPSG:32626",
      "EPSG:32627",
      "EPSG:32628",
      "EPSG:32629",
      "EPSG:32630",
      "EPSG:32631",
      "EPSG:32632",
      "EPSG:32633",
      "EPSG:32634",
      "EPSG:32635",
      "EPSG:32636",
      "EPSG:32637",
      "EPSG:32638",
      "EPSG:32639",
      "EPSG:32640",
      "EPSG:32641",
      "EPSG:32642",
      "EPSG:32643",
      "EPSG:32644",
      "EPSG:32645",
      "EPSG:32646",
      "EPSG:32647",
      "EPSG:32648",
      "EPSG:32649",
      "EPSG:32650",
      "EPSG:32651",
      "EPSG:32652",
      "EPSG:32653",
      "EPSG:32654",
      "EPSG:32655",
      "EPSG:32656",
      "EPSG:32657",
      "EPSG:32658",
      "EPSG:32659",
      "EPSG:32660"
    ],
    "bands": [
      {
        "name": "B1",
        "eo:common_name": "coastal",
        "eo:center_wavelength": 0.4439
      },
      {
        "name": "B2",
        "eo:common_name": "blue",
        "eo:center_wavelength": 0.4966
      },
      {
        "name": "B3",
        "eo:common_name": "green",
        "eo:center_wavelength": 0.56
      },
      {
        "name": "B4",
        "eo:common_name": "red",
        "eo:center_wavelength": 0.6645
      },
      {
        "name": "B5",
        "eo:center_wavelength": 0.7039
      },
      {
        "name": "B6",
        "eo:center_wavelength": 0.7402
      },
      {
        "name": "B7",
        "eo:center_wavelength": 0.7825
      },
      {
        "name": "B8",
        "eo:common_name": "nir",
        "eo:center_wavelength": 0.8351
      },
      {
        "name": "B8A",
        "eo:center_wavelength": 0.8648
      },
      {
        "name": "B9",
        "eo:center_wavelength": 0.945
      },
      {
        "name": "B10",
        "eo:center_wavelength": 1.3735
      },
      {
        "name": "B11",
        "eo:common_name": "swir16",
        "eo:center_wavelength": 1.6137
      },
      {
        "name": "B12",
        "eo:common_name": "swir22",
        "eo:center_wavelength": 2.2024
      }
    ]
  },
  "links": [
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Example Catalog"
    },
    {
      "rel": "root",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Example Catalog"
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
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<https://example.com/stac/example1/sentinel-2> a <https://example.com/stac/example1/Collection> ;
    dcterms:extent [ ] ;
    dcterms:license "other" ;
    dcterms:subject "copernicus",
        "esa",
        "eu",
        "msi",
        "radiance",
        "sentinel" ;
    rdfs:seeAlso [ rdfs:label "Example Catalog" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/catalog.json> ],
        [ rdfs:label "Legal notice on the use of Copernicus Sentinel Data and Service Information" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://scihub.copernicus.eu/twiki/pub/SciHubWebPortal/TermsConditions/Sentinel_Data_Terms_and_Conditions.pdf> ],
        [ rdfs:label "Example Catalog" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/catalog.json> ] ;
    stac:hasAsset [ ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v2.0.0/schema.json",
        "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
        "https://stac-extensions.github.io/view/v1.0.0/schema.json" ;
    stac:hasProvider [ ] ;
    stac:version "1.1.0" .


```


### STAC Collection v1.0.0
Ref to STAC example using version (1.0.0)
#### json
```json
{
  "id": "polarwarp",
  "title": "Polarwarp",
  "created": "2025-10-13T16:54:34Z",
  "osc:status": "completed",
  "type": "Collection",
  "osc:type": "product",
  "stac_version": "1.0.0",
  "description": "Polarwarp product\n\nForecast rasters (+1h … +6h) produced by the Polarwarp workflow using NEXTSIM model and S1 scenes.",
  "license": "various",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -0.0018099989187332413,
          0.00043814539682784925,
          0.001347252506956414,
          0.0007574196581714432
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2025-02-25T00:00:00Z",
          null
        ]
      ]
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Open Science Catalog"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Products"
    },
    {
      "href": "../../projects/cerulean-information-factory/collection.json",
      "rel": "related",
      "type": "application/json",
      "title": "Project: Cerulean Information Factory"
    },
    {
      "href": "../../themes/cryosphere/catalog.json",
      "rel": "related",
      "type": "application/json",
      "title": "Theme: Cryosphere"
    },
    {
      "rel": "related",
      "href": "../../experiments/polarwarp/record.json",
      "type": "application/json",
      "title": "Experiment: Polarwarp"
    },
    {
      "href": "./item.json",
      "rel": "item"
    },
    {
      "href": "https://github.com/gtif-cerulean/polarwarp",
      "rel": "via"
    }
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json"
  ],
  "osc:project": "cerulean-information-factory",
  "themes": [
    {
      "scheme": "https://github.com/stac-extensions/osc#theme",
      "concepts": [
        {
          "id": "cryosphere"
        }
      ]
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/context.jsonld",
  "id": "polarwarp",
  "title": "Polarwarp",
  "created": "2025-10-13T16:54:34Z",
  "osc:status": "completed",
  "type": "Collection",
  "osc:type": "product",
  "stac_version": "1.0.0",
  "description": "Polarwarp product\n\nForecast rasters (+1h \u2026 +6h) produced by the Polarwarp workflow using NEXTSIM model and S1 scenes.",
  "license": "various",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -0.0018099989187332413,
          0.00043814539682784925,
          0.001347252506956414,
          0.0007574196581714432
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2025-02-25T00:00:00Z",
          null
        ]
      ]
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Open Science Catalog"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Products"
    },
    {
      "href": "../../projects/cerulean-information-factory/collection.json",
      "rel": "related",
      "type": "application/json",
      "title": "Project: Cerulean Information Factory"
    },
    {
      "href": "../../themes/cryosphere/catalog.json",
      "rel": "related",
      "type": "application/json",
      "title": "Theme: Cryosphere"
    },
    {
      "rel": "related",
      "href": "../../experiments/polarwarp/record.json",
      "type": "application/json",
      "title": "Experiment: Polarwarp"
    },
    {
      "href": "./item.json",
      "rel": "item"
    },
    {
      "href": "https://github.com/gtif-cerulean/polarwarp",
      "rel": "via"
    }
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json"
  ],
  "osc:project": "cerulean-information-factory",
  "themes": [
    {
      "scheme": "https://github.com/stac-extensions/osc#theme",
      "concepts": [
        {
          "id": "cryosphere"
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <osc:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<https://example.com/stac/example1/polarwarp> a <https://example.com/stac/example1/Collection> ;
    dcterms:extent [ ] ;
    dcterms:license "various" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://github.com/gtif-cerulean/polarwarp> ],
        [ rdfs:label "Experiment: Polarwarp" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/experiments/polarwarp/record.json> ],
        [ rdfs:label "Products" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/catalog.json> ],
        [ rdfs:label "Theme: Cryosphere" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/themes/cryosphere/catalog.json> ],
        [ rdfs:label "Project: Cerulean Information Factory" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/projects/cerulean-information-factory/collection.json> ],
        [ rdfs:label "Open Science Catalog" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/catalog.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/example1/item.json> ] ;
    stac:hasExtension "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
        "https://stac-extensions.github.io/themes/v1.0.0/schema.json" ;
    stac:version "1.0.0" ;
    ns2:project "cerulean-information-factory" ;
    ns2:status "completed" ;
    ns2:type "product" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: STAC Collection Specification
description: This object represents Collections in a SpatioTemporal Asset Catalog
  (adapted from official specs)
allOf:
- $ref: '#/definitions/collection'
- $ref: https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/json-schema/common.json
- $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/components/assets/schema.yaml
definitions:
  collection:
    title: STAC Collection
    description: These are the fields specific to a STAC Collection.
    type: object
    $comment: title, description, keywords, providers and license is validated through
      the common metadata.
    required:
    - type
    - id
    - description
    - license
    - extent
    - links
    properties:
      stac_extensions:
        title: STAC extensions
        type: array
        uniqueItems: true
        items:
          title: Reference to a JSON Schema
          type: string
          format: iri
        x-jsonld-id: https://w3id.org/ogc/stac/core/hasExtension
      type:
        title: Type of STAC entity
        const: Collection
        x-jsonld-id: '@type'
      id:
        title: Identifier
        type: string
        minLength: 1
        x-jsonld-id: '@id'
      extent:
        title: Extents
        type: object
        required:
        - spatial
        - temporal
        properties:
          spatial:
            title: Spatial extent object
            type: object
            required:
            - bbox
            properties:
              bbox:
                title: Spatial extents
                type: array
                oneOf:
                - minItems: 1
                  maxItems: 1
                - minItems: 3
                items:
                  title: Spatial extent
                  type: array
                  oneOf:
                  - minItems: 4
                    maxItems: 4
                  - minItems: 6
                    maxItems: 6
                  items:
                    type: number
          temporal:
            title: Temporal extent object
            type: object
            required:
            - interval
            properties:
              interval:
                title: Temporal extents
                type: array
                minItems: 1
                items:
                  title: Temporal extent
                  type: array
                  minItems: 2
                  maxItems: 2
                  items:
                    type:
                    - string
                    - 'null'
                    format: date-time
                    pattern: (\+00:00|Z)$
        x-jsonld-id: http://purl.org/dc/terms/extent
      item_assets:
        additionalProperties:
          allOf:
          - type: object
            minProperties: 2
            properties:
              href:
                title: Disallow href
                not: {}
              title:
                title: Asset title
                type: string
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                title: Asset description
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              type:
                title: Asset type
                type: string
                x-jsonld-id: '@type'
              roles:
                title: Asset roles
                type: array
                items:
                  type: string
          - $ref: https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/json-schema/common.json
      links:
        type: array
        items:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
      summaries:
        $ref: '#/definitions/summaries'
  summaries:
    type: object
    additionalProperties:
      anyOf:
      - title: JSON Schema
        type: object
        minProperties: 1
        allOf:
        - $ref: http://json-schema.org/draft-07/schema
      - title: Range
        type: object
        required:
        - minimum
        - maximum
        properties:
          minimum:
            title: Minimum value
            type:
            - number
            - string
          maximum:
            title: Maximum value
            type:
            - number
            - string
      - title: Set of values
        type: array
        minItems: 1
        items:
          description: For each field only the original data type of the property
            can occur (except for arrays), but we can't validate that in JSON Schema
            yet. See the sumamry description in the STAC specification for details.
x-jsonld-extra-terms:
  stac_version: https://w3id.org/ogc/stac/core/version
  keywords: http://purl.org/dc/terms/subject
  license: http://purl.org/dc/terms/license
  datetime:
    x-jsonld-id: http://purl.org/dc/terms/date
    x-jsonld-type: xsd:dateTime
  start_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/start_datetime
    x-jsonld-type: xsd:dateTime
  end_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/end_datetime
    x-jsonld-type: xsd:dateTime
  providers: https://w3id.org/ogc/stac/core/hasProvider
  media_type: http://purl.org/dc/terms/format
x-jsonld-prefixes:
  stac: https://w3id.org/ogc/stac/core/
  dct: http://purl.org/dc/terms/
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml)


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
    "assets": {
      "@context": {
        "type": "dct:format",
        "title": "dct:title",
        "description": "dct:description",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac_version": "stac:version",
    "keywords": "dct:subject",
    "license": "dct:license",
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
    "providers": "stac:hasProvider",
    "media_type": "dct:format",
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/context.jsonld)

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/collection`

