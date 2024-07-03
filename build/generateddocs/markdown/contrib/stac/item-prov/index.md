
# STAC Item with Provenance (Schema)

`ogc.contrib.stac.item-prov` *v0.1*

A SpatioTemporal Asset Catalogs (STAC) item with a provenance trace supporting the PROV-O model and DAG (directed acyclic graph) through both object nesting and references

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC item with link to provenance
This is the simple item example from the STAC specification, augmented with the simplest possible form of provenance - a link to a resource that provides provenance details. 

a STAC item is a prov:Entity with the "wasGeneratedBy" property defined by PROV-O.

#### json
```json

{
    "stac_version": "1.0.0",
    "stac_extensions": ["https://stac-extensions.github.io/prov/v1.0.0/schema.json"],
    "type": "Feature",
    "id": "20201211_223832_CS2",
    "bbox": [
      172.91173669923782,
      1.3438851951615003,
      172.95469614953714,
      1.3690476620161975
    ],
    "wasGeneratedBy":  "http://mysystem.io/prov?object=20201211_223832_CS2" ,
    "geometry": {
      "type": "Point",
      "coordinates": [
        
          
            172.91173669923782,
            1.3438851951615003
          
      ]
    },
    "properties": {
      "datetime": "2020-12-11T22:38:32.125000Z"
    },
    "collection": "simple-collection",
    "links": [
      {
        "rel": "collection",
        "href": "./collection.json",
        "type": "application/json",
        "title": "Simple Example Collection"
      }
    ],
    "assets": {
    }
  }
```

#### jsonld
```jsonld
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "bbox": [
    172.91173669923782,
    1.3438851951615003,
    172.95469614953714,
    1.3690476620161975
  ],
  "wasGeneratedBy": "http://mysystem.io/prov?object=20201211_223832_CS2",
  "geometry": {
    "type": "Point",
    "coordinates": [
      172.91173669923782,
      1.3438851951615003
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32.125000Z"
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    }
  ],
  "assets": {},
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-prov/context.jsonld"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/example1/20201211_223832_CS2> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ] ;
    prov:wasGeneratedBy <http://mysystem.io/prov?object=20201211_223832_CS2> ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.729117e+02 1.343885e+00 ) ] .


```


### STAC item with a generation activity description
This is the simple item example from the STAC specification, augmented a description of the activity that generated it, with nested set of entities the object derives from. 

A STAC item is a prov:Entity with the "wasGeneratedBy" property defined by PROV-O. 

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "bbox": [
    172.91173669923782,
    1.3438851951615003,
    172.95469614953714,
    1.3690476620161975
  ],
  "wasGeneratedBy": {
    "provType": "Activity",
    "id": "surveys:DP-1-S1",
    "activityType": "InitialSurvey",
    "endedAtTime": "2023-10-05T05:03:15+01:00",
    "wasAssociatedWith": "staff:jd234",
    "used": {
      "id": "regulations:Act3",
      "entityType": "Legislation",
      "wasAttributedTo": "agents:someGovernment",
      "links": [
        {
          "href": "https://some.gov/linktoact/",
          "rel": "related"
        }
      ]
    }
  },
  "geometry": {
    "type": "Point",
    "coordinates": [
      172.91173669923782,
      1.3438851951615003
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32.125000Z"
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    }
  ],
  "assets": {}
}
```

#### jsonld
```jsonld
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "bbox": [
    172.91173669923782,
    1.3438851951615003,
    172.95469614953714,
    1.3690476620161975
  ],
  "wasGeneratedBy": {
    "provType": "Activity",
    "id": "surveys:DP-1-S1",
    "activityType": "InitialSurvey",
    "endedAtTime": "2023-10-05T05:03:15+01:00",
    "wasAssociatedWith": "staff:jd234",
    "used": {
      "id": "regulations:Act3",
      "entityType": "Legislation",
      "wasAttributedTo": "agents:someGovernment",
      "links": [
        {
          "href": "https://some.gov/linktoact/",
          "rel": "related"
        }
      ]
    }
  },
  "geometry": {
    "type": "Point",
    "coordinates": [
      172.91173669923782,
      1.3438851951615003
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32.125000Z"
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    }
  ],
  "assets": {},
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-prov/context.jsonld"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/example1/20201211_223832_CS2> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ] ;
    prov:wasGeneratedBy <surveys:DP-1-S1> ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.729117e+02 1.343885e+00 ) ] .

