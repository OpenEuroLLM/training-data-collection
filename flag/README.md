# OpenEuroLLM Training Data Collection for the “Flag” Cycle

This directory documents the training data mix for the first OpenEuroLLM
“flagship” development cycle, internally codenamed `flag`.


## English Source Datasets

**Legend**

* ✅ - complete
* ➕ - included
* ➖ - inapplicable

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample |     Packing      |        Tokens        | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:-----:|:----------------:|:--------------------:|:----:|:----------:|
| dclm-1.0                             |     1 | 1 | ✅ | ✅ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅(3.88TT)           | ✅ | ✅ |
| finepdfs-1.0.0 (eng_Latn)            |     1 | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(2.36T inc multi)  | ✅ | ✅ |
| finepdfs-edu-1.0.0 (eng_Latn)        |     1 | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(279BT inc multi)  | ✅ | ✅ |
| finephrase-0.0.0                     |     4 | 4 | ✅️ | ✅️️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅                   | ✅ | ✅ |
| hplt-4.0 (eng_Latn)                  |     3 | 3 | ✅️️ | ✅️ | ➖ | ✅ | ✅ | ✅ | ✅ | ✅‍(3.46TT inc multi) | ✅ | ✅ |
| nemotron-cc-1.0                      |     3 | 1 | ✅ | ✅️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(2.91TT)           | ✅ | ✅ |
| nemotron-mind-0.0                    |     7 | 4 | ✅️ | ✅️️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅                    | ✅ | ✅ |
| nemotron-pretraining-specialized-1.0 |     6 | 4 | ✅️ | ✅️️️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅(297BT)            | ✅ | ✅ |
| nemotron-pretraining-specialized-1.1 |     5 | 4 | ✅️ | ✅️️️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅(10BT)             | ✅ | ✅ |
| mixture-vitae-1.0                    |    13 | 4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(429BT)            | ✅ | ✅ |
| ~~olmo-mix-1124~~                    | ~~2~~ | 4 | ✅ | ✅️️️ | ➖ | ✅ | ➖ | ➖ | ✅ | ✅(83BT)             | ✅ | ✅ |

## Multilingual Source Datasets

| Path                                                                                                   | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing |      Tokens       | Copy | Validation |
|--------------------------------------------------------------------------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:-----:|:-------:|:-----------------:|:---:|:---------:|
| finepdfs-1.0.0 (multilingual)     |     36 | 2 | ✅ | ✅️ | ✅️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| finepdfs-edu-1.0.0 (multilingual) |     35 | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ~~fineweb2-hq-1.0.0~~             | ~~13~~ |   | ✅️ | ✅️ | ✅️ | ✅ | ✅ | ✅ | ➖ | ➖ | ➖ | ➖ |
| finewiki-0.0.0                    |     34 | 3 | ✅️ | ✅️ | ✅ | ✅ | ➖ | ✅ | ✅ | ✅ | ✅ | ✅ |
| hplt-4.0                          |     63 | 1 | ✅ ‍| ✅️️ | ➕ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| nemotron-cc-opus-1.1              |     20 | 3 | ✅‍ | ✅️ | ➖ | ➖ | ✅ | ➖ | ✅ | ✅ | ✅ | ✅ |
| nemotron-cc-tower+-0.1            |     16 | 3 | ✅ | ✅️️ | ➖ | ➖ | ✅ | ➖ | ✅ | ✅ | ✅ | ✅ |

## Code and Math Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing |  Tokens   | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:------:|:----:|:---------:|:----:|:----------:|
| common-pile-stackv2-0.1              |     1 | 3 | ✅ | ✅️️️ | ✅️ | ➖ | ➖ | ✅️ | ✅️ | ✅️ |    ✅ | ✅ |
| common-pile-stackv2-edu-0.1          |     1 | 3 | ✅️ | ✅️️ | ✅️ | ➖ | ➖ | ✅️ | ✅️ | ✅️ |    ✅ | ✅ |
| dolmino-mix-100b-1125                |     9 | 5 | ✅ | ✅️️️ | ➖ | ➖ | ➖ | ➖ | ✅️️️ | ✅️ |    ✅ | ✅ |
| finemath-0.0.0                       |     1 | 4 | ✅ | ✅️ | ➖ | ➖ | ➖ | ➖ | ✅️️️ | ✅️ |    ✅ | ✅ |
| megamath-0.0.0                       |     1 | 4 | ✅ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️️️ | ✅️ |    ✅ | ✅ |
| openwebmath-0.0.0                    |     1 | 5 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️ | ✅️ |    ✅ | ✅ |
| starcoder-0.0.0                      |     1 | 4 | ✅ | ✅️ | ➖ | ➖ | ➖ | ➖ | ✅️ | ✅️ |    ✅ | ✅ |
| swallow-code-2.0                     |     1 | 4 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️ | ✅️ |    ✅ | ✅ |
| swallow-math-2.0                     |     1 | 4 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️ | ✅️ |    ✅ | ✅ |
| ~~the-stack-1.2~~                    | ~~1~~ |   | ✅️️ | ✅️️️ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |

