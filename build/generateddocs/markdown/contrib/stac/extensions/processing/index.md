
# STAC Processing Extension (Schema)

`ogc.contrib.stac.extensions.processing` *v1.2.0*

STAC Processing Extension for STAC Items and STAC Collections.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Collection
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
  ],
  "type": "Collection",
  "id": "Sentinel2-L2A",
  "title": "Sentinel-2 MSI: MultiSpectral Instrument, Level-2A",
  "description": "Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission.",
  "license": "proprietary",
  "providers": [
    {
      "name": "European Union/ESA/Copernicus",
      "roles": [
        "producer",
        "licensor"
      ],
      "url": "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi",
      "processing:lineage": "Generation of Level-1C User Product",
      "processing:level": "L1",
      "processing:facility": "Copernicus S2 Processing and Archiving Facility",
      "processing:version": "02.06"
    },
    {
      "name": "Processing Corp.",
      "roles": [
        "processor"
      ],
      "processing:lineage": "Generation of Level-2A User Product",
      "processing:level": "L2A",
      "processing:software": {
        "Sentinel-2 Toolbox": "8.0.0"
      }
    },
    {
      "name": "Storage Provider, Inc.",
      "roles": [
        "host"
      ]
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
    "gsd": [
      10,
      30,
      60
    ],
    "processing:level": [
      "L1",
      "L2"
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://processing-corp.com/catalog/COPERNICUS_S2.json"
    },
    {
      "rel": "parent",
      "href": "https://processing-corp.com/catalog/catalog.json"
    },
    {
      "rel": "root",
      "href": "https://processing-corp.com/catalog/catalog.json"
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
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
  ],
  "type": "Collection",
  "id": "Sentinel2-L2A",
  "title": "Sentinel-2 MSI: MultiSpectral Instrument, Level-2A",
  "description": "Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission.",
  "license": "proprietary",
  "providers": [
    {
      "name": "European Union/ESA/Copernicus",
      "roles": [
        "producer",
        "licensor"
      ],
      "url": "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi",
      "processing:lineage": "Generation of Level-1C User Product",
      "processing:level": "L1",
      "processing:facility": "Copernicus S2 Processing and Archiving Facility",
      "processing:version": "02.06"
    },
    {
      "name": "Processing Corp.",
      "roles": [
        "processor"
      ],
      "processing:lineage": "Generation of Level-2A User Product",
      "processing:level": "L2A",
      "processing:software": {
        "Sentinel-2 Toolbox": "8.0.0"
      }
    },
    {
      "name": "Storage Provider, Inc.",
      "roles": [
        "host"
      ]
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
    "gsd": [
      10,
      30,
      60
    ],
    "processing:level": [
      "L1",
      "L2"
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://processing-corp.com/catalog/COPERNICUS_S2.json"
    },
    {
      "rel": "parent",
      "href": "https://processing-corp.com/catalog/catalog.json"
    },
    {
      "rel": "root",
      "href": "https://processing-corp.com/catalog/catalog.json"
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
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <http://stacspec.org/ontology/core#> .

<https://example.com/stac/processing/example-1/Sentinel2-L2A> a <https://example.com/stac/processing/example-1/Collection> ;
    rdfs:label "Sentinel-2 MSI: MultiSpectral Instrument, Level-2A" ;
    stac:description "Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission." ;
    stac:extent [ ] ;
    stac:license "proprietary" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://processing-corp.com/catalog/catalog.json> ],
        [ rdfs:label "Legal notice on the use of Copernicus Sentinel Data and Service Information" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://scihub.copernicus.eu/twiki/pub/SciHubWebPortal/TermsConditions/Sentinel_Data_Terms_and_Conditions.pdf> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://processing-corp.com/catalog/COPERNICUS_S2.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://processing-corp.com/catalog/catalog.json> ] .


```


### Item Model Classes
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/sat/v1.0.0/schema.json",
    "https://stac-extensions.github.io/sar/v1.0.0/schema.json",
    "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
  ],
  "id": "S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF",
  "properties": {
    "datetime": "2016-08-22T18:28:23.368922Z",
    "start_datetime": "2016-08-22T18:28:23.368922Z",
    "end_datetime": "2016-08-22T18:28:48.368201Z",
    "created": "2016-08-23T00:38:22Z",
    "platform": "sentinel-1a",
    "constellation": "sentinel-1",
    "mission": "sentinel-1",
    "instruments": [
      "c-sar"
    ],
    "sat:absolute_orbit": 12717,
    "sat:orbit_state": "ascending",
    "sat:relative_orbit": 45,
    "sat:anx_datetime": "2016-08-22T18:24:52.513706Z",
    "sar:instrument_mode": "IW",
    "sar:frequency_band": "C",
    "sar:polarizations": [
      "VV",
      "VH"
    ],
    "sar:product_type": "GRD",
    "processing:lineage": "GRD Post Processing",
    "processing:level": "L1",
    "processing:facility": "Copernicus S1 Core Ground Segment - DPA",
    "processing:software": {
      "Sentinel-1 IPF": "002.71"
    },
    "processing:datetime": "2016-08-23T00:30:33Z"
  },
  "links": [
    {
      "title": "GRD Post Processing (90AF)",
      "rel": "processing-execution",
      "href": "https://api.example.com/processing/s1-grd-l1c/jobs/90AF",
      "type": "application/json"
    }
  ],
  "assets": {
    "manifest": {
      "type": "text/xml",
      "roles": [
        "metadata"
      ],
      "title": "SAFE Manifest",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/manifest.safe",
      "created": "2016-08-23T00:30:33Z"
    },
    "quick-look": {
      "type": "image/png",
      "roles": [
        "overview"
      ],
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/preview/quick-look.png"
    },
    "annotation-vv-iw": {
      "type": "text/xml",
      "roles": [
        "metadata"
      ],
      "title": "Annotation VV IW",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.xml",
      "sar:polarizations": [
        "VV"
      ]
    },
    "amplitude-vv-iw": {
      "type": "image/tiff; application=geotiff",
      "roles": [
        "data"
      ],
      "title": "IW VV Amplitude pixel values",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.tiff",
      "sar:polarizations": [
        "VV"
      ]
    },
    "annotation-vh-iw": {
      "type": "text/xml",
      "roles": [
        "metadata"
      ],
      "title": "Annotation VH IW",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.xml",
      "sar:polarizations": [
        "VH"
      ]
    },
    "amplitude-vh-iw": {
      "type": "image/tiff; application=geotiff",
      "roles": [
        "data"
      ],
      "title": "IW VH Amplitude pixel values",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.tiff",
      "sar:polarizations": [
        "VH"
      ]
    },
    "calibration-vv-iw": {
      "type": "text/xml",
      "roles": [
        "data"
      ],
      "title": "Calibration VV IW",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/calibration/calibration-s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.xml",
      "sar:polarizations": [
        "VV"
      ]
    },
    "calibration-vh-iw": {
      "type": "text/xml",
      "roles": [
        "data"
      ],
      "title": "Calibration VH IW",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/calibration/calibration-s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.xml",
      "sar:polarizations": [
        "VH"
      ]
    }
  },
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -5.730959,
          14.953436
        ],
        [
          -3.431006,
          15.388663
        ],
        [
          -3.136116,
          13.880572
        ],
        [
          -5.419919,
          13.441674
        ],
        [
          -5.730959,
          14.953436
        ]
      ]
    ]
  },
  "bbox": [
    -5.730959,
    13.441674,
    -3.136116,
    15.388663
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/sat/v1.0.0/schema.json",
    "https://stac-extensions.github.io/sar/v1.0.0/schema.json",
    "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
  ],
  "id": "S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF",
  "properties": {
    "datetime": "2016-08-22T18:28:23.368922Z",
    "start_datetime": "2016-08-22T18:28:23.368922Z",
    "end_datetime": "2016-08-22T18:28:48.368201Z",
    "created": "2016-08-23T00:38:22Z",
    "platform": "sentinel-1a",
    "constellation": "sentinel-1",
    "mission": "sentinel-1",
    "instruments": [
      "c-sar"
    ],
    "sat:absolute_orbit": 12717,
    "sat:orbit_state": "ascending",
    "sat:relative_orbit": 45,
    "sat:anx_datetime": "2016-08-22T18:24:52.513706Z",
    "sar:instrument_mode": "IW",
    "sar:frequency_band": "C",
    "sar:polarizations": [
      "VV",
      "VH"
    ],
    "sar:product_type": "GRD",
    "processing:lineage": "GRD Post Processing",
    "processing:level": "L1",
    "processing:facility": "Copernicus S1 Core Ground Segment - DPA",
    "processing:software": {
      "Sentinel-1 IPF": "002.71"
    },
    "processing:datetime": "2016-08-23T00:30:33Z"
  },
  "links": [
    {
      "title": "GRD Post Processing (90AF)",
      "rel": "processing-execution",
      "href": "https://api.example.com/processing/s1-grd-l1c/jobs/90AF",
      "type": "application/json"
    }
  ],
  "assets": {
    "manifest": {
      "type": "text/xml",
      "roles": [
        "metadata"
      ],
      "title": "SAFE Manifest",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/manifest.safe",
      "created": "2016-08-23T00:30:33Z"
    },
    "quick-look": {
      "type": "image/png",
      "roles": [
        "overview"
      ],
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/preview/quick-look.png"
    },
    "annotation-vv-iw": {
      "type": "text/xml",
      "roles": [
        "metadata"
      ],
      "title": "Annotation VV IW",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.xml",
      "sar:polarizations": [
        "VV"
      ]
    },
    "amplitude-vv-iw": {
      "type": "image/tiff; application=geotiff",
      "roles": [
        "data"
      ],
      "title": "IW VV Amplitude pixel values",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.tiff",
      "sar:polarizations": [
        "VV"
      ]
    },
    "annotation-vh-iw": {
      "type": "text/xml",
      "roles": [
        "metadata"
      ],
      "title": "Annotation VH IW",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.xml",
      "sar:polarizations": [
        "VH"
      ]
    },
    "amplitude-vh-iw": {
      "type": "image/tiff; application=geotiff",
      "roles": [
        "data"
      ],
      "title": "IW VH Amplitude pixel values",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.tiff",
      "sar:polarizations": [
        "VH"
      ]
    },
    "calibration-vv-iw": {
      "type": "text/xml",
      "roles": [
        "data"
      ],
      "title": "Calibration VV IW",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/calibration/calibration-s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.xml",
      "sar:polarizations": [
        "VV"
      ]
    },
    "calibration-vh-iw": {
      "type": "text/xml",
      "roles": [
        "data"
      ],
      "title": "Calibration VH IW",
      "href": "data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/calibration/calibration-s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.xml",
      "sar:polarizations": [
        "VH"
      ]
    }
  },
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -5.730959,
          14.953436
        ],
        [
          -3.431006,
          15.388663
        ],
        [
          -3.136116,
          13.880572
        ],
        [
          -5.419919,
          13.441674
        ],
        [
          -5.730959,
          14.953436
        ]
      ]
    ]
  },
  "bbox": [
    -5.730959,
    13.441674,
    -3.136116,
    15.388663
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <sar:> .
@prefix ns2: <processing:> .
@prefix ns3: <https://w3id.org/ogc/stac/core/> .
@prefix ns4: <sat:> .
@prefix ns5: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <http://stacspec.org/ontology/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/processing/example-2/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF> a geojson:Feature ;
    dcterms:created "2016-08-23T00:38:22Z" ;
    stac:datetime "2016-08-22T18:28:23.368922+00:00"^^xsd:dateTime ;
    stac:end_datetime "2016-08-22T18:28:48.368201+00:00"^^xsd:dateTime ;
    stac:start_datetime "2016-08-22T18:28:23.368922+00:00"^^xsd:dateTime ;
    rdfs:seeAlso [ rdfs:label "GRD Post Processing (90AF)" ;
            dcterms:type "application/json" ;
            ns5:relation <http://www.iana.org/assignments/relation/processing-execution> ;
            oa:hasTarget <https://api.example.com/processing/s1-grd-l1c/jobs/90AF> ] ;
    geojson:bbox ( -5.730959e+00 1.344167e+01 -3.136116e+00 1.538866e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -5.730959e+00 1.495344e+01 ) ( -3.431006e+00 1.538866e+01 ) ( -3.136116e+00 1.388057e+01 ) ( -5.419919e+00 1.344167e+01 ) ( -5.730959e+00 1.495344e+01 ) ) ) ] ;
    ns3:assets <https://example.com/stac/processing/example-2/amplitude-vh-iw>,
        <https://example.com/stac/processing/example-2/amplitude-vv-iw>,
        <https://example.com/stac/processing/example-2/annotation-vh-iw>,
        <https://example.com/stac/processing/example-2/annotation-vv-iw>,
        <https://example.com/stac/processing/example-2/calibration-vh-iw>,
        <https://example.com/stac/processing/example-2/calibration-vv-iw>,
        <https://example.com/stac/processing/example-2/manifest>,
        <https://example.com/stac/processing/example-2/quick-look> ;
    ns2:datetime "2016-08-23T00:30:33Z" ;
    ns2:facility "Copernicus S1 Core Ground Segment - DPA" ;
    ns2:level "L1" ;
    ns2:lineage "GRD Post Processing" ;
    ns2:software [ ] ;
    ns1:frequency_band "C" ;
    ns1:instrument_mode "IW" ;
    ns1:polarizations "VH",
        "VV" ;
    ns1:product_type "GRD" ;
    ns4:absolute_orbit 12717 ;
    ns4:anx_datetime "2016-08-22T18:24:52.513706Z" ;
    ns4:orbit_state "ascending" ;
    ns4:relative_orbit 45 .

<https://example.com/stac/processing/example-2/amplitude-vh-iw> rdfs:label "IW VH Amplitude pixel values" ;
    oa:hasTarget <https://example.com/stac/processing/example-2/data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.tiff> ;
    ns1:polarizations "VH" .

<https://example.com/stac/processing/example-2/amplitude-vv-iw> rdfs:label "IW VV Amplitude pixel values" ;
    oa:hasTarget <https://example.com/stac/processing/example-2/data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.tiff> ;
    ns1:polarizations "VV" .

<https://example.com/stac/processing/example-2/annotation-vh-iw> a <https://example.com/stac/processing/example-2/text/xml> ;
    rdfs:label "Annotation VH IW" ;
    oa:hasTarget <https://example.com/stac/processing/example-2/data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.xml> ;
    ns1:polarizations "VH" .

<https://example.com/stac/processing/example-2/annotation-vv-iw> a <https://example.com/stac/processing/example-2/text/xml> ;
    rdfs:label "Annotation VV IW" ;
    oa:hasTarget <https://example.com/stac/processing/example-2/data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.xml> ;
    ns1:polarizations "VV" .

<https://example.com/stac/processing/example-2/calibration-vh-iw> a <https://example.com/stac/processing/example-2/text/xml> ;
    rdfs:label "Calibration VH IW" ;
    oa:hasTarget <https://example.com/stac/processing/example-2/data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/calibration/calibration-s1a-iw-grd-vh-20160822t182823-20160822t182848-012717-013ffe-002.xml> ;
    ns1:polarizations "VH" .

<https://example.com/stac/processing/example-2/calibration-vv-iw> a <https://example.com/stac/processing/example-2/text/xml> ;
    rdfs:label "Calibration VV IW" ;
    oa:hasTarget <https://example.com/stac/processing/example-2/data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/annotation/calibration/calibration-s1a-iw-grd-vv-20160822t182823-20160822t182848-012717-013ffe-001.xml> ;
    ns1:polarizations "VV" .

<https://example.com/stac/processing/example-2/manifest> a <https://example.com/stac/processing/example-2/text/xml> ;
    rdfs:label "SAFE Manifest" ;
    dcterms:created "2016-08-23T00:30:33Z" ;
    oa:hasTarget <https://example.com/stac/processing/example-2/data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/manifest.safe> .

<https://example.com/stac/processing/example-2/quick-look> a <https://example.com/stac/processing/example-2/image/png> ;
    oa:hasTarget <https://example.com/stac/processing/example-2/data/S1A_IW_GRDH_1SDV_20160822T182823_20160822T182848_012717_013FFE_90AF.SAFE/preview/quick-look.png> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Processing extension
description: Indicates from which processing chain data originates and how the data
  itself has been produced.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-v1-0-0/schema.yaml
- $ref: https://stac-extensions.github.io/processing/v1.2.0/schema.json
x-jsonld-extra-terms:
  raster:bands:
    x-jsonld-id: https://w3id.org/ogc/stac/raster/bands
    x-jsonld-context:
      '@vocab': https://w3id.org/ogc/stac/raster/
  raster:range:
    x-jsonld-id: https://w3id.org/ogc/stac/raster/range
    x-jsonld-container: '@list'
x-jsonld-prefixes:
  raster: https://w3id.org/ogc/stac/raster/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/schema.yaml)


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
    "description": "stac:description",
    "license": "stac:license",
    "extent": "stac:extent",
    "datetime": {
      "@id": "stac:datetime",
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
      "@id": "https://w3id.org/ogc/stac/core/assets",
      "@container": "@id"
    },
    "media_type": "stac:mediaType",
    "raster:bands": {
      "@id": "raster:bands",
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/raster/"
      }
    },
    "raster:range": {
      "@id": "raster:range",
      "@container": "@list"
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "raster": "https://w3id.org/ogc/stac/raster/",
    "geojson": "https://purl.org/geojson/vocab#",
    "stac": "http://stacspec.org/ontology/core#",
    "geo": "http://www.opengis.net/ont/geosparql#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/processing/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/processing)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/processing`