<regulations:Act3> a <https://example.com/stac/example1/Legislation> ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://some.gov/linktoact/> ] ;
    prov:wasAttributedTo <agents:someGovernment> .

<surveys:DP-1-S1> a prov:Activity,
        <https://example.com/stac/example1/InitialSurvey> ;
    prov:endedAtTime "2023-10-05T05:03:15+01:00"^^xsd:dateTime ;
    prov:used <regulations:Act3> ;
    prov:wasAssociatedWith <staff:jd234> .


```


### STAC item with a provenance graph
This is the simple item example from the STAC specification, augmented an array of Provenance objects that define a DAG (Directed Acyclic Graph) that can fully describe a set of contributing activities, entities and agents.) 

A STAC item is a prov:Entity with the "has_provenance" property whose range is an array of objects defined by the PROV-O model. 

#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "bbox": [
    172.91173669923782,
    1.3438851951615003,
    172.95469614953714,
    1.3690476620161975
  ],
  "has_provenance": [
    {
      "id": "DP-2223",
      "provType": "Entity",
      "featureType": "ftc:SomeKindOfSurvey",
      "wasGeneratedBy": "surveys:DP-1-S1"
    },
    {
      "provType": "Activity",
      "id": "surveys:DP-1-S1",
      "activityType": "InitialSurvey",
      "endedAtTime": "2023-10-05T05:03:15+01:00",
      "wasAssociatedWith": "staff:jd234",
      "used": {
        "id": "regulations:Act3",
        "entityType": "Legislation",
        "wasAttributedTo": "agents:someGovernment",
        "links": [
          {
            "href": "https://some.gov/linktoact/",
            "rel": "related"
          }
        ]
      }
    }
  ],
  "geometry": {
    "type": "Point",
    "coordinates": [
      172.91173669923782,
      1.3438851951615003
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32.125000Z"
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    }
  ],
  "assets": {}
}
```

