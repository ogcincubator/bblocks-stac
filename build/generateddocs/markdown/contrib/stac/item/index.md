
# STAC Item (Schema)

`ogc.contrib.stac.item` *v0.1*

A SpatioTemporal Asset Catalogs (STAC) item

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC spec simple item
This is the simple item example from the STAC specification.  

#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [],
  "type": "Feature",
  "id": "20201211_223832_CS2",
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
    "datetime": "2020-12-11T22:38:32.125000Z"
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
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
    }
  ],
  "assets": {
    "visual": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ]
    },
    "thumbnail": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg",
      "title": "Thumbnail",
      "type": "image/jpeg",
      "roles": [
        "thumbnail"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/context.jsonld",
  "stac_version": "1.1.0",
  "stac_extensions": [],
  "type": "Feature",
  "id": "20201211_223832_CS2",
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
    "datetime": "2020-12-11T22:38:32.125000Z"
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
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
    }
  ],
  "assets": {
    "visual": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "3-Band Visual",
      "roles": [
        "visual"
      ]
    },
    "thumbnail": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2.jpg",
      "title": "Thumbnail",
      "type": "image/jpeg",
      "roles": [
        "thumbnail"
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/example1/20201211_223832_CS2> dcterms:date "2020-12-11T22:38:32.125000+00:00"^^xsd:dateTime ;
    dcterms:type "Feature" ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ] ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729117e+02 1.343885e+00 ) ( 1.729547e+02 1.343885e+00 ) ( 1.729547e+02 1.369048e+00 ) ( 1.729117e+02 1.369048e+00 ) ( 1.729117e+02 1.343885e+00 ) ) ) ] ;
    stac:hasAsset [ ] ;
    stac:version "1.1.0" .


```


### STAC spec core item
This is the complete "core" item example from the STAC specification.  

#### json
```json
{
  "stac_version": "1.1.0",
  "stac_extensions": [],
  "type": "Feature",
  "id": "20201211_223832_CS2",
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
    "title": "Core Item",
    "description": "A sample STAC Item that includes examples of all common metadata",
    "datetime": null,
    "start_datetime": "2020-12-11T22:38:32.125Z",
    "end_datetime": "2020-12-11T22:38:32.327Z",
    "created": "2020-12-12T01:48:13.725Z",
    "updated": "2020-12-12T01:48:13.725Z",
    "platform": "cool_sat1",
    "instruments": [
      "cool_sensor_v1"
    ],
    "constellation": "ion",
    "mission": "collection 5624",
    "gsd": 0.512
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
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
      "rel": "alternate",
      "type": "text/html",
      "href": "http://remotedata.io/catalog/20201211_223832_CS2/index.html",
      "title": "HTML version of this STAC Item"
    }
  ],
  "assets": {
    "analytic": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
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
      ]
    },
    "udm": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic_udm.tif",
      "title": "Unusable Data Mask",
      "type": "image/tiff; application=geotiff"
    },
    "json-metadata": {
      "href": "http://remotedata.io/catalog/20201211_223832_CS2/extended-metadata.json",
      "title": "Extended Metadata",
      "type": "application/json",
      "roles": [
        "metadata"
      ]
    },
    "ephemeris": {
      "href": "http://cool-sat.com/catalog/20201211_223832_CS2/20201211_223832_CS2.EPH",
      "title": "Satellite Ephemeris Metadata"
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/context.jsonld",
  "stac_version": "1.1.0",
  "stac_extensions": [],
  "type": "Feature",
  "id": "20201211_223832_CS2",
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
    "title": "Core Item",
    "description": "A sample STAC Item that includes examples of all common metadata",
    "datetime": null,
    "start_datetime": "2020-12-11T22:38:32.125Z",
    "end_datetime": "2020-12-11T22:38:32.327Z",
    "created": "2020-12-12T01:48:13.725Z",
    "updated": "2020-12-12T01:48:13.725Z",
    "platform": "cool_sat1",
    "instruments": [
      "cool_sensor_v1"
    ],
    "constellation": "ion",
    "mission": "collection 5624",
    "gsd": 0.512
  },
  "collection": "simple-collection",
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json",
      "title": "Simple Example Collection"
    },
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
      "rel": "alternate",
      "type": "text/html",
      "href": "http://remotedata.io/catalog/20201211_223832_CS2/index.html",
      "title": "HTML version of this STAC Item"
    }
  ],
  "assets": {
    "analytic": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "4-Band Analytic",
      "roles": [
        "data"
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
      ]
    },
    "udm": {
      "href": "https://storage.googleapis.com/open-cogs/stac-examples/20201211_223832_CS2_analytic_udm.tif",
      "title": "Unusable Data Mask",
      "type": "image/tiff; application=geotiff"
    },
    "json-metadata": {
      "href": "http://remotedata.io/catalog/20201211_223832_CS2/extended-metadata.json",
      "title": "Extended Metadata",
      "type": "application/json",
      "roles": [
        "metadata"
      ]
    },
    "ephemeris": {
      "href": "http://cool-sat.com/catalog/20201211_223832_CS2/20201211_223832_CS2.EPH",
      "title": "Satellite Ephemeris Metadata"
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/example1/20201211_223832_CS2> rdfs:label "Core Item" ;
    dcterms:created "2020-12-12T01:48:13.725Z" ;
    dcterms:description "A sample STAC Item that includes examples of all common metadata" ;
    dcterms:modified "2020-12-12T01:48:13.725Z" ;
    dcterms:type "Feature" ;
    rdfs:seeAlso [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ],
        [ rdfs:label "HTML version of this STAC Item" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <http://remotedata.io/catalog/20201211_223832_CS2/index.html> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ],
        [ rdfs:label "Simple Example Collection" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/example1/collection.json> ] ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729117e+02 1.343885e+00 ) ( 1.729547e+02 1.343885e+00 ) ( 1.729547e+02 1.369048e+00 ) ( 1.729117e+02 1.369048e+00 ) ( 1.729117e+02 1.343885e+00 ) ) ) ] ;
    stac:end_datetime "2020-12-11T22:38:32.327000+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ] ;
    stac:start_datetime "2020-12-11T22:38:32.125000+00:00"^^xsd:dateTime ;
    stac:version "1.1.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: STAC Item
