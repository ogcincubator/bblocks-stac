
# STAC Collection (v1.0.0) (Schema)

`ogc.contrib.stac.collection-v1-0-0` *v1.0.0*

A SpatioTemporal Asset Catalogs (STAC) collection.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

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
  ],
  "fair:Findable_has_doi": false,
  "fair:Findable_rich_metadata": true,
  "fair:Findable_identifier": true,
  "fair:Findable_stac_assets": false,
  "fair:Findable_indexed": true,
  "fair:Findable_indexed_approved_metadata": false,
  "fair:Findable_indexed_approved_data": false,
  "fair:Accessible_general": true,
  "fair:Accessible_protocols": true,
  "fair:Accessible_files": 0.0,
  "fair:Interoperable_uses_formal_language": true,
  "fair:Interoperable_controlled_vocabularies": true,
  "fair:Interoperable_related_links": true,
  "fair:Interoperable_has_documentation": false,
  "fair:Reusable_rich_descriptions": true,
  "fair:Reusable_has_license": true,
  "fair:Reusable_workflow_exists": true,
  "fair:Reusable_cloud_assets_rate": 0.0,
  "fair:Reusable_has_visualisation": false,
  "fair:Reusable_has_access_example": false
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/context.jsonld",
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
  ],
  "fair:Findable_has_doi": false,
  "fair:Findable_rich_metadata": true,
  "fair:Findable_identifier": true,
  "fair:Findable_stac_assets": false,
  "fair:Findable_indexed": true,
  "fair:Findable_indexed_approved_metadata": false,
  "fair:Findable_indexed_approved_data": false,
  "fair:Accessible_general": true,
  "fair:Accessible_protocols": true,
  "fair:Accessible_files": 0.0,
  "fair:Interoperable_uses_formal_language": true,
  "fair:Interoperable_controlled_vocabularies": true,
  "fair:Interoperable_related_links": true,
  "fair:Interoperable_has_documentation": false,
  "fair:Reusable_rich_descriptions": true,
  "fair:Reusable_has_license": true,
  "fair:Reusable_workflow_exists": true,
  "fair:Reusable_cloud_assets_rate": 0.0,
  "fair:Reusable_has_visualisation": false,
  "fair:Reusable_has_access_example": false
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <fair:> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <osc:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/example1/polarwarp> rdfs:label "Polarwarp" ;
    ns1:Accessible_files 0e+00 ;
    ns1:Accessible_general true ;
    ns1:Accessible_protocols true ;
    ns1:Findable_has_doi false ;
    ns1:Findable_identifier true ;
    ns1:Findable_indexed true ;
    ns1:Findable_indexed_approved_data false ;
    ns1:Findable_indexed_approved_metadata false ;
    ns1:Findable_rich_metadata true ;
    ns1:Findable_stac_assets false ;
    ns1:Interoperable_controlled_vocabularies true ;
    ns1:Interoperable_has_documentation false ;
    ns1:Interoperable_related_links true ;
    ns1:Interoperable_uses_formal_language true ;
    ns1:Reusable_cloud_assets_rate 0e+00 ;
    ns1:Reusable_has_access_example false ;
    ns1:Reusable_has_license true ;
    ns1:Reusable_has_visualisation false ;
    ns1:Reusable_rich_descriptions true ;
    ns1:Reusable_workflow_exists true ;
    dcterms:description """Polarwarp product

Forecast rasters (+1h … +6h) produced by the Polarwarp workflow using NEXTSIM model and S1 scenes.""" ;
    dcterms:extent [ ] ;
    dcterms:type "Collection" ;
    rdfs:seeAlso [ rdfs:label "Experiment: Polarwarp" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/experiments/polarwarp/record.json> ],
        [ ns2:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://github.com/gtif-cerulean/polarwarp> ],
        [ ns2:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/example1/item.json> ],
        [ rdfs:label "Products" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/catalog.json> ],
        [ rdfs:label "Open Science Catalog" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/catalog.json> ],
        [ rdfs:label "Theme: Cryosphere" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/themes/cryosphere/catalog.json> ],
        [ rdfs:label "Project: Cerulean Information Factory" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.com/projects/cerulean-information-factory/collection.json> ] ;
    stac:hasExtension "https://stac-extensions.github.io/osc/v1.0.0/schema.json",
        "https://stac-extensions.github.io/themes/v1.0.0/schema.json" ;
    stac:version "1.0.0" ;
    ns3:project "cerulean-information-factory" ;
    ns3:status "completed" ;
    ns3:type "product" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: STAC Collection V1.0.0
allOf:
- $ref: https://schemas.stacspec.org/v1.0.0/collection-spec/json-schema/collection.json
- $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
- type: object
  properties:
    links:
      type: array
      items:
        $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "stac_version": "stac:version",
    "stac_extensions": "stac:hasExtension",
    "type": "dct:type",
    "id": "@id",
    "title": "rdfs:label",
    "description": "dct:description",
    "extent": "dct:extent",
    "assets": {
      "@context": {
        "title": "dct:title",
        "type": "dct:format",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        },
        "@vocab": "https://w3id.org/ogc/stac/assets/"
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "links": "rdfs:seeAlso",
    "media_type": "dct:format",
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
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection-v1-0-0/context.jsonld)

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/collection-v1-0-0`

