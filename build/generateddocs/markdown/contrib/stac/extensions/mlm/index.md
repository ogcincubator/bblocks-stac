
# STAC Machine Learning Model (Schema)

`ogc.contrib.stac.extensions.mlm` *v1.6.0*

STAC Machine Learning Model (MLM) Extension to describe ML models, their training details, and inference runtime requirements.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

The STAC Machine Learning Model (MLM) extension describes machine learning models, their inputs and
outputs, training details, and runtime requirements on STAC Items and Collections. This block provides the
JSON Schema and the JSON-LD context that map the extension fields to the
[MLM ontology](bblocks://ogc.contrib.stac.extensions.mlm-ontology). It also provides reversible
[STAC Item to RDF transforms](README.md).

## Related STAC extensions

**None of the extensions below is universally required on every MLM Item.** Which definitions are
needed depends on the model's inputs, outputs and the metadata being supplied.
The viewer's dependency graph describes reuse between building blocks, not an unconditional requirement
to list every dependency in an Item's `stac_extensions`.

### Conditional input/output relationships

These extensions describe objects or structures directly referenced by MLM. A referenced object must
have an appropriate definition, but the applicable extension or STAC core representation depends on
the field and STAC version. Datacube belongs to this group alongside EO and Raster.

| Extension | When it applies | Connection to MLM |
| --- | --- | --- |
| [EO](bblocks://ogc.contrib.stac.extensions.eo) | When referenced bands are described using EO metadata. EO is not the only supported band representation; STAC 1.1 also defines common Band Objects. | Supplies spectral band names, common names and wavelength metadata for MLM `bands` references. |
| [Raster](bblocks://ogc.contrib.stac.extensions.raster) | When referenced bands use Raster metadata. It is not required merely because the model operates on raster data; the representation depends on the STAC/extension version. | Supplies band data types, nodata values and statistics. Source statistics need not equal the model's applied `value_scaling`. |
| [Datacube](bblocks://ogc.contrib.stac.extensions.datacube) | When non-empty MLM `variables` references are supplied, corresponding Datacube variable definitions are needed. Models without variable references do not require them. | Describes selected variables and their dimensions. Shared MLM SHACL resolves variable names and dimension references. |
| [Classification](bblocks://ogc.contrib.stac.extensions.classification) | When `classification:classes` metadata is supplied for an output. Not required for every model, or merely because a task is classification. | Describes output class values and labels. |
| [Processing](bblocks://ogc.contrib.stac.extensions.processing) | When MLM supplies pre/post-processing, derivation or custom scaling expressions. Reusing its Expression Object structure does not by itself require declaring the Processing extension on the Item. | Supplies the expression structure reused by MLM processing fields. |

### Complementary model, data and software metadata

These integrations add context rather than define the objects selected by MLM `bands` or `variables`.
They apply when the corresponding metadata is provided, not automatically to every model.

| Extension | When it applies | Connection to MLM |
| --- | --- | --- |
| [ML-AOI](bblocks://ogc.contrib.stac.extensions.ml-aoi) | When documenting training, validation or test areas of interest. | Describes areas associated with the model's training data. |
| [Application](bblocks://ogc.contrib.stac.extensions.application) | When documenting the software application that packages or executes the model. | Adds application metadata alongside the model description. |
| [VCS](bblocks://ogc.contrib.stac.extensions.vcs) | When documenting model/application source repositories or revisions. | Identifies version-control resources, including repository links. |
| [File Info](bblocks://ogc.contrib.stac.extensions.file) | When supplying sizes, checksums or other file metadata for model artifacts and associated files. | Describes the files carrying the model and related resources. |
| [Scientific Citation](bblocks://ogc.contrib.stac.extensions.scientific) | When supplying publications, citations or persistent identifiers. | Records scientific references associated with the model. |
| [Versioning Indicators](bblocks://ogc.contrib.stac.extensions.version) | When documenting revisions of the model's STAC resource. | Identifies versions and links between revisions. |
| [CF](bblocks://ogc.contrib.stac.extensions.cf) | When supplying Climate and Forecast metadata for climate variables. | Adds scientific variable descriptions; it is not required merely because a model uses Datacube. |

### Complete Example

In the [**Examples**](/bblock/ogc.contrib.stac.extensions.mlm/examples) tab, a pinned Resoterre U-Net for RDPS to HRDPS
climate variables downscaling
uses Datacube and all the complementary extensions above except CF to demonstrate own their interconnexions apply.

## Order matters

> In each `input` and `result` object, `shape[i]` is the size of the axis named
> `dim_order[i]`. The order of `bands` and `variables` matches the indices along the reserved `"bands"` and
> `"variables"` axes. A `value_scaling` array either has one broadcast entry or one entry per stacked element,
> in the same order. Arrays of `pre_processing_function` or `post_processing_function` expressions run
> sequentially.
> These positions are kept as ordered RDF lists. The SHACL shapes from the ontology block reject definitions
> whose positions no longer align. See
> [Order matters](bblocks://ogc.contrib.stac.extensions.mlm-ontology) for the full table of rules.

## Examples

### Collection of items contained in the Machine Learning Model examples.
#### json
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json"
  ],
  "type": "Collection",
  "id": "ml-model-examples",
  "title": "Machine Learning Model examples",
  "description": "Collection of items contained in the Machine Learning Model examples.",
  "license": "Apache-2.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -7.882190080512502,
          37.13739173208318,
          27.911651652899923,
          58.21798141355221
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1900-01-01T00:00:00Z",
          "9999-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "item_assets": {
    "weights": {
      "title": "model weights",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "1900-01-01T00:00:00Z",
      "maximum": "9999-12-31T23:59:59Z"
    },
    "mlm:name": [
      "example-model",
      "Resnet-18 Sentinel-2 ALL MOCO",
      "UNet ClimateDiffuse ERA5 Downscaling",
      "U-Net_efficientnet-b3"
    ],
    "mlm:tasks": [
      "classification",
      "downscaling",
      "regression",
      "semantic-segmentation"
    ],
    "mlm:architecture": [
      "ResNet",
      "U-Net",
      "segmentation_models_pytorch.decoders.unet.model.Unet"
    ]
  },
  "links": [
    {
      "href": "collection.json",
      "rel": "self"
    },
    {
      "href": "item_basic.json",
      "rel": "item"
    },
    {
      "href": "item_bands_expression.json",
      "rel": "item"
    },
    {
      "href": "item_datacube_variables.json",
      "rel": "item"
    },
    {
      "href": "item_eo_bands.json",
      "rel": "item"
    },
    {
      "href": "item_eo_and_raster_bands.json",
      "rel": "item"
    },
    {
      "href": "item_eo_bands_summarized.json",
      "rel": "item"
    },
    {
      "href": "item_raster_bands.json",
      "rel": "item"
    },
    {
      "href": "item_multi_io.json",
      "rel": "item"
    },
    {
      "href": "item_pytorch_geo_unet.json",
      "rel": "item"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json"
  ],
  "type": "Collection",
  "id": "ml-model-examples",
  "title": "Machine Learning Model examples",
  "description": "Collection of items contained in the Machine Learning Model examples.",
  "license": "Apache-2.0",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -7.882190080512502,
          37.13739173208318,
          27.911651652899923,
          58.21798141355221
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1900-01-01T00:00:00Z",
          "9999-12-31T23:59:59Z"
        ]
      ]
    }
  },
  "item_assets": {
    "weights": {
      "title": "model weights",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ]
    }
  },
  "summaries": {
    "datetime": {
      "minimum": "1900-01-01T00:00:00Z",
      "maximum": "9999-12-31T23:59:59Z"
    },
    "mlm:name": [
      "example-model",
      "Resnet-18 Sentinel-2 ALL MOCO",
      "UNet ClimateDiffuse ERA5 Downscaling",
      "U-Net_efficientnet-b3"
    ],
    "mlm:tasks": [
      "classification",
      "downscaling",
      "regression",
      "semantic-segmentation"
    ],
    "mlm:architecture": [
      "ResNet",
      "U-Net",
      "segmentation_models_pytorch.decoders.unet.model.Unet"
    ]
  },
  "links": [
    {
      "href": "collection.json",
      "rel": "self"
    },
    {
      "href": "item_basic.json",
      "rel": "item"
    },
    {
      "href": "item_bands_expression.json",
      "rel": "item"
    },
    {
      "href": "item_datacube_variables.json",
      "rel": "item"
    },
    {
      "href": "item_eo_bands.json",
      "rel": "item"
    },
    {
      "href": "item_eo_and_raster_bands.json",
      "rel": "item"
    },
    {
      "href": "item_eo_bands_summarized.json",
      "rel": "item"
    },
    {
      "href": "item_raster_bands.json",
      "rel": "item"
    },
    {
      "href": "item_multi_io.json",
      "rel": "item"
    },
    {
      "href": "item_pytorch_geo_unet.json",
      "rel": "item"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<https://example.com/stac/mlm/example-1/ml-model-examples> a <https://example.com/stac/mlm/example-1/Collection> ;
    dcterms:description "Collection of items contained in the Machine Learning Model examples." ;
    dcterms:extent [ ] ;
    dcterms:title "Machine Learning Model examples" ;
    rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_raster_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_datacube_variables.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_bands_summarized.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_bands_expression.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_and_raster_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_eo_bands.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_multi_io.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_basic.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/collection.json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://example.com/stac/mlm/example-1/item_pytorch_geo_unet.json> ] ;
    dcat:license "Apache-2.0" ;
    stac:hasExtension "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json" ;
    stac:version "1.0.0" .


```


### Demonstrate the basic use of MLM with no other extension cross-references.
#### geojson
```geojson
{
  "$comment": "Demonstrate the basic use of MLM with no other extension cross-references.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json"
  ],
  "type": "Feature",
  "id": "example-model",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Basic STAC Item with only the MLM extension and no other extension cross-references.",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "example-model",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:input": [
      {
        "name": "Model with RGB input that does not refer to any band.",
        "bands": [],
        "input": {
          "shape": [
            -1,
            3,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "channel",
            "height",
            "width"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            1
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "uint8"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "BACKGROUND",
            "description": "Background non-city.",
            "color_hint": [
              0,
              0,
              0
            ]
          },
          {
            "value": 1,
            "name": "CITY",
            "description": "A city is detected.",
            "color_hint": [
              0,
              0,
              255
            ]
          }
        ]
      }
    ]
  },
  "assets": {
    "model": {
      "href": "https://huggingface.co/example/model-card",
      "title": "Pytorch weights checkpoint",
      "description": "Example model.",
      "type": "text/html",
      "roles": [
        "mlm:model"
      ],
      "mlm:artifact_type": "torch.save"
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_basic.json",
      "type": "application/geo+json"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the basic use of MLM with no other extension cross-references.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json"
  ],
  "type": "Feature",
  "id": "example-model",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Basic STAC Item with only the MLM extension and no other extension cross-references.",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "example-model",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:input": [
      {
        "name": "Model with RGB input that does not refer to any band.",
        "bands": [],
        "input": {
          "shape": [
            -1,
            3,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "channel",
            "height",
            "width"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            1
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "uint8"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "BACKGROUND",
            "description": "Background non-city.",
            "color_hint": [
              0,
              0,
              0
            ]
          },
          {
            "value": 1,
            "name": "CITY",
            "description": "A city is detected.",
            "color_hint": [
              0,
              0,
              255
            ]
          }
        ]
      }
    ]
  },
  "assets": {
    "model": {
      "href": "https://huggingface.co/example/model-card",
      "title": "Pytorch weights checkpoint",
      "description": "Example model.",
      "type": "text/html",
      "roles": [
        "mlm:model"
      ],
      "mlm:artifact_type": "torch.save"
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_basic.json",
      "type": "application/geo+json"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-2/example-model> a geojson:Feature ;
    dcterms:description "Basic STAC Item with only the MLM extension and no other extension cross-references." ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-2/item_basic.json> ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-2/collection.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns1:model <https://huggingface.co/example/model-card> ] ;
    stac:hasExtension "https://stac-extensions.github.io/mlm/v1.6.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    mlm:architecture "ResNet"^^xsd:string ;
    mlm:input ( [ mlm:bands () ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "channel" "height" "width" ) ;
                        mlm:shape ( -1 3 64 64 ) ] ;
                mlm:io_name "Model with RGB input that does not refer to any band." ] ) ;
    mlm:name "example-model"^^xsd:string ;
    mlm:output ( [ mlm:classification_classes [ mlm:color_hint 0 ;
                        mlm:io_description "Background non-city." ;
                        mlm:io_name "BACKGROUND" ;
                        mlm:value 0 ],
                    [ mlm:color_hint 0,
                            255 ;
                        mlm:io_description "A city is detected." ;
                        mlm:io_name "CITY" ;
                        mlm:value 1 ] ;
                mlm:io_name "classification" ;
                mlm:result [ mlm:data_type "uint8" ;
                        mlm:dim_order ( "batch" "class" ) ;
                        mlm:shape ( -1 1 ) ] ;
                mlm:tasks ( mlm:classification ) ] ) ;
    mlm:tasks ( mlm:classification ) .

<https://huggingface.co/example/model-card> dcterms:description "Example model." ;
    dcterms:format "text/html" ;
    dcterms:title "Pytorch weights checkpoint" ;
    stac:hasAssetroles "mlm:model"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string .


```


### Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.
#### geojson
```geojson
{
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "RBG+NDVI Bands Sentinel-2 Batch",
        "bands": [
          {
            "name": "B04"
          },
          {
            "name": "B03"
          },
          {
            "name": "B02"
          },
          {
            "name": "NDVI",
            "format": "rio-calc",
            "expression": "(B08 - B04) / (B08 + B04)"
          }
        ],
        "input": {
          "shape": [
            -1,
            4,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "segmentation",
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            2
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 1,
            "name": "vegetation",
            "title": "Vegetation",
            "description": "Pixels were vegetation is detected.",
            "color_hint": "00FF00",
            "nodata": false
          },
          {
            "value": 0,
            "name": "background",
            "title": "Non-Vegetation",
            "description": "Anything that is not classified as vegetation.",
            "color_hint": "000000",
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://example.com/model-rgb-ndvi.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A vegetation classification model trained on Sentinel-2 imagery and NDVI.",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "B02",
          "common_name": "blue",
          "description": "Blue (band 2)",
          "center_wavelength": 0.49,
          "full_width_half_max": 0.098
        },
        {
          "name": "B03",
          "common_name": "green",
          "description": "Green (band 3)",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B04",
          "common_name": "red",
          "description": "Red (band 4)",
          "center_wavelength": 0.665,
          "full_width_half_max": 0.038
        },
        {
          "name": "B08",
          "common_name": "nir",
          "description": "NIR 1 (band 8)",
          "center_wavelength": 0.842,
          "full_width_half_max": 0.145
        }
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_bands_expression.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "RBG+NDVI Bands Sentinel-2 Batch",
        "bands": [
          {
            "name": "B04"
          },
          {
            "name": "B03"
          },
          {
            "name": "B02"
          },
          {
            "name": "NDVI",
            "format": "rio-calc",
            "expression": "(B08 - B04) / (B08 + B04)"
          }
        ],
        "input": {
          "shape": [
            -1,
            4,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "segmentation",
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            2
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 1,
            "name": "vegetation",
            "title": "Vegetation",
            "description": "Pixels were vegetation is detected.",
            "color_hint": "00FF00",
            "nodata": false
          },
          {
            "value": 0,
            "name": "background",
            "title": "Non-Vegetation",
            "description": "Anything that is not classified as vegetation.",
            "color_hint": "000000",
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://example.com/model-rgb-ndvi.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A vegetation classification model trained on Sentinel-2 imagery and NDVI.",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "B02",
          "common_name": "blue",
          "description": "Blue (band 2)",
          "center_wavelength": 0.49,
          "full_width_half_max": 0.098
        },
        {
          "name": "B03",
          "common_name": "green",
          "description": "Green (band 3)",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B04",
          "common_name": "red",
          "description": "Red (band 4)",
          "center_wavelength": 0.665,
          "full_width_half_max": 0.038
        },
        {
          "name": "B08",
          "common_name": "nir",
          "description": "NIR 1 (band 8)",
          "center_wavelength": 0.842,
          "full_width_half_max": 0.145
        }
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_bands_expression.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <eo:> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <https://w3id.org/ogc/stac/assets/> .
@prefix ns4: <file:> .
@prefix ns5: <ml-aoi:> .
@prefix ns6: <https://w3id.org/ogc/stac/assets/$> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-3/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns4:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-3/item_bands_expression.json> ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns5:split "train" ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-3/collection.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns3:weights <https://example.com/model-rgb-ndvi.pth> ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    mlm:accelerator mlm:cuda ;
    mlm:accelerator_constrained false ;
    mlm:accelerator_summary "Unknown"^^xsd:string ;
    mlm:architecture "ResNet"^^xsd:string ;
    mlm:batch_size_suggestion "256"^^xsd:nonNegativeInteger ;
    mlm:framework "pytorch"^^xsd:string ;
    mlm:framework_version "2.1.2+cu121"^^xsd:string ;
    mlm:input ( [ mlm:bands ( [ mlm:reference_name "B04" ] [ mlm:reference_name "B03" ] [ mlm:reference_name "B02" ] [ mlm:reference_expression "\"(B08 - B04) / (B08 + B04)\""^^rdf:JSON ;
                            mlm:reference_format "rio-calc" ;
                            mlm:reference_name "NDVI" ] ) ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "bands" "height" "width" ) ;
                        mlm:shape ( -1 4 64 64 ) ] ;
                mlm:io_name "RBG+NDVI Bands Sentinel-2 Batch" ] ) ;
    mlm:memory_size "1"^^xsd:nonNegativeInteger ;
    mlm:name "Resnet-18 Sentinel-2 ALL MOCO"^^xsd:string ;
    mlm:output ( [ mlm:classification_classes [ dcterms:title "Non-Vegetation" ;
                        mlm:color_hint "000000" ;
                        mlm:io_description "Anything that is not classified as vegetation." ;
                        mlm:io_name "background" ;
                        mlm:nodata false ;
                        mlm:value 0 ],
                    [ dcterms:title "Vegetation" ;
                        mlm:color_hint "00FF00" ;
                        mlm:io_description "Pixels were vegetation is detected." ;
                        mlm:io_name "vegetation" ;
                        mlm:nodata false ;
                        mlm:value 1 ] ;
                mlm:io_name "classification" ;
                mlm:post_processing_function "null"^^rdf:JSON ;
                mlm:result [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "class" ) ;
                        mlm:shape ( -1 2 ) ] ;
                mlm:tasks ( mlm:segmentation mlm:semantic-segmentation ) ] ) ;
    mlm:pretrained_source "EuroSat Sentinel-2"^^xsd:string ;
    mlm:tasks ( mlm:classification ) ;
    mlm:total_parameters "11700000"^^xsd:nonNegativeInteger .

<https://example.com/model-rgb-ndvi.pth> ns1:bands [ dcterms:description "Blue (band 2)" ;
            ns3:center_wavelength 4.9e-01 ;
            ns3:common_name "blue" ;
            ns3:full_width_half_max 9.8e-02 ;
            ns3:name "B02" ],
        [ dcterms:description "Green (band 3)" ;
            ns3:center_wavelength 5.6e-01 ;
            ns3:common_name "green" ;
            ns3:full_width_half_max 4.5e-02 ;
            ns3:name "B03" ],
        [ dcterms:description "Red (band 4)" ;
            ns3:center_wavelength 6.65e-01 ;
            ns3:common_name "red" ;
            ns3:full_width_half_max 3.8e-02 ;
            ns3:name "B04" ],
        [ dcterms:description "NIR 1 (band 8)" ;
            ns3:center_wavelength 8.42e-01 ;
            ns3:common_name "nir" ;
            ns3:full_width_half_max 1.45e-01 ;
            ns3:name "B08" ] ;
    dcterms:description "A vegetation classification model trained on Sentinel-2 imagery and NDVI." ;
    dcterms:format "application/octet-stream; application=pytorch" ;
    dcterms:title "Pytorch weights checkpoint" ;
    ns6:comment "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension." ;
    stac:hasAssetroles "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string .


```


### Demonstrate the use of MLM and DataCube variables description to characterize its inputs and outputs.
#### geojson
```geojson
{
  "$comment": "Demonstrate the use of MLM and DataCube variables description to characterize its inputs and outputs.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "UNet_ClimateDiffuse_ERA5_Downscaling",
  "collection": "ml-model-examples",
  "bbox": [
    233.6,
    54.2,
    297.5,
    22.6
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          233.6,
          54.2
        ],
        [
          297.5,
          54.2
        ],
        [
          297.5,
          22.6
        ],
        [
          233.6,
          22.6
        ],
        [
          233.6,
          54.2
        ]
      ]
    ]
  },
  "properties": {
    "description": "UNet model for coarse-to-fine downscaling as regression task of climate indices of ERA5 dataset.",
    "datetime": null,
    "start_datetime": "1940-01-01T00:00:00Z",
    "end_datetime": "2100-12-31T23:59:59Z",
    "mlm:name": "UNet ClimateDiffuse ERA5 Downscaling",
    "mlm:tasks": [
      "regression",
      "downscaling"
    ],
    "mlm:architecture": "U-Net",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu118",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:input": [
      {
        "name": "Coarse climate variables employed by the model downscaling regression. This model takes 2 'constant/spatial' variables and 3 'spatio-temporal' variables provided by ERA5 datacube.",
        "variables": [
          "land_sea_mask",
          "geopotential",
          "temperature_2m",
          "10m_u_component_of_wind",
          "10m_v_component_of_wind"
        ],
        "input": {
          "shape": [
            -1,
            5,
            128,
            256
          ],
          "dim_order": [
            "time",
            "variables",
            "lat",
            "lon"
          ],
          "data_type": "float32"
        },
        "norm_by_channel": false,
        "resize_type": null,
        "pre_processing_function": {
          "description": "Script that performs the relevant normalization and concatenation of variables for model input.",
          "format": "uri",
          "expression": {
            "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/DatasetUS.py",
            "type": "text/x-python"
          }
        }
      }
    ],
    "mlm:output": [
      {
        "name": "Fine climate variables predicted by the model. Only the 3 'spatio-temporal' variables are predicted.",
        "tasks": [
          "regression",
          "downscaling"
        ],
        "variables": [
          "temperature_2m",
          "10m_u_component_of_wind",
          "10m_v_component_of_wind"
        ],
        "result": {
          "shape": [
            -1,
            3,
            128,
            256
          ],
          "dim_order": [
            "time",
            "variables",
            "lat",
            "lon"
          ],
          "data_type": "float32"
        }
      }
    ],
    "cube:dimensions": {
      "time": {
        "type": "temporal",
        "extent": [
          "1940-01-01T00:00:00Z",
          "2100-12-31T23:59:59Z"
        ],
        "step": "P1H"
      },
      "lat": {
        "type": "spatial",
        "extent": [
          54.2,
          22.6
        ],
        "axis": "y"
      },
      "lon": {
        "type": "spatial",
        "extent": [
          233.6,
          297.5
        ],
        "axis": "x"
      }
    },
    "cube:variables": {
      "land_sea_mask": {
        "shortname": "lsm",
        "description": "Proportion of land-sea, where 1 indicates land and 0 indicates sea.",
        "type": "data",
        "data_type": "float32",
        "extent": [
          0,
          1
        ],
        "dimensions": [
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/172"
      },
      "geopotential": {
        "shortname": "z",
        "description": "This parameter is the geopotential, which is the potential energy per unit mass at a point in the atmosphere, expressed in metres squared per second squared (m² s⁻²). It is a measure of the height of a point in the atmosphere relative to sea level.",
        "type": "data",
        "data_type": "float32",
        "unit": "m² s-2",
        "dimensions": [
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/129"
      },
      "temperature_2m": {
        "description": "This parameter is the temperature of air at 2m above the surface of land, sea or in-land waters.",
        "type": "data",
        "data_type": "float32",
        "unit": "K",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/167"
      },
      "10m_u_component_of_wind": {
        "shortname": "10u",
        "description": "This parameter is the eastward component of the 10m wind. It is the horizontal speed of air moving towards the east, at a height of ten metres above the surface of the Earth, in metres per second.",
        "type": "data",
        "data_type": "float32",
        "unit": "m s-1",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/165"
      },
      "10m_v_component_of_wind": {
        "shortname": "10v",
        "description": "This parameter is the northward component of the 10m wind. It is the horizontal speed of air moving towards the north, at a height of ten metres above the surface of the Earth, in metres per second.",
        "type": "data",
        "data_type": "float32",
        "unit": "m s-1",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/166"
      }
    },
    "sci:publications": [
      {
        "doi": "10.48550/arXiv.2404.17752",
        "citation": "Robbie A. Watt, Laura A. Mansfield, Generative Diffusion-based Downscaling for Climate"
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://github.com/robbiewatt1/ClimateDiffuse/raw/refs/heads/main/Model_chpt/unet.pt",
      "title": "U-Net Pytorch weights checkpoint",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "file:size": 389657415
    },
    "model": {
      "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Network.py",
      "title": "Model implementation.",
      "description": "Source code to define the U-Net model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
    },
    "train-script": {
      "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/TrainUnet.py",
      "title": "Training script.",
      "description": "Script to run training of the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:training",
        "code",
        "metadata"
      ]
    }
  },
  "inference-script": {
    "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Inference.py",
    "title": "Inference script.",
    "description": "Script to run inference with the model.",
    "type": "text/x-python",
    "roles": [
      "mlm:inference",
      "code",
      "metadata"
    ]
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_datacube_variables.json",
      "type": "application/geo+json"
    },
    {
      "rel": "via",
      "href": "https://github.com/robbiewatt1/ClimateDiffuse",
      "type": "text/html"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.48550/arXiv.2404.17752",
      "type": "text/html"
    },
    {
      "rel": "code",
      "href": "https://github.com/robbiewatt1/ClimateDiffuse",
      "type": "text/html"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and DataCube variables description to characterize its inputs and outputs.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "type": "Feature",
  "id": "UNet_ClimateDiffuse_ERA5_Downscaling",
  "collection": "ml-model-examples",
  "bbox": [
    233.6,
    54.2,
    297.5,
    22.6
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          233.6,
          54.2
        ],
        [
          297.5,
          54.2
        ],
        [
          297.5,
          22.6
        ],
        [
          233.6,
          22.6
        ],
        [
          233.6,
          54.2
        ]
      ]
    ]
  },
  "properties": {
    "description": "UNet model for coarse-to-fine downscaling as regression task of climate indices of ERA5 dataset.",
    "datetime": null,
    "start_datetime": "1940-01-01T00:00:00Z",
    "end_datetime": "2100-12-31T23:59:59Z",
    "mlm:name": "UNet ClimateDiffuse ERA5 Downscaling",
    "mlm:tasks": [
      "regression",
      "downscaling"
    ],
    "mlm:architecture": "U-Net",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu118",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:input": [
      {
        "name": "Coarse climate variables employed by the model downscaling regression. This model takes 2 'constant/spatial' variables and 3 'spatio-temporal' variables provided by ERA5 datacube.",
        "variables": [
          "land_sea_mask",
          "geopotential",
          "temperature_2m",
          "10m_u_component_of_wind",
          "10m_v_component_of_wind"
        ],
        "input": {
          "shape": [
            -1,
            5,
            128,
            256
          ],
          "dim_order": [
            "time",
            "variables",
            "lat",
            "lon"
          ],
          "data_type": "float32"
        },
        "norm_by_channel": false,
        "resize_type": null,
        "pre_processing_function": {
          "description": "Script that performs the relevant normalization and concatenation of variables for model input.",
          "format": "uri",
          "expression": {
            "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/DatasetUS.py",
            "type": "text/x-python"
          }
        }
      }
    ],
    "mlm:output": [
      {
        "name": "Fine climate variables predicted by the model. Only the 3 'spatio-temporal' variables are predicted.",
        "tasks": [
          "regression",
          "downscaling"
        ],
        "variables": [
          "temperature_2m",
          "10m_u_component_of_wind",
          "10m_v_component_of_wind"
        ],
        "result": {
          "shape": [
            -1,
            3,
            128,
            256
          ],
          "dim_order": [
            "time",
            "variables",
            "lat",
            "lon"
          ],
          "data_type": "float32"
        }
      }
    ],
    "cube:dimensions": {
      "time": {
        "type": "temporal",
        "extent": [
          "1940-01-01T00:00:00Z",
          "2100-12-31T23:59:59Z"
        ],
        "step": "P1H"
      },
      "lat": {
        "type": "spatial",
        "extent": [
          54.2,
          22.6
        ],
        "axis": "y"
      },
      "lon": {
        "type": "spatial",
        "extent": [
          233.6,
          297.5
        ],
        "axis": "x"
      }
    },
    "cube:variables": {
      "land_sea_mask": {
        "shortname": "lsm",
        "description": "Proportion of land-sea, where 1 indicates land and 0 indicates sea.",
        "type": "data",
        "data_type": "float32",
        "extent": [
          0,
          1
        ],
        "dimensions": [
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/172"
      },
      "geopotential": {
        "shortname": "z",
        "description": "This parameter is the geopotential, which is the potential energy per unit mass at a point in the atmosphere, expressed in metres squared per second squared (m\u00b2 s\u207b\u00b2). It is a measure of the height of a point in the atmosphere relative to sea level.",
        "type": "data",
        "data_type": "float32",
        "unit": "m\u00b2 s-2",
        "dimensions": [
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/129"
      },
      "temperature_2m": {
        "description": "This parameter is the temperature of air at 2m above the surface of land, sea or in-land waters.",
        "type": "data",
        "data_type": "float32",
        "unit": "K",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/167"
      },
      "10m_u_component_of_wind": {
        "shortname": "10u",
        "description": "This parameter is the eastward component of the 10m wind. It is the horizontal speed of air moving towards the east, at a height of ten metres above the surface of the Earth, in metres per second.",
        "type": "data",
        "data_type": "float32",
        "unit": "m s-1",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/165"
      },
      "10m_v_component_of_wind": {
        "shortname": "10v",
        "description": "This parameter is the northward component of the 10m wind. It is the horizontal speed of air moving towards the north, at a height of ten metres above the surface of the Earth, in metres per second.",
        "type": "data",
        "data_type": "float32",
        "unit": "m s-1",
        "dimensions": [
          "time",
          "lat",
          "lon"
        ],
        "definition": "https://codes.ecmwf.int/grib/param-db/166"
      }
    },
    "sci:publications": [
      {
        "doi": "10.48550/arXiv.2404.17752",
        "citation": "Robbie A. Watt, Laura A. Mansfield, Generative Diffusion-based Downscaling for Climate"
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://github.com/robbiewatt1/ClimateDiffuse/raw/refs/heads/main/Model_chpt/unet.pt",
      "title": "U-Net Pytorch weights checkpoint",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "file:size": 389657415
    },
    "model": {
      "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Network.py",
      "title": "Model implementation.",
      "description": "Source code to define the U-Net model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
    },
    "train-script": {
      "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/TrainUnet.py",
      "title": "Training script.",
      "description": "Script to run training of the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:training",
        "code",
        "metadata"
      ]
    }
  },
  "inference-script": {
    "href": "https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Inference.py",
    "title": "Inference script.",
    "description": "Script to run inference with the model.",
    "type": "text/x-python",
    "roles": [
      "mlm:inference",
      "code",
      "metadata"
    ]
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_datacube_variables.json",
      "type": "application/geo+json"
    },
    {
      "rel": "via",
      "href": "https://github.com/robbiewatt1/ClimateDiffuse",
      "type": "text/html"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.48550/arXiv.2404.17752",
      "type": "text/html"
    },
    {
      "rel": "code",
      "href": "https://github.com/robbiewatt1/ClimateDiffuse",
      "type": "text/html"
    }
  ]
}
```

#### ttl
```ttl
@prefix cube: <https://w3id.org/ogc/stac/datacube/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <file:> .
@prefix ns2: <sci:> .
@prefix ns3: <https://w3id.org/ogc/stac/assets/> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-4/UNet_ClimateDiffuse_ERA5_Downscaling> a geojson:Feature ;
    dcterms:description "UNet model for coarse-to-fine downscaling as regression task of climate indices of ERA5 dataset." ;
    rdfs:seeAlso [ dcterms:type "text/html" ;
            ns4:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://github.com/robbiewatt1/ClimateDiffuse> ],
        [ dcterms:type "application/geo+json" ;
            ns4:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-4/item_datacube_variables.json> ],
        [ dcterms:type "text/html" ;
            ns4:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://doi.org/10.48550/arXiv.2404.17752> ],
        [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-4/collection.json> ],
        [ dcterms:type "text/html" ;
            ns4:relation <http://www.iana.org/assignments/relation/code> ;
            oa:hasTarget <https://github.com/robbiewatt1/ClimateDiffuse> ] ;
    geojson:bbox ( 2.336e+02 5.42e+01 2.975e+02 2.26e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 2.336e+02 5.42e+01 ) ( 2.975e+02 5.42e+01 ) ( 2.975e+02 2.26e+01 ) ( 2.336e+02 2.26e+01 ) ( 2.336e+02 5.42e+01 ) ) ) ] ;
    stac:end_datetime "2100-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns3:model <https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Network.py> ;
            ns3:train-script <https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/TrainUnet.py> ;
            ns3:weights <https://github.com/robbiewatt1/ClimateDiffuse/raw/refs/heads/main/Model_chpt/unet.pt> ] ;
    stac:hasExtension "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
        "https://stac-extensions.github.io/file/v2.1.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
        "https://stac-extensions.github.io/scientific/v1.0.0/schema.json" ;
    stac:start_datetime "1940-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    cube:dimensions [ cube:extent ( "1940-01-01T00:00:00Z" "2100-12-31T23:59:59Z" ) ;
            cube:step "P1H" ;
            cube:type "temporal" ;
            mlm:datacube_dimension_name "time" ],
        [ cube:axis "x" ;
            cube:extent ( 2.336e+02 2.975e+02 ) ;
            cube:type "spatial" ;
            mlm:datacube_dimension_name "lon" ],
        [ cube:axis "y" ;
            cube:extent ( 5.42e+01 2.26e+01 ) ;
            cube:type "spatial" ;
            mlm:datacube_dimension_name "lat" ] ;
    cube:variables [ cube:data_type "float32" ;
            cube:description "This parameter is the eastward component of the 10m wind. It is the horizontal speed of air moving towards the east, at a height of ten metres above the surface of the Earth, in metres per second." ;
            cube:dimensions "lat",
                "lon",
                "time" ;
            cube:type "data" ;
            cube:unit "m s-1" ;
            mlm:datacube_variable_name "10m_u_component_of_wind" ],
        [ cube:data_type "float32" ;
            cube:description "This parameter is the northward component of the 10m wind. It is the horizontal speed of air moving towards the north, at a height of ten metres above the surface of the Earth, in metres per second." ;
            cube:dimensions "lat",
                "lon",
                "time" ;
            cube:type "data" ;
            cube:unit "m s-1" ;
            mlm:datacube_variable_name "10m_v_component_of_wind" ],
        [ cube:data_type "float32" ;
            cube:description "Proportion of land-sea, where 1 indicates land and 0 indicates sea." ;
            cube:dimensions "lat",
                "lon" ;
            cube:extent ( 0 1 ) ;
            cube:type "data" ;
            mlm:datacube_variable_name "land_sea_mask" ],
        [ cube:data_type "float32" ;
            cube:description "This parameter is the geopotential, which is the potential energy per unit mass at a point in the atmosphere, expressed in metres squared per second squared (m² s⁻²). It is a measure of the height of a point in the atmosphere relative to sea level." ;
            cube:dimensions "lat",
                "lon" ;
            cube:type "data" ;
            cube:unit "m² s-2" ;
            mlm:datacube_variable_name "geopotential" ],
        [ cube:data_type "float32" ;
            cube:description "This parameter is the temperature of air at 2m above the surface of land, sea or in-land waters." ;
            cube:dimensions "lat",
                "lon",
                "time" ;
            cube:type "data" ;
            cube:unit "K" ;
            mlm:datacube_variable_name "temperature_2m" ] ;
    mlm:accelerator mlm:cuda ;
    mlm:accelerator_constrained false ;
    mlm:architecture "U-Net"^^xsd:string ;
    mlm:framework "pytorch"^^xsd:string ;
    mlm:framework_version "2.1.2+cu118"^^xsd:string ;
    mlm:input ( [ mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "time" "variables" "lat" "lon" ) ;
                        mlm:shape ( -1 5 128 256 ) ] ;
                mlm:io_name "Coarse climate variables employed by the model downscaling regression. This model takes 2 'constant/spatial' variables and 3 'spatio-temporal' variables provided by ERA5 datacube." ;
                mlm:norm_by_channel false ;
                mlm:pre_processing_function "{\"description\":\"Script that performs the relevant normalization and concatenation of variables for model input.\",\"expression\":{\"href\":\"https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/DatasetUS.py\",\"type\":\"text/x-python\"},\"format\":\"uri\"}"^^rdf:JSON ;
                mlm:variables ( "land_sea_mask" "geopotential" "temperature_2m" "10m_u_component_of_wind" "10m_v_component_of_wind" ) ] ) ;
    mlm:name "UNet ClimateDiffuse ERA5 Downscaling"^^xsd:string ;
    mlm:output ( [ mlm:io_name "Fine climate variables predicted by the model. Only the 3 'spatio-temporal' variables are predicted." ;
                mlm:result [ mlm:data_type "float32" ;
                        mlm:dim_order ( "time" "variables" "lat" "lon" ) ;
                        mlm:shape ( -1 3 128 256 ) ] ;
                mlm:tasks ( mlm:regression mlm:downscaling ) ;
                mlm:variables ( "temperature_2m" "10m_u_component_of_wind" "10m_v_component_of_wind" ) ] ) ;
    mlm:tasks ( mlm:regression mlm:downscaling ) ;
    ns2:publications [ ] .

<https://github.com/robbiewatt1/ClimateDiffuse/raw/refs/heads/main/Model_chpt/unet.pt> ns1:size 389657415 ;
    dcterms:format "application/octet-stream; application=pytorch" ;
    dcterms:title "U-Net Pytorch weights checkpoint" ;
    stac:hasAssetroles "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string .

<https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/Network.py> dcterms:description "Source code to define the U-Net model." ;
    dcterms:format "text/x-python" ;
    dcterms:title "Model implementation." ;
    stac:hasAssetroles "code"^^xsd:string,
        "metadata"^^xsd:string,
        "mlm:source_code"^^xsd:string .

<https://raw.githubusercontent.com/robbiewatt1/ClimateDiffuse/refs/heads/main/src/TrainUnet.py> dcterms:description "Script to run training of the model." ;
    dcterms:format "text/x-python" ;
    dcterms:title "Training script." ;
    stac:hasAssetroles "code"^^xsd:string,
        "metadata"^^xsd:string,
        "mlm:training"^^xsd:string .


```


### Demonstrate the use of MLM with both EO and Raster extensions using complementary bands details to describe the Model Asset by band name reference.
#### geojson
```geojson
{
  "$comment": "Demonstrate the use of MLM with both EO and Raster extensions using complementary bands details to describe the Model Asset by band name reference.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "description": "Coastal aerosol (band 1)",
        "center_wavelength": 0.443,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "description": "Blue (band 2)",
        "center_wavelength": 0.49,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "description": "Green (band 3)",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "description": "Red (band 4)",
        "center_wavelength": 0.665,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "common_name": "rededge",
        "description": "Red edge 1 (band 5)",
        "center_wavelength": 0.704,
        "full_width_half_max": 0.019
      },
      {
        "name": "B06",
        "common_name": "rededge",
        "description": "Red edge 2 (band 6)",
        "center_wavelength": 0.74,
        "full_width_half_max": 0.018
      },
      {
        "name": "B07",
        "common_name": "rededge",
        "description": "Red edge 3 (band 7)",
        "center_wavelength": 0.783,
        "full_width_half_max": 0.028
      },
      {
        "name": "B08",
        "common_name": "nir",
        "description": "NIR 1 (band 8)",
        "center_wavelength": 0.842,
        "full_width_half_max": 0.145
      },
      {
        "name": "B8A",
        "common_name": "nir08",
        "description": "NIR 2 (band 8A)",
        "center_wavelength": 0.865,
        "full_width_half_max": 0.033
      },
      {
        "name": "B09",
        "common_name": "nir09",
        "description": "NIR 3 (band 9)",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "description": "SWIR - Cirrus (band 10)",
        "center_wavelength": 1.375,
        "full_width_half_max": 0.026
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "description": "SWIR 1 (band 11)",
        "center_wavelength": 1.61,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "description": "SWIR 2 (band 12)",
        "center_wavelength": 2.19,
        "full_width_half_max": 0.242
      }
    ],
    "raster:bands": [
      {
        "name": "B01",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B02",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B03",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B04",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B05",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B06",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B07",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B08",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B8A",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B09",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B10",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B11",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B12",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "coastal"
        },
        {
          "name": "blue"
        },
        {
          "name": "green"
        },
        {
          "name": "red"
        },
        {
          "name": "rededge1"
        },
        {
          "name": "rededge2"
        },
        {
          "name": "rededge3"
        },
        {
          "name": "nir"
        },
        {
          "name": "nir08"
        },
        {
          "name": "nir09"
        },
        {
          "name": "cirrus"
        },
        {
          "name": "swir16"
        },
        {
          "name": "swir22"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM with both EO and Raster extensions using complementary bands details to describe the Model Asset by band name reference.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "description": "Coastal aerosol (band 1)",
        "center_wavelength": 0.443,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "description": "Blue (band 2)",
        "center_wavelength": 0.49,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "description": "Green (band 3)",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "description": "Red (band 4)",
        "center_wavelength": 0.665,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "common_name": "rededge",
        "description": "Red edge 1 (band 5)",
        "center_wavelength": 0.704,
        "full_width_half_max": 0.019
      },
      {
        "name": "B06",
        "common_name": "rededge",
        "description": "Red edge 2 (band 6)",
        "center_wavelength": 0.74,
        "full_width_half_max": 0.018
      },
      {
        "name": "B07",
        "common_name": "rededge",
        "description": "Red edge 3 (band 7)",
        "center_wavelength": 0.783,
        "full_width_half_max": 0.028
      },
      {
        "name": "B08",
        "common_name": "nir",
        "description": "NIR 1 (band 8)",
        "center_wavelength": 0.842,
        "full_width_half_max": 0.145
      },
      {
        "name": "B8A",
        "common_name": "nir08",
        "description": "NIR 2 (band 8A)",
        "center_wavelength": 0.865,
        "full_width_half_max": 0.033
      },
      {
        "name": "B09",
        "common_name": "nir09",
        "description": "NIR 3 (band 9)",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "description": "SWIR - Cirrus (band 10)",
        "center_wavelength": 1.375,
        "full_width_half_max": 0.026
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "description": "SWIR 1 (band 11)",
        "center_wavelength": 1.61,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "description": "SWIR 2 (band 12)",
        "center_wavelength": 2.19,
        "full_width_half_max": 0.242
      }
    ],
    "raster:bands": [
      {
        "name": "B01",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B02",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B03",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B04",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B05",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B06",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B07",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B08",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 10,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B8A",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B09",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B10",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 60,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B11",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      },
      {
        "name": "B12",
        "nodata": 0,
        "data_type": "uint16",
        "bits_per_sample": 15,
        "spatial_resolution": 20,
        "scale": 0.0001,
        "offset": 0,
        "unit": "m"
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "coastal"
        },
        {
          "name": "blue"
        },
        {
          "name": "green"
        },
        {
          "name": "red"
        },
        {
          "name": "rededge1"
        },
        {
          "name": "rededge2"
        },
        {
          "name": "rededge3"
        },
        {
          "name": "nir"
        },
        {
          "name": "nir08"
        },
        {
          "name": "nir09"
        },
        {
          "name": "cirrus"
        },
        {
          "name": "swir16"
        },
        {
          "name": "swir22"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <eo:> .
@prefix ns3: <raster:> .
@prefix ns4: <ml-aoi:> .
@prefix ns5: <file:> .
@prefix ns6: <http://www.iana.org/assignments/> .
@prefix ns7: <https://w3id.org/ogc/stac/assets/$> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-5/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns2:bands [ dcterms:description "SWIR 2 (band 12)" ],
        [ dcterms:description "Red edge 1 (band 5)" ],
        [ dcterms:description "SWIR - Cirrus (band 10)" ],
        [ dcterms:description "NIR 2 (band 8A)" ],
        [ dcterms:description "NIR 1 (band 8)" ],
        [ dcterms:description "Red edge 3 (band 7)" ],
        [ dcterms:description "Red edge 2 (band 6)" ],
        [ dcterms:description "Blue (band 2)" ],
        [ dcterms:description "Red (band 4)" ],
        [ dcterms:description "Green (band 3)" ],
        [ dcterms:description "SWIR 1 (band 11)" ],
        [ dcterms:description "NIR 3 (band 9)" ],
        [ dcterms:description "Coastal aerosol (band 1)" ] ;
    ns5:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns6:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-5/item_eo_bands.json> ],
        [ dcterms:type "application/json" ;
            ns6:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns4:split "train" ],
        [ dcterms:type "application/json" ;
            ns6:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-5/collection.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns1:source_code <https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> ;
            ns1:weights <https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    mlm:accelerator mlm:cuda ;
    mlm:accelerator_constrained false ;
    mlm:accelerator_summary "Unknown"^^xsd:string ;
    mlm:architecture "ResNet"^^xsd:string ;
    mlm:batch_size_suggestion "256"^^xsd:nonNegativeInteger ;
    mlm:framework "pytorch"^^xsd:string ;
    mlm:framework_version "2.1.2+cu121"^^xsd:string ;
    mlm:input ( [ mlm:bands ( "B01" "B02" "B03" "B04" "B05" "B06" "B07" "B08" "B8A" "B09" "B10" "B11" "B12" ) ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "bands" "height" "width" ) ;
                        mlm:shape ( -1 13 64 64 ) ] ;
                mlm:io_name "13 Band Sentinel-2 Batch" ;
                mlm:pre_processing_function "{\"expression\":\"torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn\",\"format\":\"python\"}"^^rdf:JSON ;
                mlm:value_scaling ( [ mlm:mean 1.354405e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 2.457176e+02 ] [ mlm:mean 1.118244e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 3.330078e+02 ] [ mlm:mean 1.04293e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 3.950925e+02 ] [ mlm:mean 9.476262e+02 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 5.937506e+02 ] [ mlm:mean 1.199473e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 5.66417e+02 ] [ mlm:mean 1.999791e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 8.61184e+02 ] [ mlm:mean 2.369223e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.086631e+03 ] [ mlm:mean 2.296826e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.117982e+03 ] [ mlm:mean 7.320834e+02 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 4.049198e+02 ] [ mlm:mean 1.211328e+01 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 4.775845e+00 ] [ mlm:mean 1.81901e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.002588e+03 ] [ mlm:mean 1.118924e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 7.613032e+02 ] [ mlm:mean 2.594141e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.231586e+03 ] ) ] ) ;
    mlm:memory_size "1"^^xsd:nonNegativeInteger ;
    mlm:name "Resnet-18 Sentinel-2 ALL MOCO"^^xsd:string ;
    mlm:output ( [ mlm:classification_classes [ mlm:io_name "River" ;
                        mlm:nodata false ;
                        mlm:value 8 ],
                    [ mlm:io_name "Annual Crop" ;
                        mlm:nodata false ;
                        mlm:value 0 ],
                    [ mlm:io_name "Pasture" ;
                        mlm:nodata false ;
                        mlm:value 5 ],
                    [ mlm:io_name "Highway" ;
                        mlm:nodata false ;
                        mlm:value 3 ],
                    [ mlm:io_name "SeaLake" ;
                        mlm:nodata false ;
                        mlm:value 9 ],
                    [ mlm:io_name "Industrial Buildings" ;
                        mlm:nodata false ;
                        mlm:value 4 ],
                    [ mlm:io_name "Forest" ;
                        mlm:nodata false ;
                        mlm:value 1 ],
                    [ mlm:io_name "Herbaceous Vegetation" ;
                        mlm:nodata false ;
                        mlm:value 2 ],
                    [ mlm:io_name "Residential Buildings" ;
                        mlm:nodata false ;
                        mlm:value 7 ],
                    [ mlm:io_name "Permanent Crop" ;
                        mlm:nodata false ;
                        mlm:value 6 ] ;
                mlm:io_name "classification" ;
                mlm:post_processing_function "null"^^rdf:JSON ;
                mlm:result [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "class" ) ;
                        mlm:shape ( -1 10 ) ] ;
                mlm:tasks ( mlm:classification ) ] ) ;
    mlm:pretrained_source "EuroSat Sentinel-2"^^xsd:string ;
    mlm:tasks ( mlm:classification ) ;
    mlm:total_parameters "11700000"^^xsd:nonNegativeInteger ;
    ns3:bands [ ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ ],
        [ ] .

<https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> dcterms:description "Source code to run the model." ;
    dcterms:format "text/x-python" ;
    dcterms:title "Model implementation." ;
    stac:hasAssetroles "code"^^xsd:string,
        "metadata"^^xsd:string .

<https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> ns2:bands [ ns1:name "nir09" ],
        [ ns1:name "rededge1" ],
        [ ns1:name "rededge2" ],
        [ ns1:name "nir" ],
        [ ns1:name "nir08" ],
        [ ns1:name "swir22" ],
        [ ns1:name "cirrus" ],
        [ ns1:name "rededge3" ],
        [ ns1:name "swir16" ],
        [ ns1:name "coastal" ],
        [ ns1:name "blue" ],
        [ ns1:name "green" ],
        [ ns1:name "red" ] ;
    dcterms:description "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo" ;
    dcterms:format "application/octet-stream; application=pytorch" ;
    dcterms:title "Pytorch weights checkpoint" ;
    ns7:comment "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension." ;
    stac:hasAssetroles "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string .


```


### Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.
#### geojson
```geojson
{
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "norm_by_channel": true,
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "B01",
          "common_name": "coastal",
          "description": "Coastal aerosol (band 1)",
          "center_wavelength": 0.443,
          "full_width_half_max": 0.027
        },
        {
          "name": "B02",
          "common_name": "blue",
          "description": "Blue (band 2)",
          "center_wavelength": 0.49,
          "full_width_half_max": 0.098
        },
        {
          "name": "B03",
          "common_name": "green",
          "description": "Green (band 3)",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B04",
          "common_name": "red",
          "description": "Red (band 4)",
          "center_wavelength": 0.665,
          "full_width_half_max": 0.038
        },
        {
          "name": "B05",
          "common_name": "rededge",
          "description": "Red edge 1 (band 5)",
          "center_wavelength": 0.704,
          "full_width_half_max": 0.019
        },
        {
          "name": "B06",
          "common_name": "rededge",
          "description": "Red edge 2 (band 6)",
          "center_wavelength": 0.74,
          "full_width_half_max": 0.018
        },
        {
          "name": "B07",
          "common_name": "rededge",
          "description": "Red edge 3 (band 7)",
          "center_wavelength": 0.783,
          "full_width_half_max": 0.028
        },
        {
          "name": "B08",
          "common_name": "nir",
          "description": "NIR 1 (band 8)",
          "center_wavelength": 0.842,
          "full_width_half_max": 0.145
        },
        {
          "name": "B8A",
          "common_name": "nir08",
          "description": "NIR 2 (band 8A)",
          "center_wavelength": 0.865,
          "full_width_half_max": 0.033
        },
        {
          "name": "B09",
          "common_name": "nir09",
          "description": "NIR 3 (band 9)",
          "center_wavelength": 0.945,
          "full_width_half_max": 0.026
        },
        {
          "name": "B10",
          "common_name": "cirrus",
          "description": "SWIR - Cirrus (band 10)",
          "center_wavelength": 1.375,
          "full_width_half_max": 0.026
        },
        {
          "name": "B11",
          "common_name": "swir16",
          "description": "SWIR 1 (band 11)",
          "center_wavelength": 1.61,
          "full_width_half_max": 0.143
        },
        {
          "name": "B12",
          "common_name": "swir22",
          "description": "SWIR 2 (band 12)",
          "center_wavelength": 2.19,
          "full_width_half_max": 0.242
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "norm_by_channel": true,
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "B01",
          "common_name": "coastal",
          "description": "Coastal aerosol (band 1)",
          "center_wavelength": 0.443,
          "full_width_half_max": 0.027
        },
        {
          "name": "B02",
          "common_name": "blue",
          "description": "Blue (band 2)",
          "center_wavelength": 0.49,
          "full_width_half_max": 0.098
        },
        {
          "name": "B03",
          "common_name": "green",
          "description": "Green (band 3)",
          "center_wavelength": 0.56,
          "full_width_half_max": 0.045
        },
        {
          "name": "B04",
          "common_name": "red",
          "description": "Red (band 4)",
          "center_wavelength": 0.665,
          "full_width_half_max": 0.038
        },
        {
          "name": "B05",
          "common_name": "rededge",
          "description": "Red edge 1 (band 5)",
          "center_wavelength": 0.704,
          "full_width_half_max": 0.019
        },
        {
          "name": "B06",
          "common_name": "rededge",
          "description": "Red edge 2 (band 6)",
          "center_wavelength": 0.74,
          "full_width_half_max": 0.018
        },
        {
          "name": "B07",
          "common_name": "rededge",
          "description": "Red edge 3 (band 7)",
          "center_wavelength": 0.783,
          "full_width_half_max": 0.028
        },
        {
          "name": "B08",
          "common_name": "nir",
          "description": "NIR 1 (band 8)",
          "center_wavelength": 0.842,
          "full_width_half_max": 0.145
        },
        {
          "name": "B8A",
          "common_name": "nir08",
          "description": "NIR 2 (band 8A)",
          "center_wavelength": 0.865,
          "full_width_half_max": 0.033
        },
        {
          "name": "B09",
          "common_name": "nir09",
          "description": "NIR 3 (band 9)",
          "center_wavelength": 0.945,
          "full_width_half_max": 0.026
        },
        {
          "name": "B10",
          "common_name": "cirrus",
          "description": "SWIR - Cirrus (band 10)",
          "center_wavelength": 1.375,
          "full_width_half_max": 0.026
        },
        {
          "name": "B11",
          "common_name": "swir16",
          "description": "SWIR 1 (band 11)",
          "center_wavelength": 1.61,
          "full_width_half_max": 0.143
        },
        {
          "name": "B12",
          "common_name": "swir22",
          "description": "SWIR 2 (band 12)",
          "center_wavelength": 2.19,
          "full_width_half_max": 0.242
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <eo:> .
@prefix ns4: <file:> .
@prefix ns5: <ml-aoi:> .
@prefix ns6: <https://w3id.org/ogc/stac/assets/$> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-6/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns4:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-6/collection.json> ],
        [ dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns5:split "train" ],
        [ dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-6/item_eo_bands.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns1:source_code <https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> ;
            ns1:weights <https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    mlm:accelerator mlm:cuda ;
    mlm:accelerator_constrained false ;
    mlm:accelerator_summary "Unknown"^^xsd:string ;
    mlm:architecture "ResNet"^^xsd:string ;
    mlm:batch_size_suggestion "256"^^xsd:nonNegativeInteger ;
    mlm:framework "pytorch"^^xsd:string ;
    mlm:framework_version "2.1.2+cu121"^^xsd:string ;
    mlm:input ( [ mlm:bands ( "B01" "B02" "B03" "B04" "B05" "B06" "B07" "B08" "B8A" "B09" "B10" "B11" "B12" ) ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "bands" "height" "width" ) ;
                        mlm:shape ( -1 13 64 64 ) ] ;
                mlm:io_name "13 Band Sentinel-2 Batch" ;
                mlm:norm_by_channel true ;
                mlm:pre_processing_function "{\"expression\":\"torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn\",\"format\":\"python\"}"^^rdf:JSON ;
                mlm:value_scaling ( [ mlm:mean 1.354405e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 2.457176e+02 ] [ mlm:mean 1.118244e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 3.330078e+02 ] [ mlm:mean 1.04293e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 3.950925e+02 ] [ mlm:mean 9.476262e+02 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 5.937506e+02 ] [ mlm:mean 1.199473e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 5.66417e+02 ] [ mlm:mean 1.999791e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 8.61184e+02 ] [ mlm:mean 2.369223e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.086631e+03 ] [ mlm:mean 2.296826e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.117982e+03 ] [ mlm:mean 7.320834e+02 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 4.049198e+02 ] [ mlm:mean 1.211328e+01 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 4.775845e+00 ] [ mlm:mean 1.81901e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.002588e+03 ] [ mlm:mean 1.118924e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 7.613032e+02 ] [ mlm:mean 2.594141e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.231586e+03 ] ) ] ) ;
    mlm:memory_size "1"^^xsd:nonNegativeInteger ;
    mlm:name "Resnet-18 Sentinel-2 ALL MOCO"^^xsd:string ;
    mlm:output ( [ mlm:classification_classes [ mlm:io_name "Residential Buildings" ;
                        mlm:nodata false ;
                        mlm:value 7 ],
                    [ mlm:io_name "Forest" ;
                        mlm:nodata false ;
                        mlm:value 1 ],
                    [ mlm:io_name "Permanent Crop" ;
                        mlm:nodata false ;
                        mlm:value 6 ],
                    [ mlm:io_name "Annual Crop" ;
                        mlm:nodata false ;
                        mlm:value 0 ],
                    [ mlm:io_name "Herbaceous Vegetation" ;
                        mlm:nodata false ;
                        mlm:value 2 ],
                    [ mlm:io_name "Pasture" ;
                        mlm:nodata false ;
                        mlm:value 5 ],
                    [ mlm:io_name "River" ;
                        mlm:nodata false ;
                        mlm:value 8 ],
                    [ mlm:io_name "SeaLake" ;
                        mlm:nodata false ;
                        mlm:value 9 ],
                    [ mlm:io_name "Industrial Buildings" ;
                        mlm:nodata false ;
                        mlm:value 4 ],
                    [ mlm:io_name "Highway" ;
                        mlm:nodata false ;
                        mlm:value 3 ] ;
                mlm:io_name "classification" ;
                mlm:post_processing_function "null"^^rdf:JSON ;
                mlm:result [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "class" ) ;
                        mlm:shape ( -1 10 ) ] ;
                mlm:tasks ( mlm:classification ) ] ) ;
    mlm:pretrained_source "EuroSat Sentinel-2"^^xsd:string ;
    mlm:tasks ( mlm:classification ) ;
    mlm:total_parameters "11700000"^^xsd:nonNegativeInteger .

<https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> dcterms:description "Source code to run the model." ;
    dcterms:format "text/x-python" ;
    dcterms:title "Model implementation." ;
    stac:hasAssetroles "code"^^xsd:string,
        "metadata"^^xsd:string,
        "mlm:source_code"^^xsd:string .

<https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> ns3:bands [ dcterms:description "SWIR - Cirrus (band 10)" ;
            ns1:center_wavelength 1.375e+00 ;
            ns1:common_name "cirrus" ;
            ns1:full_width_half_max 2.6e-02 ;
            ns1:name "B10" ],
        [ dcterms:description "Red edge 1 (band 5)" ;
            ns1:center_wavelength 7.04e-01 ;
            ns1:common_name "rededge" ;
            ns1:full_width_half_max 1.9e-02 ;
            ns1:name "B05" ],
        [ dcterms:description "SWIR 1 (band 11)" ;
            ns1:center_wavelength 1.61e+00 ;
            ns1:common_name "swir16" ;
            ns1:full_width_half_max 1.43e-01 ;
            ns1:name "B11" ],
        [ dcterms:description "Red (band 4)" ;
            ns1:center_wavelength 6.65e-01 ;
            ns1:common_name "red" ;
            ns1:full_width_half_max 3.8e-02 ;
            ns1:name "B04" ],
        [ dcterms:description "NIR 2 (band 8A)" ;
            ns1:center_wavelength 8.65e-01 ;
            ns1:common_name "nir08" ;
            ns1:full_width_half_max 3.3e-02 ;
            ns1:name "B8A" ],
        [ dcterms:description "Blue (band 2)" ;
            ns1:center_wavelength 4.9e-01 ;
            ns1:common_name "blue" ;
            ns1:full_width_half_max 9.8e-02 ;
            ns1:name "B02" ],
        [ dcterms:description "Coastal aerosol (band 1)" ;
            ns1:center_wavelength 4.43e-01 ;
            ns1:common_name "coastal" ;
            ns1:full_width_half_max 2.7e-02 ;
            ns1:name "B01" ],
        [ dcterms:description "NIR 3 (band 9)" ;
            ns1:center_wavelength 9.45e-01 ;
            ns1:common_name "nir09" ;
            ns1:full_width_half_max 2.6e-02 ;
            ns1:name "B09" ],
        [ dcterms:description "Green (band 3)" ;
            ns1:center_wavelength 5.6e-01 ;
            ns1:common_name "green" ;
            ns1:full_width_half_max 4.5e-02 ;
            ns1:name "B03" ],
        [ dcterms:description "SWIR 2 (band 12)" ;
            ns1:center_wavelength 2.19e+00 ;
            ns1:common_name "swir22" ;
            ns1:full_width_half_max 2.42e-01 ;
            ns1:name "B12" ],
        [ dcterms:description "NIR 1 (band 8)" ;
            ns1:center_wavelength 8.42e-01 ;
            ns1:common_name "nir" ;
            ns1:full_width_half_max 1.45e-01 ;
            ns1:name "B08" ],
        [ dcterms:description "Red edge 3 (band 7)" ;
            ns1:center_wavelength 7.83e-01 ;
            ns1:common_name "rededge" ;
            ns1:full_width_half_max 2.8e-02 ;
            ns1:name "B07" ],
        [ dcterms:description "Red edge 2 (band 6)" ;
            ns1:center_wavelength 7.4e-01 ;
            ns1:common_name "rededge" ;
            ns1:full_width_half_max 1.8e-02 ;
            ns1:name "B06" ] ;
    dcterms:description "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo" ;
    dcterms:format "application/octet-stream; application=pytorch" ;
    dcterms:title "Pytorch weights checkpoint" ;
    ns6:comment "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension." ;
    stac:hasAssetroles "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string .


```


### Demonstrate the use of MLM and EO for bands description, with EO bands summarized in the Item properties and referenced by name in the Model Asset.
#### geojson
```geojson
{
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands summarized in the Item properties and referenced by name in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "description": "Coastal aerosol (band 1)",
        "center_wavelength": 0.443,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "description": "Blue (band 2)",
        "center_wavelength": 0.49,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "description": "Green (band 3)",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "description": "Red (band 4)",
        "center_wavelength": 0.665,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "common_name": "rededge",
        "description": "Red edge 1 (band 5)",
        "center_wavelength": 0.704,
        "full_width_half_max": 0.019
      },
      {
        "name": "B06",
        "common_name": "rededge",
        "description": "Red edge 2 (band 6)",
        "center_wavelength": 0.74,
        "full_width_half_max": 0.018
      },
      {
        "name": "B07",
        "common_name": "rededge",
        "description": "Red edge 3 (band 7)",
        "center_wavelength": 0.783,
        "full_width_half_max": 0.028
      },
      {
        "name": "B08",
        "common_name": "nir",
        "description": "NIR 1 (band 8)",
        "center_wavelength": 0.842,
        "full_width_half_max": 0.145
      },
      {
        "name": "B8A",
        "common_name": "nir08",
        "description": "NIR 2 (band 8A)",
        "center_wavelength": 0.865,
        "full_width_half_max": 0.033
      },
      {
        "name": "B09",
        "common_name": "nir09",
        "description": "NIR 3 (band 9)",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "description": "SWIR - Cirrus (band 10)",
        "center_wavelength": 1.375,
        "full_width_half_max": 0.026
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "description": "SWIR 1 (band 11)",
        "center_wavelength": 1.61,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "description": "SWIR 2 (band 12)",
        "center_wavelength": 2.19,
        "full_width_half_max": 0.242
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "coastal"
        },
        {
          "name": "blue"
        },
        {
          "name": "green"
        },
        {
          "name": "red"
        },
        {
          "name": "rededge1"
        },
        {
          "name": "rededge2"
        },
        {
          "name": "rededge3"
        },
        {
          "name": "nir"
        },
        {
          "name": "nir08"
        },
        {
          "name": "nir09"
        },
        {
          "name": "cirrus"
        },
        {
          "name": "swir16"
        },
        {
          "name": "swir22"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and EO for bands description, with EO bands summarized in the Item properties and referenced by name in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "resize_type": null,
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 1354.40546513,
            "stddev": 245.71762908
          },
          {
            "type": "z-score",
            "mean": 1118.24399958,
            "stddev": 333.00778264
          },
          {
            "type": "z-score",
            "mean": 1042.92983953,
            "stddev": 395.09249139
          },
          {
            "type": "z-score",
            "mean": 947.62620298,
            "stddev": 593.75055589
          },
          {
            "type": "z-score",
            "mean": 1199.47283961,
            "stddev": 566.4170017
          },
          {
            "type": "z-score",
            "mean": 1999.79090914,
            "stddev": 861.18399006
          },
          {
            "type": "z-score",
            "mean": 2369.22292565,
            "stddev": 1086.63139075
          },
          {
            "type": "z-score",
            "mean": 2296.82608323,
            "stddev": 1117.98170791
          },
          {
            "type": "z-score",
            "mean": 732.08340178,
            "stddev": 404.91978886
          },
          {
            "type": "z-score",
            "mean": 12.11327804,
            "stddev": 4.77584468
          },
          {
            "type": "z-score",
            "mean": 1819.01027855,
            "stddev": 1002.58768311
          },
          {
            "type": "z-score",
            "mean": 1118.92391149,
            "stddev": 761.30323499
          },
          {
            "type": "z-score",
            "mean": 2594.14080798,
            "stddev": 1231.58581042
          }
        ],
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ],
    "eo:bands": [
      {
        "name": "B01",
        "common_name": "coastal",
        "description": "Coastal aerosol (band 1)",
        "center_wavelength": 0.443,
        "full_width_half_max": 0.027
      },
      {
        "name": "B02",
        "common_name": "blue",
        "description": "Blue (band 2)",
        "center_wavelength": 0.49,
        "full_width_half_max": 0.098
      },
      {
        "name": "B03",
        "common_name": "green",
        "description": "Green (band 3)",
        "center_wavelength": 0.56,
        "full_width_half_max": 0.045
      },
      {
        "name": "B04",
        "common_name": "red",
        "description": "Red (band 4)",
        "center_wavelength": 0.665,
        "full_width_half_max": 0.038
      },
      {
        "name": "B05",
        "common_name": "rededge",
        "description": "Red edge 1 (band 5)",
        "center_wavelength": 0.704,
        "full_width_half_max": 0.019
      },
      {
        "name": "B06",
        "common_name": "rededge",
        "description": "Red edge 2 (band 6)",
        "center_wavelength": 0.74,
        "full_width_half_max": 0.018
      },
      {
        "name": "B07",
        "common_name": "rededge",
        "description": "Red edge 3 (band 7)",
        "center_wavelength": 0.783,
        "full_width_half_max": 0.028
      },
      {
        "name": "B08",
        "common_name": "nir",
        "description": "NIR 1 (band 8)",
        "center_wavelength": 0.842,
        "full_width_half_max": 0.145
      },
      {
        "name": "B8A",
        "common_name": "nir08",
        "description": "NIR 2 (band 8A)",
        "center_wavelength": 0.865,
        "full_width_half_max": 0.033
      },
      {
        "name": "B09",
        "common_name": "nir09",
        "description": "NIR 3 (band 9)",
        "center_wavelength": 0.945,
        "full_width_half_max": 0.026
      },
      {
        "name": "B10",
        "common_name": "cirrus",
        "description": "SWIR - Cirrus (band 10)",
        "center_wavelength": 1.375,
        "full_width_half_max": 0.026
      },
      {
        "name": "B11",
        "common_name": "swir16",
        "description": "SWIR 1 (band 11)",
        "center_wavelength": 1.61,
        "full_width_half_max": 0.143
      },
      {
        "name": "B12",
        "common_name": "swir22",
        "description": "SWIR 2 (band 12)",
        "center_wavelength": 2.19,
        "full_width_half_max": 0.242
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "$comment": "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension.",
      "eo:bands": [
        {
          "name": "coastal"
        },
        {
          "name": "blue"
        },
        {
          "name": "green"
        },
        {
          "name": "red"
        },
        {
          "name": "rededge1"
        },
        {
          "name": "rededge2"
        },
        {
          "name": "rededge3"
        },
        {
          "name": "nir"
        },
        {
          "name": "nir08"
        },
        {
          "name": "nir09"
        },
        {
          "name": "cirrus"
        },
        {
          "name": "swir16"
        },
        {
          "name": "swir22"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_eo_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <eo:> .
@prefix ns2: <https://w3id.org/ogc/stac/assets/> .
@prefix ns3: <ml-aoi:> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix ns5: <file:> .
@prefix ns6: <https://w3id.org/ogc/stac/assets/$> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-7/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns1:bands [ dcterms:description "Red (band 4)" ],
        [ dcterms:description "Red edge 2 (band 6)" ],
        [ dcterms:description "NIR 2 (band 8A)" ],
        [ dcterms:description "SWIR 1 (band 11)" ],
        [ dcterms:description "SWIR - Cirrus (band 10)" ],
        [ dcterms:description "Blue (band 2)" ],
        [ dcterms:description "Coastal aerosol (band 1)" ],
        [ dcterms:description "Red edge 3 (band 7)" ],
        [ dcterms:description "NIR 1 (band 8)" ],
        [ dcterms:description "NIR 3 (band 9)" ],
        [ dcterms:description "Green (band 3)" ],
        [ dcterms:description "Red edge 1 (band 5)" ],
        [ dcterms:description "SWIR 2 (band 12)" ] ;
    ns5:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-7/collection.json> ],
        [ dcterms:type "application/geo+json" ;
            ns4:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-7/item_eo_bands.json> ],
        [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns3:split "train" ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns2:source_code <https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> ;
            ns2:weights <https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    mlm:accelerator mlm:cuda ;
    mlm:accelerator_constrained false ;
    mlm:accelerator_summary "Unknown"^^xsd:string ;
    mlm:architecture "ResNet"^^xsd:string ;
    mlm:batch_size_suggestion "256"^^xsd:nonNegativeInteger ;
    mlm:framework "pytorch"^^xsd:string ;
    mlm:framework_version "2.1.2+cu121"^^xsd:string ;
    mlm:input ( [ mlm:bands ( "B01" "B02" "B03" "B04" "B05" "B06" "B07" "B08" "B8A" "B09" "B10" "B11" "B12" ) ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "bands" "height" "width" ) ;
                        mlm:shape ( -1 13 64 64 ) ] ;
                mlm:io_name "13 Band Sentinel-2 Batch" ;
                mlm:pre_processing_function "{\"expression\":\"torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn\",\"format\":\"python\"}"^^rdf:JSON ;
                mlm:value_scaling ( [ mlm:mean 1.354405e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 2.457176e+02 ] [ mlm:mean 1.118244e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 3.330078e+02 ] [ mlm:mean 1.04293e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 3.950925e+02 ] [ mlm:mean 9.476262e+02 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 5.937506e+02 ] [ mlm:mean 1.199473e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 5.66417e+02 ] [ mlm:mean 1.999791e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 8.61184e+02 ] [ mlm:mean 2.369223e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.086631e+03 ] [ mlm:mean 2.296826e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.117982e+03 ] [ mlm:mean 7.320834e+02 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 4.049198e+02 ] [ mlm:mean 1.211328e+01 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 4.775845e+00 ] [ mlm:mean 1.81901e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.002588e+03 ] [ mlm:mean 1.118924e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 7.613032e+02 ] [ mlm:mean 2.594141e+03 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 1.231586e+03 ] ) ] ) ;
    mlm:memory_size "1"^^xsd:nonNegativeInteger ;
    mlm:name "Resnet-18 Sentinel-2 ALL MOCO"^^xsd:string ;
    mlm:output ( [ mlm:classification_classes [ mlm:io_name "River" ;
                        mlm:nodata false ;
                        mlm:value 8 ],
                    [ mlm:io_name "Highway" ;
                        mlm:nodata false ;
                        mlm:value 3 ],
                    [ mlm:io_name "SeaLake" ;
                        mlm:nodata false ;
                        mlm:value 9 ],
                    [ mlm:io_name "Pasture" ;
                        mlm:nodata false ;
                        mlm:value 5 ],
                    [ mlm:io_name "Permanent Crop" ;
                        mlm:nodata false ;
                        mlm:value 6 ],
                    [ mlm:io_name "Residential Buildings" ;
                        mlm:nodata false ;
                        mlm:value 7 ],
                    [ mlm:io_name "Annual Crop" ;
                        mlm:nodata false ;
                        mlm:value 0 ],
                    [ mlm:io_name "Herbaceous Vegetation" ;
                        mlm:nodata false ;
                        mlm:value 2 ],
                    [ mlm:io_name "Forest" ;
                        mlm:nodata false ;
                        mlm:value 1 ],
                    [ mlm:io_name "Industrial Buildings" ;
                        mlm:nodata false ;
                        mlm:value 4 ] ;
                mlm:io_name "classification" ;
                mlm:post_processing_function "null"^^rdf:JSON ;
                mlm:result [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "class" ) ;
                        mlm:shape ( -1 10 ) ] ;
                mlm:tasks ( mlm:classification ) ] ) ;
    mlm:pretrained_source "EuroSat Sentinel-2"^^xsd:string ;
    mlm:tasks ( mlm:classification ) ;
    mlm:total_parameters "11700000"^^xsd:nonNegativeInteger .

<https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> dcterms:description "Source code to run the model." ;
    dcterms:format "text/x-python" ;
    dcterms:title "Model implementation." ;
    stac:hasAssetroles "code"^^xsd:string,
        "metadata"^^xsd:string .

<https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> ns1:bands [ ns2:name "blue" ],
        [ ns2:name "rededge1" ],
        [ ns2:name "swir22" ],
        [ ns2:name "red" ],
        [ ns2:name "nir" ],
        [ ns2:name "swir16" ],
        [ ns2:name "cirrus" ],
        [ ns2:name "rededge2" ],
        [ ns2:name "nir09" ],
        [ ns2:name "nir08" ],
        [ ns2:name "rededge3" ],
        [ ns2:name "coastal" ],
        [ ns2:name "green" ] ;
    dcterms:description "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo" ;
    dcterms:format "application/octet-stream; application=pytorch" ;
    dcterms:title "Pytorch weights checkpoint" ;
    ns6:comment "Following 'eo:bands' is required to fulfil schema validation of 'eo' extension." ;
    stac:hasAssetroles "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string .


```


### Demonstrate the use of MLM with a mixture of inputs, some using EO bands, others without, and some with derived properties.
#### geojson
```geojson
{
  "$comment": "Demonstrate the use of MLM with a mixture of inputs, some using EO bands, others without, and some with derived properties.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "model-multi-input",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Generic model that employs multiple input sources with different combination of bands, and some inputs without any band at all.",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "RGB",
        "bands": [
          "B04",
          "B03",
          "B02"
        ],
        "input": {
          "shape": [
            -1,
            3,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "uint16"
        },
        "value_scaling": null,
        "resize_type": null
      },
      {
        "description": "Compute NDVI from Sentinel-2 bands. The single 'NDVI' virtual band is then fed as 'bands' dimension to the model input.",
        "name": "NDVI",
        "bands": [
          "B04",
          "B08"
        ],
        "pre_processing_function": {
          "format": "gdal-calc",
          "expression": "(A - B) / (A + B)"
        },
        "input": {
          "shape": [
            -1,
            1,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "uint16"
        }
      },
      {
        "description": "Digital elevation model. Comes from another source than the Sentinel bands. Therefore, no 'bands' associated to it.",
        "name": "DEM",
        "bands": [],
        "input": {
          "shape": [
            -1,
            1,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "h",
            "y",
            "x"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "vegetation-segmentation",
        "tasks": [
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            1
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "uint8"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "NON_VEGETATION",
            "description": "background pixels",
            "color_hint": null
          },
          {
            "value": 1,
            "name": "VEGETATION",
            "description": "pixels where vegetation was detected",
            "color_hint": [
              0,
              255,
              0
            ]
          }
        ],
        "post_processing_function": null
      },
      {
        "name": "inverse-mask",
        "tasks": [
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            1
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "uint8"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "NON_VEGETATION",
            "description": "background pixels",
            "color_hint": [
              255,
              255,
              255
            ]
          },
          {
            "value": 1,
            "name": "VEGETATION",
            "description": "pixels where vegetation was detected",
            "color_hint": [
              0,
              0,
              0
            ]
          }
        ],
        "post_processing_function": {
          "format": "gdal-calc",
          "expression": "logical_not(A)"
        }
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet50_sentinel2_rgb_moco/blob/main/resnet50_sentinel2_rgb_moco.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-50 classification model trained on Sentinel-2 RGB imagery with torchgeo.",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "raster:bands": [
        {
          "name": "B02",
          "common_name": "blue",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B03",
          "common_name": "green",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B04",
          "common_name": "red",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B08",
          "common_name": "nir",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        }
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_multi_io.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM with a mixture of inputs, some using EO bands, others without, and some with derived properties.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "model-multi-input",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Generic model that employs multiple input sources with different combination of bands, and some inputs without any band at all.",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "RGB",
        "bands": [
          "B04",
          "B03",
          "B02"
        ],
        "input": {
          "shape": [
            -1,
            3,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "uint16"
        },
        "value_scaling": null,
        "resize_type": null
      },
      {
        "description": "Compute NDVI from Sentinel-2 bands. The single 'NDVI' virtual band is then fed as 'bands' dimension to the model input.",
        "name": "NDVI",
        "bands": [
          "B04",
          "B08"
        ],
        "pre_processing_function": {
          "format": "gdal-calc",
          "expression": "(A - B) / (A + B)"
        },
        "input": {
          "shape": [
            -1,
            1,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "uint16"
        }
      },
      {
        "description": "Digital elevation model. Comes from another source than the Sentinel bands. Therefore, no 'bands' associated to it.",
        "name": "DEM",
        "bands": [],
        "input": {
          "shape": [
            -1,
            1,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "h",
            "y",
            "x"
          ],
          "data_type": "float32"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "vegetation-segmentation",
        "tasks": [
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            1
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "uint8"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "NON_VEGETATION",
            "description": "background pixels",
            "color_hint": null
          },
          {
            "value": 1,
            "name": "VEGETATION",
            "description": "pixels where vegetation was detected",
            "color_hint": [
              0,
              255,
              0
            ]
          }
        ],
        "post_processing_function": null
      },
      {
        "name": "inverse-mask",
        "tasks": [
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            1
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "uint8"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "NON_VEGETATION",
            "description": "background pixels",
            "color_hint": [
              255,
              255,
              255
            ]
          },
          {
            "value": 1,
            "name": "VEGETATION",
            "description": "pixels where vegetation was detected",
            "color_hint": [
              0,
              0,
              0
            ]
          }
        ],
        "post_processing_function": {
          "format": "gdal-calc",
          "expression": "logical_not(A)"
        }
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet50_sentinel2_rgb_moco/blob/main/resnet50_sentinel2_rgb_moco.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-50 classification model trained on Sentinel-2 RGB imagery with torchgeo.",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "raster:bands": [
        {
          "name": "B02",
          "common_name": "blue",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B03",
          "common_name": "green",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B04",
          "common_name": "red",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B08",
          "common_name": "nir",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        }
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_multi_io.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <file:> .
@prefix ns3: <raster:> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix ns5: <ml-aoi:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-8/model-multi-input> a geojson:Feature ;
    ns2:size 43000000 ;
    dcterms:description "Generic model that employs multiple input sources with different combination of bands, and some inputs without any band at all." ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns5:split "train" ],
        [ dcterms:type "application/geo+json" ;
            ns4:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-8/item_multi_io.json> ],
        [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-8/collection.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns1:weights <https://huggingface.co/torchgeo/resnet50_sentinel2_rgb_moco/blob/main/resnet50_sentinel2_rgb_moco.pth> ] ;
    stac:hasExtension "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    mlm:accelerator mlm:cuda ;
    mlm:accelerator_constrained false ;
    mlm:accelerator_summary "Unknown"^^xsd:string ;
    mlm:architecture "ResNet"^^xsd:string ;
    mlm:batch_size_suggestion "256"^^xsd:nonNegativeInteger ;
    mlm:framework "pytorch"^^xsd:string ;
    mlm:framework_version "2.1.2+cu121"^^xsd:string ;
    mlm:input ( [ mlm:bands ( "B04" "B03" "B02" ) ;
                mlm:input_structure [ mlm:data_type "uint16" ;
                        mlm:dim_order ( "batch" "bands" "height" "width" ) ;
                        mlm:shape ( -1 3 64 64 ) ] ;
                mlm:io_name "RGB" ;
                mlm:value_scaling () ] [ mlm:bands ( "B04" "B08" ) ;
                mlm:input_structure [ mlm:data_type "uint16" ;
                        mlm:dim_order ( "batch" "bands" "height" "width" ) ;
                        mlm:shape ( -1 1 64 64 ) ] ;
                mlm:io_description "Compute NDVI from Sentinel-2 bands. The single 'NDVI' virtual band is then fed as 'bands' dimension to the model input." ;
                mlm:io_name "NDVI" ;
                mlm:pre_processing_function "{\"expression\":\"(A - B) / (A + B)\",\"format\":\"gdal-calc\"}"^^rdf:JSON ] [ mlm:bands () ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "h" "y" "x" ) ;
                        mlm:shape ( -1 1 64 64 ) ] ;
                mlm:io_description "Digital elevation model. Comes from another source than the Sentinel bands. Therefore, no 'bands' associated to it." ;
                mlm:io_name "DEM" ] ) ;
    mlm:memory_size "1"^^xsd:nonNegativeInteger ;
    mlm:name "Resnet-18 Sentinel-2 ALL MOCO"^^xsd:string ;
    mlm:output ( [ mlm:classification_classes [ mlm:io_description "background pixels" ;
                        mlm:io_name "NON_VEGETATION" ;
                        mlm:value 0 ],
                    [ mlm:color_hint 0,
                            255 ;
                        mlm:io_description "pixels where vegetation was detected" ;
                        mlm:io_name "VEGETATION" ;
                        mlm:value 1 ] ;
                mlm:io_name "vegetation-segmentation" ;
                mlm:post_processing_function "null"^^rdf:JSON ;
                mlm:result [ mlm:data_type "uint8" ;
                        mlm:dim_order ( "batch" "class" ) ;
                        mlm:shape ( -1 1 ) ] ;
                mlm:tasks ( mlm:semantic-segmentation ) ] [ mlm:classification_classes [ mlm:color_hint 0 ;
                        mlm:io_description "pixels where vegetation was detected" ;
                        mlm:io_name "VEGETATION" ;
                        mlm:value 1 ],
                    [ mlm:color_hint 255 ;
                        mlm:io_description "background pixels" ;
                        mlm:io_name "NON_VEGETATION" ;
                        mlm:value 0 ] ;
                mlm:io_name "inverse-mask" ;
                mlm:post_processing_function "{\"expression\":\"logical_not(A)\",\"format\":\"gdal-calc\"}"^^rdf:JSON ;
                mlm:result [ mlm:data_type "uint8" ;
                        mlm:dim_order ( "batch" "class" ) ;
                        mlm:shape ( -1 1 ) ] ;
                mlm:tasks ( mlm:semantic-segmentation ) ] ) ;
    mlm:pretrained_source "EuroSat Sentinel-2"^^xsd:string ;
    mlm:tasks ( mlm:classification ) ;
    mlm:total_parameters "11700000"^^xsd:nonNegativeInteger .

<https://huggingface.co/torchgeo/resnet50_sentinel2_rgb_moco/blob/main/resnet50_sentinel2_rgb_moco.pth> dcterms:description "A Resnet-50 classification model trained on Sentinel-2 RGB imagery with torchgeo." ;
    dcterms:format "application/octet-stream; application=pytorch" ;
    dcterms:title "Pytorch weights checkpoint" ;
    stac:hasAssetroles "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string ;
    ns3:bands [ ns1:bits_per_sample 15 ;
            ns1:common_name "green" ;
            ns1:data_type "uint16" ;
            ns1:name "B03" ;
            ns1:nodata 0 ;
            ns1:offset 0 ;
            ns1:scale 1e-04 ;
            ns1:spatial_resolution 10 ;
            ns1:unit "m" ],
        [ ns1:bits_per_sample 15 ;
            ns1:common_name "red" ;
            ns1:data_type "uint16" ;
            ns1:name "B04" ;
            ns1:nodata 0 ;
            ns1:offset 0 ;
            ns1:scale 1e-04 ;
            ns1:spatial_resolution 10 ;
            ns1:unit "m" ],
        [ ns1:bits_per_sample 15 ;
            ns1:common_name "blue" ;
            ns1:data_type "uint16" ;
            ns1:name "B02" ;
            ns1:nodata 0 ;
            ns1:offset 0 ;
            ns1:scale 1e-04 ;
            ns1:spatial_resolution 10 ;
            ns1:unit "m" ],
        [ ns1:bits_per_sample 15 ;
            ns1:common_name "nir" ;
            ns1:data_type "uint16" ;
            ns1:name "B08" ;
            ns1:nodata 0 ;
            ns1:offset 0 ;
            ns1:scale 1e-04 ;
            ns1:spatial_resolution 10 ;
            ns1:unit "m" ] .


```


### STAC item auto-generated using unet_mlm() in https://raw.githubusercontent.com/stac-extensions/mlm/refs/heads/main/stac_model/examples.py
#### geojson
```geojson
{
  "$comment": "STAC item auto-generated using unet_mlm() in https://raw.githubusercontent.com/stac-extensions/mlm/refs/heads/main/stac_model/examples.py",
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json"
  ],
  "id": "pytorch_geo_unet",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.88,
          37.13
        ],
        [
          -7.88,
          58.21
        ],
        [
          27.91,
          58.21
        ],
        [
          27.91,
          37.13
        ],
        [
          -7.88,
          37.13
        ]
      ]
    ]
  },
  "bbox": [
    -7.88,
    37.13,
    27.91,
    58.21
  ],
  "properties": {
    "description": "STAC item generated using unet_mlm() in stac_model/examples.py example. Specified in https://github.com/fieldsoftheworld/ftw-baselines First 4 S2 bands are for image t1 and last 4 bands are for image t2",
    "start_datetime": "2015-06-23T00:00:00Z",
    "end_datetime": "2024-08-27T23:59:59Z",
    "mlm:framework": "segmentation_models_pytorch.decoders.unet.model",
    "mlm:accelerator_constrained": false,
    "mlm:name": "U-Net_efficientnet-b3",
    "mlm:architecture": "segmentation_models_pytorch.decoders.unet.model.Unet",
    "mlm:tasks": [
      "semantic-segmentation"
    ],
    "mlm:input": [
      {
        "bands": [
          "B4",
          "B3",
          "B2",
          "B8",
          "B4",
          "B3",
          "B2",
          "B8"
        ],
        "variables": [],
        "name": "model_input",
        "input": {
          "shape": [
            -1,
            8,
            3,
            3
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 0,
            "stddev": 3000
          }
        ],
        "pre_processing_function": null
      }
    ],
    "mlm:output": [
      {
        "bands": [],
        "variables": [],
        "name": "model_output",
        "tasks": [
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            2
          ],
          "dim_order": [
            "batch",
            "classes"
          ],
          "data_type": "float32"
        },
        "classification:classes": [
          {
            "value": 0,
            "name": "class_0",
            "description": "Auto-generated class 0"
          },
          {
            "value": 1,
            "name": "class_1",
            "description": "Auto-generated class 1"
          }
        ],
        "post_processing_function": null
      }
    ],
    "mlm:total_parameters": 13160978,
    "mlm:pretrained": true,
    "datetime": null
  },
  "links": [
    {
      "rel": "cite-as",
      "href": "https://arxiv.org/abs/2409.16252",
      "type": "text/html",
      "title": "Publication for the training dataset of the model"
    },
    {
      "rel": "self",
      "href": "./item_pytorch_geo_unet.json",
      "type": "application/geo+json"
    },
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    }
  ],
  "assets": {
    "model": {
      "href": "https://huggingface.co/torchgeo/ftw/resolve/d2fdab6ea9d9cd38b491292cc9a5c8642533cef5/noncommercial/2-class/sentinel2_unet_effb3-bf010a31.pth",
      "type": "application/octet-stream; application=pytorch",
      "title": "U-Net_efficientnet-b3",
      "description": "A U-Net segmentation model with efficientnet-b3 encoder Weights are non-commercial.",
      "mlm:artifact_type": "torch.save",
      "eo:bands": [
        {
          "name": "B4"
        },
        {
          "name": "B3"
        },
        {
          "name": "B2"
        },
        {
          "name": "B8"
        },
        {
          "name": "B4"
        },
        {
          "name": "B3"
        },
        {
          "name": "B2"
        },
        {
          "name": "B8"
        }
      ],
      "roles": [
        "mlm:model",
        "mlm:weights",
        "data"
      ]
    },
    "source_code": {
      "href": "https://github.com/qubvel-org/segmentation_models.pytorch",
      "type": "text/html",
      "title": "Source code for U-Net_efficientnet-b3",
      "description": "GitHub repo of the pytorch model",
      "roles": [
        "mlm:source_code",
        "code"
      ]
    }
  },
  "collection": "ml-model-examples",
  "mlm:entrypoint": "segmentation_models_pytorch.decoders.unet.model.Unet"
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "STAC item auto-generated using unet_mlm() in https://raw.githubusercontent.com/stac-extensions/mlm/refs/heads/main/stac_model/examples.py",
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json"
  ],
  "id": "pytorch_geo_unet",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.88,
          37.13
        ],
        [
          -7.88,
          58.21
        ],
        [
          27.91,
          58.21
        ],
        [
          27.91,
          37.13
        ],
        [
          -7.88,
          37.13
        ]
      ]
    ]
  },
  "bbox": [
    -7.88,
    37.13,
    27.91,
    58.21
  ],
  "properties": {
    "description": "STAC item generated using unet_mlm() in stac_model/examples.py example. Specified in https://github.com/fieldsoftheworld/ftw-baselines First 4 S2 bands are for image t1 and last 4 bands are for image t2",
    "start_datetime": "2015-06-23T00:00:00Z",
    "end_datetime": "2024-08-27T23:59:59Z",
    "mlm:framework": "segmentation_models_pytorch.decoders.unet.model",
    "mlm:accelerator_constrained": false,
    "mlm:name": "U-Net_efficientnet-b3",
    "mlm:architecture": "segmentation_models_pytorch.decoders.unet.model.Unet",
    "mlm:tasks": [
      "semantic-segmentation"
    ],
    "mlm:input": [
      {
        "bands": [
          "B4",
          "B3",
          "B2",
          "B8",
          "B4",
          "B3",
          "B2",
          "B8"
        ],
        "variables": [],
        "name": "model_input",
        "input": {
          "shape": [
            -1,
            8,
            3,
            3
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "value_scaling": [
          {
            "type": "z-score",
            "mean": 0,
            "stddev": 3000
          }
        ],
        "pre_processing_function": null
      }
    ],
    "mlm:output": [
      {
        "bands": [],
        "variables": [],
        "name": "model_output",
        "tasks": [
          "semantic-segmentation"
        ],
        "result": {
          "shape": [
            -1,
            2
          ],
          "dim_order": [
            "batch",
            "classes"
          ],
          "data_type": "float32"
        },
        "classification:classes": [
          {
            "value": 0,
            "name": "class_0",
            "description": "Auto-generated class 0"
          },
          {
            "value": 1,
            "name": "class_1",
            "description": "Auto-generated class 1"
          }
        ],
        "post_processing_function": null
      }
    ],
    "mlm:total_parameters": 13160978,
    "mlm:pretrained": true,
    "datetime": null
  },
  "links": [
    {
      "rel": "cite-as",
      "href": "https://arxiv.org/abs/2409.16252",
      "type": "text/html",
      "title": "Publication for the training dataset of the model"
    },
    {
      "rel": "self",
      "href": "./item_pytorch_geo_unet.json",
      "type": "application/geo+json"
    },
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    }
  ],
  "assets": {
    "model": {
      "href": "https://huggingface.co/torchgeo/ftw/resolve/d2fdab6ea9d9cd38b491292cc9a5c8642533cef5/noncommercial/2-class/sentinel2_unet_effb3-bf010a31.pth",
      "type": "application/octet-stream; application=pytorch",
      "title": "U-Net_efficientnet-b3",
      "description": "A U-Net segmentation model with efficientnet-b3 encoder Weights are non-commercial.",
      "mlm:artifact_type": "torch.save",
      "eo:bands": [
        {
          "name": "B4"
        },
        {
          "name": "B3"
        },
        {
          "name": "B2"
        },
        {
          "name": "B8"
        },
        {
          "name": "B4"
        },
        {
          "name": "B3"
        },
        {
          "name": "B2"
        },
        {
          "name": "B8"
        }
      ],
      "roles": [
        "mlm:model",
        "mlm:weights",
        "data"
      ]
    },
    "source_code": {
      "href": "https://github.com/qubvel-org/segmentation_models.pytorch",
      "type": "text/html",
      "title": "Source code for U-Net_efficientnet-b3",
      "description": "GitHub repo of the pytorch model",
      "roles": [
        "mlm:source_code",
        "code"
      ]
    }
  },
  "collection": "ml-model-examples",
  "mlm:entrypoint": "segmentation_models_pytorch.decoders.unet.model.Unet"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <eo:> .
@prefix ns3: <classification:> .
@prefix ns4: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-9/pytorch_geo_unet> a geojson:Feature ;
    dcterms:description "STAC item generated using unet_mlm() in stac_model/examples.py example. Specified in https://github.com/fieldsoftheworld/ftw-baselines First 4 S2 bands are for image t1 and last 4 bands are for image t2" ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns4:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-9/item_pytorch_geo_unet.json> ],
        [ rdfs:label "Publication for the training dataset of the model" ;
            dcterms:type "text/html" ;
            ns4:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://arxiv.org/abs/2409.16252> ],
        [ dcterms:type "application/json" ;
            ns4:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-9/collection.json> ] ;
    geojson:bbox ( -7.88e+00 3.713e+01 2.791e+01 5.821e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88e+00 3.713e+01 ) ( -7.88e+00 5.821e+01 ) ( 2.791e+01 5.821e+01 ) ( 2.791e+01 3.713e+01 ) ( -7.88e+00 3.713e+01 ) ) ) ] ;
    stac:end_datetime "2024-08-27T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns1:model <https://huggingface.co/torchgeo/ftw/resolve/d2fdab6ea9d9cd38b491292cc9a5c8642533cef5/noncommercial/2-class/sentinel2_unet_effb3-bf010a31.pth> ;
            ns1:source_code <https://github.com/qubvel-org/segmentation_models.pytorch> ] ;
    stac:hasExtension "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json" ;
    stac:start_datetime "2015-06-23T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    mlm:accelerator_constrained false ;
    mlm:architecture "segmentation_models_pytorch.decoders.unet.model.Unet"^^xsd:string ;
    mlm:entrypoint "segmentation_models_pytorch.decoders.unet.model.Unet"^^xsd:string ;
    mlm:framework "segmentation_models_pytorch.decoders.unet.model"^^xsd:string ;
    mlm:input ( [ mlm:bands ( "B4" "B3" "B2" "B8" "B4" "B3" "B2" "B8" ) ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "bands" "height" "width" ) ;
                        mlm:shape ( -1 8 3 3 ) ] ;
                mlm:io_name "model_input" ;
                mlm:pre_processing_function "null"^^rdf:JSON ;
                mlm:value_scaling ( [ mlm:mean 0 ;
                            mlm:scaling_type mlm:z-score ;
                            mlm:stddev 3000 ] ) ;
                mlm:variables () ] ) ;
    mlm:name "U-Net_efficientnet-b3"^^xsd:string ;
    mlm:output ( [ ns3:classes [ ns3:description "Auto-generated class 1" ;
                        ns3:name "class_1" ;
                        ns3:value 1 ],
                    [ ns3:description "Auto-generated class 0" ;
                        ns3:name "class_0" ;
                        ns3:value 0 ] ;
                mlm:bands () ;
                mlm:io_name "model_output" ;
                mlm:post_processing_function "null"^^rdf:JSON ;
                mlm:result [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "classes" ) ;
                        mlm:shape ( -1 2 ) ] ;
                mlm:tasks ( mlm:semantic-segmentation ) ;
                mlm:variables () ] ) ;
    mlm:pretrained true ;
    mlm:tasks ( mlm:semantic-segmentation ) ;
    mlm:total_parameters "13160978"^^xsd:nonNegativeInteger .

