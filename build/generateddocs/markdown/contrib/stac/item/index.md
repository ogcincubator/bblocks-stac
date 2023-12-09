
# STAC Item (Schema)

`ogc.contrib.stac.item` *v0.1*

A SpatioTemporal Asset Catalogs (STAC) item

[*Status*](http://www.opengis.net/def/status): Under development

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