type: object
description: This object represents the metadata for an item in a SpatioTemporal Asset
  Catalog.
allOf:
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-records/build/annotated/api/records/v1/schemas/recordGeoJSON/schema.yaml
- $ref: '#/definitions/core'
definitions:
  core:
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml
    - oneOf:
      - type: object
        required:
        - geometry
        - bbox
        properties:
          geometry:
            $ref: https://geojson.org/schema/Geometry.json
          bbox:
            type: array
            oneOf:
            - minItems: 4
              maxItems: 4
            - minItems: 6
              maxItems: 6
            items:
              type: number
      - type: object
        required:
        - geometry
        properties:
          geometry:
            type: 'null'
          bbox:
            not: {}
    - type: object
      required:
      - stac_version
      - id
      - links
      - assets
      - properties
      properties:
        stac_version:
          title: STAC version
          type: string
          const: 1.1.0
          x-jsonld-id: https://w3id.org/ogc/stac/core/version
        stac_extensions:
          title: STAC extensions
          type: array
          uniqueItems: true
          items:
            title: Reference to a JSON Schema
            type: string
            format: iri
          x-jsonld-id: https://w3id.org/ogc/stac/core/hasExtension
        id:
          title: Provider ID
          description: Provider item ID
          type: string
          minLength: 1
          x-jsonld-id: '@id'
        links:
          $ref: '#/definitions/links'
        assets:
          $ref: '#/definitions/assets'
          x-jsonld-id: https://w3id.org/ogc/stac/core/hasAsset
          x-jsonld-container: '@set'
        properties:
          allOf:
          - $ref: https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/json-schema/common.json
          - anyOf:
            - required:
              - datetime
              properties:
                datetime:
                  not:
                    type: 'null'
                  x-jsonld-id: http://purl.org/dc/terms/date
                  x-jsonld-type: xsd:dateTime
            - required:
              - datetime
              - start_datetime
              - end_datetime
      $comment: Rules enforcement for STAC Item
      allOf:
      - if:
          properties:
            links:
              contains:
                required:
                - rel
                properties:
                  rel:
                    const: collection
        then:
          required:
          - collection
          properties:
            collection:
              title: Collection ID
              description: The ID of the STAC Collection this Item references to.
              type: string
              minLength: 1
        else:
          properties:
            collection:
              not: {}
      - $comment: The if-then-else below checks whether the bands field is given in
          assets or not. If not, allows bands in properties (then), otherwise, disallows
          bands in properties (else).
        if:
          $comment: If there is no asset with bands...
          required:
          - assets
          properties:
            assets:
              type: object
              additionalProperties:
                properties:
                  bands: false
        then:
          $comment: '... then bands are not allowed in properties...'
          properties:
            properties:
              properties:
                bands: false
        else:
          $comment: '... otherwise bands are allowed in properties.'
          properties:
            properties:
              $ref: https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/json-schema/bands.json
  links:
    title: Item links
    description: Links to item relations
    type: array
    items:
      allOf:
      - $ref: '#/definitions/link'
      - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml
  link:
    allOf:
    - type: object
      required:
      - rel
      - href
      properties:
        href:
          title: Link reference
          type: string
          format: iri-reference
          minLength: 1
        rel:
          title: Link relation type
          type: string
          minLength: 1
        type:
          title: Link type
          type: string
          x-jsonld-id: '@type'
        title:
          title: Link title
          type: string
          x-jsonld-id: http://purl.org/dc/terms/title
        method:
          title: Link method
          type: string
          pattern: ^[A-Z]+$
          default: GET
        headers:
          title: Link headers
          type: object
          additionalProperties:
            oneOf:
            - type: string
            - type: array
              items:
                type: string
        body:
          title: Link body
          $comment: Any type is allowed.
      $comment: Link with relationship `self` must be absolute URI
      if:
        properties:
          rel:
            const: self
      then:
        properties:
          href:
            format: iri
    - $ref: https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/json-schema/common.json
  assets:
    title: Asset links
    description: Links to assets
    type: object
    additionalProperties:
      $ref: '#/definitions/asset'
  asset:
    allOf:
    - type: object
      required:
      - href
      properties:
        href:
          title: Asset reference
          type: string
          format: iri-reference
          minLength: 1
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
          x-jsonld-id: http://purl.org/dc/terms/format
        roles:
          title: Asset roles
          type: array
          items:
            type: string
          x-jsonld-id: https://w3id.org/ogc/stac/core/roles
          x-jsonld-container: '@set'
    - $ref: https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/json-schema/common.json
x-jsonld-extra-terms:
  type: '@type'
  title: http://purl.org/dc/terms/title
  description: http://purl.org/dc/terms/description
  keywords: http://purl.org/dc/terms/subject
  license: http://purl.org/dc/terms/license
  extent: http://purl.org/dc/terms/extent
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
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
    "type": "dct:type",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "type": "@type",
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
    "links": "rdfs:seeAlso",
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "time": "dct:temporal",
    "created": "dct:created",
    "updated": "dct:modified",
    "title": {
      "@container": "@set",
      "@id": "rdfs:label"
    },
    "description": {
      "@container": "@set",
      "@id": "dct:description"
    },
    "keywords": {
      "@container": "@set",
      "@id": "dcat:keyword"
    },
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
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dcat:license",
    "rights": "dcat:rights",
    "linkTemplates": {
      "@context": {
        "type": "dct:format",
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
    "stac_version": "stac:version",
    "stac_extensions": "stac:hasExtension",
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
    "assets": {
      "@context": {
        "title": "dct:title",
        "type": "dct:format",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "extent": "dct:extent",
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
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
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
    "stac": "https://w3id.org/ogc/stac/core/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/context.jsonld)

## Sources

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/item`