<https://github.com/qubvel-org/segmentation_models.pytorch> dcterms:description "GitHub repo of the pytorch model" ;
    dcterms:format "text/html" ;
    dcterms:title "Source code for U-Net_efficientnet-b3" ;
    stac:hasAssetroles "code"^^xsd:string,
        "mlm:source_code"^^xsd:string .

<https://huggingface.co/torchgeo/ftw/resolve/d2fdab6ea9d9cd38b491292cc9a5c8642533cef5/noncommercial/2-class/sentinel2_unet_effb3-bf010a31.pth> ns2:bands [ ns1:name "B2" ],
        [ ns1:name "B4" ],
        [ ns1:name "B3" ],
        [ ns1:name "B8" ],
        [ ns1:name "B3" ],
        [ ns1:name "B8" ],
        [ ns1:name "B2" ],
        [ ns1:name "B4" ] ;
    dcterms:description "A U-Net segmentation model with efficientnet-b3 encoder Weights are non-commercial." ;
    dcterms:format "application/octet-stream; application=pytorch" ;
    dcterms:title "U-Net_efficientnet-b3" ;
    stac:hasAssetroles "data"^^xsd:string,
        "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string .


```


### Demonstrate the use of MLM and Raster for bands description, with Raster bands directly in the Model Asset.
#### geojson
```geojson
{
  "$comment": "Demonstrate the use of MLM and Raster for bands description, with Raster bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "value_scaling": null,
        "resize_type": null,
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "raster:bands": [
        {
          "name": "B01",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B02",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B03",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B04",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B05",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B06",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B07",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B08",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B8A",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B09",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B10",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B11",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B12",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_raster_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "$comment": "Demonstrate the use of MLM and Raster for bands description, with Raster bands directly in the Model Asset.",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v1.0.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json"
  ],
  "type": "Feature",
  "id": "resnet-18_sentinel-2_all_moco_classification",
  "collection": "ml-model-examples",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -7.882190080512502,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          58.21798141355221
        ],
        [
          27.911651652899923,
          58.21798141355221
        ],
        [
          27.911651652899923,
          37.13739173208318
        ],
        [
          -7.882190080512502,
          37.13739173208318
        ]
      ]
    ]
  },
  "bbox": [
    -7.882190080512502,
    37.13739173208318,
    27.911651652899923,
    58.21798141355221
  ],
  "properties": {
    "description": "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO",
    "datetime": null,
    "start_datetime": "1900-01-01T00:00:00Z",
    "end_datetime": "9999-12-31T23:59:59Z",
    "mlm:name": "Resnet-18 Sentinel-2 ALL MOCO",
    "mlm:tasks": [
      "classification"
    ],
    "mlm:architecture": "ResNet",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.1.2+cu121",
    "file:size": 43000000,
    "mlm:memory_size": 1,
    "mlm:total_parameters": 11700000,
    "mlm:pretrained_source": "EuroSat Sentinel-2",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:accelerator_summary": "Unknown",
    "mlm:batch_size_suggestion": 256,
    "mlm:input": [
      {
        "name": "13 Band Sentinel-2 Batch",
        "bands": [
          "B01",
          "B02",
          "B03",
          "B04",
          "B05",
          "B06",
          "B07",
          "B08",
          "B8A",
          "B09",
          "B10",
          "B11",
          "B12"
        ],
        "input": {
          "shape": [
            -1,
            13,
            64,
            64
          ],
          "dim_order": [
            "batch",
            "bands",
            "height",
            "width"
          ],
          "data_type": "float32"
        },
        "value_scaling": null,
        "resize_type": null,
        "pre_processing_function": {
          "format": "python",
          "expression": "torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn"
        }
      }
    ],
    "mlm:output": [
      {
        "name": "classification",
        "tasks": [
          "classification"
        ],
        "result": {
          "shape": [
            -1,
            10
          ],
          "dim_order": [
            "batch",
            "class"
          ],
          "data_type": "float32"
        },
        "classification_classes": [
          {
            "value": 0,
            "name": "Annual Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 1,
            "name": "Forest",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 2,
            "name": "Herbaceous Vegetation",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 3,
            "name": "Highway",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 4,
            "name": "Industrial Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 5,
            "name": "Pasture",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 6,
            "name": "Permanent Crop",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 7,
            "name": "Residential Buildings",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 8,
            "name": "River",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          },
          {
            "value": 9,
            "name": "SeaLake",
            "description": null,
            "title": null,
            "color_hint": null,
            "nodata": false
          }
        ],
        "post_processing_function": null
      }
    ]
  },
  "assets": {
    "weights": {
      "href": "https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth",
      "title": "Pytorch weights checkpoint",
      "description": "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo",
      "type": "application/octet-stream; application=pytorch",
      "roles": [
        "mlm:model",
        "mlm:weights"
      ],
      "mlm:artifact_type": "torch.save",
      "raster:bands": [
        {
          "name": "B01",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B02",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B03",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B04",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B05",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B06",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B07",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B08",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 10,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B8A",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B09",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B10",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 60,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B11",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        },
        {
          "name": "B12",
          "nodata": 0,
          "data_type": "uint16",
          "bits_per_sample": 15,
          "spatial_resolution": 20,
          "scale": 0.0001,
          "offset": 0,
          "unit": "m"
        }
      ]
    },
    "source_code": {
      "href": "https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207",
      "title": "Model implementation.",
      "description": "Source code to run the model.",
      "type": "text/x-python",
      "roles": [
        "mlm:source_code",
        "code",
        "metadata"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "./collection.json",
      "type": "application/json"
    },
    {
      "rel": "self",
      "href": "./item_raster_bands.json",
      "type": "application/geo+json"
    },
    {
      "rel": "derived_from",
      "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
      "type": "application/json",
      "ml-aoi:split": "train"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <raster:> .
@prefix ns3: <https://w3id.org/ogc/stac/assets/> .
@prefix ns4: <file:> .
@prefix ns5: <ml-aoi:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/example-10/resnet-18_sentinel-2_all_moco_classification> a geojson:Feature ;
    ns4:size 43000000 ;
    dcterms:description "Sourced from torchgeo python library, identifier is ResNet18_Weights.SENTINEL2_ALL_MOCO" ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://example.com/stac/mlm/example-10/collection.json> ],
        [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a> ;
            ns5:split "train" ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/example-10/item_raster_bands.json> ] ;
    geojson:bbox ( -7.88219e+00 3.713739e+01 2.791165e+01 5.821798e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -7.88219e+00 3.713739e+01 ) ( -7.88219e+00 5.821798e+01 ) ( 2.791165e+01 5.821798e+01 ) ( 2.791165e+01 3.713739e+01 ) ( -7.88219e+00 3.713739e+01 ) ) ) ] ;
    stac:end_datetime "9999-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns3:source_code <https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> ;
            ns3:weights <https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> ] ;
    stac:hasExtension "https://stac-extensions.github.io/file/v1.0.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
        "https://stac-extensions.github.io/raster/v1.1.0/schema.json" ;
    stac:start_datetime "1900-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    mlm:accelerator mlm:cuda ;
    mlm:accelerator_constrained false ;
    mlm:accelerator_summary "Unknown"^^xsd:string ;
    mlm:architecture "ResNet"^^xsd:string ;
    mlm:batch_size_suggestion "256"^^xsd:nonNegativeInteger ;
    mlm:framework "pytorch"^^xsd:string ;
    mlm:framework_version "2.1.2+cu121"^^xsd:string ;
    mlm:input ( [ mlm:bands ( "B01" "B02" "B03" "B04" "B05" "B06" "B07" "B08" "B8A" "B09" "B10" "B11" "B12" ) ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "bands" "height" "width" ) ;
                        mlm:shape ( -1 13 64 64 ) ] ;
                mlm:io_name "13 Band Sentinel-2 Batch" ;
                mlm:pre_processing_function "{\"expression\":\"torchgeo.datamodules.eurosat.EuroSATDataModule.collate_fn\",\"format\":\"python\"}"^^rdf:JSON ;
                mlm:value_scaling () ] ) ;
    mlm:memory_size "1"^^xsd:nonNegativeInteger ;
    mlm:name "Resnet-18 Sentinel-2 ALL MOCO"^^xsd:string ;
    mlm:output ( [ mlm:classification_classes [ mlm:io_name "Forest" ;
                        mlm:nodata false ;
                        mlm:value 1 ],
                    [ mlm:io_name "River" ;
                        mlm:nodata false ;
                        mlm:value 8 ],
                    [ mlm:io_name "Herbaceous Vegetation" ;
                        mlm:nodata false ;
                        mlm:value 2 ],
                    [ mlm:io_name "Pasture" ;
                        mlm:nodata false ;
                        mlm:value 5 ],
                    [ mlm:io_name "Permanent Crop" ;
                        mlm:nodata false ;
                        mlm:value 6 ],
                    [ mlm:io_name "Residential Buildings" ;
                        mlm:nodata false ;
                        mlm:value 7 ],
                    [ mlm:io_name "Highway" ;
                        mlm:nodata false ;
                        mlm:value 3 ],
                    [ mlm:io_name "Industrial Buildings" ;
                        mlm:nodata false ;
                        mlm:value 4 ],
                    [ mlm:io_name "Annual Crop" ;
                        mlm:nodata false ;
                        mlm:value 0 ],
                    [ mlm:io_name "SeaLake" ;
                        mlm:nodata false ;
                        mlm:value 9 ] ;
                mlm:io_name "classification" ;
                mlm:post_processing_function "null"^^rdf:JSON ;
                mlm:result [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "class" ) ;
                        mlm:shape ( -1 10 ) ] ;
                mlm:tasks ( mlm:classification ) ] ) ;
    mlm:pretrained_source "EuroSat Sentinel-2"^^xsd:string ;
    mlm:tasks ( mlm:classification ) ;
    mlm:total_parameters "11700000"^^xsd:nonNegativeInteger .