## Parallel Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample |   Packing   |        Tokens        | Copy | Validation |
|--------------------------------------|:-----:|:-:|:-----:|:-----:|:--------:|:-------------:|:---:|:------:|:-----------:|:--------------------:|:----:|:----------:|
| fineopus-filtered-0.4                |    41 | 5 | ✅ | ✅️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅ | ✅ | ✅ |
| dochplt-3.1                          |    28 | 5 | ✅️️️ | ✅️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅ | ✅ | ✅ |

## Reasoning Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing |  Tokens  | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:------:|:-------:|:--------:|:----:|:----------:|
| agenttrove-0.0                       |     1 |   | ✅️️ | ✅️️️ | ➖ | ✅ | ➖ | ➖ | ✅ | ✅️ | ✅ | ✅ |
| ~~openthoughts-3~~                   | ~~1~~ |   | ✅️️ | ✅️️️ | ➖ | ✅ | ➖ | ➖ | ✅ | ✅️ | ✅ | ✅ |

## Annotations: Contamination

Decontamination proceeded in two steps, (a) contamination annotation and (b)
document filtering.
Starting from a [comprehensive list of LLMs benchmarks](benchmarks.txt), an
augmented version of [NeMo Curator](https://github.com/NVIDIA-NeMo/Curator)
served to compile per-language search indices of n-grams between 8 and 13
word tokens.
For all datasets except code & math, n-gram matches were annotated; these
are available below the `nemo-curator/` sub-directory for each dataset.

In final packing, documents containing such matches were removed.
For technical reasons, this process regrettably failed for the two reasoning
datasets, `agenttrove-0.0` and `openthoughts-3`.

## Annotations: Personally Identifiable Information

## Filtering and Resampling

There will likely be two layers of data selection for the `flag` cycle,
**filtering** and **resampling**.
Both will be based on available annotations, as e.g. web doc scores (WDS), 
web registers, various propella properties, and ordinal “quality” signals
from various classifiers, notably the BSC-edu model.
To the highest degree possible (for transparency and replicability), the
data selection processes should follow declarative specifications, e.g.
inclusion of all relevant parameters and weighting formulas in the
`metadata.yaml` files for each dataset.


Resampling will take a pseudo-probabilistic perspective, where each candidate
document is assigned a numeric weight, where values below `1` correspond to
downsampling, and values above `1` can introduce repetition of documents.
One way of spelling out the weighting formula would be as a snippet of
Python code, taking a full document as its input and returning its score.

For each dataset, the individual filtering and resampling settings could then
be specified as part of `metadata.yaml`, e.g.
```
  sample: high-density-sigmoid()
```

One open question is whether it will be possible to pre-compute target token
budgets (and random sampling probabilities) independent of filtering or
resampling.
It seems likely, however, that a separate step of effectuating all filtering
and resampling will be necessary (as was the case for `wds+register` sampling
in the `baby` cycle), to then compute updated token counts and
determine random sampling rates against the target budget for the `baby`
data mix.


## Packing: Putting it all Together

Instructions on how to run packaging are found in 
[training-data-packer repository](https://github.com/OpenEuroLLM/training-data-packer).

## Tokenization and Roll-Up
Instructions on how to run tokenization are found in 
[tokenization repository](https://github.com/mrunesson/tokenizer/tree/flag/flag-tokenization).
[PR](https://github.com/OpenEuroLLM/tokenizer/pull/3) for merge
into https://github.com/openEuroLLM/tokenizer


| Dataset | Shards | Documents | Sequences | Zero-seq docs | Tokens | .bin size |
|---|---:|---:|---:|---:|---:|---:|
| `agenttrove-0.0` | 1 | 1,568,413 | 1,568,412 | 0 | **20.22B** (20,222,264,518) | 75.3 GB |
| `common-pile-stackv2-0.1` | 8 | 53,178,535 | 53,178,498 | 29 | **709.80B** (709,796,742,143) | 2.6 TB |
| `common-pile-stackv2-edu-0.1` | 1 | 67,741,991 | 67,738,215 | 3,775 | **80.13B** (80,127,925,281) | 298.5 GB |
| `dclm-1.0` | 100 | 2,938,207,599 | 2,938,207,499 | 0 | **3.88T** (3,881,440,468,527) | 14.1 TB |
| `dolmino-mix-100b-1125` | 9 | 58,827,943 | 58,827,934 | 0 | **49.12B** (49,115,755,676) | 183.0 GB |
| `finemath-0.0.0` | 1 | 21,405,611 | 21,405,610 | 0 | **39.39B** (39,392,831,972) | 146.7 GB |
| `finepdfs-1.0.0` | 52 | 381,257,191 | 381,257,139 | 0 | **2.36T** (2,363,087,814,974) | 8.6 TB |
| `finepdfs-edu-1.0.0` | 36 | 41,829,242 | 41,829,206 | 0 | **278.22B** (278,220,221,477) | 1.0 TB |
| `finewiki-0.0.0` | 34 | 25,542,775 | 25,542,741 | 0 | **24.68B** (24,680,252,446) | 91.9 GB |
| `hplt-4.0` | 85 | 3,060,134,483 | 3,060,134,398 | 0 | **3.46T** (3,464,728,446,893) | 12.6 TB |
| `megamath-0.0.0` | 4 | 204,140,620 | 201,627,951 | 2,512,665 | **318.25B** (318,250,972,069) | 1.2 TB |
| `mixture-vitae-1.0` | 5 | 331,820,120 | 331,820,115 | 0 | **428.55B** (428,553,045,248) | 1.6 TB |
| `nemotron-cc-1.0` | 30 | 3,312,610,617 | 3,312,610,587 | 0 | **2.91T** (2,906,643,850,905) | 10.6 TB |
| `nemotron-cc-opus-1.1` | 19 | 174,458,237 | 174,457,659 | 559 | **142.03B** (142,026,750,931) | 529.1 GB |
| `nemotron-cc-tower+-0.1` | 17 | 835,840,554 | 835,832,012 | 8,525 | **541.43B** (541,429,591,377) | 2.0 TB |
| `nemotron-pretraining-specialized-1.0` | 4 | 60,570,166 | 60,570,162 | 0 | **296.89B** (296,892,525,288) | 1.1 TB |
| `nemotron-pretraining-specialized-1.1` | 1 | 19,630,063 | 19,630,061 | 1 | **10.22B** (10,223,996,293) | 38.1 GB |
| `olmo-mix-1124` | 2 | 42,737,264 | 42,737,259 | 3 | **82.55B** (82,554,462,771) | 307.5 GB |
| `openthoughts-3` | 1 | 1,200,001 | 1,200,000 | 0 | **20.20B** (20,204,891,733) | 75.3 GB |
| `openwebmath-0.0.0` | 1 | 6,315,234 | 6,315,233 | 0 | **13.80B** (13,799,966,008) | 51.4 GB |
| `starcoder-0.0.0` | 3 | 188,045,986 | 188,045,983 | 0 | **252.14B** (252,143,641,106) | 939.3 GB |
| `swallow-code-2.0` | 1 | 22,963,269 | 22,942,344 | 20,924 | **50.20B** (50,195,195,420) | 187.0 GB |
| `swallow-math-2.0` | 1 | 25,938,076 | 25,938,075 | 0 | **35.07B** (35,067,810,215) | 130.6 GB |
| **total** | 416 | | | | **16.01T** (16,008,799,423,271) | 58.2 TB |

## Mirroring and Validation

```bash
for t in megatron-lm md5 counts; do
  for d in $(cat etc/datasets.txt); do
    if [ -d ${d}/${t} ]; then
      echo ${d};
      rclone --transfers 16 --checkers 32 --config ${HOME}/.config/rclone/jsc.conf -v \
        sync ${d}/${t} sftp:/e/scratch/e-sta-openeurollm/training/collection/flag/${d}/${t} \
        --sftp-ssh "ssh -F ${HOME}/.ssh/config judac" 2>&1 \
      | tee -a ${d}/tmp/rclone.log;
    fi;
  done;
done
```

```bash
for i in $(egrep -v 'dclm-1.0|hplt-4.0|nemotron-cc-1.0' baby/etc/annealing.txt); do
  echo $i;
  ssh -xt data.leonardo.cineca.it \
    rclone --config ${HOME}/.config/rclone/rclone.conf -v \
      --exclude openeurollm-256k-v2/** --exclude gpt-oss-120b/** --exclude **.md5 \
      sync sftp:/scratch/project_465002530/training/collection/${i}/ \
      /leonardo_work/OELLM_prod2026/training/collection/${i}/ \
      --sftp-ssh \"/bin/ssh -F ${HOME}/.ssh/config lumi\" \
  | tee -a $(dirname ${i})/megatron-lm.log 2>&1;
done
```

## Breakdown

### Section A — General

| Language | Native source | Synthetic source | % of source | Release tokens | % of release | Datasets |
|:---|---:|---:|---:|---:|---:|:---|
| eng | 8,446,490,966,326 | — | 35.84% | 7,028,585,633,677 | 52.44% | dclm-1.0, dochplt-3.1, fineopus-filtered-0.4, finepdfs-edu-1.0.0, finephrase-0.0.0, hplt-4.0, mixture-vitae-1.0, nemotron-cc-1.0, nemotron-pretraining-specialized-1.0, nemotron-pretraining-specialized-1.1, olmo-mix-1124-arxiv, olmo-mix-1124-pes2o |
| spa | 1,362,831,489,955 | 91,611,305,219 | 6.17% | 703,407,614,415 | 5.25% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| fra | 1,207,538,399,806 | 102,377,460,080 | 5.56% | 612,435,288,688 | 4.57% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| deu | 1,109,302,181,041 | 81,859,660,544 | 5.05% | 512,549,027,676 | 3.82% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| por | 454,868,766,269 | 90,185,273,844 | 2.31% | 329,720,018,780 | 2.46% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| ita | 401,103,173,503 | 82,285,655,894 | 2.05% | 293,554,844,036 | 2.19% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| pol | 290,288,399,565 | 83,828,958,663 | 1.59% | 231,920,445,057 | 1.73% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| nld | 232,971,969,250 | 93,648,923,682 | 1.39% | 210,184,896,196 | 1.57% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| ukr | 129,321,538,072 | 102,496,405,840 | 0.98% | 169,730,959,314 | 1.27% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| tur | 181,500,459,635 | 274,833,282,698 | 1.94% | 169,666,699,693 | 1.27% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| hun | 134,849,124,074 | 99,853,552,237 | 1.00% | 166,583,364,465 | 1.24% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| ron | 155,208,725,137 | 100,047,217,252 | 1.08% | 162,634,106,230 | 1.21% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| ces | 131,199,129,033 | 222,757,438,780 | 1.50% | 156,320,294,889 | 1.17% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| ell | 125,549,443,805 | 154,930,307,068 | 1.19% | 140,897,577,579 | 1.05% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| swe | 131,096,760,554 | 89,681,716,339 | 0.94% | 132,339,934,790 | 0.99% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| fin | 101,194,080,428 | 93,248,682,940 | 0.82% | 108,484,370,132 | 0.81% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| dan | 88,083,007,756 | 87,700,534,458 | 0.75% | 103,306,513,583 | 0.77% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| bul | 69,419,676,823 | 290,025,674,270 | 1.53% | 96,206,587,852 | 0.72% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| slk | 67,864,952,193 | 113,218,597,419 | 0.77% | 79,334,698,766 | 0.59% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| nob | 104,670,533,300 | 84,161,194,674 | 0.80% | 70,258,869,127 | 0.52% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| cat | 42,610,628,238 | 124,353,668,852 | 0.71% | 62,702,501,669 | 0.47% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| lit | 41,431,282,071 | 114,912,176,393 | 0.66% | 61,996,865,879 | 0.46% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| hrv | 50,426,300,821 | 108,210,878,830 | 0.67% | 59,453,742,635 | 0.44% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| lvs | 37,074,884,344 | 170,792,299,748 | 0.88% | 55,007,187,264 | 0.41% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| slv | 36,102,957,516 | 112,583,053,500 | 0.63% | 54,837,470,314 | 0.41% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| est | 30,667,078,198 | 267,380,655,295 | 1.26% | 51,777,030,894 | 0.39% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| srp | 39,682,650,676 | 130,924,280,324 | 0.72% | 50,084,845,041 | 0.37% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| sqi | 20,676,319,704 | 174,219,266,179 | 0.83% | 31,525,850,249 | 0.24% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| bos | 21,480,819,782 | 98,924,620,356 | 0.51% | 23,991,446,057 | 0.18% | dochplt-3.1, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| mkd | 9,641,146,303 | 125,518,960,998 | 0.57% | 16,069,721,881 | 0.12% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| isl | 10,959,448,370 | 97,348,571,405 | 0.46% | 15,713,483,734 | 0.12% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| eus | 7,289,528,403 | 102,052,460,721 | 0.46% | 10,001,914,343 | 0.07% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| glg | 6,952,461,929 | 109,875,137,469 | 0.50% | 7,606,817,948 | 0.06% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| gle | 3,440,050,457 | 296,758,394,210 | 1.27% | 6,284,109,250 | 0.05% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| mlt | 4,380,772,012 | 134,951,009,011 | 0.59% | 4,412,768,991 | 0.03% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| nno | 2,488,197,640 | 90,132,244,358 | 0.39% | 3,538,386,588 | 0.03% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |

**Subtotal A** — native: 15,290,657,302,989 · synthetic: 4,597,689,519,550 · source: 19,888,346,822,539 (84.38%) · release: 11,993,125,887,682 (89.48%)

### Section B — Other

| Dataset | Native source | Synthetic source | % of source | Release tokens | % of release | Datasets |
|:---|---:|---:|---:|---:|---:|:---|
| common-pile-stackv2-0.1 | 2,928,642,538,533 | — | 12.43% | 709,743,563,645 | 5.30% | common-pile-stackv2-0.1 |
| megamath-0.0.0 | 318,049,344,118 | — | 1.35% | 318,049,344,118 | 2.37% | megamath-0.0.0 |
| starcoder-0.0.0 | 276,861,687,159 | — | 1.17% | 251,955,595,123 | 1.88% | starcoder-0.0.0 |
| common-pile-stackv2-edu-0.1 | 80,134,962,542 | — | 0.34% | 80,060,187,066 | 0.60% | common-pile-stackv2-edu-0.1 |
| swallow-code-2.0 | 62,716,070,265 | — | 0.27% | 50,172,253,076 | 0.37% | swallow-code-2.0 |
| dolmino-mix-100b-1125 | 48,542,080,162 | — | 0.21% | 48,542,080,162 | 0.36% | dolmino-mix-100b-1125 |
| finemath-0.0.0 | 39,371,426,362 | — | 0.17% | 39,371,426,362 | 0.29% | finemath-0.0.0 |
| swallow-math-2.0 | 35,041,872,140 | — | 0.15% | 35,041,872,140 | 0.26% | swallow-math-2.0 |
| agenttrove-0.0 | 20,220,696,106 | — | 0.09% | 20,220,696,106 | 0.15% | agenttrove-0.0 |
| openwebmath-0.0.0 | 13,793,650,775 | — | 0.06% | 13,793,650,775 | 0.10% | openwebmath-0.0.0 |
| openthoughts-3 | 20,203,691,733 | — | 0.09% | — | — | openthoughts-3 |
| nemotron-mind-0.0 | 132,299,120,775 | — | 0.56% | — | — | nemotron-mind-0.0 |

**Subtotal B** — native: 3,975,877,140,670 · synthetic: — · source: 3,975,877,140,670 (16.87%) · release: 1,566,950,668,573 (11.69%)

### Unique source tokens: 23,5TT
### Unique release tokens: 13,4TT


## Background Documents

+ [Overall roadmap](https://docs.google.com/spreadsheets/d/1CbuQfx8ZJVw1TaYXeGGkm17U4j5T_RrD9i0a2tYC5Y8/edit?usp=sharing)
+ [training data sources](https://github.com/OpenEuroLLM/task4.3/blob/main/flagship-data-sources.md)
+ [pretraining benchmarks](https://docs.google.com/document/d/1lpKgHLgBK8usB6RZmD_8yS0m-eUSuuxJ3DtV7sGeL2g/edit?usp=sharing)
+ [posttraining benchmarks](https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/rhoosmej4in99mujt7yhik9hmc)
+ [task-internal schedule](https://docs.google.com/spreadsheets/d/1CbuQfx8ZJVw1TaYXeGGkm17U4j5T_RrD9i0a2tYC5Y8/edit?usp=sharing)
