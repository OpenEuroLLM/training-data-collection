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

| Path                   | Data | Propella | Contamination | PII | Metadata | Packing | Tokens | Copy | Validation |
|------------------------|:----:|:--------:|:-------------:|:---:|:--------:|:-------:|:------:|:----:|:----------:|
| dclm-1.0                             | ✅ | ➖ | | | | | | |
| hplt-4.0 AB                          | 🏃‍➡️ | ➖ | | | | | | |
| hplt-4.0 CC New                      | 🏃‍➡️ | ➖ | | | | | | |
| finephrase-0.0.0                     | 🏃‍➡️ | ➖ | | | | | | |
| finepdfs-1.0.0                       | ✅ | 🏃‍➡️ | | | | | | |
| finepdfs-edu-1.0.0                   | ✅ | ❓ | | | | | | |
| nemotron-cc-1.0                      | ✅ | 🏃‍➡️ | | | | | | |
| nemotron-mind-0.0                    | 🏃‍➡️ | ➖ | | | | | | |
| nemotron-pretraining-specialized-1.0 | 🏃‍➡️ | ➖ | | | | | | |
| nemotron-pretraining-specialized-1.1 | 🏃‍➡️ | ➖ | | | | | | |
| mixture-vitae-1.0                    | ✅ | ➖ | | | | | | |
| olmo-mix-1124                        | ✅ | ➖ | | | | | | |

## Annotations: Contamination Detection

## Annotations: PII Detection

## Filtering and Up-Sampling

## Packing: Putting it all Together