<https://github.com/microsoft/torchgeo/blob/61efd2e2c4df7ebe3bd03002ebbaeaa3cfe9885a/torchgeo/models/resnet.py#L207> dcterms:description "Source code to run the model." ;
    dcterms:format "text/x-python" ;
    dcterms:title "Model implementation." ;
    stac:hasAssetroles "code"^^xsd:string,
        "metadata"^^xsd:string,
        "mlm:source_code"^^xsd:string .

<https://huggingface.co/torchgeo/resnet18_sentinel2_all_moco/resolve/main/resnet18_sentinel2_all_moco-59bfdff9.pth> dcterms:description "A Resnet-18 classification model trained on normalized Sentinel-2 imagery with Eurosat landcover labels with torchgeo" ;
    dcterms:format "application/octet-stream; application=pytorch" ;
    dcterms:title "Pytorch weights checkpoint" ;
    stac:hasAssetroles "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string ;
    mlm:artifact_type "torch.save"^^xsd:string ;
    ns2:bands [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B8A" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 20 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B02" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 10 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B01" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 60 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B11" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 20 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B07" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 20 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B03" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 10 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B04" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 10 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B05" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 20 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B10" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 60 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B09" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 60 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B12" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 20 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B06" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 20 ;
            ns3:unit "m" ],
        [ ns3:bits_per_sample 15 ;
            ns3:data_type "uint16" ;
            ns3:name "B08" ;
            ns3:nodata 0 ;
            ns3:offset 0 ;
            ns3:scale 1e-04 ;
            ns3:spatial_resolution 10 ;
            ns3:unit "m" ] .


