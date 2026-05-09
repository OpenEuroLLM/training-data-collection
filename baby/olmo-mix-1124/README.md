# OpenEuroLLM “Baby”: OLMo 2 (November 2024) Pretraining Set

## Overview

This direcctory contains the three parts of the Olmo-Mix 1124 dataset thar
contribute to the pre-training data mix for the OpenEuroLLM “baby” model.  For
historical reasons, there are two distinct copies of the dataset, even though
these are assumed to be equivalent in content.

## Turku Variant

Contamination and PII annotation was applied to a variant of the dataset that
was prepared by the TurkuNLP team, with some minor local modifications (to be
recovered and documented).
To play things safe, this variant (in the `turku/` subdirectory) serves as the
data source for final packing of all training data.

The files have been copied into the “baby” training data collection from the
LUMI path `/scratch/project_462000963/datasets/allenai/`:
```
drwxrws--- 2 galicato project_462000963 4096 Oct 21  2025 ./arxiv
drwxrws--- 2 galicato project_462000963 4096 Oct 17  2025 ./pes2o
drwxrws--- 2 galicato project_462000963 4096 Apr 13 10:45 ./Wiki
```

For increased uniformity and compatibility with the original Olmo-Mix release,
a few renamings have been applied

+ `arxiv/*.json` → `*.jsonl`
+ `Wiki` → `wiki`
+ `wiki/*.json` → `*.jsonl`

Additionally, all JSONLines files have been compressed using: `zstd -z --rm`.

## HuggingFace Distribution

For reference, e.g. to compare token and document counts, the original version
of the dataset, as distributed through the HuggingFace Hub, is also available
in the `source/` subdirectory.

directory 
```
git lfs install --skip-smudge
git config --global lfs.concurrenttransfers 16
git clone --verbose --jobs 8 --single-branch --branch main https://huggingface.co/datasets/allenai/olmo-mix-1124 tmp
cd tmp
for i in arxiv pes2o wiki; do git lfs pull --include data/${i}/\*; done
git lfs fsck | egrep -v 'algebraic-stack|dclm|open-web-math|starcode'
mv data/arxiv/train/* data/arxiv
rmdir data/arxiv/train
mv data ../source
cd ..
rm -rf tmp
rm -rf source/{algebraic-stack,dclm,open-web-math,starcoder}
```
