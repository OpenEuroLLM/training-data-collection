# OpenEuroLLM Training Data Collection

## Motivation

The OpenEuroLLM consortium will collectively exectute at least three full LLM **development cycles**,

+ (a) a first “production” model around 8B parameters (“mid-size”) available by mid-2026, codenamed [`baby`](./baby/README.md);
+ (b) the first “flagship” model around 30–70B parameters by late 2026, codenamed `flag`; and
+ (c) the final “flagship” model to become available towards the project end and yet to be codenamed.

This repository serves to coordinate training data management for this work.
Data preparation for each cycle encompasses a series of steps, including

1. identification and acquisition of suitable **source datasets**;
2. definition of **subsets**, e.g. by volume or based on available metadata;
3. **annotation** with e.g. contamination against benchmarks and PII flags;
4. possibly additional annotation, e.g. “quality” signals, WDS, registers;
5. **effectuating** the above, i.e. creating the exact and full training data.

The result of these steps is called the OpenEuroLLM **Training Data Collection**
(which is distinct from the Training Data Catalogue, but see below).
For transparency and replicability, this data shall be made generally available
beyond the consortium, for example via general download.
If public restribution of the full and exact training data should prove legally
impossible, steps 2. through 5. above must be fully specified and automated, so
as to be able to publish the exact “recipe” for training data preparation.

## Organization

The master copy of the training data collection is organized on LUMI, using
storage that is part of the EuroHPC strategic access (`project_465002530`).
Data identification and preparation works at the interface between WP3 and WP4,
coordinated (in mid-2026) by AI Sweden, Prompsit, and UiO.

The collection is maintained as a directory tree rooted
in `/scratch/project_465002530/training/collection/`.
The top-level directory is sub-divided by production cycles,
i.e. currently distinguishes `baby` and `flag`.

For each cycle, the collection is further organized by individual
datasets, typically well-defined resources like e.g. DCLM-baseline, FinePDFs,
HPLT, Nemotron-CC, The Stack, etc.
For each dataset, all relevant information is gathered in one subdirectory,
e.g. `dclm-1.0/`, `finepdfs-1.0.0/`, `hplt-3.0/`, etc.

There are five mandatory components to each dataset in the collection,
the original `source/` and the final `release/` version, plus at least
annotations of benchmark contamination (`contamination/`)
and personally identifiable information (`pii/`).
Furthermore, cycle-specific statistics are compiled in a separate directory
`counts/` (see below).
For datasets that are part of the [OpenEuroLLM Training Data Catalogue](https://github.com/OpenEuroLLM/training-data-catalogue), the source data is not copied into the collection but rather
identified uniquely through softlinks into the corresponding data subdirectories
in the catalogue.
Only files that contribute to the release cycle are linked into the collection.

The `release/` version of each dataset comprises the collection of files
that serve as the exact point of departure for LLM training, i.e. feed
directly into tokenization.
The release versions are uniformly created in Zstandard-compressed JSONLines
with minimal normalization of key names, notably standardizing on `"text"`
for the actual document contents.

Reflecting step 2. in the above, creation of the release version for each
dataset will typically encompass selection of a subset of data and|or possibly
metadata-based upsampling.
This process is implemented by code associated with the training data
collection (this repository), which we tentatively dub the
[OpenEuroLLM **packer**](https://github.com/OpenEuroLLM/training-data-packer).
Pack(ag)ing of the release versions of each dataset at the same time applies
decontamination and PII masking, on the basis of available annotations.

For the “baby” cycle, for example, a language like Spanish will be represented
with around 200B tokens, which is about one fifth of the available data in the union
of the core multilingual datasets, HPLT 3.0, FinePDFs, and the translations
of MultiSynt.
For HPLT 3.0, a sampling strategy will be applied that takes into account
available metadata, notably WDS document “quality” estimates and web register
annotations.
Other source datasets are downsampled randomly.
The `release` versions of HPLT 3.0, FinePDFs, and the MultiSynt translations
in the `baby` collection, thus, will comprise only a reduced sample of
available Spanish tokens, the “best” subset within the per-language
training budget.

## Workflow

Training data preparation for each cycle typically spans several months,
moving sequentially through steps 1. (source data identification and acqusition)
through 5. (creation of the actual collection, the `release` version).
Scripts and instructions for data acquisition, annotation, and packing are
maintained as part of this repository.

The high-level configuration of the training data collection and parameters
for the packing process are to the largest possible degree maintained in
machine-readable form, as files `metadata.yaml` in the top-level directory
and the root directories for each of the source datasets.

## Statistics and Sampling

For each source datasets and its component parts, document and token counts
are computed using the exact tokenizer for the specific cycle, e.g.
`openeurollm/tokenizer-256k` for the “baby” cycle (as specified by the
`tokenizer` property in `baby/metadata.yaml`).
These counts are organized in a directory tree parallel to the internal
structure of each source dataset, below the `counts/` subdirectory of each
dataset (see `count.slurm` for details).

For example, the “baby” cycle draws on three of the available parts in
Nemotron-CC 1.0, called `high/actual`, `medium-high/actual`, and
`medium-actual`.
Statistics for each of these subsets are organized as e.g.
`baby/nemotron-cc-1.0/counts/high/actual/source.json`,
`baby/nemotron-cc-1.0/counts/medium-high/actual/source.json`, etc.

For a multilingual source dataset like HPLT 3.0, the internal parts
reflect individual language–script combinations.
Thus, statistics for the Spanish HPLT 3.0 part, for example, are
available as `baby/hplt-3.0/counts/spa_Latn/source.json`.
These counts serve to define per-part target token budgets for
sampling and packing.

For the initial “baby” cycle, three sampling strategies are defined:

+ `full`: no downsampling; all available documents (after filtering) are packed;
+ `random`: random downsampling, packing a subset of documents at a set probability; and
+ `wds+register`: down- and upsampling based on WDS and web register annotations (see below).

The first two sampling strategies are exemplified by e.g. the three parts
specified in `baby/nemotron-cc-1.0/metadata.yaml`, where the `full` strategy
takes no parameters, and the `random` one is given its target document `budget`
as a percentage of the full source.

``
release:
  high/actual:
    sample: full
  medium-high/actual:
    sample: full
  medium/actual:
    sample: random
    budget: 64%
```

## Mirroring across EuroHPC Systems