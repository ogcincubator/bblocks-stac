
# STAC Collection (Schema)

`ogc.contrib.stac.collection` *v1.1.0*

A SpatioTemporal Asset Catalogs (STAC) collection.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example STAC Collection
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
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

[] rdfs:label "Sentinel-2 MSI: MultiSpectral Instrument, Level-1C" ;
    dcterms:type "Collection" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: STAC Collection
allOf:
- $ref: https://github.com/radiantearth/stac-spec/raw/master/collection-spec/json-schema/collection.json
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-features/build/annotated/api/features/v1/schemas/collection/schema.yaml
- type: object
  properties:
    links:
      type: array
      items:
        $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml)


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
    "type": "dct:type",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
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