```


### Resoterre RDPS to HRDPS U-Net MLM item with interconnected STAC extensions.
#### geojson
```geojson
{
  "type": "Feature",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/version/v1.2.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
    "https://stac-extensions.github.io/application/v0.1.0/schema.json",
    "https://stac-extensions.github.io/vcs/v0.1.0/schema.json"
  ],
  "id": "unet_rdps_to_hrdps",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -86.45,
          37.52
        ],
        [
          -86.45,
          53.25
        ],
        [
          -64.16,
          53.25
        ],
        [
          -64.16,
          37.52
        ],
        [
          -86.45,
          37.52
        ]
      ]
    ]
  },
  "bbox": [
    -86.45,
    37.52,
    -64.16,
    53.25
  ],
  "properties": {
    "description": "U-Net trained to downscale RDPS meteorological data to HRDPS resolution.",
    "start_datetime": "2017-05-22T07:00:00Z",
    "end_datetime": "2100-12-31T23:59:59Z",
    "license": "Apache-2.0",
    "providers": [
      {
        "name": "Ouranos",
        "description": "Producer and licensor of the model.",
        "roles": [
          "producer",
          "licensor"
        ],
        "url": "https://www.ouranos.ca/"
      },
      {
        "name": "CRIM",
        "description": "Deployment host and inference-container processor.",
        "roles": [
          "host",
          "processor"
        ],
        "url": "https://www.crim.ca/"
      }
    ],
    "version": "0.1.3.dev9",
    "experimental": true,
    "sci:citation": "Gauvin St-Denis, B., and Smith, T. J. resoterre (version 0.1.3.dev9). Ouranos.",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.14.0+cu130",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:name": "UNet RDPS HRDPS Downscaling",
    "mlm:architecture": "U-Net",
    "mlm:tasks": [
      "downscaling",
      "super-resolution"
    ],
    "mlm:input": [
      {
        "bands": [],
        "variables": [
          "TT_model_levels",
          "PR",
          "UU_model_levels",
          "VV_model_levels",
          "PC",
          "PN",
          "TT850",
          "GZ500",
          "GZ850",
          "HU850",
          "HU700",
          "TD",
          "UU850",
          "VV850"
        ],
        "name": "rdps_inputs",
        "input": {
          "shape": [
            -1,
            14,
            128,
            128
          ],
          "dim_order": [
            "batch",
            "variables",
            "rlat",
            "rlon"
          ],
          "data_type": "float32"
        },
        "pre_processing_function": null,
        "description": "Fourteen normalized RDPS meteorological channels on the 128x128 coarse rotated grid. Each flexible batch element represents one independently selected valid time. The time identifies samples in the surrounding dataset but is not a tensor axis because the U-Net does not jointly process a temporal sequence."
      },
      {
        "bands": [],
        "variables": [
          "orog",
          "sftlf"
        ],
        "name": "hrdps_geophysical_inputs",
        "input": {
          "shape": [
            -1,
            2,
            512,
            512
          ],
          "dim_order": [
            "batch",
            "variables",
            "rlat",
            "rlon"
          ],
          "data_type": "float32"
        },
        "pre_processing_function": null,
        "description": "Static orography and land-fraction channels on the 512x512 target grid. The geographic lat/lon are auxiliary coordinates over rlat/rlon."
      }
    ],
    "mlm:output": [
      {
        "bands": [],
        "variables": [
          "HRDPS_P_TT_10000",
          "HRDPS_P_PR_SFC",
          "HRDPS_P_UUC_10000",
          "HRDPS_P_VVC_10000"
        ],
        "name": "hrdps_outputs",
        "tasks": [
          "downscaling",
          "super-resolution"
        ],
        "result": {
          "shape": [
            -1,
            4,
            512,
            512
          ],
          "dim_order": [
            "batch",
            "variables",
            "rlat",
            "rlon"
          ],
          "data_type": "float32"
        },
        "post_processing_function": null,
        "description": "Four continuous HRDPS fields reconstructed for the same valid time on the 512x512 target rotated grid."
      }
    ],
    "mlm:hyperparameters": {
      "coarsen_factor": 4,
      "kernel_size": 3,
      "initial_nb_of_hidden_channels": 144,
      "depth": 2,
      "reduction_ratio": 4,
      "learning_rate": 0.002,
      "weight_decay": 1e-05,
      "mse_loss_weight": 0.5,
      "mae_loss_weight": 0.0,
      "mass_loss_weight": 0.0,
      "ssim_loss_weight": 0.5,
      "num_workers": 8,
      "num_threads": 16,
      "device": "cpu",
      "training_batch_size": 64,
      "global_start_datetime": "2017-05-22 07:00:00",
      "global_end_datetime": "2024-09-01 12:00:00",
      "validation_period_start": "2023-01-10 00:00:00",
      "test_period_start": "2023-06-01 00:00:00",
      "nb_of_epochs": 18,
      "optimizer": "Adam",
      "ssim_kernel_size": 11,
      "ssim_sigma": 1.5,
      "ssim_k1": 0.01,
      "ssim_k2": 0.03
    },
    "mlm:total_parameters": 9871888,
    "mlm:pretrained": false,
    "cube:dimensions": {
      "time": {
        "type": "temporal",
        "description": "Valid time associated with each independently processed model sample.",
        "extent": [
          "2017-05-22T07:00:00Z",
          "2100-12-31T23:59:59Z"
        ],
        "unit": "s"
      },
      "rlat": {
        "type": "spatial",
        "description": "Row coordinate of the 512x512 HRDPS target array in its rotated-pole grid. The geographic positions are provided by the two-dimensional lat/lon auxiliary coordinates.",
        "axis": "y",
        "extent": [
          0,
          511
        ],
        "unit": "index"
      },
      "rlon": {
        "type": "spatial",
        "description": "Column coordinate of the 512x512 HRDPS target array in its rotated-pole grid. The geographic positions are provided by the two-dimensional lat/lon auxiliary coordinates.",
        "axis": "x",
        "extent": [
          0,
          511
        ],
        "unit": "index"
      }
    },
    "cube:variables": {
      "TT_model_levels": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS air temperature on model levels, normalized before inference."
      },
      "PR": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS precipitation rate at the surface, normalized before inference."
      },
      "UU_model_levels": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS eastward wind component on model levels, normalized before inference."
      },
      "VV_model_levels": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS northward wind component on model levels, normalized before inference."
      },
      "PC": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS convective precipitation at the surface, normalized before inference."
      },
      "PN": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS pressure at the surface, normalized before inference."
      },
      "TT850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS air temperature at 850 hPa, normalized before inference."
      },
      "GZ500": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS geopotential height at 500 hPa, normalized before inference."
      },
      "GZ850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS geopotential height at 850 hPa, normalized before inference."
      },
      "HU850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS relative humidity at 850 hPa, normalized before inference."
      },
      "HU700": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS relative humidity at 700 hPa, normalized before inference."
      },
      "TD": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS dew-point temperature, normalized before inference."
      },
      "UU850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS eastward wind component at 850 hPa, normalized before inference."
      },
      "VV850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS northward wind component at 850 hPa, normalized before inference."
      },
      "HRDPS_P_TT_10000": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "HRDPS air temperature at 10 m, reconstructed on the target grid."
      },
      "HRDPS_P_PR_SFC": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "HRDPS precipitation rate at the surface, reconstructed on the target grid."
      },
      "HRDPS_P_UUC_10000": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "HRDPS eastward wind component at 10 m, reconstructed on the target grid."
      },
      "HRDPS_P_VVC_10000": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "HRDPS northward wind component at 10 m, reconstructed on the target grid."
      },
      "orog": {
        "dimensions": [
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "Static HRDPS orography on the target rotated grid, aligned to the output patch."
      },
      "sftlf": {
        "dimensions": [
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "Static HRDPS land-fraction field on the target rotated grid, aligned to the output patch."
      },
      "lat": {
        "dimensions": [
          "rlat",
          "rlon"
        ],
        "type": "auxiliary",
        "data_type": "float32",
        "unit": "degree_north",
        "description": "Geographic latitude auxiliary coordinate for the rotated grid."
      },
      "lon": {
        "dimensions": [
          "rlat",
          "rlon"
        ],
        "type": "auxiliary",
        "data_type": "float32",
        "unit": "degree_east",
        "description": "Geographic longitude auxiliary coordinate for the rotated grid."
      }
    },
    "vcs:type": "git",
    "vcs:branch": "main",
    "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8",
    "datetime": null
  },
  "links": [
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/RDPS_CRIM",
      "title": "RDPS train samples",
      "ml-aoi:split": "train",
      "ml-aoi:role": "feature",
      "description": "RDPS train-split input samples used as machine-learning features."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM",
      "title": "HRDPS train samples",
      "ml-aoi:split": "train",
      "ml-aoi:role": "label",
      "description": "HRDPS train-split target samples used as labels and predicted downscaling results."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/RDPS_CRIM",
      "title": "RDPS validate samples",
      "ml-aoi:split": "validate",
      "ml-aoi:role": "feature",
      "description": "RDPS validate-split input samples used as machine-learning features."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM",
      "title": "HRDPS validate samples",
      "ml-aoi:split": "validate",
      "ml-aoi:role": "label",
      "description": "HRDPS validate-split target samples used as labels and predicted downscaling results."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/RDPS_CRIM",
      "title": "RDPS test samples",
      "ml-aoi:split": "test",
      "ml-aoi:role": "feature",
      "description": "RDPS test-split input samples used as machine-learning features."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM",
      "title": "HRDPS test samples",
      "ml-aoi:split": "test",
      "ml-aoi:role": "label",
      "description": "HRDPS test-split target samples used as labels and predicted downscaling results."
    },
    {
      "rel": "cite-as",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/CITATION.cff",
      "type": "text/yaml",
      "title": "resoterre citation metadata"
    },
    {
      "rel": "application",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_unet_workflow.cwl",
      "type": "application/cwl+yaml",
      "title": "RDPS-to-HRDPS downscaling CWL workflow",
      "file:size": 2624,
      "file:checksum": "122054639a4072d5fb7e2a0039975ca8446e9fc3e95e91c91f9f4b37bebd3e798937",
      "description": "CWL Workflow chaining the file listing, download and U-Net inference steps.",
      "application:languages": [
        "Common Workflow Language"
      ],
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "application",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_generate_file_list.cwl",
      "type": "application/cwl+yaml",
      "title": "RDPS file listing CWL tool",
      "file:size": 2284,
      "file:checksum": "1220b41206d6ae38ceedfb499c179851d670555a73bfe7a70819ba47b511c1f78f01",
      "description": "CWL CommandLineTool listing the RDPS files required for a requested datetime range.",
      "application:languages": [
        "Common Workflow Language"
      ],
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "application",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_download_files.cwl",
      "type": "application/cwl+yaml",
      "title": "RDPS download CWL tool",
      "file:size": 1611,
      "file:checksum": "1220cfe6377d576e12763fa6e0f89f1fbc61a587475fbacf29c0d4921cdba758db19",
      "description": "CWL CommandLineTool downloading the listed RDPS files into a local directory.",
      "application:languages": [
        "Common Workflow Language"
      ],
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "application",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_unet.cwl",
      "type": "application/cwl+yaml",
      "title": "U-Net inference CWL tool",
      "file:size": 2359,
      "file:checksum": "122081999f65ffb1cf3256b1a72a3aed25134b4ba446acea1b781b5a783f6ac6b09f",
      "description": "CWL CommandLineTool running the U-Net downscaling inference on the downloaded RDPS data.",
      "application:languages": [
        "Common Workflow Language"
      ],
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "vcs",
      "href": "https://github.com/Ouranosinc/resoterre.git",
      "title": "resoterre source repository",
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "self",
      "href": "unet_rdps_to_hrdps.json",
      "type": "application/geo+json"
    }
  ],
  "assets": {
    "model": {
      "href": "https://huggingface.co/bstdenis/unet-rdps-to-hrdps-downscaling/blob/main/unet_epoch_mebojo_018.safetensors",
      "type": "application/octet-stream; framework=pytorch",
      "title": "Epoch 18 U-Net SafeTensors weights",
      "description": "SafeTensors weights loaded by the resoterre U-Net implementation.",
      "mlm:artifact_type": "safetensors.torch.save_file",
      "application:entrypoint": "resoterre.ml.neural_networks_unet:UNet",
      "file:checksum": "122090e4bbd8583de97cea555072b98479920d1c2c6949daa3254f3c771571cebf6b",
      "file:size": 39526256,
      "roles": [
        "mlm:model",
        "mlm:weights",
        "model",
        "weights",
        "data"
      ]
    },
    "source_code": {
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/scripts/meta_workflows/downscaling/rdps_to_hrdps.smk",
      "type": "text/x-snakemake",
      "title": "RDPS-to-HRDPS Snakemake workflow",
      "description": "Executable Snakemake workflow that preprocesses RDPS data and runs downscaling inference.",
      "mlm:entrypoint": "snakemake -s scripts/meta_workflows/downscaling/rdps_to_hrdps.smk --config config_yaml=/app/configs/downscaling/downscaling_rdps_to_hrdps_cwl.yaml -j1 --directory=/app",
      "application:entrypoint": "scripts/meta_workflows/downscaling/rdps_to_hrdps.smk",
      "application:languages": [
        "Python"
      ],
      "file:checksum": "1220fbfe7b7f39796c9e378dc2522a82581ec9024781222327a5d75ba59dc3b32046",
      "file:size": 1700,
      "roles": [
        "mlm:source_code",
        "code"
      ]
    },
    "configuration": {
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/configs/downscaling/downscaling_rdps_to_hrdps_cwl.yaml",
      "type": "application/yaml",
      "title": "Training and inference configuration",
      "description": "Configuration consumed by the Snakemake workflow.",
      "file:checksum": "1220386fc766bf6ab79ef6a9dd6f0ac3f706669bf09a037be02b87991b159af44136",
      "file:size": 3606,
      "roles": [
        "configuration",
        "metadata"
      ]
    },
    "container": {
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/docker/Dockerfile.inference",
      "type": "text/x-dockerfile",
      "title": "Inference container definition",
      "description": "Generic Dockerfile used to build the inference container image.",
      "application:languages": [
        "Dockerfile"
      ],
      "file:checksum": "12201afe4cb941fb434e8fac2bd83a4ddf3a701993bd050a3bae82584e94b3b0824b",
      "file:size": 1626,
      "roles": [
        "container"
      ]
    },
    "runtime": {
      "href": "docker://resoterre-inference:0.1.3.dev9",
      "type": "application/vnd.oci.image.index.v1+json",
      "title": "resoterre inference container 0.1.3.dev9",
      "description": "Versioned OCI container that packages PyTorch, Snakemake, the workflow, and model dependencies.",
      "roles": [
        "mlm:inference-runtime",
        "runtime"
      ]
    },
    "citation": {
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/CITATION.cff",
      "type": "text/yaml",
      "title": "Citation metadata",
      "description": "Citation File Format metadata for resoterre.",
      "file:checksum": "1220ffe80cd84de27fed65be4cd5289bcf00defe4553f2fc7086465228bec4d28476",
      "file:size": 945,
      "roles": [
        "metadata"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld",
  "type": "Feature",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/version/v1.2.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
    "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
    "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
    "https://stac-extensions.github.io/application/v0.1.0/schema.json",
    "https://stac-extensions.github.io/vcs/v0.1.0/schema.json"
  ],
  "id": "unet_rdps_to_hrdps",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -86.45,
          37.52
        ],
        [
          -86.45,
          53.25
        ],
        [
          -64.16,
          53.25
        ],
        [
          -64.16,
          37.52
        ],
        [
          -86.45,
          37.52
        ]
      ]
    ]
  },
  "bbox": [
    -86.45,
    37.52,
    -64.16,
    53.25
  ],
  "properties": {
    "description": "U-Net trained to downscale RDPS meteorological data to HRDPS resolution.",
    "start_datetime": "2017-05-22T07:00:00Z",
    "end_datetime": "2100-12-31T23:59:59Z",
    "license": "Apache-2.0",
    "providers": [
      {
        "name": "Ouranos",
        "description": "Producer and licensor of the model.",
        "roles": [
          "producer",
          "licensor"
        ],
        "url": "https://www.ouranos.ca/"
      },
      {
        "name": "CRIM",
        "description": "Deployment host and inference-container processor.",
        "roles": [
          "host",
          "processor"
        ],
        "url": "https://www.crim.ca/"
      }
    ],
    "version": "0.1.3.dev9",
    "experimental": true,
    "sci:citation": "Gauvin St-Denis, B., and Smith, T. J. resoterre (version 0.1.3.dev9). Ouranos.",
    "mlm:framework": "pytorch",
    "mlm:framework_version": "2.14.0+cu130",
    "mlm:accelerator": "cuda",
    "mlm:accelerator_constrained": false,
    "mlm:name": "UNet RDPS HRDPS Downscaling",
    "mlm:architecture": "U-Net",
    "mlm:tasks": [
      "downscaling",
      "super-resolution"
    ],
    "mlm:input": [
      {
        "bands": [],
        "variables": [
          "TT_model_levels",
          "PR",
          "UU_model_levels",
          "VV_model_levels",
          "PC",
          "PN",
          "TT850",
          "GZ500",
          "GZ850",
          "HU850",
          "HU700",
          "TD",
          "UU850",
          "VV850"
        ],
        "name": "rdps_inputs",
        "input": {
          "shape": [
            -1,
            14,
            128,
            128
          ],
          "dim_order": [
            "batch",
            "variables",
            "rlat",
            "rlon"
          ],
          "data_type": "float32"
        },
        "pre_processing_function": null,
        "description": "Fourteen normalized RDPS meteorological channels on the 128x128 coarse rotated grid. Each flexible batch element represents one independently selected valid time. The time identifies samples in the surrounding dataset but is not a tensor axis because the U-Net does not jointly process a temporal sequence."
      },
      {
        "bands": [],
        "variables": [
          "orog",
          "sftlf"
        ],
        "name": "hrdps_geophysical_inputs",
        "input": {
          "shape": [
            -1,
            2,
            512,
            512
          ],
          "dim_order": [
            "batch",
            "variables",
            "rlat",
            "rlon"
          ],
          "data_type": "float32"
        },
        "pre_processing_function": null,
        "description": "Static orography and land-fraction channels on the 512x512 target grid. The geographic lat/lon are auxiliary coordinates over rlat/rlon."
      }
    ],
    "mlm:output": [
      {
        "bands": [],
        "variables": [
          "HRDPS_P_TT_10000",
          "HRDPS_P_PR_SFC",
          "HRDPS_P_UUC_10000",
          "HRDPS_P_VVC_10000"
        ],
        "name": "hrdps_outputs",
        "tasks": [
          "downscaling",
          "super-resolution"
        ],
        "result": {
          "shape": [
            -1,
            4,
            512,
            512
          ],
          "dim_order": [
            "batch",
            "variables",
            "rlat",
            "rlon"
          ],
          "data_type": "float32"
        },
        "post_processing_function": null,
        "description": "Four continuous HRDPS fields reconstructed for the same valid time on the 512x512 target rotated grid."
      }
    ],
    "mlm:hyperparameters": {
      "coarsen_factor": 4,
      "kernel_size": 3,
      "initial_nb_of_hidden_channels": 144,
      "depth": 2,
      "reduction_ratio": 4,
      "learning_rate": 0.002,
      "weight_decay": "1e-05",
      "mse_loss_weight": 0.5,
      "mae_loss_weight": 0.0,
      "mass_loss_weight": 0.0,
      "ssim_loss_weight": 0.5,
      "num_workers": 8,
      "num_threads": 16,
      "device": "cpu",
      "training_batch_size": 64,
      "global_start_datetime": "2017-05-22 07:00:00",
      "global_end_datetime": "2024-09-01 12:00:00",
      "validation_period_start": "2023-01-10 00:00:00",
      "test_period_start": "2023-06-01 00:00:00",
      "nb_of_epochs": 18,
      "optimizer": "Adam",
      "ssim_kernel_size": 11,
      "ssim_sigma": 1.5,
      "ssim_k1": 0.01,
      "ssim_k2": 0.03
    },
    "mlm:total_parameters": 9871888,
    "mlm:pretrained": false,
    "cube:dimensions": {
      "time": {
        "type": "temporal",
        "description": "Valid time associated with each independently processed model sample.",
        "extent": [
          "2017-05-22T07:00:00Z",
          "2100-12-31T23:59:59Z"
        ],
        "unit": "s"
      },
      "rlat": {
        "type": "spatial",
        "description": "Row coordinate of the 512x512 HRDPS target array in its rotated-pole grid. The geographic positions are provided by the two-dimensional lat/lon auxiliary coordinates.",
        "axis": "y",
        "extent": [
          0,
          511
        ],
        "unit": "index"
      },
      "rlon": {
        "type": "spatial",
        "description": "Column coordinate of the 512x512 HRDPS target array in its rotated-pole grid. The geographic positions are provided by the two-dimensional lat/lon auxiliary coordinates.",
        "axis": "x",
        "extent": [
          0,
          511
        ],
        "unit": "index"
      }
    },
    "cube:variables": {
      "TT_model_levels": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS air temperature on model levels, normalized before inference."
      },
      "PR": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS precipitation rate at the surface, normalized before inference."
      },
      "UU_model_levels": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS eastward wind component on model levels, normalized before inference."
      },
      "VV_model_levels": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS northward wind component on model levels, normalized before inference."
      },
      "PC": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS convective precipitation at the surface, normalized before inference."
      },
      "PN": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS pressure at the surface, normalized before inference."
      },
      "TT850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS air temperature at 850 hPa, normalized before inference."
      },
      "GZ500": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS geopotential height at 500 hPa, normalized before inference."
      },
      "GZ850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS geopotential height at 850 hPa, normalized before inference."
      },
      "HU850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS relative humidity at 850 hPa, normalized before inference."
      },
      "HU700": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS relative humidity at 700 hPa, normalized before inference."
      },
      "TD": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS dew-point temperature, normalized before inference."
      },
      "UU850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS eastward wind component at 850 hPa, normalized before inference."
      },
      "VV850": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "RDPS northward wind component at 850 hPa, normalized before inference."
      },
      "HRDPS_P_TT_10000": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "HRDPS air temperature at 10 m, reconstructed on the target grid."
      },
      "HRDPS_P_PR_SFC": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "HRDPS precipitation rate at the surface, reconstructed on the target grid."
      },
      "HRDPS_P_UUC_10000": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "HRDPS eastward wind component at 10 m, reconstructed on the target grid."
      },
      "HRDPS_P_VVC_10000": {
        "dimensions": [
          "time",
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "HRDPS northward wind component at 10 m, reconstructed on the target grid."
      },
      "orog": {
        "dimensions": [
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "Static HRDPS orography on the target rotated grid, aligned to the output patch."
      },
      "sftlf": {
        "dimensions": [
          "rlat",
          "rlon"
        ],
        "type": "data",
        "data_type": "float32",
        "description": "Static HRDPS land-fraction field on the target rotated grid, aligned to the output patch."
      },
      "lat": {
        "dimensions": [
          "rlat",
          "rlon"
        ],
        "type": "auxiliary",
        "data_type": "float32",
        "unit": "degree_north",
        "description": "Geographic latitude auxiliary coordinate for the rotated grid."
      },
      "lon": {
        "dimensions": [
          "rlat",
          "rlon"
        ],
        "type": "auxiliary",
        "data_type": "float32",
        "unit": "degree_east",
        "description": "Geographic longitude auxiliary coordinate for the rotated grid."
      }
    },
    "vcs:type": "git",
    "vcs:branch": "main",
    "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8",
    "datetime": null
  },
  "links": [
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/RDPS_CRIM",
      "title": "RDPS train samples",
      "ml-aoi:split": "train",
      "ml-aoi:role": "feature",
      "description": "RDPS train-split input samples used as machine-learning features."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM",
      "title": "HRDPS train samples",
      "ml-aoi:split": "train",
      "ml-aoi:role": "label",
      "description": "HRDPS train-split target samples used as labels and predicted downscaling results."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/RDPS_CRIM",
      "title": "RDPS validate samples",
      "ml-aoi:split": "validate",
      "ml-aoi:role": "feature",
      "description": "RDPS validate-split input samples used as machine-learning features."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM",
      "title": "HRDPS validate samples",
      "ml-aoi:split": "validate",
      "ml-aoi:role": "label",
      "description": "HRDPS validate-split target samples used as labels and predicted downscaling results."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/RDPS_CRIM",
      "title": "RDPS test samples",
      "ml-aoi:split": "test",
      "ml-aoi:role": "feature",
      "description": "RDPS test-split input samples used as machine-learning features."
    },
    {
      "rel": "derived_from",
      "href": "https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM",
      "title": "HRDPS test samples",
      "ml-aoi:split": "test",
      "ml-aoi:role": "label",
      "description": "HRDPS test-split target samples used as labels and predicted downscaling results."
    },
    {
      "rel": "cite-as",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/CITATION.cff",
      "type": "text/yaml",
      "title": "resoterre citation metadata"
    },
    {
      "rel": "application",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_unet_workflow.cwl",
      "type": "application/cwl+yaml",
      "title": "RDPS-to-HRDPS downscaling CWL workflow",
      "file:size": 2624,
      "file:checksum": "122054639a4072d5fb7e2a0039975ca8446e9fc3e95e91c91f9f4b37bebd3e798937",
      "description": "CWL Workflow chaining the file listing, download and U-Net inference steps.",
      "application:languages": [
        "Common Workflow Language"
      ],
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "application",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_generate_file_list.cwl",
      "type": "application/cwl+yaml",
      "title": "RDPS file listing CWL tool",
      "file:size": 2284,
      "file:checksum": "1220b41206d6ae38ceedfb499c179851d670555a73bfe7a70819ba47b511c1f78f01",
      "description": "CWL CommandLineTool listing the RDPS files required for a requested datetime range.",
      "application:languages": [
        "Common Workflow Language"
      ],
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "application",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_download_files.cwl",
      "type": "application/cwl+yaml",
      "title": "RDPS download CWL tool",
      "file:size": 1611,
      "file:checksum": "1220cfe6377d576e12763fa6e0f89f1fbc61a587475fbacf29c0d4921cdba758db19",
      "description": "CWL CommandLineTool downloading the listed RDPS files into a local directory.",
      "application:languages": [
        "Common Workflow Language"
      ],
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "application",
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_unet.cwl",
      "type": "application/cwl+yaml",
      "title": "U-Net inference CWL tool",
      "file:size": 2359,
      "file:checksum": "122081999f65ffb1cf3256b1a72a3aed25134b4ba446acea1b781b5a783f6ac6b09f",
      "description": "CWL CommandLineTool running the U-Net downscaling inference on the downloaded RDPS data.",
      "application:languages": [
        "Common Workflow Language"
      ],
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "vcs",
      "href": "https://github.com/Ouranosinc/resoterre.git",
      "title": "resoterre source repository",
      "vcs:type": "git",
      "vcs:branch": "main",
      "vcs:revision": "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8"
    },
    {
      "rel": "self",
      "href": "unet_rdps_to_hrdps.json",
      "type": "application/geo+json"
    }
  ],
  "assets": {
    "model": {
      "href": "https://huggingface.co/bstdenis/unet-rdps-to-hrdps-downscaling/blob/main/unet_epoch_mebojo_018.safetensors",
      "type": "application/octet-stream; framework=pytorch",
      "title": "Epoch 18 U-Net SafeTensors weights",
      "description": "SafeTensors weights loaded by the resoterre U-Net implementation.",
      "mlm:artifact_type": "safetensors.torch.save_file",
      "application:entrypoint": "resoterre.ml.neural_networks_unet:UNet",
      "file:checksum": "122090e4bbd8583de97cea555072b98479920d1c2c6949daa3254f3c771571cebf6b",
      "file:size": 39526256,
      "roles": [
        "mlm:model",
        "mlm:weights",
        "model",
        "weights",
        "data"
      ]
    },
    "source_code": {
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/scripts/meta_workflows/downscaling/rdps_to_hrdps.smk",
      "type": "text/x-snakemake",
      "title": "RDPS-to-HRDPS Snakemake workflow",
      "description": "Executable Snakemake workflow that preprocesses RDPS data and runs downscaling inference.",
      "mlm:entrypoint": "snakemake -s scripts/meta_workflows/downscaling/rdps_to_hrdps.smk --config config_yaml=/app/configs/downscaling/downscaling_rdps_to_hrdps_cwl.yaml -j1 --directory=/app",
      "application:entrypoint": "scripts/meta_workflows/downscaling/rdps_to_hrdps.smk",
      "application:languages": [
        "Python"
      ],
      "file:checksum": "1220fbfe7b7f39796c9e378dc2522a82581ec9024781222327a5d75ba59dc3b32046",
      "file:size": 1700,
      "roles": [
        "mlm:source_code",
        "code"
      ]
    },
    "configuration": {
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/configs/downscaling/downscaling_rdps_to_hrdps_cwl.yaml",
      "type": "application/yaml",
      "title": "Training and inference configuration",
      "description": "Configuration consumed by the Snakemake workflow.",
      "file:checksum": "1220386fc766bf6ab79ef6a9dd6f0ac3f706669bf09a037be02b87991b159af44136",
      "file:size": 3606,
      "roles": [
        "configuration",
        "metadata"
      ]
    },
    "container": {
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/docker/Dockerfile.inference",
      "type": "text/x-dockerfile",
      "title": "Inference container definition",
      "description": "Generic Dockerfile used to build the inference container image.",
      "application:languages": [
        "Dockerfile"
      ],
      "file:checksum": "12201afe4cb941fb434e8fac2bd83a4ddf3a701993bd050a3bae82584e94b3b0824b",
      "file:size": 1626,
      "roles": [
        "container"
      ]
    },
    "runtime": {
      "href": "docker://resoterre-inference:0.1.3.dev9",
      "type": "application/vnd.oci.image.index.v1+json",
      "title": "resoterre inference container 0.1.3.dev9",
      "description": "Versioned OCI container that packages PyTorch, Snakemake, the workflow, and model dependencies.",
      "roles": [
        "mlm:inference-runtime",
        "runtime"
      ]
    },
    "citation": {
      "href": "https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/CITATION.cff",
      "type": "text/yaml",
      "title": "Citation metadata",
      "description": "Citation File Format metadata for resoterre.",
      "file:checksum": "1220ffe80cd84de27fed65be4cd5289bcf00defe4553f2fc7086465228bec4d28476",
      "file:size": 945,
      "roles": [
        "metadata"
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix cube: <https://w3id.org/ogc/stac/datacube/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix mlm: <https://w3id.org/ogc/stac/mlm/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <vcs:> .
@prefix ns3: <file:> .
@prefix ns4: <application:> .
@prefix ns5: <https://w3id.org/ogc/stac/assets/> .
@prefix ns6: <ml-aoi:> .
@prefix ns7: <sci:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/stac/mlm/resoterre-unet/unet_rdps_to_hrdps> a geojson:Feature ;
    dcterms:description "U-Net trained to downscale RDPS meteorological data to HRDPS resolution." ;
    rdfs:seeAlso [ rdfs:label "RDPS train samples" ;
            dcterms:description "RDPS train-split input samples used as machine-learning features." ;
            ns1:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://hirondelle.crim.ca/stac/collections/RDPS_CRIM> ;
            ns6:role "feature" ;
            ns6:split "train" ],
        [ rdfs:label "RDPS test samples" ;
            dcterms:description "RDPS test-split input samples used as machine-learning features." ;
            ns1:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://hirondelle.crim.ca/stac/collections/RDPS_CRIM> ;
            ns6:role "feature" ;
            ns6:split "test" ],
        [ rdfs:label "RDPS validate samples" ;
            dcterms:description "RDPS validate-split input samples used as machine-learning features." ;
            ns1:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://hirondelle.crim.ca/stac/collections/RDPS_CRIM> ;
            ns6:role "feature" ;
            ns6:split "validate" ],
        [ rdfs:label "resoterre citation metadata" ;
            dcterms:type "text/yaml" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/CITATION.cff> ],
        [ rdfs:label "RDPS download CWL tool" ;
            ns4:languages "Common Workflow Language" ;
            ns3:checksum "1220cfe6377d576e12763fa6e0f89f1fbc61a587475fbacf29c0d4921cdba758db19" ;
            ns3:size 1611 ;
            dcterms:description "CWL CommandLineTool downloading the listed RDPS files into a local directory." ;
            dcterms:type "application/cwl+yaml" ;
            ns1:relation <http://www.iana.org/assignments/relation/application> ;
            oa:hasTarget <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_download_files.cwl> ;
            ns2:branch "main" ;
            ns2:revision "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8" ;
            ns2:type "git" ],
        [ rdfs:label "HRDPS validate samples" ;
            dcterms:description "HRDPS validate-split target samples used as labels and predicted downscaling results." ;
            ns1:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM> ;
            ns6:role "label" ;
            ns6:split "validate" ],
        [ rdfs:label "RDPS file listing CWL tool" ;
            ns4:languages "Common Workflow Language" ;
            ns3:checksum "1220b41206d6ae38ceedfb499c179851d670555a73bfe7a70819ba47b511c1f78f01" ;
            ns3:size 2284 ;
            dcterms:description "CWL CommandLineTool listing the RDPS files required for a requested datetime range." ;
            dcterms:type "application/cwl+yaml" ;
            ns1:relation <http://www.iana.org/assignments/relation/application> ;
            oa:hasTarget <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_generate_file_list.cwl> ;
            ns2:branch "main" ;
            ns2:revision "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8" ;
            ns2:type "git" ],
        [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://example.com/stac/mlm/resoterre-unet/unet_rdps_to_hrdps.json> ],
        [ rdfs:label "resoterre source repository" ;
            ns1:relation <http://www.iana.org/assignments/relation/vcs> ;
            oa:hasTarget <https://github.com/Ouranosinc/resoterre.git> ;
            ns2:branch "main" ;
            ns2:revision "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8" ;
            ns2:type "git" ],
        [ rdfs:label "U-Net inference CWL tool" ;
            ns4:languages "Common Workflow Language" ;
            ns3:checksum "122081999f65ffb1cf3256b1a72a3aed25134b4ba446acea1b781b5a783f6ac6b09f" ;
            ns3:size 2359 ;
            dcterms:description "CWL CommandLineTool running the U-Net downscaling inference on the downloaded RDPS data." ;
            dcterms:type "application/cwl+yaml" ;
            ns1:relation <http://www.iana.org/assignments/relation/application> ;
            oa:hasTarget <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_unet.cwl> ;
            ns2:branch "main" ;
            ns2:revision "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8" ;
            ns2:type "git" ],
        [ rdfs:label "HRDPS test samples" ;
            dcterms:description "HRDPS test-split target samples used as labels and predicted downscaling results." ;
            ns1:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM> ;
            ns6:role "label" ;
            ns6:split "test" ],
        [ rdfs:label "HRDPS train samples" ;
            dcterms:description "HRDPS train-split target samples used as labels and predicted downscaling results." ;
            ns1:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://hirondelle.crim.ca/stac/collections/HRDPS_CRIM> ;
            ns6:role "label" ;
            ns6:split "train" ],
        [ rdfs:label "RDPS-to-HRDPS downscaling CWL workflow" ;
            ns4:languages "Common Workflow Language" ;
            ns3:checksum "122054639a4072d5fb7e2a0039975ca8446e9fc3e95e91c91f9f4b37bebd3e798937" ;
            ns3:size 2624 ;
            dcterms:description "CWL Workflow chaining the file listing, download and U-Net inference steps." ;
            dcterms:type "application/cwl+yaml" ;
            ns1:relation <http://www.iana.org/assignments/relation/application> ;
            oa:hasTarget <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/examples/deploy/downscaling_unet_workflow.cwl> ;
            ns2:branch "main" ;
            ns2:revision "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8" ;
            ns2:type "git" ] ;
    dcat:license "Apache-2.0" ;
    geojson:bbox ( -8.645e+01 3.752e+01 -6.416e+01 5.325e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -8.645e+01 3.752e+01 ) ( -8.645e+01 5.325e+01 ) ( -6.416e+01 5.325e+01 ) ( -6.416e+01 3.752e+01 ) ( -8.645e+01 3.752e+01 ) ) ) ] ;
    stac:end_datetime "2100-12-31T23:59:59+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns5:citation <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/CITATION.cff> ;
            ns5:configuration <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/configs/downscaling/downscaling_rdps_to_hrdps_cwl.yaml> ;
            ns5:container <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/docker/Dockerfile.inference> ;
            ns5:model <https://huggingface.co/bstdenis/unet-rdps-to-hrdps-downscaling/blob/main/unet_epoch_mebojo_018.safetensors> ;
            ns5:runtime <docker://resoterre-inference:0.1.3.dev9> ;
            ns5:source_code <https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/scripts/meta_workflows/downscaling/rdps_to_hrdps.smk> ] ;
    stac:hasExtension "https://stac-extensions.github.io/application/v0.1.0/schema.json",
        "https://stac-extensions.github.io/datacube/v2.3.0/schema.json",
        "https://stac-extensions.github.io/file/v2.1.0/schema.json",
        "https://stac-extensions.github.io/ml-aoi/v0.2.0/schema.json",
        "https://stac-extensions.github.io/mlm/v1.6.0/schema.json",
        "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
        "https://stac-extensions.github.io/vcs/v0.1.0/schema.json",
        "https://stac-extensions.github.io/version/v1.2.0/schema.json" ;
    stac:hasProvider [ dcterms:description "Producer and licensor of the model." ],
        [ dcterms:description "Deployment host and inference-container processor." ] ;
    stac:start_datetime "2017-05-22T07:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.1.0" ;
    cube:dimensions [ cube:description "Valid time associated with each independently processed model sample." ;
            cube:extent ( "2017-05-22T07:00:00Z" "2100-12-31T23:59:59Z" ) ;
            cube:type "temporal" ;
            cube:unit "s" ;
            mlm:datacube_dimension_name "time" ],
        [ cube:axis "y" ;
            cube:description "Row coordinate of the 512x512 HRDPS target array in its rotated-pole grid. The geographic positions are provided by the two-dimensional lat/lon auxiliary coordinates." ;
            cube:extent ( 0 511 ) ;
            cube:type "spatial" ;
            cube:unit "index" ;
            mlm:datacube_dimension_name "rlat" ],
        [ cube:axis "x" ;
            cube:description "Column coordinate of the 512x512 HRDPS target array in its rotated-pole grid. The geographic positions are provided by the two-dimensional lat/lon auxiliary coordinates." ;
            cube:extent ( 0 511 ) ;
            cube:type "spatial" ;
            cube:unit "index" ;
            mlm:datacube_dimension_name "rlon" ] ;
    cube:variables [ cube:data_type "float32" ;
            cube:description "RDPS geopotential height at 850 hPa, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "GZ850" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS geopotential height at 500 hPa, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "GZ500" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS northward wind component at 850 hPa, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "VV850" ],
        [ cube:data_type "float32" ;
            cube:description "HRDPS northward wind component at 10 m, reconstructed on the target grid." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "HRDPS_P_VVC_10000" ],
        [ cube:data_type "float32" ;
            cube:description "Geographic latitude auxiliary coordinate for the rotated grid." ;
            cube:dimensions "rlat",
                "rlon" ;
            cube:type "auxiliary" ;
            cube:unit "degree_north" ;
            mlm:datacube_variable_name "lat" ],
        [ cube:data_type "float32" ;
            cube:description "Static HRDPS orography on the target rotated grid, aligned to the output patch." ;
            cube:dimensions "rlat",
                "rlon" ;
            cube:type "data" ;
            mlm:datacube_variable_name "orog" ],
        [ cube:data_type "float32" ;
            cube:description "HRDPS eastward wind component at 10 m, reconstructed on the target grid." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "HRDPS_P_UUC_10000" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS air temperature on model levels, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "TT_model_levels" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS eastward wind component at 850 hPa, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "UU850" ],
        [ cube:data_type "float32" ;
            cube:description "HRDPS air temperature at 10 m, reconstructed on the target grid." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "HRDPS_P_TT_10000" ],
        [ cube:data_type "float32" ;
            cube:description "Static HRDPS land-fraction field on the target rotated grid, aligned to the output patch." ;
            cube:dimensions "rlat",
                "rlon" ;
            cube:type "data" ;
            mlm:datacube_variable_name "sftlf" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS pressure at the surface, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "PN" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS precipitation rate at the surface, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "PR" ],
        [ cube:data_type "float32" ;
            cube:description "Geographic longitude auxiliary coordinate for the rotated grid." ;
            cube:dimensions "rlat",
                "rlon" ;
            cube:type "auxiliary" ;
            cube:unit "degree_east" ;
            mlm:datacube_variable_name "lon" ],
        [ cube:data_type "float32" ;
            cube:description "HRDPS precipitation rate at the surface, reconstructed on the target grid." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "HRDPS_P_PR_SFC" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS relative humidity at 850 hPa, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "HU850" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS convective precipitation at the surface, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "PC" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS dew-point temperature, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "TD" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS northward wind component on model levels, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "VV_model_levels" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS eastward wind component on model levels, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "UU_model_levels" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS air temperature at 850 hPa, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "TT850" ],
        [ cube:data_type "float32" ;
            cube:description "RDPS relative humidity at 700 hPa, normalized before inference." ;
            cube:dimensions "rlat",
                "rlon",
                "time" ;
            cube:type "data" ;
            mlm:datacube_variable_name "HU700" ] ;
    mlm:accelerator mlm:cuda ;
    mlm:accelerator_constrained false ;
    mlm:architecture "U-Net"^^xsd:string ;
    mlm:framework "pytorch"^^xsd:string ;
    mlm:framework_version "2.14.0+cu130"^^xsd:string ;
    mlm:hyperparameters "{\"coarsen_factor\":4,\"depth\":2,\"device\":\"cpu\",\"global_end_datetime\":\"2024-09-01 12:00:00\",\"global_start_datetime\":\"2017-05-22 07:00:00\",\"initial_nb_of_hidden_channels\":144,\"kernel_size\":3,\"learning_rate\":0.002,\"mae_loss_weight\":0.0,\"mass_loss_weight\":0.0,\"mse_loss_weight\":0.5,\"nb_of_epochs\":18,\"num_threads\":16,\"num_workers\":8,\"optimizer\":\"Adam\",\"reduction_ratio\":4,\"ssim_k1\":0.01,\"ssim_k2\":0.03,\"ssim_kernel_size\":11,\"ssim_loss_weight\":0.5,\"ssim_sigma\":1.5,\"test_period_start\":\"2023-06-01 00:00:00\",\"training_batch_size\":64,\"validation_period_start\":\"2023-01-10 00:00:00\",\"weight_decay\":\"1e-05\"}"^^rdf:JSON ;
    mlm:input ( [ mlm:bands () ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "variables" "rlat" "rlon" ) ;
                        mlm:shape ( -1 14 128 128 ) ] ;
                mlm:io_description "Fourteen normalized RDPS meteorological channels on the 128x128 coarse rotated grid. Each flexible batch element represents one independently selected valid time. The time identifies samples in the surrounding dataset but is not a tensor axis because the U-Net does not jointly process a temporal sequence." ;
                mlm:io_name "rdps_inputs" ;
                mlm:pre_processing_function "null"^^rdf:JSON ;
                mlm:variables ( "TT_model_levels" "PR" "UU_model_levels" "VV_model_levels" "PC" "PN" "TT850" "GZ500" "GZ850" "HU850" "HU700" "TD" "UU850" "VV850" ) ] [ mlm:bands () ;
                mlm:input_structure [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "variables" "rlat" "rlon" ) ;
                        mlm:shape ( -1 2 512 512 ) ] ;
                mlm:io_description "Static orography and land-fraction channels on the 512x512 target grid. The geographic lat/lon are auxiliary coordinates over rlat/rlon." ;
                mlm:io_name "hrdps_geophysical_inputs" ;
                mlm:pre_processing_function "null"^^rdf:JSON ;
                mlm:variables ( "orog" "sftlf" ) ] ) ;
    mlm:name "UNet RDPS HRDPS Downscaling"^^xsd:string ;
    mlm:output ( [ mlm:bands () ;
                mlm:io_description "Four continuous HRDPS fields reconstructed for the same valid time on the 512x512 target rotated grid." ;
                mlm:io_name "hrdps_outputs" ;
                mlm:post_processing_function "null"^^rdf:JSON ;
                mlm:result [ mlm:data_type "float32" ;
                        mlm:dim_order ( "batch" "variables" "rlat" "rlon" ) ;
                        mlm:shape ( -1 4 512 512 ) ] ;
                mlm:tasks ( mlm:downscaling mlm:super-resolution ) ;
                mlm:variables ( "HRDPS_P_TT_10000" "HRDPS_P_PR_SFC" "HRDPS_P_UUC_10000" "HRDPS_P_VVC_10000" ) ] ) ;
    mlm:pretrained false ;
    mlm:tasks ( mlm:downscaling mlm:super-resolution ) ;
    mlm:total_parameters "9871888"^^xsd:nonNegativeInteger ;
    ns7:citation "Gauvin St-Denis, B., and Smith, T. J. resoterre (version 0.1.3.dev9). Ouranos." ;
    ns2:branch "main" ;
    ns2:revision "5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8" ;
    ns2:type "git" .

