
# STAC Extension - ESA Open Science Catalog (Schema)

`ogc.contrib.stac.extensions.osc` *v0.1*

STAC Extension for the ESA Open Science Catalog

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Project OSC extension fields in a Collection.
#### json
```json
{
  "type": "Collection",
  "id": "3d-earth",
  "stac_version": "1.0.0",
  "description": "The goal of this project is establish a global 3D reference model model of the crust and upper mantle based on the analysis of satellite gravity and (electro) magnetic missions in combination with seismological models and analyse the feedback between processes in Earths deep mantle and the lithosphere. Selected case examples will provide the possibility to test these approaches on a global and regional scale. This will result in a framework for consistent models that will be used to link the crust and upper mantle to the dynamic mantle. The prime objective is to integrate, for the first time, seismological models and satellite observation towards a consistent image of the crust and upper mantle in 3D.  Satellite gravity and (electro) magnetic data help to transfer velocity images towards composition and temperature that reflect the tectonic state and evolution of the Earth and offer a novel understanding of the processes that shape our planet. The limitations and sensitivity of the different geophysical methods in context of their imaging capability are analysed and combined with forward and inverse modelling to be able to evaluate the possibilities of these approaches to reveal the Earths structure. For the inverse modelling, we will explore the sensitivity of joint inversion to the individual data sets and compare these to inversions relying on only a single or a few data sets. To analyse the structure of the deep mantle, we will try to combine knowledge about mantle conductivity and mineral physics with the geophysical observations. We will assess the role of Earths internal layering and mantle convection on the evolution of the Earths surface (dynamic topography). The data and methods we propose to use in this study will significantly supersede previous attempts and will be a first step towards an understanding of the Earth in space and time, a necessary step towards the development of a 4D Earth model.",
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Open Science Catalog"
    },
    {
      "rel": "via",
      "href": "http://www.3dearth.uni-kiel.de/en",
      "title": "Website"
    },
    {
      "rel": "via",
      "href": "https://eo4society.esa.int/projects/stse-3d-earth/",
      "title": "EO4Society Link"
    },
    {
      "rel": "child",
      "href": "../../products/crust-and-upper-mantle-model-3d-earth/collection.json",
      "type": "application/json",
      "title": "Global Model of Crust and Upper Mantle_WINTERC-G_GOCE"
    },
    {
      "rel": "child",
      "href": "../../products/geothermal-heat-flow-greenland-3d-earth/collection.json",
      "type": "application/json",
      "title": "Geothermal Heat Flow Database and Map_Greenland_GOCE_SWARM"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Projects"
    },
    {
      "rel": "self",
      "href": "https://esa-earthcode.github.io/open-science-catalog-metadata/projects/3d-earth/collection.json",
      "type": "application/json"
    },
    {
      "rel": "related",
      "href": "../../themes/solid-earth/catalog.json",
      "type": "application/json",
      "title": "Theme: Solid Earth"
    }
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json",
    "https://stac-extensions.github.io/contacts/v0.1.1/schema.json"
  ],
  "osc:status": "completed",
  "themes": [
    {
      "scheme": "https://github.com/stac-extensions/osc#theme",
      "concepts": [
        {
          "id": "solid-earth"
        }
      ]
    }
  ],
  "osc:type": "project",
  "contacts": [
    {
      "name": "Roger Haagmans",
      "emails": [
        {
          "value": "roger.haagmans@esa.int"
        }
      ],
      "roles": [
        "technical_officer"
      ]
    },
    {
      "name": "UNIVERSITY OF KIEL (DE)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "BRITISH ANTARCTIC SURVEY (GB)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "DUBLIN INSTITUTE FOR ADVANCED STUDIES (DIAS) (IE)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "GEOLOGICAL SURVEY OF DENMARK AND GREENLAND (DK)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "TU DELFT (NL)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "Technical University of Denmark (DK)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "UNIVERSITY OF OSLO (NO)",
      "roles": [
        "consortium_member"
      ]
    }
  ],
  "updated": "2024-09-12T20:32:23.030110Z",
  "title": "3D-EARTH",
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
          "2019-10-22T00:00:00Z",
          "2020-12-11T23:59:59Z"
        ]
      ]
    }
  },
  "license": "proprietary",
  "keywords": []
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/osc/context.jsonld",
  "type": "Collection",
  "id": "3d-earth",
  "stac_version": "1.0.0",
  "description": "The goal of this project is establish a global 3D reference model model of the crust and upper mantle based on the analysis of satellite gravity and (electro) magnetic missions in combination with seismological models and analyse the feedback between processes in Earths deep mantle and the lithosphere. Selected case examples will provide the possibility to test these approaches on a global and regional scale. This will result in a framework for consistent models that will be used to link the crust and upper mantle to the dynamic mantle. The prime objective is to integrate, for the first time, seismological models and satellite observation towards a consistent image of the crust and upper mantle in 3D.  Satellite gravity and (electro) magnetic data help to transfer velocity images towards composition and temperature that reflect the tectonic state and evolution of the Earth and offer a novel understanding of the processes that shape our planet. The limitations and sensitivity of the different geophysical methods in context of their imaging capability are analysed and combined with forward and inverse modelling to be able to evaluate the possibilities of these approaches to reveal the Earths structure. For the inverse modelling, we will explore the sensitivity of joint inversion to the individual data sets and compare these to inversions relying on only a single or a few data sets. To analyse the structure of the deep mantle, we will try to combine knowledge about mantle conductivity and mineral physics with the geophysical observations. We will assess the role of Earths internal layering and mantle convection on the evolution of the Earths surface (dynamic topography). The data and methods we propose to use in this study will significantly supersede previous attempts and will be a first step towards an understanding of the Earth in space and time, a necessary step towards the development of a 4D Earth model.",
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Open Science Catalog"
    },
    {
      "rel": "via",
      "href": "http://www.3dearth.uni-kiel.de/en",
      "title": "Website"
    },
    {
      "rel": "via",
      "href": "https://eo4society.esa.int/projects/stse-3d-earth/",
      "title": "EO4Society Link"
    },
    {
      "rel": "child",
      "href": "../../products/crust-and-upper-mantle-model-3d-earth/collection.json",
      "type": "application/json",
      "title": "Global Model of Crust and Upper Mantle_WINTERC-G_GOCE"
    },
    {
      "rel": "child",
      "href": "../../products/geothermal-heat-flow-greenland-3d-earth/collection.json",
      "type": "application/json",
      "title": "Geothermal Heat Flow Database and Map_Greenland_GOCE_SWARM"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Projects"
    },
    {
      "rel": "self",
      "href": "https://esa-earthcode.github.io/open-science-catalog-metadata/projects/3d-earth/collection.json",
      "type": "application/json"
    },
    {
      "rel": "related",
      "href": "../../themes/solid-earth/catalog.json",
      "type": "application/json",
      "title": "Theme: Solid Earth"
    }
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json",
    "https://stac-extensions.github.io/contacts/v0.1.1/schema.json"
  ],
  "osc:status": "completed",
  "themes": [
    {
      "scheme": "https://github.com/stac-extensions/osc#theme",
      "concepts": [
        {
          "id": "solid-earth"
        }
      ]
    }
  ],
  "osc:type": "project",
  "contacts": [
    {
      "name": "Roger Haagmans",
      "emails": [
        {
          "value": "roger.haagmans@esa.int"
        }
      ],
      "roles": [
        "technical_officer"
      ]
    },
    {
      "name": "UNIVERSITY OF KIEL (DE)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "BRITISH ANTARCTIC SURVEY (GB)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "DUBLIN INSTITUTE FOR ADVANCED STUDIES (DIAS) (IE)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "GEOLOGICAL SURVEY OF DENMARK AND GREENLAND (DK)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "TU DELFT (NL)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "Technical University of Denmark (DK)",
      "roles": [
        "consortium_member"
      ]
    },
    {
      "name": "UNIVERSITY OF OSLO (NO)",
      "roles": [
        "consortium_member"
      ]
    }
  ],
  "updated": "2024-09-12T20:32:23.030110Z",
  "title": "3D-EARTH",
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
          "2019-10-22T00:00:00Z",
          "2020-12-11T23:59:59Z"
        ]
      ]
    }
  },
  "license": "proprietary",
  "keywords": []
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <osc:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .

<https://example.com/stac/osc/example-1/3d-earth> rdfs:label "3D-EARTH" ;
    dcterms:description "The goal of this project is establish a global 3D reference model model of the crust and upper mantle based on the analysis of satellite gravity and (electro) magnetic missions in combination with seismological models and analyse the feedback between processes in Earths deep mantle and the lithosphere. Selected case examples will provide the possibility to test these approaches on a global and regional scale. This will result in a framework for consistent models that will be used to link the crust and upper mantle to the dynamic mantle. The prime objective is to integrate, for the first time, seismological models and satellite observation towards a consistent image of the crust and upper mantle in 3D.  Satellite gravity and (electro) magnetic data help to transfer velocity images towards composition and temperature that reflect the tectonic state and evolution of the Earth and offer a novel understanding of the processes that shape our planet. The limitations and sensitivity of the different geophysical methods in context of their imaging capability are analysed and combined with forward and inverse modelling to be able to evaluate the possibilities of these approaches to reveal the Earths structure. For the inverse modelling, we will explore the sensitivity of joint inversion to the individual data sets and compare these to inversions relying on only a single or a few data sets. To analyse the structure of the deep mantle, we will try to combine knowledge about mantle conductivity and mineral physics with the geophysical observations. We will assess the role of Earths internal layering and mantle convection on the evolution of the Earths surface (dynamic topography). The data and methods we propose to use in this study will significantly supersede previous attempts and will be a first step towards an understanding of the Earth in space and time, a necessary step towards the development of a 4D Earth model." ;
    dcterms:extent [ ] ;
    dcterms:format "Collection" ;
    dcterms:license "proprietary" ;
    dcterms:modified "2024-09-12T20:32:23.030110Z" ;
    rdfs:seeAlso [ rdfs:label "EO4Society Link" ;
            ns1:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://eo4society.esa.int/projects/stse-3d-earth/> ],
        [ rdfs:label "Global Model of Crust and Upper Mantle_WINTERC-G_GOCE" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/products/crust-and-upper-mantle-model-3d-earth/collection.json> ],
        [ rdfs:label "Open Science Catalog" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/catalog.json> ],
        [ rdfs:label "Theme: Solid Earth" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/themes/solid-earth/catalog.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://esa-earthcode.github.io/open-science-catalog-metadata/projects/3d-earth/collection.json> ],
        [ rdfs:label "Geothermal Heat Flow Database and Map_Greenland_GOCE_SWARM" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <https://example.com/stac/products/geothermal-heat-flow-greenland-3d-earth/collection.json> ],
        [ rdfs:label "Website" ;
            ns1:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <http://www.3dearth.uni-kiel.de/en> ],
        [ rdfs:label "Projects" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/osc/catalog.json> ] ;
    thns:schemes [ thns:concepts [ thns:id "solid-earth" ] ;
            thns:scheme "https://github.com/stac-extensions/osc#theme" ] ;
    ns2:status "completed" ;
    ns2:type "project" .


```


