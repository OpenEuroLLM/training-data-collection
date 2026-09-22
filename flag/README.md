# OpenEuroLLM Training Data Collection for the “Flag” Cycle

This directory collects and documents the training data mix for the first
“flagship” development cycle, codenamed `flag`.

## Background Documents

+ [Overall roadmap](https://docs.google.com/spreadsheets/d/1CbuQfx8ZJVw1TaYXeGGkm17U4j5T_RrD9i0a2tYC5Y8/edit?usp=sharing)
+ [training data sources](https://github.com/OpenEuroLLM/task4.3/blob/main/flagship-data-sources.md)
+ [pretraining benchmarks](https://docs.google.com/document/d/1lpKgHLgBK8usB6RZmD_8yS0m-eUSuuxJ3DtV7sGeL2g/edit?usp=sharing)
+ [posttraining benchmarks](https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/rhoosmej4in99mujt7yhik9hmc)
+ [task-internal schedule](https://docs.google.com/spreadsheets/d/1CbuQfx8ZJVw1TaYXeGGkm17U4j5T_RrD9i0a2tYC5Y8/edit?usp=sharing)


## English Source Datasets

**Legend**

* ✅ - complete
* ➕ - included
* ➖ - inapplicable

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample |     Packing      |        Tokens        | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:-----:|:----------------:|:--------------------:|:----:|:----------:|
| dclm-1.0                             |  1 | 1 | ✅ | ✅ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅(3.88TT)           | ✅ | ✅ |
| finepdfs-1.0.0 (eng_Latn)            |  1 | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(2.36T inc multi)  | ✅ | ✅ |
| finepdfs-edu-1.0.0 (eng_Latn)        |  1 | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(279BT inc multi)  | ✅ | ✅ |
| finephrase-0.0.0                     |  4 | 4 | ✅️ | ✅️️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅                   | ✅ | ✅ |
| hplt-4.0 (eng_Latn)                  |  3 | 3 | ✅️️ | ✅️ | ➖ | ✅ | ✅ | ✅ | ✅ | ✅‍(3.46TT inc multi) | ✅ | ✅ |
| nemotron-cc-1.0                      |  3 | 1 | ✅ | ✅️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(2.91TT)           | ✅ | ✅ |
| nemotron-mind-0.0                    |  7 | 4 | ✅️ | ✅️️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅                    | ✅ | ✅ |
| nemotron-pretraining-specialized-1.0 |  6 | 4 | ✅️ | ✅️️️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅(297BT)            | ✅ | ✅ |
| nemotron-pretraining-specialized-1.1 |  5 | 4 | ✅️ | ✅️️️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅(10BT)             | ✅ | ✅ |
| mixture-vitae-1.0                    | 13 | 4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(429BT)            | ✅ | ✅ |
| olmo-mix-1124                        |  2 | 4 | ✅ | ✅️️️ | ➖ | ✅ | ➖ | ➖ | ✅ | ✅(83BT)             | ✅ | ✅ |

## Multilingual Source Datasets

| Path                                                                                                   | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing |      Tokens       | Copy | Validation |
|--------------------------------------------------------------------------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:-----:|:-------:|:-----------------:|:---:|:---------:|
| finepdfs-1.0.0 (multilingual)     | 36     | 2 | ✅ | ✅️ | ✅️ | ✅ | ✅ | ✅ | ✅ | ✅(2.36T inc eng)  | ✅ | ✅ |
| finepdfs-edu-1.0.0 (multilingual) | 35     | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(279BT inc eng)  | ✅ | ✅ |
| ~~fineweb2-hq-1.0.0~~             | ~~13~~ |   | ✅️ | ✅️ | ✅️ | ✅ | ✅ | ✅ | ➖ |         ➖         | ➖ | ➖ |
| finewiki-0.0.0                    | 34     | 3 | ✅️ | ✅️ | ✅ | ✅ | ➖ | ✅ | ✅ | ✅(25BT)           | ✅ | ✅ |
| hplt-4.0                          | 63     | 1 | ✅ ‍| ✅️️ | ➕ | ✅ | ✅ | ✅ | ✅ | ✅(3.46TT inc eng) | ✅ | ✅ |
| nemotron-cc-opus-1.1              | 20     | 3 | ✅‍ | ✅️ | ➖ | ➖ | ✅ | ➖ | ✅ | ✅(142BT)          | ✅ | ✅ |
| nemotron-cc-tower+-0.1            | 16     | 3 | ✅ | ✅️️ | ➖ | ➖ | ✅ | ➖ | ✅ | ✅(541BT)          | ✅ | ✅ |

## Code and Math Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing |  Tokens   | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:------:|:----:|:---------:|:----:|:----------:|
| common-pile-stackv2-0.1              |     1 | 3 | ✅ | ✅️️️ | ✅️ | ➖ | ➖ | ✅️ | ✅️ | ✅️(710B)  |    ✅ | ✅ |
| common-pile-stackv2-edu-0.1          |     1 | 3 | ✅️ | ✅️️ | ✅️ | ➖ | ➖ | ✅️ | ✅️ | ✅️(80BT)  |    ✅ | ✅ |
| dolmino-mix-100b-1125                |     9 | 5 | ✅ | ✅️️️ | ➖ | ➖ | ➖ | ➖ | ✅️️️ | ✅️(49BT)  |    ✅ | ✅ |
| finemath-0.0.0                       |     1 | 4 | ✅ | ✅️ | ➖ | ➖ | ➖ | ➖ | ✅️️️ | ✅️(40BT)  |    ✅ | ✅ |
| megamath-0.0.0                       |     1 | 4 | ✅ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️️️ | ✅️(318BT) |    ✅ | ✅ |
| openwebmath-0.0.0                    |     1 | 5 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️ | ✅️(14BT)  |    ✅ | ✅ |
| starcoder-0.0.0                      |     1 | 4 | ✅ | ✅️ | ➖ | ➖ | ➖ | ➖ | ✅️ | ✅️(252BT) |    ✅ | ✅ |
| swallow-code-2.0                     |     1 | 4 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️ | ✅️(50BT)  |    ✅ | ✅ |
| swallow-math-2.0                     |     1 | 4 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️ | ✅️(35BT)  |    ✅ | ✅ |
| ~~the-stack-1.2~~                    | ~~1~~ |   | ✅️️ | ✅️️️ | ➖ | ➖ | ➖ | ➖ | ➖ |     ➖     | ➖ | ➖ |

## Parallel Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample |   Packing   |        Tokens        | Copy | Validation |
|--------------------------------------|:-----:|:-:|:-----:|:-----:|:--------:|:-------------:|:---:|:------:|:-----------:|:--------------------:|:----:|:----------:|
| fineopus-filtered-0.4                |    41 | 5 | ✅ | ✅️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅ | ✅ | ✅ |
| dochplt-3.1                          |    28 | 5 | ✅️️️ | ✅️ | ➖ | ✅ | ✅ | ➖ | ✅ | ✅ | ✅ | ✅ |

## Reasoning Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing |  Tokens  | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:------:|:-------:|:--------:|:----:|:----------:|
| agenttrove-0.0                       |     1 |   | ✅️️ | ✅️️️ | ➖ | ✅ | ➖ | ➖ | ✅ | ✅️(20BT) | ✅ | ✅ |
| openthoughts-3                       |     1 |   | ✅️️ | ✅️️️ | ➖ | ✅ | ➖ | ➖ | ✅ | ✅(20BT)️ | ✅ | ✅ |

## Annotations: Contamination

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

For filtering, one can imagine a tiny specification language, composed
of a small inventory of operators, field identifiers, comparison values,
and boolean connectives.
A match of one or more filter expression will trigger removal of documents,
for example:
```
hplt-low-resource:
  or:
  - in:
      propella-4b.content_safety: [illegal, harmful]
  - =:
      propella-4b.content_quality: unacceptable
  - <=:
      doc_scores.0: 2
  … 
```

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

```
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

## Breakdown

### Section A — Language datasets


| Language | Source tokens | % of source | Release tokens | % of release | Datasets |
|:---|---:|---:|---:|---:|:---|
| eng | 8,363,813,579,783 | 35.64% | 7,028,585,633,677 | 52.44% | dclm-1.0, dochplt-3.1, fineopus-filtered-0.4, finepdfs-edu-1.0.0, finephrase-0.0.0, hplt-4.0, mixture-vitae-1.0, nemotron-cc-1.0, nemotron-pretraining-specialized-1.0, nemotron-pretraining-specialized-1.1 |
| spa | 1,454,442,795,174 | 6.20% | 703,407,614,415 | 5.25% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| fra | 1,309,915,859,886 | 5.58% | 612,435,288,688 | 4.57% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| deu | 1,191,161,841,585 | 5.08% | 512,549,027,676 | 3.82% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| por | 545,054,040,113 | 2.32% | 329,720,018,780 | 2.46% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| ita | 483,388,829,397 | 2.06% | 293,554,844,036 | 2.19% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| pol | 374,117,358,228 | 1.59% | 231,920,445,057 | 1.73% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| nld | 326,620,892,932 | 1.39% | 210,184,896,196 | 1.57% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| ukr | 231,817,943,912 | 0.99% | 169,730,959,314 | 1.27% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| tur | 456,333,742,333 | 1.94% | 169,666,699,693 | 1.27% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| hun | 234,702,676,311 | 1.00% | 166,583,364,465 | 1.24% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| ron | 255,255,942,389 | 1.09% | 162,634,106,230 | 1.21% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| ces | 353,956,567,813 | 1.51% | 156,320,294,889 | 1.17% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| ell | 280,479,750,873 | 1.20% | 140,897,577,579 | 1.05% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| swe | 220,778,476,893 | 0.94% | 132,339,934,790 | 0.99% | fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| fin | 194,442,763,368 | 0.83% | 108,484,370,132 | 0.81% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| dan | 175,783,542,214 | 0.75% | 103,306,513,583 | 0.77% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| bul | 359,445,351,093 | 1.53% | 96,206,587,852 | 0.72% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| slk | 181,083,549,612 | 0.77% | 79,334,698,766 | 0.59% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| nob | 188,831,727,974 | 0.80% | 70,258,869,127 | 0.52% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| cat | 166,964,297,090 | 0.71% | 62,702,501,669 | 0.47% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| lit | 156,343,458,464 | 0.67% | 61,996,865,879 | 0.46% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| hrv | 158,637,179,651 | 0.68% | 59,453,742,635 | 0.44% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| lvs | 207,867,184,092 | 0.89% | 55,007,187,264 | 0.41% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| slv | 148,686,011,016 | 0.63% | 54,837,470,314 | 0.41% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| est | 298,047,733,493 | 1.27% | 51,777,030,894 | 0.39% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| srp | 170,606,931,000 | 0.73% | 50,084,845,041 | 0.37% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| sqi | 194,895,585,883 | 0.83% | 31,525,850,249 | 0.24% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| bos | 120,405,440,138 | 0.51% | 23,991,446,057 | 0.18% | dochplt-3.1, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| mkd | 135,160,107,301 | 0.58% | 16,069,721,881 | 0.12% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| isl | 108,308,019,775 | 0.46% | 15,713,483,734 | 0.12% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |
| eus | 109,341,989,124 | 0.47% | 10,001,914,343 | 0.07% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| glg | 116,827,599,398 | 0.50% | 7,606,817,948 | 0.06% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| gle | 300,198,444,667 | 1.28% | 6,284,109,250 | 0.05% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| mlt | 139,331,781,023 | 0.59% | 4,412,768,991 | 0.03% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, finewiki-0.0.0, hplt-4.0, nemotron-cc-opus-1.1 |
| nno | 92,620,441,998 | 0.39% | 3,538,386,588 | 0.03% | dochplt-3.1, fineopus-filtered-0.4, finepdfs-1.0.0, finepdfs-edu-1.0.0, hplt-4.0, nemotron-cc-tower+-0.1 |

**Subtotal A** — source: 19,805,669,435,996 (84.4%) · release: 11,993,125,887,682 (89.5%)

### Section B — Math, code, reasoning datasets

| Dataset | Source tokens | % of source | Release tokens | % of release | 
|:---|---:|---:|---:|---:|
| common-pile-stackv2-0.1 | 2,928,642,538,533 | 12.48% | 709,743,563,645 | 5.30% | 
| megamath-0.0.0 | 318,049,344,118 | 1.36% | 318,049,344,118 | 2.37% | 
| starcoder-0.0.0 | 276,861,687,159 | 1.18% | 251,955,595,123 | 1.88% | 
| common-pile-stackv2-edu-0.1 | 80,134,962,542 | 0.34% | 80,060,187,066 | 0.60% | 
| swallow-code-2.0 | 62,716,070,265 | 0.27% | 50,172,253,076 | 0.37% | 
| dolmino-mix-100b-1125 | 48,542,080,162 | 0.21% | 48,542,080,162 | 0.36% | 
| finemath-0.0.0 | 39,371,426,362 | 0.17% | 39,371,426,362 | 0.29% | 
| swallow-math-2.0 | 35,041,872,140 | 0.15% | 35,041,872,140 | 0.26% | 
| agenttrove-0.0 | 20,220,696,106 | 0.09% | 20,220,696,106 | 0.15% | 
| openwebmath-0.0.0 | 13,793,650,775 | 0.06% | 13,793,650,775 | 0.10% |
| nemotron-mind-0.0 | 132,299,120,775 | 0.56% | — | — | 

**Subtotal B** — source: 3,955,673,448,937 (16.6%) · release: 1,566,950,668,573 (11.5%)

### Unique source tokens: 23,4TT
### Unique release tokens: 13,4TT