<docker://resoterre-inference:0.1.3.dev9> dcterms:description "Versioned OCI container that packages PyTorch, Snakemake, the workflow, and model dependencies." ;
    dcterms:format "application/vnd.oci.image.index.v1+json" ;
    dcterms:title "resoterre inference container 0.1.3.dev9" ;
    stac:hasAssetroles "mlm:inference-runtime"^^xsd:string,
        "runtime"^^xsd:string .

<https://huggingface.co/bstdenis/unet-rdps-to-hrdps-downscaling/blob/main/unet_epoch_mebojo_018.safetensors> ns4:entrypoint "resoterre.ml.neural_networks_unet:UNet" ;
    ns3:checksum "122090e4bbd8583de97cea555072b98479920d1c2c6949daa3254f3c771571cebf6b" ;
    ns3:size 39526256 ;
    dcterms:description "SafeTensors weights loaded by the resoterre U-Net implementation." ;
    dcterms:format "application/octet-stream; framework=pytorch" ;
    dcterms:title "Epoch 18 U-Net SafeTensors weights" ;
    stac:hasAssetroles "data"^^xsd:string,
        "mlm:model"^^xsd:string,
        "mlm:weights"^^xsd:string,
        "model"^^xsd:string,
        "weights"^^xsd:string ;
    mlm:artifact_type "safetensors.torch.save_file"^^xsd:string .

