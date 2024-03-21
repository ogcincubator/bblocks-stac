
# STAC Item (Schema)

`ogc.contrib.stac.item` *v0.1*

A SpatioTemporal Asset Catalogs (STAC) item

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### STAC simple item
This is the simple item example from the STAC specification.  

#### json
```json
{
  "stac_version": "1.0.0",
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
  "stac_version": "1.0.0",
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
  },
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/context.jsonld"
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/example1/20201211_223832_CS2> a geojson:Feature ;
    geojson:bbox ( 1.729117e+02 1.343885e+00 1.729547e+02 1.369048e+00 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.729117e+02 1.343885e+00 ) ( 1.729547e+02 1.343885e+00 ) ( 1.729547e+02 1.369048e+00 ) ( 1.729117e+02 1.369048e+00 ) ( 1.729117e+02 1.343885e+00 ) ) ) ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: STAC Collection
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml
- $ref: https://github.com/radiantearth/stac-spec/raw/master/item-spec/json-schema/item.json

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "id": "@id",
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
    "geojson": "https://purl.org/geojson/vocab#",
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

