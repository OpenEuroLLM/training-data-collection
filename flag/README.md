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

* ❓ - undecided
* 🏃‍➡️ - running
* ✅ - complete
* 🔁 - Need to rerun
* ➕ - included
* ➖ - inapplicable
* 🫷 - blocked
* 💣 - problematic

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing  |  Tokens   | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:-----:|:--------:|:---------:|:----:|:----------:|
| dclm-1.0                             |  1 | 1 | ✅ | ✅ | ➖ | ✅ | ✅ | ➖ | ✅   | 🏃‍➡️ | | |
| finepdfs-1.0.0 (eng_Latn)            |  1 | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🏃‍🕛️ |           | | |
| finepdfs-edu-1.0.0 (eng_Latn)        |  1 | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🏃‍🕛️ |           | | |
| finephrase-0.0.0                     |  4 | 4 | ✅️ | ✅️️ | ➖ | 🏃‍➡️ | ❓ | ➖ |      |           | | |
| hplt-4.0 (eng_Latn)                  |  3 | 3 | ✅️️ | ✅️ | ➖ | 🏃‍➡️ | ✅ | ✅ |      |           | | |
| nemotron-cc-1.0                      |  3 | 1 | ✅ | ✅️ | ✅ | ✅ | ✅ | ✅ | 🏃‍➡️   |           | | |
| nemotron-mind-0.0                    |  7 | 4 | ✅️ | ✅️️ | ➖ | 🏃‍➡️ | ❓ | ➖ |      |           | | |
| nemotron-pretraining-specialized-1.0 |  6 | 4 | ✅️ | ✅️️️ | ➖ | 🏃‍➡️ | ❓ | ➖ |      |           | | |
| nemotron-pretraining-specialized-1.1 |  5 | 4 | ✅️ | ✅️️️ | ➖ | 🏃‍➡️ | ❓ | ➖ |      |           | | |
| mixture-vitae-1.0                    | 13 | 4 | ✅ | ✅ | ✅ |    | ❓ | ✅ |      |           | | |
| olmo-mix-1124                        |  2 | 4 | ✅ | ✅️️️ | ➖ |    | ➖ | ➖ |      |           | | |

## Multilingual Source Datasets

| Path                                                                                                   | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing | Tokens | Copy | Validation |
|--------------------------------------------------------------------------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:-----:|:-------:|:-----:|:---:|:---------:|
| finepdfs-1.0.0 (multilingual)                                                                          | 36 | 2 | ✅ | ✅️ | ✅️ | ✅ | ✅ | ✅ | 🏃‍🕛️ | | | |
| finepdfs-edu-1.0.0 (multilingual)                                                                      | 35 | 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🏃‍➡️🕛 | | | |
| [~~fineweb2-hq-1.0.0~~](https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/ik3a1eo1jjra5b4xrpy38rq5se) | 13 | 3 | ✅️ | ✅️ | ✅️ | ✅ | ✅ | ✅ |➖|➖|➖|➖|
| finewiki-0.0.0                                                                                         | 36 | 3 | ✅️ | ✅️ | ✅ | ✅ | ➖ | ✅ | 🏃‍➡️🕛 | | | |
| hplt-4.0                                                                                               | 64 | 1 | ✅ ‍| ✅️️ | ➕ | ✅ | ✅ | ✅ |     | | | |
| nemotron-cc-opus-1.1                                                                                   | 20 | 3 | ✅‍ | ✅️ | ➖ | ➖ | ✅ | ➖ | 🏃‍➡️🕛 | | | |
| nemotron-cc-tower+-0.1                                                                                 | 16 | 3 | ✅ | ✅️️ | ➖ | ➖ | ✅ | ➖ | 🏃‍➡️🕛 | | | |

## Code and Math Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing |  Tokens   | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:------:|:----:|:---------:|:----:|:----------:|
| common-pile-stackv2-0.1              |     1 | 3 | ✅ | ✅️️️ | ✅️ | ➖ | ➖ | ✅️ |  🏃‍🕛 |           |    |
| common-pile-stackv2-edu-0.1          |     1 | 3 | ✅️ | ✅️️ | ✅️ | ➖ | ➖ | ✅️ |   ✅️ | ✅️(80BT)  |    |
| dolmino-mix-100b-1125                |     9 | 5 | ✅ | ✅️️️ | ➖ | ➖ | ➖ | ➖ |  ✅️️️ | 🏃‍➡️ |    |
| finemath-0.0.0                       |     1 | 4 | ✅ | ✅️ | ➖ | ➖ | ➖ | ➖ |  ✅️️️ |🏃‍|    |
| megamath-0.0.0                       |     1 | 4 | ✅ | ✅️️ | ➖ | ➖ | ➖ | ➖ |  ✅️️️ |🏃‍|    |
| openwebmath-0.0.0                    |     1 | 5 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ |   ✅️ | ✅️(14BT)  |    |
| starcoder-0.0.0                      |     1 | 4 | ✅ | ✅️ | ➖ | ➖ | ➖ | ➖ |   ✅️ | 🏃‍➡️ |    |
| swallow-code-2.0                     |     1 | 4 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ |   ✅️ | ✅️(50BT)  |    |
| swallow-math-2.0                     |     1 | 4 | ✅️ | ✅️️ | ➖ | ➖ | ➖ | ➖ | ✅️   |🏃‍|    |
| ~~the-stack-1.2~~                    | ~~1~~ |   | ✅️️ | ✅️️️ | ➖ | ➖ | ➖ | ➖ |    ➖ |     ➖     | ➖ |

## Parallel Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing | Tokens | Copy | Validation |
|--------------------------------------|:-----:|:-:|:-----:|:-----:|:--------:|:-------------:|:---:|:------:|:-------:|:------:|:----:|:----------:|
| fineopus-filtered-0.4                |    41 | 5 | ✅ | ✅️ | ➖ | |   | ➖ | | | | |
| dochplt-3.1                          |    ?  |   | ✅️️️ | ✅️ | ➖ | |   | ➖ | | | | |

## Reasoning Datasets

| Path                                 | Parts | # | Data | Counts | Propella | Contamination | PII | Sample | Packing | Tokens | Copy | Validation |
|--------------------------------------|:-----:|:-:|:----:|:------:|:--------:|:-------------:|:---:|:------:|:-------:|:------:|:----:|:----------:|
| agenttrove-0.0                       |     1 |   | ✅️️ | ✅️️️ | ➖ | | ➖ | ➖ | | | | |
| openthoughts-3                       |     1 |   | 🏃‍➡️ |    | ➖ | | ➖ | ➖ | | | | |

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

## Tokenization: Nemotron tokanization
Instructions on how to run tokenization are found in 
[tokenization repository](https://github.com/mrunesson/tokenizer/tree/flag/flag-tokenization).
TODO: Will be merged into https://github.com/openEuroLLM/tokenizer
