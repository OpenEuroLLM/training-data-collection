# OpenEuroLLM Training Data Collection

## Motivation

The OpenEuroLLM consortium will collectively exectute at least three full LLM **development cycles**,

+ (a) a first “production” model around 8B parameters (“mid-size”) available by mid-2026, codenamed [`baby`](./baby/README.md);
+ (b) the first “flagship” model around 30–70B parameters by late 2026, codenamed `flag`; and
+ (c) the final “flagship” model to become available towards the project end.

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

There are four mandatory components to each dataset in the collection,
the original `source/` and the final `release/` version, plus at least
annotations of benchmark contamination (`contamination/`)
and personally identifiable information (`pii/`).
For datasets that are part of the [OpenEuroLLM Training Data Catalogue](https://github.com/OpenEuroLLM/training-data-catalogue), the source data is not copied into the collection but rather
identified uniquely through a softlink into the corresponding data subdirectory
in the catalogue.

The `release/` version of each dataset comprises the collection of files
that serve as the exact point of departure for LLM training, i.e. feed
directly into tokenization.
The release versions are uniformly created in Zstandard-compressed JSONLines
with minimal normalization of key names, notably standardizing on `"text"`
for the actual document contents.

Reflecting step 2. in the above, creation of the release version for each
dataset will typically encompass selection of a subset of data and possibly
metadata-based upsampling.
This process is implemented by code maintained as part of the training data
collection (this repository), which we tentatively dub the OpenEuroLLM **packer**.
Pack(ag)ing of the release versions of each data set at the same applies
decontamination and PII masking, on the basis of available annotations.

For the “baby” cycle, for example, a language like Spanish will be represented
with 100B tokens, which is about one tenth of the available data in the union
of the core multilingual datasets, HPLT 3.0, FinePDFs, and the translations
of MultiSynt.
For HPLT 3.0, a sampling strategy will be applied that takes into account
available metadata, notably WDS document “quality” estimates and web register
annotations.
The `release` version of HPLT 3.0 in the `baby` collection, thus, will comprise
at most 100B tokens, the “best” subset within the available per-language
training budget.

## Workflow

Training data preparation for each cycle typically spans several months,
moving sequentially through steps 1. (source data identification and acqusition)
through 5. (creation of the actual collection, the `release` version).
Scripts and instructions for data acquisition, annotation, and packing are
maintained as part of this repository.