### Product OSC extension fields in a Collection.
#### json
```json
{
  "type": "Collection",
  "id": "absolute-sea-level-heights-baltics-sar-hsu",
  "stac_version": "1.0.0",
  "description": "Time series of absolute sea level heights of tide gauge stations involved in the project BALTIC+ Geodetic SAR for Baltic Height System Unification (SAR-HSU). Product details available at: https://www.asg.ed.tum.de/fileadmin/w00cip/iapg/Baltic/SAR-HSU-TN-0019_Dataset_User_Manual.pdf",
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Open Science Catalog"
    },
    {
      "rel": "via",
      "href": "https://www.asg.ed.tum.de/fileadmin/w00cip/iapg/Baltic/SL-ABS.zip",
      "title": "Access"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Products"
    },
    {
      "rel": "related",
      "href": "../../projects/baltic-geodetic-sar-for-baltic-height-system-unification-sar-hsu/collection.json",
      "type": "application/json",
      "title": "Project: SAR-HSU"
    },
    {
      "rel": "related",
      "href": "../../themes/oceans/catalog.json",
      "type": "application/json",
      "title": "Theme: Oceans"
    },
    {
      "rel": "related",
      "href": "../../variables/sea-surface-height-anomaly-ssha/catalog.json",
      "type": "application/json",
      "title": "Variable: Sea Surface Height Anomaly (SSHA)"
    },
    {
      "rel": "related",
      "href": "../../eo-missions/goce/catalog.json",
      "type": "application/json",
      "title": "EO Mission: GOCE"
    },
    {
      "rel": "related",
      "href": "../../eo-missions/sentinel-1/catalog.json",
      "type": "application/json",
      "title": "EO Mission: Sentinel-1"
    },
    {
      "rel": "related",
      "href": "../../eo-missions/glonass/catalog.json",
      "type": "application/json",
      "title": "EO Mission: GLONASS"
    },
    {
      "rel": "self",
      "href": "https://esa-earthcode.github.io/open-science-catalog-metadata/products/absolute-sea-level-heights-baltics-sar-hsu/collection.json",
      "type": "application/json"
    }
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
  ],
  "osc:project": "baltic-geodetic-sar-for-baltic-height-system-unification-sar-hsu",
  "osc:status": "ongoing",
  "osc:region": "Baltics",
  "osc:type": "product",
  "created": "2021-07-07T00:00:00Z",
  "cf:parameter": [
    {
      "name": "absolute_sea_level_heights"
    }
  ],
  "themes": [
    {
      "scheme": "https://github.com/stac-extensions/osc#theme",
      "concepts": [
        {
          "id": "oceans"
        }
      ]
    }
  ],
  "osc:variables": [
    "sea-surface-height-anomaly-ssha"
  ],
  "osc:missions": [
    "goce",
    "sentinel-1",
    "glonass"
  ],
  "updated": "2024-09-12T20:32:06.209108Z",
  "title": "SL-ABS: Absolute Sea Level Heights_Baltics_Multimission",
  "extent": {
    "spatial": {
      "bbox": [
        [
          9.0405918788,
          53.8666553578,
          31.3371258934,
          66.1535071282
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2020-01-01T00:00:00Z",
          "2020-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "license": "proprietary",
  "keywords": [
    "Sea Surface Topography",
    "Sea Surface Height",
    "Sea Surface Height Anomaly (SSHA)"
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/osc/context.jsonld",
  "type": "Collection",
  "id": "absolute-sea-level-heights-baltics-sar-hsu",
  "stac_version": "1.0.0",
  "description": "Time series of absolute sea level heights of tide gauge stations involved in the project BALTIC+ Geodetic SAR for Baltic Height System Unification (SAR-HSU). Product details available at: https://www.asg.ed.tum.de/fileadmin/w00cip/iapg/Baltic/SAR-HSU-TN-0019_Dataset_User_Manual.pdf",
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json",
      "title": "Open Science Catalog"
    },
    {
      "rel": "via",
      "href": "https://www.asg.ed.tum.de/fileadmin/w00cip/iapg/Baltic/SL-ABS.zip",
      "title": "Access"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "Products"
    },
    {
      "rel": "related",
      "href": "../../projects/baltic-geodetic-sar-for-baltic-height-system-unification-sar-hsu/collection.json",
      "type": "application/json",
      "title": "Project: SAR-HSU"
    },
    {
      "rel": "related",
      "href": "../../themes/oceans/catalog.json",
      "type": "application/json",
      "title": "Theme: Oceans"
    },
    {
      "rel": "related",
      "href": "../../variables/sea-surface-height-anomaly-ssha/catalog.json",
      "type": "application/json",
      "title": "Variable: Sea Surface Height Anomaly (SSHA)"
    },
    {
      "rel": "related",
      "href": "../../eo-missions/goce/catalog.json",
      "type": "application/json",
      "title": "EO Mission: GOCE"
    },
    {
      "rel": "related",
      "href": "../../eo-missions/sentinel-1/catalog.json",
      "type": "application/json",
      "title": "EO Mission: Sentinel-1"
    },
    {
      "rel": "related",
      "href": "../../eo-missions/glonass/catalog.json",
      "type": "application/json",
      "title": "EO Mission: GLONASS"
    },
    {
      "rel": "self",
      "href": "https://esa-earthcode.github.io/open-science-catalog-metadata/products/absolute-sea-level-heights-baltics-sar-hsu/collection.json",
      "type": "application/json"
    }
  ],
  "stac_extensions": [
    "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
  ],
  "osc:project": "baltic-geodetic-sar-for-baltic-height-system-unification-sar-hsu",
  "osc:status": "ongoing",
  "osc:region": "Baltics",
  "osc:type": "product",
  "created": "2021-07-07T00:00:00Z",
  "cf:parameter": [
    {
      "name": "absolute_sea_level_heights"
    }
  ],
  "themes": [
    {
      "scheme": "https://github.com/stac-extensions/osc#theme",
      "concepts": [
        {
          "id": "oceans"
        }
      ]
    }
  ],
  "osc:variables": [
    "sea-surface-height-anomaly-ssha"
  ],
  "osc:missions": [
    "goce",
    "sentinel-1",
    "glonass"
  ],
  "updated": "2024-09-12T20:32:06.209108Z",
  "title": "SL-ABS: Absolute Sea Level Heights_Baltics_Multimission",
  "extent": {
    "spatial": {
      "bbox": [
        [
          9.0405918788,
          53.8666553578,
          31.3371258934,
          66.1535071282
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2020-01-01T00:00:00Z",
          "2020-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "license": "proprietary",
  "keywords": [
    "Sea Surface Topography",
    "Sea Surface Height",
    "Sea Surface Height Anomaly (SSHA)"
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <osc:> .
@prefix ns3: <cf:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .

<https://example.com/stac/osc/example-1/absolute-sea-level-heights-baltics-sar-hsu> rdfs:label "SL-ABS: Absolute Sea Level Heights_Baltics_Multimission" ;
    ns3:parameter [ ] ;
    dcterms:created "2021-07-07T00:00:00Z" ;
    dcterms:description "Time series of absolute sea level heights of tide gauge stations involved in the project BALTIC+ Geodetic SAR for Baltic Height System Unification (SAR-HSU). Product details available at: https://www.asg.ed.tum.de/fileadmin/w00cip/iapg/Baltic/SAR-HSU-TN-0019_Dataset_User_Manual.pdf" ;
    dcterms:extent [ ] ;
    dcterms:format "Collection" ;
    dcterms:license "proprietary" ;
    dcterms:modified "2024-09-12T20:32:06.209108Z" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://esa-earthcode.github.io/open-science-catalog-metadata/products/absolute-sea-level-heights-baltics-sar-hsu/collection.json> ],
        [ rdfs:label "Variable: Sea Surface Height Anomaly (SSHA)" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/variables/sea-surface-height-anomaly-ssha/catalog.json> ],
        [ rdfs:label "EO Mission: GOCE" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/eo-missions/goce/catalog.json> ],
        [ rdfs:label "Theme: Oceans" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/themes/oceans/catalog.json> ],
        [ rdfs:label "Project: SAR-HSU" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/projects/baltic-geodetic-sar-for-baltic-height-system-unification-sar-hsu/collection.json> ],
        [ rdfs:label "EO Mission: Sentinel-1" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/eo-missions/sentinel-1/catalog.json> ],
        [ rdfs:label "Open Science Catalog" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/catalog.json> ],
        [ rdfs:label "Products" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/osc/catalog.json> ],
        [ rdfs:label "Access" ;
            ns1:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://www.asg.ed.tum.de/fileadmin/w00cip/iapg/Baltic/SL-ABS.zip> ],
        [ rdfs:label "EO Mission: GLONASS" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/stac/eo-missions/glonass/catalog.json> ] ;
    thns:schemes [ thns:concepts [ thns:id "oceans" ] ;
            thns:scheme "https://github.com/stac-extensions/osc#theme" ] ;
    ns2:missions "glonass",
        "goce",
        "sentinel-1" ;
    ns2:project "baltic-geodetic-sar-for-baltic-height-system-unification-sar-hsu" ;
    ns2:region "Baltics" ;
    ns2:status "ongoing" ;
    ns2:type "product" ;
    ns2:variables "sea-surface-height-anomaly-ssha" .


```