<https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/configs/downscaling/downscaling_rdps_to_hrdps_cwl.yaml> ns3:checksum "1220386fc766bf6ab79ef6a9dd6f0ac3f706669bf09a037be02b87991b159af44136" ;
    ns3:size 3606 ;
    dcterms:description "Configuration consumed by the Snakemake workflow." ;
    dcterms:format "application/yaml" ;
    dcterms:title "Training and inference configuration" ;
    stac:hasAssetroles "configuration"^^xsd:string,
        "metadata"^^xsd:string .

<https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/docker/Dockerfile.inference> ns4:languages "Dockerfile" ;
    ns3:checksum "12201afe4cb941fb434e8fac2bd83a4ddf3a701993bd050a3bae82584e94b3b0824b" ;
    ns3:size 1626 ;
    dcterms:description "Generic Dockerfile used to build the inference container image." ;
    dcterms:format "text/x-dockerfile" ;
    dcterms:title "Inference container definition" ;
    stac:hasAssetroles "container"^^xsd:string .

<https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/scripts/meta_workflows/downscaling/rdps_to_hrdps.smk> ns4:entrypoint "scripts/meta_workflows/downscaling/rdps_to_hrdps.smk" ;
    ns4:languages "Python" ;
    ns3:checksum "1220fbfe7b7f39796c9e378dc2522a82581ec9024781222327a5d75ba59dc3b32046" ;
    ns3:size 1700 ;
    dcterms:description "Executable Snakemake workflow that preprocesses RDPS data and runs downscaling inference." ;
    dcterms:format "text/x-snakemake" ;
    dcterms:title "RDPS-to-HRDPS Snakemake workflow" ;
    stac:hasAssetroles "code"^^xsd:string,
        "mlm:source_code"^^xsd:string ;
    mlm:entrypoint "snakemake -s scripts/meta_workflows/downscaling/rdps_to_hrdps.smk --config config_yaml=/app/configs/downscaling/downscaling_rdps_to_hrdps_cwl.yaml -j1 --directory=/app"^^xsd:string .

