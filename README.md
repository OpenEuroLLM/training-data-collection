# OpenEuroLLM Training Data Collection

## Motivation

The OpenEuroLLM consortium will collectively exectute at least three full LLM development cycles,

+ (a) a first “production” model around 8B parameters available by mid-2026, codenamed `baby`;
+ (b) the first “flagship” model around 30–70B parameters by late 2026, codenamed `flag`; and
+ (c) the final “flagship” model to become available towards the project end.

This repository serves to coordinate training data management.
Data preparation for each cycle encompasses a series of steps, including

1. identification and acquisition of suitable **source datasets**;
2. definition of subsets, e.g. by volume or based on available metadata;
3. annotation with e.g. contamination against benchmarks and PII flags;
4. possibly additional annotation, e.g. “quality” signals, WDS, registers;
5. effectuating the above, i.e. creating the exact and full training data.

The result of these steps is called the OpenEuroLLM **training data collection**.
For transparency and replicability, this data shall be made generally available
beyond the consortium, for example via general download.
If public restribution of the full and exact training data should prove legally
impossible, steps 2. through 5. above must be fully specified and automated, so
as to be able to publish the exact “recipe” for training data preparation.

## Organization

The master copy of the training data collection is organized on LUMI, using
storage that is part of the EuroHPC strategic access (`project_465002530`).
Data identification and preparation works at the interface between WP3 and WP4,
coordinated by Prompsit, AI Sweden, and UiO.

The collection is maintained as a directory tree rooted
in `/scratch/project_465002530/training/collection/`.
The top-level directory is sub-divided by production cycles,
i.e. currently distinguishes `baby` and `flag`.
For each cycle, the collection is further organized by individual
datasets, typically well-defined resources like e.g. DCLM-baseline, FineWeb,
HPLT, Nemotron-CC, The Stack, etc.
For each dataset, it 