### Product OSC  extension fields in a STAC item.
#### json
```json
{
  "type": "Feature",
  "id": "example",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json"
  ],
  "geometry": null,
  "properties": {
    "osc:missions": [
      "SWARM"
    ],
    "osc:project": "4DIONOSPHERE (SWARM VIP)",
    "osc:variables": [
      "Ionospheric plasma density"
    ],
    "osc:status": "completed",
    "osc:type": "product",
    "themes": [
      {
        "concepts": [
          {
            "id": "magnetosphere-ionosphere",
            "title": "Magnetosphere Ionosphere"
          }
        ],
        "scheme": "https://github.com/stac-extensions/osc#theme"
      }
    ],
    "keywords": [
      "theme:Magnetosphere_Ionosphere",
      "variable:Ionospheric plasma density",
      "region:None"
    ],
    "datetime": "2023-03-15T16:24:03.357451Z"
  },
  "collection": "model-ionosphere-4dionosphere",
  "links": [
    {
      "rel": "parent",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Semi-empiric model of ionosphere processes_SWARM"
    },
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Semi-empiric model of ionosphere processes_SWARM"
    },
    {
      "rel": "root",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "SWARM VIP"
    }
  ],
  "assets": {
    "model": {
      "href": "https://osc.example/model.xyz",
      "type": "application/octet-stream"
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/osc/context.jsonld",
  "type": "Feature",
  "id": "example",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
    "https://stac-extensions.github.io/themes/v1.0.0/schema.json"
  ],
  "geometry": null,
  "properties": {
    "osc:missions": [
      "SWARM"
    ],
    "osc:project": "4DIONOSPHERE (SWARM VIP)",
    "osc:variables": [
      "Ionospheric plasma density"
    ],
    "osc:status": "completed",
    "osc:type": "product",
    "themes": [
      {
        "concepts": [
          {
            "id": "magnetosphere-ionosphere",
            "title": "Magnetosphere Ionosphere"
          }
        ],
        "scheme": "https://github.com/stac-extensions/osc#theme"
      }
    ],
    "keywords": [
      "theme:Magnetosphere_Ionosphere",
      "variable:Ionospheric plasma density",
      "region:None"
    ],
    "datetime": "2023-03-15T16:24:03.357451Z"
  },
  "collection": "model-ionosphere-4dionosphere",
  "links": [
    {
      "rel": "parent",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Semi-empiric model of ionosphere processes_SWARM"
    },
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Semi-empiric model of ionosphere processes_SWARM"
    },
    {
      "rel": "root",
      "href": "../catalog.json",
      "type": "application/json",
      "title": "SWARM VIP"
    }
  ],
  "assets": {
    "model": {
      "href": "https://osc.example/model.xyz",
      "type": "application/octet-stream"
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <osc:> .
@prefix ns3: <https://w3id.org/ogc/stac/core/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/osc/example-2/example> dcterms:date "2023-03-15T16:24:03.357451+00:00"^^xsd:dateTime ;
    dcterms:format "Feature" ;
    rdfs:seeAlso [ rdfs:label "SWARM VIP" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/osc/catalog.json> ],
        [ rdfs:label "Semi-empiric model of ionosphere processes_SWARM" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/osc/example-2/collection.json> ],
        [ rdfs:label "Semi-empiric model of ionosphere processes_SWARM" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/osc/example-2/collection.json> ] ;
    ns3:assets <https://example.com/stac/osc/example-2/model> ;
    thns:schemes [ thns:concepts [ rdfs:label "Magnetosphere Ionosphere" ;
                    thns:id "magnetosphere-ionosphere" ] ;
            thns:scheme "https://github.com/stac-extensions/osc#theme" ] ;
    ns2:missions "SWARM" ;
    ns2:project "4DIONOSPHERE (SWARM VIP)" ;
    ns2:status "completed" ;
    ns2:type "product" ;
    ns2:variables "Ionospheric plasma density" .

<https://example.com/stac/osc/example-2/model> dcterms:format "application/octet-stream" ;
    oa:hasTarget <https://osc.example/model.xyz> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: STAC Extension for the ESA Open Science Catalog
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-v1-0-0/schema.yaml
- $ref: https://stac-extensions.github.io/osc/v1.0.0/schema.json
x-jsonld-extra-terms:
  themes:
    x-jsonld-id: https://w3id.org/ogc/stac/themes/schemes
    x-jsonld-container: '@set'
  concepts:
    x-jsonld-id: https://w3id.org/ogc/stac/themes/concepts
    x-jsonld-container: '@set'
    x-jsonld-context:
      name: https://w3id.org/ogc/stac/themes/name
      id: https://w3id.org/ogc/stac/themes/id
      url: '@id'
  scheme: https://w3id.org/ogc/stac/themes/scheme
x-jsonld-prefixes:
  thns: https://w3id.org/ogc/stac/themes/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/osc/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/osc/schema.yaml)


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
    "type": "dct:format",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
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
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "type": "@type"
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
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
    "description": "dct:description",
    "license": "dct:license",
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
      "@id": "https://w3id.org/ogc/stac/core/assets",
      "@container": "@id",
      "@context": {
        "thumbnail": "stac:thumbnail",
        "overview": "stac:overview",
        "data": "stac:data",
        "metadata": "stac:metadata",
        "title": "dct:title",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      }
    },
    "media_type": "dct:format",
    "themes": {
      "@id": "thns:schemes",
      "@container": "@set"
    },
    "concepts": {
      "@id": "thns:concepts",
      "@container": "@set",
      "@context": {
        "name": "thns:name",
        "id": "thns:id",
        "url": "@id"
      }
    },
    "scheme": "thns:scheme",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "geojson": "https://purl.org/geojson/vocab#",
    "stac": "http://stacspec.org/ontology/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/osc/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/osc)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/osc`