<https://raw.githubusercontent.com/Ouranosinc/resoterre/5d4d884a775fb84ea9b12404c47aefc5ee8d8fa8/CITATION.cff> ns3:checksum "1220ffe80cd84de27fed65be4cd5289bcf00defe4553f2fc7086465228bec4d28476" ;
    ns3:size 945 ;
    dcterms:description "Citation File Format metadata for resoterre." ;
    dcterms:format "text/yaml" ;
    dcterms:title "Citation metadata" ;
    stac:hasAssetroles "metadata"^^xsd:string .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: MLM extension 1.6
description: STAC MLM for STAC Items and STAC Collections.
allOf:
- anyOf:
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://stac-extensions.github.io/mlm/v1.6/schema.json
x-jsonld-extra-terms:
  cube:variables:
    x-jsonld-id: https://w3id.org/ogc/stac/datacube/variables
    x-jsonld-container: '@index'
    x-jsonld-index: https://w3id.org/ogc/stac/mlm/datacube_variable_name
    x-jsonld-context:
      dimensions:
        '@id': https://w3id.org/ogc/stac/datacube/dimensions
        '@container': '@set'
      type: https://w3id.org/ogc/stac/datacube/type
      description: https://w3id.org/ogc/stac/datacube/description
      extent:
        '@id': https://w3id.org/ogc/stac/datacube/extent
        '@container': '@list'
      values:
        '@id': https://w3id.org/ogc/stac/datacube/values
        '@container': '@list'
      unit: https://w3id.org/ogc/stac/datacube/unit
      nodata: https://w3id.org/ogc/stac/datacube/nodata
      data_type: https://w3id.org/ogc/stac/datacube/data_type
  cube:dimensions:
    x-jsonld-id: https://w3id.org/ogc/stac/datacube/dimensions
    x-jsonld-container: '@index'
    x-jsonld-index: https://w3id.org/ogc/stac/mlm/datacube_dimension_name
    x-jsonld-context:
      type: https://w3id.org/ogc/stac/datacube/type
      axis: https://w3id.org/ogc/stac/datacube/axis
      axes:
        '@id': https://w3id.org/ogc/stac/datacube/axes
        '@container': '@set'
      description: https://w3id.org/ogc/stac/datacube/description
      extent:
        '@id': https://w3id.org/ogc/stac/datacube/extent
        '@container': '@list'
      values:
        '@id': https://w3id.org/ogc/stac/datacube/values
        '@container': '@list'
      step: https://w3id.org/ogc/stac/datacube/step
      unit: https://w3id.org/ogc/stac/datacube/unit
      reference_system: https://w3id.org/ogc/stac/datacube/reference_system
      bbox:
        '@id': https://w3id.org/ogc/stac/datacube/bbox
        '@container': '@list'
      geometry_types:
        '@id': https://w3id.org/ogc/stac/datacube/geometry_types
        '@container': '@set'
  mlm:name:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/name
    x-jsonld-type: xsd:string
  mlm:architecture:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/architecture
    x-jsonld-type: xsd:string
  mlm:tasks:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/tasks
    x-jsonld-type: '@vocab'
    x-jsonld-container: '@list'
    x-jsonld-context:
      regression: https://w3id.org/ogc/stac/mlm/regression
      classification: https://w3id.org/ogc/stac/mlm/classification
      scene-classification: https://w3id.org/ogc/stac/mlm/scene-classification
      detection: https://w3id.org/ogc/stac/mlm/detection
      object-detection: https://w3id.org/ogc/stac/mlm/object-detection
      segmentation: https://w3id.org/ogc/stac/mlm/segmentation
      semantic-segmentation: https://w3id.org/ogc/stac/mlm/semantic-segmentation
      instance-segmentation: https://w3id.org/ogc/stac/mlm/instance-segmentation
      panoptic-segmentation: https://w3id.org/ogc/stac/mlm/panoptic-segmentation
      similarity-search: https://w3id.org/ogc/stac/mlm/similarity-search
      generative: https://w3id.org/ogc/stac/mlm/generative
      image-captioning: https://w3id.org/ogc/stac/mlm/image-captioning
      super-resolution: https://w3id.org/ogc/stac/mlm/super-resolution
      downscaling: https://w3id.org/ogc/stac/mlm/downscaling
  mlm:framework:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/framework
    x-jsonld-type: xsd:string
  mlm:framework_version:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/framework_version
    x-jsonld-type: xsd:string
  mlm:memory_size:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/memory_size
    x-jsonld-type: xsd:nonNegativeInteger
  mlm:total_parameters:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/total_parameters
    x-jsonld-type: xsd:nonNegativeInteger
  mlm:pretrained:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/pretrained
    x-jsonld-type: xsd:boolean
  mlm:pretrained_source:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/pretrained_source
    x-jsonld-type: xsd:string
  mlm:batch_size_suggestion:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/batch_size_suggestion
    x-jsonld-type: xsd:nonNegativeInteger
  mlm:accelerator:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/accelerator
    x-jsonld-type: '@vocab'
    x-jsonld-context:
      amd64: https://w3id.org/ogc/stac/mlm/amd64
      cuda: https://w3id.org/ogc/stac/mlm/cuda
      xla: https://w3id.org/ogc/stac/mlm/xla
      amd-rocm: https://w3id.org/ogc/stac/mlm/amd-rocm
      intel-ipex-cpu: https://w3id.org/ogc/stac/mlm/intel-ipex-cpu
      intel-ipex-gpu: https://w3id.org/ogc/stac/mlm/intel-ipex-gpu
      macos-arm: https://w3id.org/ogc/stac/mlm/macos-arm
  mlm:accelerator_constrained:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/accelerator_constrained
    x-jsonld-type: xsd:boolean
  mlm:accelerator_summary:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/accelerator_summary
    x-jsonld-type: xsd:string
  mlm:accelerator_count:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/accelerator_count
    x-jsonld-type: xsd:positiveInteger
  mlm:hyperparameters:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/hyperparameters
    x-jsonld-type: '@json'
  mlm:artifact_type:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/artifact_type
    x-jsonld-type: xsd:string
  mlm:compile_method:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/compile_method
    x-jsonld-type: xsd:string
  mlm:entrypoint:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/entrypoint
    x-jsonld-type: xsd:string
  mlm:input:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/input
    x-jsonld-container: '@list'
    x-jsonld-type: https://w3id.org/ogc/stac/mlm/ModelInput
    x-jsonld-context:
      '@vocab': https://w3id.org/ogc/stac/mlm/
      name: https://w3id.org/ogc/stac/mlm/io_name
      description: https://w3id.org/ogc/stac/mlm/io_description
      bands:
        '@id': https://w3id.org/ogc/stac/mlm/bands
        '@container': '@list'
        '@context':
          name: https://w3id.org/ogc/stac/mlm/reference_name
          format: https://w3id.org/ogc/stac/mlm/reference_format
          expression:
            '@id': https://w3id.org/ogc/stac/mlm/reference_expression
            '@type': '@json'
      variables:
        '@id': https://w3id.org/ogc/stac/mlm/variables
        '@container': '@list'
        '@context':
          name: https://w3id.org/ogc/stac/mlm/reference_name
          format: https://w3id.org/ogc/stac/mlm/reference_format
          expression:
            '@id': https://w3id.org/ogc/stac/mlm/reference_expression
            '@type': '@json'
      resize_type:
        '@id': https://w3id.org/ogc/stac/mlm/resize_type
        '@type': '@vocab'
        '@context':
          crop: https://w3id.org/ogc/stac/mlm/crop
          pad: https://w3id.org/ogc/stac/mlm/pad
          interpolation-nearest: https://w3id.org/ogc/stac/mlm/interpolation-nearest
          interpolation-linear: https://w3id.org/ogc/stac/mlm/interpolation-linear
          interpolation-cubic: https://w3id.org/ogc/stac/mlm/interpolation-cubic
          interpolation-area: https://w3id.org/ogc/stac/mlm/interpolation-area
          interpolation-lanczos4: https://w3id.org/ogc/stac/mlm/interpolation-lanczos4
          interpolation-max: https://w3id.org/ogc/stac/mlm/interpolation-max
          wrap-fill-outliers: https://w3id.org/ogc/stac/mlm/wrap-fill-outliers
          wrap-inverse-map: https://w3id.org/ogc/stac/mlm/wrap-inverse-map
      pre_processing_function:
        '@id': https://w3id.org/ogc/stac/mlm/pre_processing_function
        '@type': '@json'
      value_scaling:
        '@id': https://w3id.org/ogc/stac/mlm/value_scaling
        '@container': '@list'
        '@type': https://w3id.org/ogc/stac/mlm/ValueScaling
        '@context':
          '@vocab': https://w3id.org/ogc/stac/mlm/
          type:
            '@id': https://w3id.org/ogc/stac/mlm/scaling_type
            '@type': '@vocab'
            '@context':
              min-max: https://w3id.org/ogc/stac/mlm/min-max
              z-score: https://w3id.org/ogc/stac/mlm/z-score
              clip: https://w3id.org/ogc/stac/mlm/clip
              clip-min: https://w3id.org/ogc/stac/mlm/clip-min
              clip-max: https://w3id.org/ogc/stac/mlm/clip-max
              offset: https://w3id.org/ogc/stac/mlm/offset
              scale: https://w3id.org/ogc/stac/mlm/scale
              processing: https://w3id.org/ogc/stac/mlm/processing
          minimum: https://w3id.org/ogc/stac/mlm/minimum
          maximum: https://w3id.org/ogc/stac/mlm/maximum
          mean: https://w3id.org/ogc/stac/mlm/mean
          stddev: https://w3id.org/ogc/stac/mlm/stddev
          value: https://w3id.org/ogc/stac/mlm/scaling_value
      input:
        '@id': https://w3id.org/ogc/stac/mlm/input_structure
        '@type': https://w3id.org/ogc/stac/mlm/InputStructure
        '@context':
          '@vocab': https://w3id.org/ogc/stac/mlm/
          shape:
            '@id': https://w3id.org/ogc/stac/mlm/shape
            '@container': '@list'
          dim_order:
            '@id': https://w3id.org/ogc/stac/mlm/dim_order
            '@container': '@list'
          data_type: https://w3id.org/ogc/stac/mlm/data_type
  mlm:output:
    x-jsonld-id: https://w3id.org/ogc/stac/mlm/output
    x-jsonld-container: '@list'
    x-jsonld-type: https://w3id.org/ogc/stac/mlm/ModelOutput
    x-jsonld-context:
      '@vocab': https://w3id.org/ogc/stac/mlm/
      name: https://w3id.org/ogc/stac/mlm/io_name
      description: https://w3id.org/ogc/stac/mlm/io_description
      bands:
        '@id': https://w3id.org/ogc/stac/mlm/bands
        '@container': '@list'
        '@context':
          name: https://w3id.org/ogc/stac/mlm/reference_name
          format: https://w3id.org/ogc/stac/mlm/reference_format
          expression:
            '@id': https://w3id.org/ogc/stac/mlm/reference_expression
            '@type': '@json'
      variables:
        '@id': https://w3id.org/ogc/stac/mlm/variables
        '@container': '@list'
        '@context':
          name: https://w3id.org/ogc/stac/mlm/reference_name
          format: https://w3id.org/ogc/stac/mlm/reference_format
          expression:
            '@id': https://w3id.org/ogc/stac/mlm/reference_expression
            '@type': '@json'
      classification:classes:
        '@id': classification:classes
        '@container': '@set'
        '@context':
          '@vocab': https://w3id.org/ogc/stac/classification/
          value: classification:value
          name: classification:name
          title: classification:title
          description: classification:description
          color_hint: classification:color_hint
          nodata: classification:nodata
          percentage: classification:percentage
          count: classification:count
      tasks:
        '@id': https://w3id.org/ogc/stac/mlm/tasks
        '@type': '@vocab'
        '@container': '@list'
        '@context':
          regression: https://w3id.org/ogc/stac/mlm/regression
          classification: https://w3id.org/ogc/stac/mlm/classification
          scene-classification: https://w3id.org/ogc/stac/mlm/scene-classification
          detection: https://w3id.org/ogc/stac/mlm/detection
          object-detection: https://w3id.org/ogc/stac/mlm/object-detection
          segmentation: https://w3id.org/ogc/stac/mlm/segmentation
          semantic-segmentation: https://w3id.org/ogc/stac/mlm/semantic-segmentation
          instance-segmentation: https://w3id.org/ogc/stac/mlm/instance-segmentation
          panoptic-segmentation: https://w3id.org/ogc/stac/mlm/panoptic-segmentation
          similarity-search: https://w3id.org/ogc/stac/mlm/similarity-search
          generative: https://w3id.org/ogc/stac/mlm/generative
          image-captioning: https://w3id.org/ogc/stac/mlm/image-captioning
          super-resolution: https://w3id.org/ogc/stac/mlm/super-resolution
          downscaling: https://w3id.org/ogc/stac/mlm/downscaling
      post_processing_function:
        '@id': https://w3id.org/ogc/stac/mlm/post_processing_function
        '@type': '@json'
      result:
        '@id': https://w3id.org/ogc/stac/mlm/result
        '@type': https://w3id.org/ogc/stac/mlm/ResultStructure
        '@context':
          '@vocab': https://w3id.org/ogc/stac/mlm/
          shape:
            '@id': https://w3id.org/ogc/stac/mlm/shape
            '@container': '@list'
          dim_order:
            '@id': https://w3id.org/ogc/stac/mlm/dim_order
            '@container': '@list'
          data_type: https://w3id.org/ogc/stac/mlm/data_type
