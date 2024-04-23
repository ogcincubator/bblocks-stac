---
title: STAC Collection (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>STAC Collection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: STAC Collection (Schema)
---


# STAC Collection `ogc.contrib.stac.collection`

A SpatioTemporal Asset Catalogs (STAC) collection.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="warning">
Validation for this building block has <strong><a href="https://github.com/ogcincubator/bblocks-stac/blob/master/build/tests/contrib/stac/collection/" target="_blank">failed</a></strong>
</aside>

# Examples

## Example STAC Collection



```json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json"
  ],
  "id": "sentinel-2",
  "title": "Sentinel-2 MSI: MultiSpectral Instrument, Level-1C",
  "description": "Sentinel-2 is a wide-swath, high-resolution, multi-spectral\nimaging mission supporting Copernicus Land Monitoring studies,\nincluding the monitoring of vegetation, soil and water cover,\nas well as observation of inland waterways and coastal areas.\n\nThe Sentinel-2 data contain 13 UINT16 spectral bands representing\nTOA reflectance scaled by 10000. See the [Sentinel-2 User Handbook](https://sentinel.esa.int/documents/247904/685211/Sentinel-2_User_Handbook)\nfor details. In addition, three QA bands are present where one\n(QA60) is a bitmask band with cloud mask information. For more\ndetails, [see the full explanation of how cloud masks are computed.](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-1c/cloud-masks)\n\nEach Sentinel-2 product (zip archive) may contain multiple\ngranules. Each granule becomes a separate Earth Engine asset.\nEE asset ids for Sentinel-2 assets have the following format:\nCOPERNICUS/S2/20151128T002653_20151128T102149_T56MNN. Here the\nfirst numeric part represents the sensing date and time, the\nsecond numeric part represents the product generation date and\ntime, and the final 6-character string is a unique granule identifier\nindicating its UTM grid reference (see [MGRS](https://en.wikipedia.org/wiki/Military_Grid_Reference_System)).\n\nFor more details on Sentinel-2 radiometric resoltuon, [see this page](https://earth.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/radiometric).\n",
  "license": "proprietary",
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
    "proj:epsg": [
      32601,
      32602,
      32603,
      32604,
      32605,
      32606,
      32607,
      32608,
      32609,
      32610,
      32611,
      32612,
      32613,
      32614,
      32615,
      32616,
      32617,
      32618,
      32619,
      32620,
      32621,
      32622,
      32623,
      32624,
      32625,
      32626,
      32627,
      32628,
      32629,
      32630,
      32631,
      32632,
      32633,
      32634,
      32635,
      32636,
      32637,
      32638,
      32639,
      32640,
      32641,
      32642,
      32643,
      32644,
      32645,
      32646,
      32647,
      32648,
      32649,
      32650,
      32651,
      32652,
      32653,
      32654,
      32655,
      32656,
      32657,
      32658,
      32659,
      32660
    ],
    "eo:bands": [
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

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/collection/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fcollection%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/view/v1.0.0/schema.json"
  ],
  "id": "sentinel-2",
  "title": "Sentinel-2 MSI: MultiSpectral Instrument, Level-1C",
  "description": "Sentinel-2 is a wide-swath, high-resolution, multi-spectral\nimaging mission supporting Copernicus Land Monitoring studies,\nincluding the monitoring of vegetation, soil and water cover,\nas well as observation of inland waterways and coastal areas.\n\nThe Sentinel-2 data contain 13 UINT16 spectral bands representing\nTOA reflectance scaled by 10000. See the [Sentinel-2 User Handbook](https://sentinel.esa.int/documents/247904/685211/Sentinel-2_User_Handbook)\nfor details. In addition, three QA bands are present where one\n(QA60) is a bitmask band with cloud mask information. For more\ndetails, [see the full explanation of how cloud masks are computed.](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-1c/cloud-masks)\n\nEach Sentinel-2 product (zip archive) may contain multiple\ngranules. Each granule becomes a separate Earth Engine asset.\nEE asset ids for Sentinel-2 assets have the following format:\nCOPERNICUS/S2/20151128T002653_20151128T102149_T56MNN. Here the\nfirst numeric part represents the sensing date and time, the\nsecond numeric part represents the product generation date and\ntime, and the final 6-character string is a unique granule identifier\nindicating its UTM grid reference (see [MGRS](https://en.wikipedia.org/wiki/Military_Grid_Reference_System)).\n\nFor more details on Sentinel-2 radiometric resoltuon, [see this page](https://earth.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/radiometric).\n",
  "license": "proprietary",
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
    "proj:epsg": [
      32601,
      32602,
      32603,
      32604,
      32605,
      32606,
      32607,
      32608,
      32609,
      32610,
      32611,
      32612,
      32613,
      32614,
      32615,
      32616,
      32617,
      32618,
      32619,
      32620,
      32621,
      32622,
      32623,
      32624,
      32625,
      32626,
      32627,
      32628,
      32629,
      32630,
      32631,
      32632,
      32633,
      32634,
      32635,
      32636,
      32637,
      32638,
      32639,
      32640,
      32641,
      32642,
      32643,
      32644,
      32645,
      32646,
      32647,
      32648,
      32649,
      32650,
      32651,
      32652,
      32653,
      32654,
      32655,
      32656,
      32657,
      32658,
      32659,
      32660
    ],
    "eo:bands": [
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
  ],
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/collection/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Ftests%2Fcontrib%2Fstac%2Fcollection%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

[] rdfs:label "Sentinel-2 MSI: MultiSpectral Instrument, Level-1C" ;
    dcterms:type "Collection" .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/bblocks-stac/build/tests/contrib/stac/collection/example_1_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: STAC Collection
allOf:
- $ref: https://github.com/radiantearth/stac-spec/raw/master/collection-spec/json-schema/collection.json
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordGeoJSON/schema.yaml
- type: object
  properties:
    links:
      type: array
      items:
        $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fcollection%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.json" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.json</a>


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

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fcollection%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/context.jsonld" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/context.jsonld</a>

# References

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/bblocks-stac" target="_blank">https://github.com/ogcincubator/bblocks-stac</a>
* Path:
<code><a href="https://github.com/ogcincubator/bblocks-stac/blob/HEAD/_sources/collection" target="_blank">_sources/collection</a></code>

