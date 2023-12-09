---
title: STAC Item (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>STAC Item</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: STAC Item (Schema)
---


# STAC Item `ogc.contrib.stac.item`

A SpatioTemporal Asset Catalogs (STAC) item

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: STAC Collection
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml
- $ref: https://github.com/radiantearth/stac-spec/raw/master/item-spec/json-schema/item.json

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fitem%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.json" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.json</a>


# JSON-LD Context

```json--ldContext
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

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Fbblocks-stac%2Fbuild%2Fannotated%2Fcontrib%2Fstac%2Fitem%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/context.jsonld" target="_blank">https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/context.jsonld</a>

# References

* [STAC Specification](https://stacspec.org/en/about/stac-spec/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/bblocks-stac" target="_blank">https://github.com/ogcincubator/bblocks-stac</a>
* Path:
<code><a href="https://github.com/ogcincubator/bblocks-stac/blob/HEAD/_sources/item" target="_blank">_sources/item</a></code>

