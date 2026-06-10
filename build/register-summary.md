# OGC Building Blocks for STAC

These [Building Blocks](https://ogcincubator.github.io/bblocks-docs/) provide a validation and documentation wrapper over STAC and extension schemas, and aid in transparent re-use of STAC elements

Allows for validation and testing of STAC examples.

**STAC extends OGC API Records** (i.e. Records is designed to be compatible with the prior STAC mode) - this packaging supports validation of STAC extensions against underlying Records, Features and Common elements.

Supports definition and testing of transformations to/from STAC from other formats.

Implementers can fork this repository and add additional examples in the `tests/` directory of each Building Block and run validation processes locally.

Provides a framework for documentation and testing of additional extensions.


## Building Blocks

### `ogc.contrib.stac.components.assets` — Assets object

**Type:** schema

Assets sub-schema reused in items and collections

### `ogc.contrib.stac.extensions.cf-ontology` — STAC CF Extension Ontology

**Type:** model

### `ogc.contrib.stac.extensions.osc-ontology` — STAC Open Science Extension Ontology

**Type:** model

### `ogc.contrib.stac.extensions.processes-ontology` — STAC Processes Extension Ontology

**Type:** model

### `ogc.contrib.stac.core-ontology` — STAC Core Ontology

**Type:** model

### `ogc.contrib.stac.collection` — STAC Collection

**Type:** schema

A SpatioTemporal Asset Catalogs (STAC) collection.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

### `ogc.contrib.stac.collection-v1-0-0` — STAC Collection (v1.0.0)

**Type:** schema

A SpatioTemporal Asset Catalogs (STAC) collection.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

### `ogc.contrib.stac.collection-v1-1-0` — STAC Collection (v1.1.0)

**Type:** schema

A SpatioTemporal Asset Catalogs (STAC) collection.  This building block implements validation of examples using the canonical schema and a JSON-LD context to a map to a RDF format that can support richer logical constraints and integration with related data.

### `ogc.contrib.stac.item` — Version agnostic STAC Item

**Type:** schema

Version-neutral SpatioTemporal Asset Catalogs (STAC) item - STAC versions are schema incompatible due to hard restrictions on version numbers. This BuildingBlock covers the interoperability that exists between versions by identifying the common elements, and is extended by version-specific restrictions and extensions.

### `ogc.contrib.stac.extensions.accuracy` — STAC Accuracy Extension

**Type:** schema

TBD

### `ogc.contrib.stac.extensions.cf` — STAC CF Extension

**Type:** schema

CF Extension to the SpatioTemporal Asset Catalog (STAC) specification. Allows to provide the Standard Name Table based on the CF metadata convention.

### `ogc.contrib.stac.extensions.classification` — STAC Classification Extension

**Type:** schema

STAC Classification Extension for STAC Items and STAC Collections.

### `ogc.contrib.stac.extensions.eo` — STAC Electro-Optical Extension

**Type:** schema

Electro-Optical (EO) Extension to the SpatioTemporal Asset Catalog (STAC) specification.

EO data is considered to be data that represents a snapshot of the Earth for a single date and time. It could consist of multiple spectral bands in any part of the electromagnetic spectrum. Examples of EO data include sensors with visible, short-wave and mid-wave IR bands (e.g., the OLI instrument on Landsat-8), long-wave IR bands (e.g. TIRS aboard Landsat-8).

### `ogc.contrib.stac.extensions.osc` — STAC Extension - ESA Open Science Catalog

**Type:** schema

STAC Extension for the ESA Open Science Catalog

### `ogc.contrib.stac.extensions.processing` — STAC Processing Extension

**Type:** schema

STAC Processing Extension for STAC Items and STAC Collections.

### `ogc.contrib.stac.extensions.raster` — STAC Raster Extension

**Type:** schema

An item can describe assets that are rasters of one or multiple bands with some information common to them all (raster size, projection) and also specific to each of them (data type, unit, number of bits used, nodata). A raster is often strongly linked with the georeferencing transform and coordinate system definition of all bands (using the projection extension). In many applications, it is interesting to have some metadata about the rasters in the asset (values statistics, value interpretation, transforms).

### `ogc.contrib.stac.extensions.themes` — STAC Themes Extension

**Type:** schema

Themes Extension to the SpatioTemporal Asset Catalog (STAC) specification.
A knowledge organization system used to classify the resource (controlled vocabularies / keywords)

### `ogc.contrib.stac.extensions.themes-jq` — STAC Themes Extension with JQ pre-uplift step

**Type:** schema

Themes Extension to the SpatioTemporal Asset Catalog (STAC) specification.
A knowledge organization system used to classify the resource (controlled vocabularies / keywords)

### `ogc.contrib.stac.extensions.themes-shacl` — STAC Themes Extension with SHACL semantic uplift step

**Type:** schema

Themes Extension to the SpatioTemporal Asset Catalog (STAC) specification.
A knowledge organization system used to classify the resource (controlled vocabularies / keywords)

### `ogc.contrib.stac.item-prov` — STAC Item with Provenance

**Type:** schema

A SpatioTemporal Asset Catalogs (STAC) item with a provenance trace supporting the PROV-O model and DAG (directed acyclic graph) through both object nesting and references

### `ogc.contrib.stac.item-v1-0-0` — STAC Item (v1.0.0)

**Type:** schema

A SpatioTemporal Asset Catalogs (STAC) item. This version specific building block enforces the schema restriction on STAC version by importing the canonical STAC 1.0 schema, but also cross-validates against the STAC version agnostic schema.

### `ogc.contrib.stac.item-v1-1-0` — STAC Item (v1.1.0)

**Type:** schema

A SpatioTemporal Asset Catalogs (STAC) item

### `ogc.contrib.stac.extensions.mlm` — STAC Machine Learning Model

**Type:** schema

STAC Machine Learning Model (MLM) Extension to describe ML models, their training details, and inference runtime requirements.

