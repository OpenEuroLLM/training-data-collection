# OpenEuroLLM Training Data Collection for the “Flag” Cycle

This directory collects and documents the training data mix for the first
“flagship” development cycle, codenamed `flag`.

## Background Documents

+ [Overall roadmap](https://docs.google.com/spreadsheets/d/1CbuQfx8ZJVw1TaYXeGGkm17U4j5T_RrD9i0a2tYC5Y8/edit?usp=sharing)
+ [training data sources](https://github.com/OpenEuroLLM/task4.3/blob/main/flagship-data-sources.md)
+ [pretraining benchmarks](https://docs.google.com/document/d/1lpKgHLgBK8usB6RZmD_8yS0m-eUSuuxJ3DtV7sGeL2g/edit?usp=sharing)
+ [posttraining benchmarks](https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/rhoosmej4in99mujt7yhik9hmc)
+ [task-internal schedule](https://docs.google.com/spreadsheets/d/1CbuQfx8ZJVw1TaYXeGGkm17U4j5T_RrD9i0a2tYC5Y8/edit?usp=sharing)

Legend:
* ✅ - Done
* 🏃‍➡️ - Running
* ➖ - No need to run
* 🫷 - Wait for previous
* 💣 - Problem

## English Source Datasets

| Path                                 | Parts | Data | Counts | Propella | Contamination | PII | Metadata | Packing | Tokens | Copy | Validation |
|--------------------------------------|:-----:|:----:|:------:|:--------:|:-------------:|:---:|:--------:|:-------:|:------:|:----:|:----------:|
| dclm-1.0                             | 1 | ✅ | ➖ | | | | | | | |
| hplt-4.0 CC+ (eng_Latn)              | 1 | 🏃‍➡️ | ➖ | | | | | | | |
| hplt-4.0 IA (eng_Latn)               | 1 | 🏃‍➡️ | ➖ | | | | | | | |
| finephrase-0.0.0                     | 4 | 🏃‍➡️ | ➖ | | | | | | | |
| finepdfs-1.0.0 (eng_Latn)            | 1 | ✅ | ✅ | | | | | | | |
| finepdfs-edu-1.0.0 (eng_Latn)        | 1 | ✅ | 🏃‍➡️ | | | | | | | |
| nemotron-cc-1.0                      | 3 | ✅ | 🏃‍➡️ | | | | | | | |
| nemotron-mind-0.0                    | ? | 🏃‍➡️ | ➖ | | | | | | | |
| nemotron-pretraining-specialized-1.0 | ? | 🏃‍➡️ | ➖ | | | | | | | |
| nemotron-pretraining-specialized-1.1 | ? | 🏃‍➡️ | ➖ | | | | | | | |
| mixture-vitae-1.0                    | ? | ✅ | 🏃‍➡️ | | | | | | | |
| olmo-mix-1124                        | 3 | ✅ | ➖ | | | | | | | |

## Multilingual Source Datasets

| Path                                 | Parts | Data | Counts | Propella | Contamination | PII | Metadata | Packing | Tokens | Copy | Validation |
|--------------------------------------|:-----:|:----:|:------:|:--------:|:-------------:|:---:|:--------:|:-------:|:------:|:----:|:----------:|
| finepdfs-1.0.0 (multilingual)     | 37 | ✅ | ✅️ | | | | | | | |
| finepdfs-edu-1.0.0 (multilingual) | 36 | ✅ | 🏃‍➡️ | | | | | | | |
| fineweb2-hq-1.0.0                 | 20 | 🏃‍➡️ | 🫷 | | | | | | | |
| finewiki-0-0-0                    | 36 | ✅️ | 🫷 | | | | | | | |
| hplt-4.0                          | 39 | 🏃‍➡️ | ➖ | | | | | | | |
| nemotron-cc-opus-1.1              | 37 | ✅‍ | ➖ | | | | | | | |
| nemotron-cc-tower+-0.1            | 16 | ✅ | ➖ | | | | | | | |

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
  - >=:
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