x-jsonld-prefixes:
  cube: https://w3id.org/ogc/stac/datacube/
  mlm: https://w3id.org/ogc/stac/mlm/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "stac_extensions": "stac:hasExtension",
    "type": "@type",
    "id": "@id",
    "extent": "dct:extent",
    "links": {
      "@context": {
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
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "title": {
      "@id": "dct:title",
      "@container": "@set"
    },
    "description": {
      "@id": "dct:description",
      "@container": "@set"
    },
    "keywords": {
      "@id": "dcat:keyword",
      "@container": "@set"
    },
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
    "created": "dct:created",
    "updated": "dct:modified",
    "license": "dcat:license",
    "providers": "stac:hasProvider",
    "assets": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/assets/",
        "href": "@id",
        "type": "dct:format",
        "roles": {
          "@id": "stac:hasAssetroles",
          "@type": "xsd:string",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac_version": "stac:version",
    "media_type": "dct:format",
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
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "time": "dct:temporal",
    "linkTemplates": {
      "@context": {
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
        "uriTemplate": {
          "@type": "xsd:string",
          "@id": "rec:uriTemplate"
        },
        "varBase": "rec:varBase",
        "variables": {
          "@id": "rec:hasVariable",
          "@container": "@index",
          "@index": "dct:identifier"
        }
      },
      "@id": "rec:hasLinkTemplate"
    },
    "cube:variables": {
      "@id": "cube:variables",
      "@container": "@index",
      "@index": "mlm:datacube_variable_name",
      "@context": {
        "dimensions": {
          "@id": "cube:dimensions",
          "@container": "@set"
        },
        "type": "cube:type",
        "description": "cube:description",
        "extent": {
          "@id": "cube:extent",
          "@container": "@list"
        },
        "values": {
          "@id": "cube:values",
          "@container": "@list"
        },
        "unit": "cube:unit",
        "nodata": "cube:nodata",
        "data_type": "cube:data_type"
      }
    },
    "cube:dimensions": {
      "@id": "cube:dimensions",
      "@container": "@index",
      "@index": "mlm:datacube_dimension_name",
      "@context": {
        "type": "cube:type",
        "axis": "cube:axis",
        "axes": {
          "@id": "cube:axes",
          "@container": "@set"
        },
        "description": "cube:description",
        "extent": {
          "@id": "cube:extent",
          "@container": "@list"
        },
        "values": {
          "@id": "cube:values",
          "@container": "@list"
        },
        "step": "cube:step",
        "unit": "cube:unit",
        "reference_system": "cube:reference_system",
        "bbox": {
          "@id": "cube:bbox",
          "@container": "@list"
        },
        "geometry_types": {
          "@id": "cube:geometry_types",
          "@container": "@set"
        }
      }
    },
    "mlm:name": {
      "@id": "mlm:name",
      "@type": "xsd:string"
    },
    "mlm:architecture": {
      "@id": "mlm:architecture",
      "@type": "xsd:string"
    },
    "mlm:tasks": {
      "@id": "mlm:tasks",
      "@type": "@vocab",
      "@container": "@list",
      "@context": {
        "regression": "mlm:regression",
        "classification": "mlm:classification",
        "scene-classification": "mlm:scene-classification",
        "detection": "mlm:detection",
        "object-detection": "mlm:object-detection",
        "segmentation": "mlm:segmentation",
        "semantic-segmentation": "mlm:semantic-segmentation",
        "instance-segmentation": "mlm:instance-segmentation",
        "panoptic-segmentation": "mlm:panoptic-segmentation",
        "similarity-search": "mlm:similarity-search",
        "generative": "mlm:generative",
        "image-captioning": "mlm:image-captioning",
        "super-resolution": "mlm:super-resolution",
        "downscaling": "mlm:downscaling"
      }
    },
    "mlm:framework": {
      "@id": "mlm:framework",
      "@type": "xsd:string"
    },
    "mlm:framework_version": {
      "@id": "mlm:framework_version",
      "@type": "xsd:string"
    },
    "mlm:memory_size": {
      "@id": "mlm:memory_size",
      "@type": "xsd:nonNegativeInteger"
    },
    "mlm:total_parameters": {
      "@id": "mlm:total_parameters",
      "@type": "xsd:nonNegativeInteger"
    },
    "mlm:pretrained": {
      "@id": "mlm:pretrained",
      "@type": "xsd:boolean"
    },
    "mlm:pretrained_source": {
      "@id": "mlm:pretrained_source",
      "@type": "xsd:string"
    },
    "mlm:batch_size_suggestion": {
      "@id": "mlm:batch_size_suggestion",
      "@type": "xsd:nonNegativeInteger"
    },
    "mlm:accelerator": {
      "@id": "mlm:accelerator",
      "@type": "@vocab",
      "@context": {
        "amd64": "mlm:amd64",
        "cuda": "mlm:cuda",
        "xla": "mlm:xla",
        "amd-rocm": "mlm:amd-rocm",
        "intel-ipex-cpu": "mlm:intel-ipex-cpu",
        "intel-ipex-gpu": "mlm:intel-ipex-gpu",
        "macos-arm": "mlm:macos-arm"
      }
    },
    "mlm:accelerator_constrained": {
      "@id": "mlm:accelerator_constrained",
      "@type": "xsd:boolean"
    },
    "mlm:accelerator_summary": {
      "@id": "mlm:accelerator_summary",
      "@type": "xsd:string"
    },
    "mlm:accelerator_count": {
      "@id": "mlm:accelerator_count",
      "@type": "xsd:positiveInteger"
    },
    "mlm:hyperparameters": {
      "@id": "mlm:hyperparameters",
      "@type": "@json"
    },
    "mlm:artifact_type": {
      "@id": "mlm:artifact_type",
      "@type": "xsd:string"
    },
    "mlm:compile_method": {
      "@id": "mlm:compile_method",
      "@type": "xsd:string"
    },
    "mlm:entrypoint": {
      "@id": "mlm:entrypoint",
      "@type": "xsd:string"
    },
    "mlm:input": {
      "@id": "mlm:input",
      "@container": "@list",
      "@type": "mlm:ModelInput",
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/mlm/",
        "name": "mlm:io_name",
        "description": "mlm:io_description",
        "bands": {
          "@id": "mlm:bands",
          "@container": "@list",
          "@context": {
            "name": "mlm:reference_name",
            "format": "mlm:reference_format",
            "expression": {
              "@id": "mlm:reference_expression",
              "@type": "@json"
            }
          }
        },
        "variables": {
          "@id": "mlm:variables",
          "@container": "@list",
          "@context": {
            "name": "mlm:reference_name",
            "format": "mlm:reference_format",
            "expression": {
              "@id": "mlm:reference_expression",
              "@type": "@json"
            }
          }
        },
        "resize_type": {
          "@id": "mlm:resize_type",
          "@type": "@vocab",
          "@context": {
            "crop": "mlm:crop",
            "pad": "mlm:pad",
            "interpolation-nearest": "mlm:interpolation-nearest",
            "interpolation-linear": "mlm:interpolation-linear",
            "interpolation-cubic": "mlm:interpolation-cubic",
            "interpolation-area": "mlm:interpolation-area",
            "interpolation-lanczos4": "mlm:interpolation-lanczos4",
            "interpolation-max": "mlm:interpolation-max",
            "wrap-fill-outliers": "mlm:wrap-fill-outliers",
            "wrap-inverse-map": "mlm:wrap-inverse-map"
          }
        },
        "pre_processing_function": {
          "@id": "mlm:pre_processing_function",
          "@type": "@json"
        },
        "value_scaling": {
          "@id": "mlm:value_scaling",
          "@container": "@list",
          "@type": "mlm:ValueScaling",
          "@context": {
            "@vocab": "https://w3id.org/ogc/stac/mlm/",
            "type": {
              "@id": "mlm:scaling_type",
              "@type": "@vocab",
              "@context": {
                "min-max": "mlm:min-max",
                "z-score": "mlm:z-score",
                "clip": "mlm:clip",
                "clip-min": "mlm:clip-min",
                "clip-max": "mlm:clip-max",
                "offset": "mlm:offset",
                "scale": "mlm:scale",
                "processing": "mlm:processing"
              }
            },
            "minimum": "mlm:minimum",
            "maximum": "mlm:maximum",
            "mean": "mlm:mean",
            "stddev": "mlm:stddev",
            "value": "mlm:scaling_value"
          }
        },
        "input": {
          "@id": "mlm:input_structure",
          "@type": "mlm:InputStructure",
          "@context": {
            "@vocab": "https://w3id.org/ogc/stac/mlm/",
            "shape": {
              "@id": "mlm:shape",
              "@container": "@list"
            },
            "dim_order": {
              "@id": "mlm:dim_order",
              "@container": "@list"
            },
            "data_type": "mlm:data_type"
          }
        }
      }
    },
    "mlm:output": {
      "@id": "mlm:output",
      "@container": "@list",
      "@type": "mlm:ModelOutput",
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/mlm/",
        "name": "mlm:io_name",
        "description": "mlm:io_description",
        "bands": {
          "@id": "mlm:bands",
          "@container": "@list",
          "@context": {
            "name": "mlm:reference_name",
            "format": "mlm:reference_format",
            "expression": {
              "@id": "mlm:reference_expression",
              "@type": "@json"
            }
          }
        },
        "variables": {
          "@id": "mlm:variables",
          "@container": "@list",
          "@context": {
            "name": "mlm:reference_name",
            "format": "mlm:reference_format",
            "expression": {
              "@id": "mlm:reference_expression",
              "@type": "@json"
            }
          }
        },
        "classification:classes": {
          "@id": "classification:classes",
          "@container": "@set",
          "@context": {
            "@vocab": "https://w3id.org/ogc/stac/classification/",
            "value": "classification:value",
            "name": "classification:name",
            "title": "classification:title",
            "description": "classification:description",
            "color_hint": "classification:color_hint",
            "nodata": "classification:nodata",
            "percentage": "classification:percentage",
            "count": "classification:count"
          }
        },
        "tasks": {
          "@id": "mlm:tasks",
          "@type": "@vocab",
          "@container": "@list",
          "@context": {
            "regression": "mlm:regression",
            "classification": "mlm:classification",
            "scene-classification": "mlm:scene-classification",
            "detection": "mlm:detection",
            "object-detection": "mlm:object-detection",
            "segmentation": "mlm:segmentation",
            "semantic-segmentation": "mlm:semantic-segmentation",
            "instance-segmentation": "mlm:instance-segmentation",
            "panoptic-segmentation": "mlm:panoptic-segmentation",
            "similarity-search": "mlm:similarity-search",
            "generative": "mlm:generative",
            "image-captioning": "mlm:image-captioning",
            "super-resolution": "mlm:super-resolution",
            "downscaling": "mlm:downscaling"
          }
        },
        "post_processing_function": {
          "@id": "mlm:post_processing_function",
          "@type": "@json"
        },
        "result": {
          "@id": "mlm:result",
          "@type": "mlm:ResultStructure",
          "@context": {
            "@vocab": "https://w3id.org/ogc/stac/mlm/",
            "shape": {
              "@id": "mlm:shape",
              "@container": "@list"
            },
            "dim_order": {
              "@id": "mlm:dim_order",
              "@container": "@list"
            },
            "data_type": "mlm:data_type"
          }
        }
      }
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "cube": "https://w3id.org/ogc/stac/datacube/",
    "mlm": "https://w3id.org/ogc/stac/mlm/",
    "geojson": "https://purl.org/geojson/vocab#",
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
    "thns": "https://w3id.org/ogc/stac/themes/",
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
      "@context": {
        "concepts": {
          "@context": {
            "id": "thns:id",
            "url": "@id"
          },
          "@id": "thns:concepts",
          "@container": "@set"
        },
        "scheme": "thns:scheme"
      },
      "@container": "@set",
      "@id": "rec:themes"
    },
    "formats": {
      "@context": {
        "name": "rec:name",
        "mediaType": "rec:mediaType"
      },
      "@container": "@set",
      "@id": "rec:format",
      "@type": "@id"
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "rights": "dcat:rights",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/mlm/context.jsonld)

## Sources

* [GitHub Repository](https://github.com/stac-extensions/mlm)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-stac](https://github.com/ogcincubator/bblocks-stac)
* Path: `_sources/extensions/mlm`