#### jsonld
```jsonld
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "20201211_223832_CS2",
  "bbox": [
    172.91173669923782,
    1.3438851951615003,
    172.95469614953714,
    1.3690476620161975
  ],
  "has_provenance": [
    {
      "id": "DP-2223",
      "provType": "Entity",
      "featureType": "ftc:SomeKindOfSurvey",
      "wasGeneratedBy": "surveys:DP-1-S1"
    },
    {
      "provType": "Activity",
      "id": "surveys:DP-1-S1",
      "activityType": "InitialSurvey",
      "endedAtTime": "2023-10-05T05:03:15+01:00",
      "wasAssociatedWith": "staff:jd234",
      "used": {
        "id": "regulations:Act3",
        "entityType": "Legislation",
        "wasAttributedTo": "agents:someGovernment",
        "links": [
          {
            "href": "https://some.gov/linktoact/",
            "rel": "related"
          }
        ]
      }
    }
  ],
  "geometry": {
    "type": "Point",
    "coordinates": [
      172.91173669923782,
      1.3438851951615003
    ]
  },
  "properties": {
    "datetime": "2020-12-11T22:38:32.125000Z"
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    }
  ],
  "assets": {},
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-prov/context.jsonld"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/example1/20201211_223832_CS2> a geojson:Feature ;
    dcterms:provenance <https://example.com/stac/example1/DP-2223>,
        <surveys:DP-1-S1> ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ] ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.729117e+02 1.343885e+00 ) ] .

<https://example.com/stac/example1/DP-2223> a <ftc:SomeKindOfSurvey>,
        prov:Entity ;
    prov:wasGeneratedBy <surveys:DP-1-S1> .

<regulations:Act3> a <https://example.com/stac/example1/Legislation> ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://some.gov/linktoact/> ] ;
    prov:wasAttributedTo <agents:someGovernment> .

<surveys:DP-1-S1> a prov:Activity,
        <https://example.com/stac/example1/InitialSurvey> ;
    prov:endedAtTime "2023-10-05T05:03:15+01:00"^^xsd:dateTime ;
    prov:used <regulations:Act3> ;
    prov:wasAssociatedWith <staff:jd234> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: STAC Collection
allOf:
- $ref: https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.yaml#/$defs/Entity
- $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- type: object
  properties:
    stac_extensions:
      type: array
      contains:
        const: https://stac-extensions.github.io/prov/v1.0.0/schema.json

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-prov/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-prov/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "featureType": "@type",
    "entityType": "@type",
    "has_provenance": {
      "@context": {
        "activityType": "@type",
        "endedAtTime": {
          "@id": "prov:endedAtTime",
          "@type": "xsd:dateTime"
        },
        "wasAssociatedWith": {
          "@context": {
            "type": "dct:type"
          },
          "@id": "prov:wasAssociatedWith",
          "@type": "@id"
        },
        "wasInformedBy": {
          "@id": "prov:wasInformedBy",
          "@type": "@id"
        },
        "used": {
          "@id": "prov:used",
          "@type": "@id"
        },
        "wasStartedBy": {
          "@id": "prov:wasStartedBy",
          "@type": "@id"
        },
        "wasEndedBy": {
          "@id": "prov:wasEndedBy",
          "@type": "@id"
        },
        "invalidated": {
          "@id": "prov:invalidated",
          "@type": "@id"
        },
        "generated": {
          "@id": "prov:generated",
          "@type": "@id"
        },
        "qualifiedUsage": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedUsage",
          "@type": "@id"
        },
        "qualifiedCommunication": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedCommunication",
          "@type": "@id"
        },
        "qualifiedStart": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedStart",
          "@type": "@id"
        },
        "qualifiedEnd": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedEnd",
          "@type": "@id"
        },
        "qualifiedAssociation": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "hadPlan": {
              "@id": "prov:hadPlan",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAssociation",
          "@type": "@id"
        },
        "agentType": "@type",
        "name": "rdfs:label",
        "actedOnBehalfOf": {
          "@context": {
            "type": "dct:type"
          },
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedDelegation",
          "@type": "@id"
        }
      },
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@context": {
        "activityType": "@type",
        "endedAtTime": {
          "@id": "prov:endedAtTime",
          "@type": "xsd:dateTime"
        },
        "wasAssociatedWith": {
          "@context": {
            "type": "dct:type",
            "agentType": "@type",
            "name": "rdfs:label",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedDelegation",
              "@type": "@id"
            }
          },
          "@id": "prov:wasAssociatedWith",
          "@type": "@id"
        },
        "wasInformedBy": {
          "@id": "prov:wasInformedBy",
          "@type": "@id"
        },
        "used": {
          "@id": "prov:used",
          "@type": "@id"
        },
        "wasStartedBy": {
          "@id": "prov:wasStartedBy",
          "@type": "@id"
        },
        "wasEndedBy": {
          "@id": "prov:wasEndedBy",
          "@type": "@id"
        },
        "invalidated": {
          "@id": "prov:invalidated",
          "@type": "@id"
        },
        "generated": {
          "@id": "prov:generated",
          "@type": "@id"
        },
        "qualifiedUsage": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedUsage",
          "@type": "@id"
        },
        "qualifiedCommunication": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedCommunication",
          "@type": "@id"
        },
        "qualifiedStart": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedStart",
          "@type": "@id"
        },
        "qualifiedEnd": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedEnd",
          "@type": "@id"
        },
        "qualifiedAssociation": {
          "@context": {
            "agent": {
              "@context": {
                "agentType": "@type",
                "name": "rdfs:label",
                "actedOnBehalfOf": {
                  "@context": {
                    "type": "dct:type"
                  },
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@context": {
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id"
                }
              },
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "hadPlan": {
              "@id": "prov:hadPlan",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAssociation",
          "@type": "@id"
        }
      },
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@context": {
        "type": "dct:type",
        "agentType": "@type",
        "name": "rdfs:label",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@context": {
                "activityType": "@type",
                "endedAtTime": {
                  "@id": "prov:endedAtTime",
                  "@type": "xsd:dateTime"
                },
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "wasInformedBy": {
                  "@id": "prov:wasInformedBy",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "xsd:dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id"
                },
                "qualifiedCommunication": {
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "xsd:dateTime"
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedCommunication",
                  "@type": "@id"
                },
                "qualifiedStart": {
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "xsd:dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedStart",
                  "@type": "@id"
                },
                "qualifiedEnd": {
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "xsd:dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id"
                },
                "qualifiedAssociation": {
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id"
                }
              },
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedDelegation",
          "@type": "@id"
        }
      },
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "wasInvalidatedBy": {
      "@context": {
        "activityType": "@type",
        "endedAtTime": {
          "@id": "prov:endedAtTime",
          "@type": "xsd:dateTime"
        },
        "wasAssociatedWith": {
          "@context": {
            "type": "dct:type",
            "agentType": "@type",
            "name": "rdfs:label",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedDelegation",
              "@type": "@id"
            }
          },
          "@id": "prov:wasAssociatedWith",
          "@type": "@id"
        },
        "wasInformedBy": {
          "@id": "prov:wasInformedBy",
          "@type": "@id"
        },
        "used": {
          "@id": "prov:used",
          "@type": "@id"
        },
        "wasStartedBy": {
          "@id": "prov:wasStartedBy",
          "@type": "@id"
        },
        "wasEndedBy": {
          "@id": "prov:wasEndedBy",
          "@type": "@id"
        },
        "invalidated": {
          "@id": "prov:invalidated",
          "@type": "@id"
        },
        "generated": {
          "@id": "prov:generated",
          "@type": "@id"
        },
        "qualifiedUsage": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedUsage",
          "@type": "@id"
        },
        "qualifiedCommunication": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedCommunication",
          "@type": "@id"
        },
        "qualifiedStart": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedStart",
          "@type": "@id"
        },
        "qualifiedEnd": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedEnd",
          "@type": "@id"
        },
        "qualifiedAssociation": {
          "@context": {
            "agent": {
              "@context": {
                "agentType": "@type",
                "name": "rdfs:label",
                "actedOnBehalfOf": {
                  "@context": {
                    "type": "dct:type"
                  },
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@context": {
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id"
                }
              },
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "hadPlan": {
              "@id": "prov:hadPlan",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAssociation",
          "@type": "@id"
        }
      },
      "@id": "prov:wasInvalidatedBy",
      "@type": "@id"
    },
    "wasQuotedFrom": {
      "@id": "prov:wasQuotedFrom",
      "@type": "@id"
    },
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "links": {
      "@context": {
        "type": "dct:type"
      },
      "@id": "rdfs:seeAlso"
    },
    "qualifiedGeneration": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "influencer": {
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "hadActivity": {
          "@context": {
            "activityType": "@type",
            "endedAtTime": {
              "@id": "prov:endedAtTime",
              "@type": "xsd:dateTime"
            },
            "wasAssociatedWith": {
              "@context": {
                "type": "dct:type",
                "agentType": "@type",
                "name": "rdfs:label",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id"
                }
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "wasInformedBy": {
              "@id": "prov:wasInformedBy",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedUsage",
              "@type": "@id"
            },
            "qualifiedCommunication": {
              "@id": "prov:qualifiedCommunication",
              "@type": "@id"
            },
            "qualifiedStart": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedStart",
              "@type": "@id"
            },
            "qualifiedEnd": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedEnd",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "agentType": "@type",
                    "name": "rdfs:label",
                    "actedOnBehalfOf": {
                      "@context": {
                        "type": "dct:type"
                      },
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        },
        "activity": {
          "@context": {
            "activityType": "@type",
            "endedAtTime": {
              "@id": "prov:endedAtTime",
              "@type": "xsd:dateTime"
            },
            "wasAssociatedWith": {
              "@context": {
                "type": "dct:type",
                "agentType": "@type",
                "name": "rdfs:label",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id"
                }
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "wasInformedBy": {
              "@id": "prov:wasInformedBy",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedUsage",
              "@type": "@id"
            },
            "qualifiedCommunication": {
              "@id": "prov:qualifiedCommunication",
              "@type": "@id"
            },
            "qualifiedStart": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedStart",
              "@type": "@id"
            },
            "qualifiedEnd": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedEnd",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "agentType": "@type",
                    "name": "rdfs:label",
                    "actedOnBehalfOf": {
                      "@context": {
                        "type": "dct:type"
                      },
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:activity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedGeneration",
      "@type": "@id"
    },
    "qualifiedInvalidation": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "influencer": {
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "hadActivity": {
          "@context": {
            "activityType": "@type",
            "endedAtTime": {
              "@id": "prov:endedAtTime",
              "@type": "xsd:dateTime"
            },
            "wasAssociatedWith": {
              "@context": {
                "type": "dct:type",
                "agentType": "@type",
                "name": "rdfs:label",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id"
                }
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "wasInformedBy": {
              "@id": "prov:wasInformedBy",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedUsage",
              "@type": "@id"
            },
            "qualifiedCommunication": {
              "@id": "prov:qualifiedCommunication",
              "@type": "@id"
            },
            "qualifiedStart": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedStart",
              "@type": "@id"
            },
            "qualifiedEnd": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedEnd",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "agentType": "@type",
                    "name": "rdfs:label",
                    "actedOnBehalfOf": {
                      "@context": {
                        "type": "dct:type"
                      },
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        },
        "activity": {
          "@context": {
            "activityType": "@type",
            "endedAtTime": {
              "@id": "prov:endedAtTime",
              "@type": "xsd:dateTime"
            },
            "wasAssociatedWith": {
              "@context": {
                "type": "dct:type",
                "agentType": "@type",
                "name": "rdfs:label",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id"
                }
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "wasInformedBy": {
              "@id": "prov:wasInformedBy",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedUsage",
              "@type": "@id"
            },
            "qualifiedCommunication": {
              "@id": "prov:qualifiedCommunication",
              "@type": "@id"
            },
            "qualifiedStart": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedStart",
              "@type": "@id"
            },
            "qualifiedEnd": {
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedEnd",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "agentType": "@type",
                    "name": "rdfs:label",
                    "actedOnBehalfOf": {
                      "@context": {
                        "type": "dct:type"
                      },
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:activity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedInvalidation",
      "@type": "@id"
    },
    "qualifiedDerivation": {
      "@context": {
        "hadGeneration": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "activity": {
              "@context": {
                "activityType": "@type",
                "endedAtTime": {
                  "@id": "prov:endedAtTime",
                  "@type": "xsd:dateTime"
                },
                "wasAssociatedWith": {
                  "@context": {
                    "type": "dct:type",
                    "agentType": "@type",
                    "name": "rdfs:label",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "wasInformedBy": {
                  "@id": "prov:wasInformedBy",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id"
                },
                "qualifiedCommunication": {
                  "@id": "prov:qualifiedCommunication",
                  "@type": "@id"
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id"
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id"
                },
                "qualifiedAssociation": {
                  "@context": {
                    "agent": {
                      "@context": {
                        "agentType": "@type",
                        "name": "rdfs:label",
                        "actedOnBehalfOf": {
                          "@context": {
                            "type": "dct:type"
                          },
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id"
                }
              },
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:hadGeneration",
          "@type": "@id"
        },
        "hadActivity": {
          "@context": {
            "activityType": "@type",
            "endedAtTime": {
              "@id": "prov:endedAtTime",
              "@type": "xsd:dateTime"
            },
            "wasAssociatedWith": {
              "@context": {
                "type": "dct:type",
                "agentType": "@type",
                "name": "rdfs:label",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id"
                }
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "wasInformedBy": {
              "@id": "prov:wasInformedBy",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                }
              },
              "@id": "prov:qualifiedUsage",
              "@type": "@id"
            },
            "qualifiedCommunication": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedCommunication",
              "@type": "@id"
            },
            "qualifiedStart": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                }
              },
              "@id": "prov:qualifiedStart",
              "@type": "@id"
            },
            "qualifiedEnd": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                }
              },
              "@id": "prov:qualifiedEnd",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "agentType": "@type",
                    "name": "rdfs:label",
                    "actedOnBehalfOf": {
                      "@context": {
                        "type": "dct:type"
                      },
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        },
        "hadUsage": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            }
          },
          "@id": "prov:hadUsage",
          "@type": "@id"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedAttribution": {
      "@context": {
        "agent": {
          "@context": {
            "agentType": "@type",
            "name": "rdfs:label",
            "actedOnBehalfOf": {
              "@context": {
                "type": "dct:type"
              },
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@context": {
                "hadActivity": {
                  "@context": {
                    "activityType": "@type",
                    "endedAtTime": {
                      "@id": "prov:endedAtTime",
                      "@type": "xsd:dateTime"
                    },
                    "wasAssociatedWith": {
                      "@context": {
                        "type": "dct:type"
                      },
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "wasInformedBy": {
                      "@id": "prov:wasInformedBy",
                      "@type": "@id"
                    },
                    "used": {
                      "@id": "prov:used",
                      "@type": "@id"
                    },
                    "wasStartedBy": {
                      "@id": "prov:wasStartedBy",
                      "@type": "@id"
                    },
                    "wasEndedBy": {
                      "@id": "prov:wasEndedBy",
                      "@type": "@id"
                    },
                    "invalidated": {
                      "@id": "prov:invalidated",
                      "@type": "@id"
                    },
                    "generated": {
                      "@id": "prov:generated",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "xsd:dateTime"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id"
                    },
                    "qualifiedCommunication": {
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "xsd:dateTime"
                        },
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedCommunication",
                      "@type": "@id"
                    },
                    "qualifiedStart": {
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "xsd:dateTime"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedStart",
                      "@type": "@id"
                    },
                    "qualifiedEnd": {
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "xsd:dateTime"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedDelegation",
              "@type": "@id"
            }
          },
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedAttribution",
      "@type": "@id"
    },
    "wasInfluencedBy": {
      "@context": {
        "activityType": "@type",
        "endedAtTime": {
          "@id": "prov:endedAtTime",
          "@type": "xsd:dateTime"
        },
        "wasAssociatedWith": {
          "@id": "prov:wasAssociatedWith",
          "@type": "@id"
        },
        "wasInformedBy": {
          "@id": "prov:wasInformedBy",
          "@type": "@id"
        },
        "used": {
          "@id": "prov:used",
          "@type": "@id"
        },
        "wasStartedBy": {
          "@id": "prov:wasStartedBy",
          "@type": "@id"
        },
        "wasEndedBy": {
          "@id": "prov:wasEndedBy",
          "@type": "@id"
        },
        "invalidated": {
          "@id": "prov:invalidated",
          "@type": "@id"
        },
        "generated": {
          "@id": "prov:generated",
          "@type": "@id"
        },
        "qualifiedUsage": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedUsage",
          "@type": "@id"
        },
        "qualifiedCommunication": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedCommunication",
          "@type": "@id"
        },
        "qualifiedStart": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedStart",
          "@type": "@id"
        },
        "qualifiedEnd": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedEnd",
          "@type": "@id"
        },
        "qualifiedAssociation": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "hadPlan": {
              "@id": "prov:hadPlan",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAssociation",
          "@type": "@id"
        },
        "type": "dct:type",
        "agentType": "@type",
        "name": "rdfs:label",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedDelegation",
          "@type": "@id"
        }
      },
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@context": {
        "influencer": {
          "@context": {
            "activityType": "@type",
            "endedAtTime": {
              "@id": "prov:endedAtTime",
              "@type": "xsd:dateTime"
            },
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "wasInformedBy": {
              "@id": "prov:wasInformedBy",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                }
              },
              "@id": "prov:qualifiedUsage",
              "@type": "@id"
            },
            "qualifiedCommunication": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedCommunication",
              "@type": "@id"
            },
            "qualifiedStart": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedStart",
              "@type": "@id"
            },
            "qualifiedEnd": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedEnd",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            },
            "type": "dct:type",
            "agentType": "@type",
            "name": "rdfs:label",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@context": {
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedDelegation",
              "@type": "@id"
            }
          },
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id"
        },
        "activity": {
          "@context": {
            "activityType": "@type",
            "endedAtTime": {
              "@id": "prov:endedAtTime",
              "@type": "xsd:dateTime"
            },
            "wasAssociatedWith": {
              "@context": {
                "type": "dct:type",
                "agentType": "@type",
                "name": "rdfs:label",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@context": {
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id"
                }
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "wasInformedBy": {
              "@id": "prov:wasInformedBy",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                }
              },
              "@id": "prov:qualifiedUsage",
              "@type": "@id"
            },
            "qualifiedCommunication": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedCommunication",
              "@type": "@id"
            },
            "qualifiedStart": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedStart",
              "@type": "@id"
            },
            "qualifiedEnd": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedEnd",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "agentType": "@type",
                    "name": "rdfs:label",
                    "actedOnBehalfOf": {
                      "@context": {
                        "type": "dct:type"
                      },
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@context": {
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:activity",
          "@type": "@id"
        },
        "agent": {
          "@context": {
            "type": "dct:type",
            "agentType": "@type",
            "name": "rdfs:label",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@context": {
                "hadActivity": {
                  "@context": {
                    "activityType": "@type",
                    "endedAtTime": {
                      "@id": "prov:endedAtTime",
                      "@type": "xsd:dateTime"
                    },
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "wasInformedBy": {
                      "@id": "prov:wasInformedBy",
                      "@type": "@id"
                    },
                    "used": {
                      "@id": "prov:used",
                      "@type": "@id"
                    },
                    "wasStartedBy": {
                      "@id": "prov:wasStartedBy",
                      "@type": "@id"
                    },
                    "wasEndedBy": {
                      "@id": "prov:wasEndedBy",
                      "@type": "@id"
                    },
                    "invalidated": {
                      "@id": "prov:invalidated",
                      "@type": "@id"
                    },
                    "generated": {
                      "@id": "prov:generated",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "xsd:dateTime"
                        }
                      },
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id"
                    },
                    "qualifiedCommunication": {
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "xsd:dateTime"
                        },
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedCommunication",
                      "@type": "@id"
                    },
                    "qualifiedStart": {
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "xsd:dateTime"
                        }
                      },
                      "@id": "prov:qualifiedStart",
                      "@type": "@id"
                    },
                    "qualifiedEnd": {
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "xsd:dateTime"
                        }
                      },
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      },
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id"
                    }
                  },
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedDelegation",
              "@type": "@id"
            }
          },
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "provType": "@type",
    "hadMember": {
      "@context": {},
      "@id": "prov:hadMember",
      "@type": "@id"
    },
    "type": "@type",
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
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
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
    "created": "dct:created",
    "updated": "dct:modified",
    "uriTemplate": {
      "@type": "xsd:string",
      "@id": "oa:hasTarget"
    },
    "Activity": "prov:Activity",
    "ActivityInfluence": "prov:ActivityInfluence",
    "Agent": "prov:Agent",
    "AgentInfluence": "prov:AgentInfluence",
    "Association": "prov:Association",
    "Attribution": "prov:Attribution",
    "Bundle": "prov:Bundle",
    "Collection": "prov:Collection",
    "Communication": "prov:Communication",
    "Delegation": "prov:Delegation",
    "Derivation": "prov:Derivation",
    "EmptyCollection": "prov:EmptyCollection",
    "End": "prov:End",
    "Entity": "prov:Entity",
    "EntityInfluence": "prov:EntityInfluence",
    "Generation": "prov:Generation",
    "Influence": "prov:Influence",
    "InstantaneousEvent": "prov:InstantaneousEvent",
    "Invalidation": "prov:Invalidation",
    "Location": "prov:Location",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "prov:Role",
    "SoftwareAgent": "prov:SoftwareAgent",
    "Start": "prov:Start",
    "Usage": "prov:Usage",
    "ServiceDescription": "prov:ServiceDescription",
    "DirectQueryService": "prov:DirectQueryService",
    "Accept": "prov:Accept",
    "Contribute": "prov:Contribute",
    "Contributor": "prov:Contributor",
    "Copyright": "prov:Copyright",
    "Create": "prov:Create",
    "Creator": "prov:Creator",
    "Modify": "prov:Modify",
    "Publish": "prov:Publish",
    "Publisher": "prov:Publisher",
    "Replace": "prov:Replace",
    "RightsAssignment": "prov:RightsAssignment",
    "RightsHolder": "prov:RightsHolder",
    "Submit": "prov:Submit",
    "Dictionary": "prov:Dictionary",
    "EmptyDictionary": "prov:EmptyDictionary",
    "KeyEntityPair": "prov:KeyEntityPair",
    "Insertion": "prov:Insertion",
    "Removal": "prov:Removal",
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "prov:value",
    "provenanceUriTemplate": "prov:provenanceUriTemplate",
    "pairKey": {
      "@id": "prov:pairKey",
      "@type": "rdfs:Literal"
    },
    "removedKey": {
      "@id": "prov:removedKey",
      "@type": "rdfs:Literal"
    },
    "influenced": {
      "@id": "prov:influenced",
      "@type": "@id"
    },
    "qualifiedPrimarySource": {
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_query_service": {
      "@id": "prov:has_query_service",
      "@type": "@id"
    },
    "describesService": {
      "@id": "prov:describesService",
      "@type": "@id"
    },
    "pingback": {
      "@id": "prov:pingback",
      "@type": "@id"
    },
    "dictionary": {
      "@id": "prov:dictionary",
      "@type": "@id"
    },
    "derivedByInsertionFrom": {
      "@id": "prov:derivedByInsertionFrom",
      "@type": "@id"
    },
    "derivedByRemovalFrom": {
      "@id": "prov:derivedByRemovalFrom",
      "@type": "@id"
    },
    "insertedKeyEntityPair": {
      "@id": "prov:insertedKeyEntityPair",
      "@type": "@id"
    },
    "hadDictionaryMember": {
      "@id": "prov:hadDictionaryMember",
      "@type": "@id"
    },
    "pairEntity": {
      "@id": "prov:pairEntity",
      "@type": "@id"
    },
    "qualifiedInsertion": {
      "@id": "prov:qualifiedInsertion",
      "@type": "@id"
    },
    "qualifiedRemoval": {
      "@id": "prov:qualifiedRemoval",
      "@type": "@id"
    },
    "asInBundle": {
      "@id": "prov:asInBundle",
      "@type": "@id"
    },
    "mentionOf": {
      "@id": "prov:mentionOf",
      "@type": "@id"
    },
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "oa": "http://www.w3.org/ns/oa#",
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-prov/context.jsonld)

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)
* [PROV-O Specification](https://www.w3.org/TR/prov-o/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/item-prov`

