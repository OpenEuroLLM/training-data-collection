# OpenEuroLLM Training Data Collection for Prelude 9B

This directory documents the training data mix for the first OpenEuroLLM
production model [Prelude 9B](https://huggingface.co/openeurollm/prelude-base),
which was internally codenamed `baby`.
For full transparency and replicability, the full and exact training data
is made publicly available (see below).
Further, the full software stack and exact recipes for training data
preparation are available under open-source licenses.
Additional background information is available as a
[public summary of training content](eu-summary.pdf) according to the
EU AI Act.

Training data preparation was carried out on the EuroHPC supercomputer
[LUMI](https://lumi-supercomputer.eu/).
For project-internal use, select parts of the collection are mirrored to
other EuroHPC systems, viz. the tokenized binary files for training with
Megatron-LM, document and token counts, and MD5 checksums.

+ LUMI: `/scratch/project_465002530/training/collection/baby/`
+ Leonardo: `/leonardo_work/OELLM_prod2026/training/collection/baby/`
+ MareNostrum 5: `/gpfs/projects/ehpc533/training/collection/baby/`


## Data Statistics

Prelude 9B was [pretrained on eight trillion](pretraining.txt) tokens
and [annealed on another two trillion tokens](annealing.txt).
The Prelude base model further has undergone a stage of context extension.
Pretraining drew data for [36 distinct languages](languages.txt) plus some
code and math from the `baby` data collection (this directory).
Conversely, annealing and context extension availed themselves of data
from the newer
[`flag` training data collection](https://github.com/OpenEuroLLM/training-data-collection/blob/main/flag/README.md), which will be published in December 2026.

For Prelude training, the data has undergone
[filtering for benchmark contamination](https://github.com/OpenEuroLLM/decontamination-benchmarks),
[masking of personally identifiable information](https://github.com/OpenEuroLLM/training-data-collection/issues/2)
(PII), and up- and down-sampling towards preset token budgets.
Thus, data statistics distinguish between _source tokens_ (in the original
dataset), _release tokens_ (in the actual OpenEuroLLM training data collection),
and _token budgets_ in individual training phases.
All token counts are in terms of the
[OpenEuroLLM 256k Tokenizer](https://huggingface.co/openeurollm/tokenizer-256k) (`v1`).

The tables below provide high-level breakdowns by languages and dataset parts;
these counts can also be explored interactively and further broken down by
individual data types.
More detailed statistics are available in machine-readable form for
[pretraining](pretraining.csv), and will be provided for annealing and
context extension over the next few weeks.

<details>
<summary><b>Pretraining: Languages</b></summary>

| **Language** | **Source Tokens** | **Release Tokens** | **%**| **Token Budget** | **%** | **Share** |
|--------------|------------------:|-------------------:|-----:|-----------------:|------:|----------:|
| `eng_Latn` | 8,608,247,768,327 | 7,402,695,986,047 | 86.0 | 5,824,000,000,003 | 78.7 | 74.5 |
| `code` | 276,861,687,159 | 276,861,687,159 | 100.0 | 576,000,000,001 | 208.0 | 7.4 |
| `spa_Latn` | 1,027,223,535,454 | 253,364,476,233 | 24.7 | 163,072,000,000 | 64.4 | 2.1 |
| `fra_Latn` | 914,218,948,972 | 181,228,995,955 | 19.8 | 111,912,000,000 | 61.8 | 1.4 |
| `por_Latn` | 525,145,124,161 | 139,754,673,871 | 26.6 | 90,632,000,001 | 64.9 | 1.2 |
| `deu_Latn` | 801,386,790,941 | 140,724,945,459 | 17.6 | 84,800,000,000 | 60.3 | 1.1 |
| `ita_Latn` | 471,700,522,920 | 125,627,646,650 | 26.6 | 80,864,000,000 | 64.4 | 1.0 |
| `pol_Latn` | 354,718,646,334 | 80,567,524,717 | 22.7 | 52,144,000,000 | 64.7 | 0.7 |
| `ell_Grek` | 277,327,057,442 | 77,884,877,234 | 28.1 | 50,200,000,000 | 64.5 | 0.6 |
| `nld_Latn` | 310,459,769,255 | 73,386,420,949 | 23.6 | 47,528,000,000 | 64.8 | 0.6 |
| `tur_Latn` | 284,086,199,602 | 69,581,777,278 | 24.5 | 44,208,000,000 | 63.5 | 0.6 |
| `ron_Latn` | 222,964,472,410 | 60,368,536,567 | 27.1 | 39,056,000,000 | 64.7 | 0.5 |
| `hun_Latn` | 224,266,273,453 | 59,444,927,952 | 26.5 | 38,328,000,000 | 64.5 | 0.5 |
| `ukr_Cyrl` | 207,438,727,178 | 55,868,518,834 | 26.9 | 35,744,000,000 | 64.0 | 0.5 |
| `ces_Latn` | 218,765,925,675 | 53,946,056,543 | 24.7 | 34,616,000,000 | 64.2 | 0.4 |
| `als_Latn` | 187,574,173,212 | 39,944,091,576 | 21.3 | 32,928,000,000 | 82.4 | 0.4 |
| `swe_Latn` | 216,721,533,392 | 51,553,933,988 | 23.8 | 32,912,000,000 | 63.8 | 0.4 |
| `lvs_Latn` | 194,282,618,377 | 47,003,815,714 | 24.2 | 32,408,000,000 | 68.9 | 0.4 |
| `bul_Cyrl` | 175,146,528,951 | 47,852,340,833 | 27.3 | 30,800,000,000 | 64.4 | 0.4 |
| `fin_Latn` | 172,378,237,111 | 44,027,347,287 | 25.5 | 28,320,000,000 | 64.3 | 0.4 |
| `cat_Latn` | 157,622,188,000 | 43,055,139,805 | 27.3 | 27,592,000,000 | 64.1 | 0.4 |
| `srp_Cyrl` | 151,964,197,047 | 33,935,209,113 | 22.3 | 26,672,000,000 | 78.6 | 0.3 |
| `slk_Latn` | 158,842,585,363 | 40,528,859,424 | 25.5 | 26,192,000,000 | 64.6 | 0.3 |
| `hrv_Latn` | 150,546,530,821 | 41,052,070,541 | 27.3 | 26,024,000,000 | 63.4 | 0.3 |
| `dan_Latn` | 156,575,599,369 | 37,616,451,252 | 24.0 | 24,304,000,001 | 64.6 | 0.3 |
| `lit_Latn` | 143,860,020,049 | 37,219,105,967 | 25.9 | 23,952,000,000 | 64.4 | 0.3 |
| `mlt_Latn` | 136,537,234,028 | 19,495,627,869 | 14.3 | 23,856,000,000 | 122.4 | 0.3 |
| `slv_Latn` | 137,822,279,465 | 36,629,487,034 | 26.6 | 23,776,000,000 | 64.9 | 0.3 |
| `bos_Latn` | 133,229,798,052 | 36,978,520,929 | 27.8 | 23,392,000,001 | 63.3 | 0.3 |
| `ekk_Latn` | 135,670,447,596 | 34,731,175,862 | 25.6 | 23,056,000,000 | 66.4 | 0.3 |
| `mkd_Cyrl` | 132,248,796,173 | 22,576,744,999 | 17.1 | 22,432,000,000 | 99.4 | 0.3 |
| `nob_Latn` | 140,025,492,332 | 34,639,138,289 | 24.7 | 21,920,000,000 | 63.3 | 0.3 |
| `glg_Latn` | 114,841,923,549 | 18,965,278,077 | 16.5 | 19,720,000,000 | 104.0 | 0.3 |
| `gle_Latn` | 127,390,409,505 | 15,982,655,821 | 12.5 | 19,328,000,000 | 120.9 | 0.2 |
| `eus_Latn` | 107,581,748,535 | 18,780,787,523 | 17.5 | 18,824,000,000 | 100.2 | 0.2 |
| `isl_Latn` | 105,541,050,627 | 19,662,896,633 | 18.6 | 17,856,000,000 | 90.8 | 0.2 |
| `nno_Latn` | 91,934,814,797 | 13,386,415,601 | 14.6 | 15,952,000,000 | 119.2 | 0.2 |
</details>

<details>
<summary><b>Pretraining: Datasets</b></summary>

| **Dataset** | **Part** | **Source Tokens** | **Release Tokens** | **%**| **Token Budget** | **%** |
|-------------|----------|------------------:|-------------------:|-----:|-----------------:|------:|
| `baby/dclm-1.0` |  | 3,845,395,936,156 | 3,493,015,206,249 | 90.8 | 2,591,976,000,001 | 74.2 |
| `baby/finemath-0.0.0` | `finemath-4plus` | 10,684,233,758 | 10,616,534,301 | 99.4 | 32,000,000,000 | 301.4 |
| `baby/finepdfs-1.0.0` | `als_Latn` | 2,353,482,366 | 2,353,482,366 | 100.0 | 4,888,000,000 | 207.7 |
| `baby/finepdfs-1.0.0` | `bos_Latn` | 5,627,374,893 | 3,999,982,671 | 71.1 | 2,960,000,000 | 74.0 |
| `baby/finepdfs-1.0.0` | `bul_Cyrl` | 7,943,829,750 | 5,338,256,924 | 67.2 | 3,928,000,000 | 73.6 |
| `baby/finepdfs-1.0.0` | `cat_Latn` | 11,084,337,859 | 4,970,649,678 | 44.8 | 3,488,000,000 | 70.2 |
| `baby/finepdfs-1.0.0` | `ces_Latn` | 25,735,988,104 | 4,376,190,666 | 17.0 | 2,272,000,000 | 51.9 |
| `baby/finepdfs-1.0.0` | `dan_Latn` | 11,723,952,358 | 3,881,030,351 | 33.1 | 2,536,000,000 | 65.3 |
| `baby/finepdfs-1.0.0` | `deu_Latn` | 154,018,911,871 | 9,251,990,551 | 6.0 | 120,000,000 | 1.3 |
| `baby/finepdfs-1.0.0` | `ekk_Latn` | 2,912,687,889 | 2,912,687,889 | 100.0 | 3,360,000,000 | 115.4 |
| `baby/finepdfs-1.0.0` | `ell_Grek` | 16,495,925,964 | 8,574,937,950 | 52.0 | 6,160,000,000 | 71.8 |
| `baby/finepdfs-1.0.0` | `eng_Latn` | 1,316,304,236,277 | 1,131,370,937,441 | 86.0 | 851,024,000,001 | 75.2 |
| `baby/finepdfs-1.0.0` | `eus_Latn` | 2,696,420,052 | 2,696,420,052 | 100.0 | 2,776,000,000 | 103.0 |
| `baby/finepdfs-1.0.0` | `fin_Latn` | 13,197,482,048 | 4,492,674,627 | 34.0 | 2,960,000,000 | 65.9 |
| `baby/finepdfs-1.0.0` | `fra_Latn` | 168,589,430,004 | 13,418,209,758 | 8.0 | 3,872,000,000 | 28.9 |
| `baby/finepdfs-1.0.0` | `gle_Latn` | 300,703,698 | 300,703,698 | 100.0 | 2,896,000,000 | 963.1 |
| `baby/finepdfs-1.0.0` | `glg_Latn` | 1,737,198,341 | 1,737,198,341 | 100.0 | 2,968,000,000 | 170.8 |
| `baby/finepdfs-1.0.0` | `hrv_Latn` | 10,440,955,240 | 4,171,379,082 | 40.0 | 2,864,000,000 | 68.7 |
| `baby/finepdfs-1.0.0` | `hun_Latn` | 28,761,473,161 | 4,318,410,781 | 15.0 | 2,240,000,000 | 51.9 |
| `baby/finepdfs-1.0.0` | `isl_Latn` | 3,125,767,392 | 3,125,767,392 | 100.0 | 2,656,000,000 | 85.0 |
| `baby/finepdfs-1.0.0` | `ita_Latn` | 81,555,508,409 | 10,568,898,395 | 13.0 | 4,768,000,000 | 45.1 |
| `baby/finepdfs-1.0.0` | `lit_Latn` | 5,341,006,388 | 4,236,671,358 | 79.3 | 3,128,000,000 | 73.8 |
| `baby/finepdfs-1.0.0` | `lvs_Latn` | 4,229,372,445 | 4,229,372,445 | 100.0 | 4,736,000,000 | 112.0 |
| `baby/finepdfs-1.0.0` | `mkd_Cyrl` | 1,655,260,079 | 1,655,260,079 | 100.0 | 3,376,000,000 | 204.0 |
| `baby/finepdfs-1.0.0` | `mlt_Latn` | 737,732,814 | 737,732,814 | 100.0 | 3,736,000,000 | 506.4 |
| `baby/finepdfs-1.0.0` | `nld_Latn` | 43,632,511,070 | 6,974,685,720 | 16.0 | 3,680,000,000 | 52.8 |
| `baby/finepdfs-1.0.0` | `nno_Latn` | 340,874,944 | 340,874,944 | 100.0 | 2,520,000,000 | 739.3 |
| `baby/finepdfs-1.0.0` | `nob_Latn` | 9,974,679,166 | 3,572,054,890 | 35.8 | 2,464,000,000 | 69.0 |
| `baby/finepdfs-1.0.0` | `pol_Latn` | 41,724,854,569 | 4,967,277,451 | 11.9 | 2,320,000,000 | 46.7 |
| `baby/finepdfs-1.0.0` | `por_Latn` | 94,299,880,209 | 10,196,322,891 | 10.8 | 4,224,000,001 | 41.4 |
| `baby/finepdfs-1.0.0` | `ron_Latn` | 20,365,874,849 | 4,501,111,002 | 22.1 | 2,696,000,000 | 59.9 |
| `baby/finepdfs-1.0.0` | `slk_Latn` | 10,722,613,075 | 3,982,747,128 | 37.1 | 2,720,000,000 | 68.3 |
| `baby/finepdfs-1.0.0` | `slv_Latn` | 7,058,209,834 | 4,519,441,551 | 64.0 | 3,312,000,000 | 73.3 |
| `baby/finepdfs-1.0.0` | `spa_Latn` | 214,982,410,543 | 14,906,029,302 | 6.9 | 3,320,000,000 | 22.3 |
| `baby/finepdfs-1.0.0` | `srp_Cyrl` | 10,096,061,037 | 3,931,458,254 | 38.9 | 2,728,000,000 | 69.4 |
| `baby/finepdfs-1.0.0` | `swe_Latn` | 21,917,786,744 | 4,580,527,164 | 20.9 | 2,648,000,000 | 57.8 |
| `baby/finepdfs-1.0.0` | `tur_Latn` | 15,429,740,155 | 7,224,451,098 | 46.8 | 5,112,000,000 | 70.8 |
| `baby/finepdfs-1.0.0` | `ukr_Cyrl` | 24,556,069,044 | 3,677,449,138 | 15.0 | 1,896,000,000 | 51.6 |
| `baby/finepdfs-edu-1.0.0` | `als_Latn` | 472,332,224 | 472,318,823 | 100.0 | 376,000,000 | 79.6 |
| `baby/finepdfs-edu-1.0.0` | `bos_Latn` | 981,965,136 | 981,906,549 | 100.0 | 784,000,000 | 79.8 |
| `baby/finepdfs-edu-1.0.0` | `bul_Cyrl` | 1,245,739,246 | 1,245,658,103 | 100.0 | 1,000,000,000 | 80.3 |
| `baby/finepdfs-edu-1.0.0` | `cat_Latn` | 1,148,874,840 | 1,148,760,642 | 100.0 | 920,000,000 | 80.1 |
| `baby/finepdfs-edu-1.0.0` | `ces_Latn` | 4,076,220,329 | 4,075,729,681 | 100.0 | 3,264,000,000 | 80.1 |
| `baby/finepdfs-edu-1.0.0` | `dan_Latn` | 1,685,264,681 | 1,685,048,727 | 100.0 | 1,352,000,000 | 80.2 |
| `baby/finepdfs-edu-1.0.0` | `deu_Latn` | 16,814,852,514 | 16,811,365,622 | 100.0 | 13,448,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `ekk_Latn` | 406,649,970 | 406,620,025 | 100.0 | 328,000,000 | 80.7 |
| `baby/finepdfs-edu-1.0.0` | `ell_Grek` | 2,338,140,100 | 2,338,025,715 | 100.0 | 1,872,000,000 | 80.1 |
| `baby/finepdfs-edu-1.0.0` | `eng_Latn` | 141,839,278,641 | 141,823,476,237 | 100.0 | 113,472,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `eus_Latn` | 295,150,093 | 295,128,097 | 100.0 | 240,000,000 | 81.3 |
| `baby/finepdfs-edu-1.0.0` | `fin_Latn` | 1,960,226,158 | 1,960,054,642 | 100.0 | 1,568,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `fra_Latn` | 17,538,489,293 | 17,536,229,598 | 100.0 | 14,032,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `glg_Latn` | 235,935,307 | 235,918,227 | 100.0 | 192,000,000 | 81.4 |
| `baby/finepdfs-edu-1.0.0` | `hrv_Latn` | 1,631,281,189 | 1,631,173,114 | 100.0 | 1,304,000,000 | 79.9 |
| `baby/finepdfs-edu-1.0.0` | `hun_Latn` | 4,870,661,193 | 4,870,393,233 | 100.0 | 3,896,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `isl_Latn` | 249,999,161 | 249,974,399 | 100.0 | 200,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `ita_Latn` | 10,213,000,226 | 10,211,705,449 | 100.0 | 8,168,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `lit_Latn` | 877,919,983 | 877,866,294 | 100.0 | 704,000,000 | 80.2 |
| `baby/finepdfs-edu-1.0.0` | `lvs_Latn` | 556,807,151 | 556,754,028 | 100.0 | 448,000,000 | 80.5 |
| `baby/finepdfs-edu-1.0.0` | `mkd_Cyrl` | 265,851,572 | 265,841,124 | 100.0 | 216,000,000 | 81.3 |
| `baby/finepdfs-edu-1.0.0` | `mlt_Latn` | 96,357,755 | 96,353,648 | 100.0 | 80,000,000 | 83.0 |
| `baby/finepdfs-edu-1.0.0` | `nld_Latn` | 4,900,246,544 | 4,899,584,616 | 100.0 | 3,920,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `nno_Latn` | 41,136,949 | 41,133,601 | 100.0 | 32,000,000 | 77.8 |
| `baby/finepdfs-edu-1.0.0` | `nob_Latn` | 1,300,940,922 | 1,300,810,558 | 100.0 | 1,040,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `pol_Latn` | 7,533,696,810 | 7,533,155,804 | 100.0 | 6,024,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `por_Latn` | 12,838,655,867 | 12,837,399,189 | 100.0 | 10,272,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `ron_Latn` | 4,438,041,427 | 4,437,834,181 | 100.0 | 3,552,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `slk_Latn` | 1,842,001,862 | 1,841,843,297 | 100.0 | 1,472,000,000 | 79.9 |
| `baby/finepdfs-edu-1.0.0` | `slv_Latn` | 617,331,653 | 617,268,590 | 100.0 | 496,000,000 | 80.4 |
| `baby/finepdfs-edu-1.0.0` | `spa_Latn` | 28,472,950,718 | 28,471,094,450 | 100.0 | 22,776,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `srp_Cyrl` | 1,921,150,029 | 1,921,081,318 | 100.0 | 1,536,000,000 | 80.0 |
| `baby/finepdfs-edu-1.0.0` | `swe_Latn` | 3,274,257,693 | 3,273,919,321 | 100.0 | 2,616,000,000 | 79.9 |
| `baby/finepdfs-edu-1.0.0` | `tur_Latn` | 2,447,914,948 | 2,447,801,974 | 100.0 | 1,960,000,000 | 80.1 |
| `baby/finepdfs-edu-1.0.0` | `ukr_Cyrl` | 4,784,078,683 | 4,783,929,387 | 100.0 | 3,824,000,000 | 79.9 |
| `baby/hplt-3.0` | `als_Latn` | 10,529,092,443 | 12,735,389,362 | 121.0 | 16,464,000,000 | 129.3 |
| `baby/hplt-3.0` | `bos_Latn` | 27,695,837,667 | 16,161,519,161 | 58.4 | 11,696,000,000 | 72.4 |
| `baby/hplt-3.0` | `bul_Cyrl` | 42,713,367,493 | 21,564,996,135 | 50.5 | 15,400,000,000 | 71.4 |
| `baby/hplt-3.0` | `cat_Latn` | 21,035,306,449 | 18,286,495,183 | 86.9 | 13,800,000,000 | 75.5 |
| `baby/hplt-3.0` | `ces_Latn` | 93,521,314,847 | 25,468,238,167 | 27.2 | 17,312,000,000 | 68.0 |
| `baby/hplt-3.0` | `dan_Latn` | 55,465,847,872 | 17,141,293,788 | 30.9 | 12,152,000,000 | 70.9 |
| `baby/hplt-3.0` | `deu_Latn` | 548,693,366,012 | 73,753,387,702 | 13.4 | 42,400,000,000 | 57.5 |
| `baby/hplt-3.0` | `ekk_Latn` | 17,670,864,848 | 15,367,416,308 | 87.0 | 11,528,000,000 | 75.0 |
| `baby/hplt-3.0` | `ell_Grek` | 103,562,684,310 | 37,558,069,994 | 36.3 | 25,104,000,000 | 66.8 |
| `baby/hplt-3.0` | `eus_Latn` | 2,537,717,669 | 2,524,688,658 | 99.5 | 9,408,000,000 | 372.6 |
| `baby/hplt-3.0` | `fin_Latn` | 63,971,845,965 | 20,801,858,025 | 32.5 | 14,160,000,000 | 68.1 |
| `baby/hplt-3.0` | `fra_Latn` | 625,713,569,595 | 97,075,568,612 | 15.5 | 55,960,000,000 | 57.6 |
| `baby/hplt-3.0` | `gle_Latn` | 827,777,248 | 540,275,521 | 65.3 | 9,664,000,000 | 1788.7 |
| `baby/hplt-3.0` | `glg_Latn` | 2,993,652,432 | 2,714,057,143 | 90.7 | 9,856,000,000 | 363.1 |
| `baby/hplt-3.0` | `hrv_Latn` | 30,263,415,562 | 17,945,430,519 | 59.3 | 13,008,000,000 | 72.5 |
| `baby/hplt-3.0` | `hun_Latn` | 90,780,586,862 | 28,297,539,442 | 31.2 | 19,160,000,000 | 67.7 |
| `baby/hplt-3.0` | `isl_Latn` | 4,816,712,669 | 3,646,579,138 | 75.7 | 8,928,000,000 | 244.8 |
| `baby/hplt-3.0` | `ita_Latn` | 297,646,358,391 | 66,197,515,208 | 22.2 | 40,432,000,000 | 61.1 |
| `baby/hplt-3.0` | `lit_Latn` | 22,728,917,285 | 16,026,793,669 | 70.5 | 11,976,000,000 | 74.7 |
| `baby/hplt-3.0` | `lvs_Latn` | 18,704,139,033 | 18,321,525,857 | 98.0 | 16,208,000,000 | 88.5 |
| `baby/hplt-3.0` | `mkd_Cyrl` | 4,808,723,524 | 4,346,615,370 | 90.4 | 11,216,000,000 | 258.0 |
| `baby/hplt-3.0` | `mlt_Latn` | 752,134,448 | 1,135,757,682 | 151.0 | 11,928,000,000 | 1050.2 |
| `baby/hplt-3.0` | `nld_Latn` | 168,278,087,959 | 36,248,296,138 | 21.5 | 23,768,000,000 | 65.6 |
| `baby/hplt-3.0` | `nno_Latn` | 1,420,558,546 | 1,292,495,298 | 91.0 | 7,976,000,000 | 617.1 |
| `baby/hplt-3.0` | `nob_Latn` | 44,588,677,570 | 15,464,897,198 | 34.7 | 10,960,000,000 | 70.9 |
| `baby/hplt-3.0` | `pol_Latn` | 221,631,136,292 | 41,260,411,594 | 18.6 | 26,072,000,000 | 63.2 |
| `baby/hplt-3.0` | `por_Latn` | 327,821,314,241 | 73,454,333,231 | 22.4 | 45,320,000,000 | 61.7 |
| `baby/hplt-3.0` | `ron_Latn` | 98,113,338,882 | 29,435,322,570 | 30.0 | 19,528,000,000 | 66.3 |
| `baby/hplt-3.0` | `slk_Latn` | 33,059,373,007 | 17,727,473,039 | 53.6 | 13,096,000,000 | 73.9 |
| `baby/hplt-3.0` | `slv_Latn` | 17,563,684,478 | 15,736,901,668 | 89.6 | 11,888,000,000 | 75.5 |
| `baby/hplt-3.0` | `spa_Latn` | 692,156,868,974 | 135,827,129,796 | 19.6 | 81,536,000,000 | 60.0 |
| `baby/hplt-3.0` | `srp_Cyrl` | 9,022,705,657 | 9,741,790,076 | 108.0 | 13,336,000,000 | 136.9 |
| `baby/hplt-3.0` | `swe_Latn` | 101,847,772,616 | 24,880,794,250 | 24.4 | 16,456,000,000 | 66.1 |
| `baby/hplt-3.0` | `tur_Latn` | 149,012,480,113 | 34,137,289,154 | 22.9 | 22,104,000,000 | 64.8 |
| `baby/hplt-3.0` | `ukr_Cyrl` | 75,602,173,611 | 26,922,263,959 | 35.6 | 17,872,000,000 | 66.4 |
| `baby/megamath-0.0.0` | `megamath-text-code-block` | 48,138,848,818 | 22,617,868,611 | 47.0 | 16,000,000,000 | 70.7 |
| `baby/megamath-0.0.0` | `megamath-web-pro` | 14,183,867,585 | 14,147,469,034 | 99.7 | 16,000,000,000 | 113.1 |
| `baby/nemotron-cc-1.0` | `high/actual` | 565,924,264,266 | 564,839,963,667 | 99.8 | 432,000,000,000 | 76.5 |
| `baby/nemotron-cc-1.0` | `medium/actual` | 2,063,798,579,550 | 1,422,938,530,652 | 68.9 | 1,051,520,000,000 | 73.9 |
| `baby/nemotron-cc-1.0` | `medium-high/actual` | 515,465,110,905 | 514,882,927,275 | 99.9 | 432,008,000,001 | 83.9 |
| `baby/nemotron-cc-opus-1.1` | `bos_Latn` | 98,924,620,356 | 15,835,112,548 | 16.0 | 7,952,000,001 | 50.2 |
| `baby/nemotron-cc-opus-1.1` | `bul_Cyrl` | 123,243,592,462 | 19,703,429,671 | 16.0 | 10,472,000,000 | 53.1 |
| `baby/nemotron-cc-opus-1.1` | `cat_Latn` | 124,353,668,852 | 18,649,234,302 | 15.0 | 9,384,000,000 | 50.3 |
| `baby/nemotron-cc-opus-1.1` | `ces_Latn` | 95,432,402,395 | 20,025,898,029 | 21.0 | 11,768,000,000 | 58.8 |
| `baby/nemotron-cc-opus-1.1` | `ell_Grek` | 154,930,307,068 | 29,413,843,575 | 19.0 | 17,064,000,000 | 58.0 |
| `baby/nemotron-cc-opus-1.1` | `est_Latn` | 114,680,244,889 | 16,044,451,640 | 14.0 | 7,840,000,000 | 48.9 |
| `baby/nemotron-cc-opus-1.1` | `eus_Latn` | 102,052,460,721 | 13,264,550,716 | 13.0 | 6,400,000,000 | 48.2 |
| `baby/nemotron-cc-opus-1.1` | `gle_Latn` | 126,261,928,559 | 15,141,676,602 | 12.0 | 6,768,000,000 | 44.7 |
| `baby/nemotron-cc-opus-1.1` | `glg_Latn` | 109,875,137,469 | 14,278,104,366 | 13.0 | 6,704,000,000 | 47.0 |
| `baby/nemotron-cc-opus-1.1` | `hrv_Latn` | 108,210,878,830 | 17,304,087,826 | 16.0 | 8,848,000,000 | 51.1 |
| `baby/nemotron-cc-opus-1.1` | `lav_Latn` | 170,792,299,748 | 23,896,163,384 | 14.0 | 11,016,000,000 | 46.1 |
| `baby/nemotron-cc-opus-1.1` | `lit_Latn` | 114,912,176,393 | 16,077,774,646 | 14.0 | 8,144,000,000 | 50.7 |
| `baby/nemotron-cc-opus-1.1` | `mkd_Cyrl` | 125,518,960,998 | 16,309,028,426 | 13.0 | 7,624,000,000 | 46.7 |
| `baby/nemotron-cc-opus-1.1` | `mlt_Latn` | 134,951,009,011 | 17,525,783,725 | 13.0 | 8,112,000,000 | 46.3 |
| `baby/nemotron-cc-opus-1.1` | `slk_Latn` | 113,218,597,419 | 16,976,795,960 | 15.0 | 8,904,000,000 | 52.4 |
| `baby/nemotron-cc-opus-1.1` | `slv_Latn` | 112,583,053,500 | 15,755,875,225 | 14.0 | 8,080,000,000 | 51.3 |
| `baby/nemotron-cc-opus-1.1` | `sqi_Latn` | 174,219,266,179 | 24,382,901,025 | 14.0 | 11,200,000,000 | 45.9 |
| `baby/nemotron-cc-opus-1.1` | `srp_Cyrl` | 130,924,280,324 | 18,340,879,465 | 14.0 | 9,072,000,000 | 49.5 |
| `baby/nemotron-cc-opus-1.1` | `tur_Latn` | 117,196,064,386 | 25,772,235,052 | 22.0 | 15,032,000,000 | 58.3 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower72b/deu_Latn` | 81,859,660,544 | 40,908,201,584 | 50.0 | 28,832,000,000 | 70.5 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower72b/fin_Latn` | 93,248,682,940 | 16,772,759,993 | 18.0 | 9,632,000,000 | 57.4 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower72b/ita_Latn` | 82,285,655,894 | 38,649,527,598 | 47.0 | 27,496,000,000 | 71.1 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower72b/spa_Latn` | 91,611,305,219 | 74,160,222,685 | 81.0 | 55,440,000,000 | 74.8 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower72b/swe_Latn` | 89,681,716,339 | 18,818,693,253 | 21.0 | 11,192,000,000 | 59.5 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/dan_Latn` | 87,700,534,458 | 14,909,078,386 | 17.0 | 8,264,000,001 | 55.4 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/fra_Latn` | 102,377,460,080 | 53,198,987,987 | 52.0 | 38,048,000,000 | 71.5 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/hun_Latn` | 99,853,552,237 | 21,958,584,496 | 22.0 | 13,032,000,000 | 59.3 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/isl_Latn` | 97,348,571,405 | 12,640,575,704 | 13.0 | 6,072,000,000 | 48.0 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/nld_Latn` | 93,648,923,682 | 25,263,854,475 | 27.0 | 16,160,000,000 | 64.0 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/nno_Latn` | 90,132,244,358 | 11,711,911,758 | 13.0 | 5,424,000,000 | 46.3 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/nob_Latn` | 84,161,194,674 | 14,301,375,643 | 17.0 | 7,456,000,000 | 52.1 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/pol_Latn` | 83,828,958,663 | 26,806,679,868 | 32.0 | 17,728,000,000 | 66.1 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/por_Latn` | 90,185,273,844 | 43,266,618,560 | 48.0 | 30,816,000,000 | 71.2 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/ron_Latn` | 100,047,217,252 | 21,994,268,814 | 22.0 | 13,280,000,000 | 60.4 |
| `baby/nemotron-cc-tower+-0.1` | `parallel/tower9b/ukr_Cyrl` | 102,496,405,840 | 20,484,876,350 | 20.0 | 12,152,000,000 | 59.3 |
| `baby/olmo-mix-1124` | `arxiv` | 22,325,465,870 | 22,287,607,951 | 99.8 | 73,600,000,000 | 330.2 |
| `baby/olmo-mix-1124` | `pes2o` | 60,351,920,673 | 60,336,371,648 | 100.0 | 202,400,000,000 | 335.5 |
| `baby/olmo-mix-1124` | `wiki` | 3,836,025,828 | 3,819,092,981 | 99.6 | 12,000,000,000 | 314.2 |
| `baby/starcoder-0.0.0` |  | 276,861,687,159 | 276,861,687,159 | 100.0 | 576,000,000,001 | 208.0 |
</details>

## Data Access

To facilitate data auditing, verification, and replication, the full and exact
Prelude training data is redistributed to the general public.
The OpenEuroLLM training data collections build exclusively on generally available
and redistributable source datasets.
However, the consortium does not claim or assign any rights to the majority of
textual content in these datasets, seeing as these predominantly derive from
third-party web crawls.
We solely license the packaging of these data, i.e. contamination and PII
annotations and the file organization of the data collection under the
[Creative Commons CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) license 

Redistribution of the `baby` data collection comprises what are called
the `release/` files (the result of resampling, filtering, masking, and packing),
the underlying `contamination/` and `pii/` annotations, as well as the actual
binary token shards in [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) format.
The total data volume is around 55 terabytes (of which a little more than 70%
corresponds to token binaries).
It is recommended to only retrieve the subset of files necessary for a specific
purpose.
The [full list of available files](manifest.json), including download links
(in the `url` field) is provided in JSONLines format.
For convenience, following is a table of download links for the subset of
`release/` files, i.e. the actual training data shards that were input to
tokenization.

<details>
<summary><b>Pretraining: Downloads</b></summary>

| **URL** | **Size** |
|---------|----------|
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_0_0000.jsonl.zst) | 64,901,832,057 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_1_0000.jsonl.zst) | 64,884,824,400 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_2_0000.jsonl.zst) | 64,887,933,530 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_3_0000.jsonl.zst) | 64,883,746,004 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_4_0000.jsonl.zst) | 64,900,602,394 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_5_0000.jsonl.zst) | 64,907,956,741 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_6_0000.jsonl.zst) | 64,883,072,259 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_7_0000.jsonl.zst) | 64,880,635,419 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_8_0000.jsonl.zst) | 64,889,826,759 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/01_9_0000.jsonl.zst) | 64,880,120,000 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_0_0000.jsonl.zst) | 64,890,931,563 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_1_0000.jsonl.zst) | 64,949,431,186 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_2_0000.jsonl.zst) | 64,878,830,416 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_3_0000.jsonl.zst) | 64,874,301,215 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_4_0000.jsonl.zst) | 64,909,043,718 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_5_0000.jsonl.zst) | 64,896,818,360 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_6_0000.jsonl.zst) | 64,908,706,423 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_7_0000.jsonl.zst) | 64,927,255,839 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_8_0000.jsonl.zst) | 64,908,448,890 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/02_9_0000.jsonl.zst) | 64,870,054,562 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_0_0000.jsonl.zst) | 64,874,889,187 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_1_0000.jsonl.zst) | 42,991,261,674 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_2_0000.jsonl.zst) | 64,932,901,017 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_3_0000.jsonl.zst) | 64,889,342,496 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_4_0000.jsonl.zst) | 64,904,780,455 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_5_0000.jsonl.zst) | 64,895,070,990 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_6_0000.jsonl.zst) | 64,940,663,591 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_7_0000.jsonl.zst) | 64,949,020,741 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_8_0000.jsonl.zst) | 64,969,655,765 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/03_9_0000.jsonl.zst) | 64,884,622,472 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_0_0000.jsonl.zst) | 64,920,807,309 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_1_0000.jsonl.zst) | 64,956,736,081 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_2_0000.jsonl.zst) | 65,012,930,339 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_3_0000.jsonl.zst) | 64,908,640,727 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_4_0000.jsonl.zst) | 64,942,840,328 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_5_0000.jsonl.zst) | 64,979,170,144 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_6_0000.jsonl.zst) | 64,970,142,741 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_7_0000.jsonl.zst) | 64,988,387,330 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_8_0000.jsonl.zst) | 64,944,009,116 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/04_9_0000.jsonl.zst) | 64,941,374,663 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_0_0000.jsonl.zst) | 64,973,591,916 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_1_0000.jsonl.zst) | 65,002,657,784 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_2_0000.jsonl.zst) | 65,008,285,916 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_3_0000.jsonl.zst) | 64,944,337,073 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_4_0000.jsonl.zst) | 64,976,007,582 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_5_0000.jsonl.zst) | 64,978,723,650 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_6_0000.jsonl.zst) | 64,966,645,207 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_7_0000.jsonl.zst) | 64,977,998,937 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_8_0000.jsonl.zst) | 65,029,715,402 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/05_9_0000.jsonl.zst) | 64,988,075,453 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_0_0000.jsonl.zst) | 64,905,270,992 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_1_0000.jsonl.zst) | 64,944,415,423 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_2_0000.jsonl.zst) | 64,936,861,634 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_3_0000.jsonl.zst) | 64,930,748,452 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_4_0000.jsonl.zst) | 64,914,659,849 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_5_0000.jsonl.zst) | 64,907,549,268 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_6_0000.jsonl.zst) | 64,936,538,410 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_7_0000.jsonl.zst) | 64,936,248,267 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_8_0000.jsonl.zst) | 64,924,993,133 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/06_9_0000.jsonl.zst) | 64,946,341,150 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_0_0000.jsonl.zst) | 64,928,274,195 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_1_0000.jsonl.zst) | 64,954,874,025 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_2_0000.jsonl.zst) | 64,945,003,984 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_3_0000.jsonl.zst) | 64,949,714,408 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_4_0000.jsonl.zst) | 64,922,543,227 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_5_0000.jsonl.zst) | 64,970,577,733 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_6_0000.jsonl.zst) | 64,940,572,181 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_7_0000.jsonl.zst) | 64,918,629,380 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_8_0000.jsonl.zst) | 64,936,651,573 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/07_9_0000.jsonl.zst) | 64,955,041,384 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_0_0000.jsonl.zst) | 65,029,460,278 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_1_0000.jsonl.zst) | 64,974,438,343 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_2_0000.jsonl.zst) | 64,990,033,816 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_3_0000.jsonl.zst) | 64,984,429,827 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_4_0000.jsonl.zst) | 64,996,737,081 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_5_0000.jsonl.zst) | 64,993,877,799 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_6_0000.jsonl.zst) | 64,981,277,151 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_7_0000.jsonl.zst) | 65,007,458,152 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_8_0000.jsonl.zst) | 64,978,081,468 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/08_9_0000.jsonl.zst) | 64,989,085,005 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_0_0000.jsonl.zst) | 64,806,822,217 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_1_0000.jsonl.zst) | 64,844,015,924 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_2_0000.jsonl.zst) | 64,810,312,535 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_3_0000.jsonl.zst) | 64,820,909,691 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_4_0000.jsonl.zst) | 64,850,884,725 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_5_0000.jsonl.zst) | 64,843,303,738 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_6_0000.jsonl.zst) | 64,806,215,817 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_7_0000.jsonl.zst) | 64,829,431,736 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_8_0000.jsonl.zst) | 64,825,055,261 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/09_9_0000.jsonl.zst) | 64,801,849,045 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_0_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_0_0000.jsonl.zst) | 64,851,412,008 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_1_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_1_0000.jsonl.zst) | 64,826,057,174 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_2_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_2_0000.jsonl.zst) | 64,813,257,782 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_3_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_3_0000.jsonl.zst) | 64,869,727,403 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_4_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_4_0000.jsonl.zst) | 64,844,449,405 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_5_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_5_0000.jsonl.zst) | 64,835,986,446 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_6_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_6_0000.jsonl.zst) | 64,880,485,726 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_7_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_7_0000.jsonl.zst) | 64,875,581,875 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_8_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_8_0000.jsonl.zst) | 64,847,143,561 |
| [`https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_9_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/dclm-1.0/release/10_9_0000.jsonl.zst) | 64,817,798,548 |
| [`https://data.openeurollm.eu/prelude/baby/finemath-0.0.0/release/finemath-4plus/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finemath-0.0.0/release/finemath-4plus/shard_0000.jsonl.zst) | 12,426,892,939 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/als_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/als_Latn/shard_0000.jsonl.zst) | 1,890,145,847 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/bos_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/bos_Latn/shard_0000.jsonl.zst) | 4,433,471,940 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/bul_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/bul_Cyrl/shard_0000.jsonl.zst) | 6,534,201,956 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/cat_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/cat_Latn/shard_0000.jsonl.zst) | 5,273,922,543 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ces_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ces_Latn/shard_0000.jsonl.zst) | 5,568,406,192 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/dan_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/dan_Latn/shard_0000.jsonl.zst) | 4,431,957,026 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/deu_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/deu_Latn/shard_0000.jsonl.zst) | 11,861,437,790 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ekk_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ekk_Latn/shard_0000.jsonl.zst) | 3,148,609,208 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ell_Grek/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ell_Grek/shard_0000.jsonl.zst) | 8,982,593,498 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0000.jsonl.zst) | 127,939,029,456 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0001.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0001.jsonl.zst) | 127,358,974,690 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0002.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0002.jsonl.zst) | 128,156,368,653 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0003.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0003.jsonl.zst) | 127,350,629,761 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0004.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0004.jsonl.zst) | 124,081,625,467 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0005.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0005.jsonl.zst) | 120,060,014,216 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0006.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0006.jsonl.zst) | 115,069,093,960 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0007.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0007.jsonl.zst) | 115,287,616,780 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0008.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0008.jsonl.zst) | 114,529,097,613 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0009.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0009.jsonl.zst) | 115,790,322,079 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0010.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0010.jsonl.zst) | 115,193,226,566 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0011.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eng_Latn/shard_0011.jsonl.zst) | 13,985,631,065 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eus_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/eus_Latn/shard_0000.jsonl.zst) | 2,933,223,335 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/fin_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/fin_Latn/shard_0000.jsonl.zst) | 4,967,739,129 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/fra_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/fra_Latn/shard_0000.jsonl.zst) | 14,731,046,524 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/gle_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/gle_Latn/shard_0000.jsonl.zst) | 317,647,606 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/glg_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/glg_Latn/shard_0000.jsonl.zst) | 1,883,875,854 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/hrv_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/hrv_Latn/shard_0000.jsonl.zst) | 4,096,409,837 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/hun_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/hun_Latn/shard_0000.jsonl.zst) | 4,728,015,529 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/isl_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/isl_Latn/shard_0000.jsonl.zst) | 3,382,919,684 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ita_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ita_Latn/shard_0000.jsonl.zst) | 13,169,395,208 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/kat_Geor/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/kat_Geor/shard_0000.jsonl.zst) | 1,037,876,589 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/lit_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/lit_Latn/shard_0000.jsonl.zst) | 4,505,014,815 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/lvs_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/lvs_Latn/shard_0000.jsonl.zst) | 3,216,195,803 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/mkd_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/mkd_Cyrl/shard_0000.jsonl.zst) | 1,856,587,067 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/mlt_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/mlt_Latn/shard_0000.jsonl.zst) | 742,731,808 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/nld_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/nld_Latn/shard_0000.jsonl.zst) | 7,957,637,811 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/nno_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/nno_Latn/shard_0000.jsonl.zst) | 401,276,406 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/nob_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/nob_Latn/shard_0000.jsonl.zst) | 4,197,354,011 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/pol_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/pol_Latn/shard_0000.jsonl.zst) | 5,907,083,759 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/por_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/por_Latn/shard_0000.jsonl.zst) | 9,797,000,730 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ron_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ron_Latn/shard_0000.jsonl.zst) | 4,490,101,569 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/slk_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/slk_Latn/shard_0000.jsonl.zst) | 4,080,505,328 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/slv_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/slv_Latn/shard_0000.jsonl.zst) | 4,789,850,633 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/spa_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/spa_Latn/shard_0000.jsonl.zst) | 16,003,905,673 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/srp_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/srp_Cyrl/shard_0000.jsonl.zst) | 4,192,584,584 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/swe_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/swe_Latn/shard_0000.jsonl.zst) | 5,247,412,868 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/tur_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/tur_Latn/shard_0000.jsonl.zst) | 7,934,009,872 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ukr_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-1.0.0/release/ukr_Cyrl/shard_0000.jsonl.zst) | 4,964,240,785 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/als_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/als_Latn/shard_0000.jsonl.zst) | 419,021,269 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/bos_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/bos_Latn/shard_0000.jsonl.zst) | 1,284,229,395 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/bul_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/bul_Cyrl/shard_0000.jsonl.zst) | 1,865,593,392 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/cat_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/cat_Latn/shard_0000.jsonl.zst) | 1,425,156,035 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ces_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ces_Latn/shard_0000.jsonl.zst) | 6,165,992,426 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/dan_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/dan_Latn/shard_0000.jsonl.zst) | 2,173,701,963 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/deu_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/deu_Latn/shard_0000.jsonl.zst) | 25,460,455,807 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ekk_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ekk_Latn/shard_0000.jsonl.zst) | 489,834,850 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ell_Grek/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ell_Grek/shard_0000.jsonl.zst) | 2,790,016,739 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/eng_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/eng_Latn/shard_0000.jsonl.zst) | 189,196,943,994 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/eus_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/eus_Latn/shard_0000.jsonl.zst) | 372,177,702 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/fin_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/fin_Latn/shard_0000.jsonl.zst) | 2,414,584,954 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/fra_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/fra_Latn/shard_0000.jsonl.zst) | 21,703,908,342 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/glg_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/glg_Latn/shard_0000.jsonl.zst) | 284,616,352 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/hrv_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/hrv_Latn/shard_0000.jsonl.zst) | 2,080,337,768 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/hun_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/hun_Latn/shard_0000.jsonl.zst) | 6,068,128,426 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/isl_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/isl_Latn/shard_0000.jsonl.zst) | 305,265,133 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ita_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ita_Latn/shard_0000.jsonl.zst) | 15,040,274,545 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/kat_Geor/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/kat_Geor/shard_0000.jsonl.zst) | 194,678,067 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/lit_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/lit_Latn/shard_0000.jsonl.zst) | 1,145,141,635 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/lvs_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/lvs_Latn/shard_0000.jsonl.zst) | 513,419,876 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/mkd_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/mkd_Cyrl/shard_0000.jsonl.zst) | 362,125,515 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/mlt_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/mlt_Latn/shard_0000.jsonl.zst) | 104,976,086 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/nld_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/nld_Latn/shard_0000.jsonl.zst) | 6,407,243,826 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/nno_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/nno_Latn/shard_0000.jsonl.zst) | 54,603,120 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/nob_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/nob_Latn/shard_0000.jsonl.zst) | 1,682,265,128 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/pol_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/pol_Latn/shard_0000.jsonl.zst) | 10,426,524,643 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/por_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/por_Latn/shard_0000.jsonl.zst) | 15,861,759,652 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ron_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ron_Latn/shard_0000.jsonl.zst) | 5,241,765,812 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/slk_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/slk_Latn/shard_0000.jsonl.zst) | 2,404,715,702 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/slv_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/slv_Latn/shard_0000.jsonl.zst) | 810,223,374 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/spa_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/spa_Latn/shard_0000.jsonl.zst) | 35,796,204,610 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/srp_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/srp_Cyrl/shard_0000.jsonl.zst) | 2,516,343,896 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/swe_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/swe_Latn/shard_0000.jsonl.zst) | 4,168,505,687 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/tur_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/tur_Latn/shard_0000.jsonl.zst) | 2,948,138,568 |
| [`https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ukr_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/finepdfs-edu-1.0.0/release/ukr_Cyrl/shard_0000.jsonl.zst) | 7,001,946,334 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/als_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/als_Latn/shard_0000.jsonl.zst) | 9,826,677,094 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/bos_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/bos_Latn/shard_0000.jsonl.zst) | 22,480,006,829 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/bul_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/bul_Cyrl/shard_0000.jsonl.zst) | 31,015,158,801 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/cat_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/cat_Latn/shard_0000.jsonl.zst) | 19,565,580,481 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ces_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ces_Latn/shard_0000.jsonl.zst) | 42,366,062,825 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/dan_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/dan_Latn/shard_0000.jsonl.zst) | 21,581,114,143 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/deu_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/deu_Latn/shard_0000.jsonl.zst) | 133,057,604,005 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ekk_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ekk_Latn/shard_0000.jsonl.zst) | 13,816,705,984 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ell_Grek/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ell_Grek/shard_0000.jsonl.zst) | 49,752,680,911 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/eus_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/eus_Latn/shard_0000.jsonl.zst) | 2,587,143,262 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/fin_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/fin_Latn/shard_0000.jsonl.zst) | 25,828,849,308 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/fra_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/fra_Latn/shard_0000.jsonl.zst) | 138,127,385,516 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/gle_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/gle_Latn/shard_0000.jsonl.zst) | 515,093,332 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/glg_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/glg_Latn/shard_0000.jsonl.zst) | 3,329,701,930 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/hrv_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/hrv_Latn/shard_0000.jsonl.zst) | 21,577,337,335 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/hun_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/hun_Latn/shard_0000.jsonl.zst) | 35,802,164,663 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/isl_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/isl_Latn/shard_0000.jsonl.zst) | 3,625,712,486 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ita_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ita_Latn/shard_0000.jsonl.zst) | 113,120,985,803 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/kat_Geor/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/kat_Geor/shard_0000.jsonl.zst) | 7,896,296,272 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/lit_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/lit_Latn/shard_0000.jsonl.zst) | 16,742,191,638 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/lvs_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/lvs_Latn/shard_0000.jsonl.zst) | 10,852,166,204 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/mkd_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/mkd_Cyrl/shard_0000.jsonl.zst) | 5,885,705,106 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/mlt_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/mlt_Latn/shard_0000.jsonl.zst) | 858,681,392 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/nld_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/nld_Latn/shard_0000.jsonl.zst) | 52,905,518,575 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/nno_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/nno_Latn/shard_0000.jsonl.zst) | 1,352,195,221 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/nob_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/nob_Latn/shard_0000.jsonl.zst) | 21,193,591,974 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/pol_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/pol_Latn/shard_0000.jsonl.zst) | 68,529,549,282 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/por_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/por_Latn/shard_0000.jsonl.zst) | 109,699,276,717 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ron_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ron_Latn/shard_0000.jsonl.zst) | 39,424,790,878 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/slk_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/slk_Latn/shard_0000.jsonl.zst) | 21,856,269,635 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/slv_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/slv_Latn/shard_0000.jsonl.zst) | 14,710,363,667 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/spa_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/spa_Latn/shard_0000.jsonl.zst) | 212,211,795,078 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/srp_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/srp_Cyrl/shard_0000.jsonl.zst) | 9,856,628,780 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/swe_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/swe_Latn/shard_0000.jsonl.zst) | 35,527,287,669 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/tur_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/tur_Latn/shard_0000.jsonl.zst) | 47,479,294,179 |
| [`https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ukr_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/hplt-3.0/release/ukr_Cyrl/shard_0000.jsonl.zst) | 43,202,996,283 |
| [`https://data.openeurollm.eu/prelude/baby/megamath-0.0.0/release/megamath-text-code-block/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/megamath-0.0.0/release/megamath-text-code-block/shard_0000.jsonl.zst) | 12,041,344,005 |
| [`https://data.openeurollm.eu/prelude/baby/megamath-0.0.0/release/megamath-web-pro/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/megamath-0.0.0/release/megamath-web-pro/shard_0000.jsonl.zst) | 13,748,407,364 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0000.jsonl.zst) | 154,555,825,527 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0001.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0001.jsonl.zst) | 161,160,519,623 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0002.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0002.jsonl.zst) | 164,889,011,768 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0003.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0003.jsonl.zst) | 175,950,657,023 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0004.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0004.jsonl.zst) | 191,038,569,075 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0005.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/high/actual/shard_0005.jsonl.zst) | 134,020,265,036 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0000.jsonl.zst) | 205,337,845,067 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0001.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0001.jsonl.zst) | 205,046,729,770 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0002.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0002.jsonl.zst) | 212,315,716,042 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0003.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0003.jsonl.zst) | 216,409,796,951 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0004.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium-high/actual/shard_0004.jsonl.zst) | 49,536,351,932 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0000.jsonl.zst) | 172,568,599,788 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0001.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0001.jsonl.zst) | 179,192,211,686 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0002.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0002.jsonl.zst) | 182,118,349,881 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0003.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0003.jsonl.zst) | 175,214,895,123 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0004.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0004.jsonl.zst) | 178,648,265,015 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0005.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0005.jsonl.zst) | 174,420,960,276 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0006.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0006.jsonl.zst) | 180,249,258,551 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0007.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0007.jsonl.zst) | 179,083,725,227 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0008.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0008.jsonl.zst) | 179,362,558,603 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0009.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0009.jsonl.zst) | 179,050,680,611 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0010.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0010.jsonl.zst) | 177,406,330,128 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0011.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0011.jsonl.zst) | 178,717,213,717 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0012.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0012.jsonl.zst) | 171,763,952,229 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0013.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0013.jsonl.zst) | 166,678,111,055 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0014.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-1.0/release/medium/actual/shard_0014.jsonl.zst) | 33,302,943,399 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/bos_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/bos_Latn/shard_0000.jsonl.zst) | 25,920,505,695 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/bul_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/bul_Cyrl/shard_0000.jsonl.zst) | 35,912,361,343 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/cat_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/cat_Latn/shard_0000.jsonl.zst) | 26,617,195,470 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/ces_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/ces_Latn/shard_0000.jsonl.zst) | 37,899,035,549 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/ell_Grek/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/ell_Grek/shard_0000.jsonl.zst) | 46,102,989,088 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/est_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/est_Latn/shard_0000.jsonl.zst) | 23,752,302,745 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/eus_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/eus_Latn/shard_0000.jsonl.zst) | 19,831,487,405 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/gle_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/gle_Latn/shard_0000.jsonl.zst) | 21,491,003,782 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/glg_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/glg_Latn/shard_0000.jsonl.zst) | 22,412,901,412 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/hrv_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/hrv_Latn/shard_0000.jsonl.zst) | 27,937,516,312 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/kat_Geor/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/kat_Geor/shard_0000.jsonl.zst) | 33,626,179,967 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/lav_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/lav_Latn/shard_0000.jsonl.zst) | 24,704,462,860 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/lit_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/lit_Latn/shard_0000.jsonl.zst) | 24,923,341,642 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/mkd_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/mkd_Cyrl/shard_0000.jsonl.zst) | 28,919,327,773 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/mlt_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/mlt_Latn/shard_0000.jsonl.zst) | 23,249,851,355 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/slk_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/slk_Latn/shard_0000.jsonl.zst) | 27,330,027,414 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/slv_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/slv_Latn/shard_0000.jsonl.zst) | 24,232,883,999 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/sqi_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/sqi_Latn/shard_0000.jsonl.zst) | 25,863,518,443 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/srp_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/srp_Cyrl/shard_0000.jsonl.zst) | 30,843,566,231 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/tur_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-opus-1.1/release/tur_Latn/shard_0000.jsonl.zst) | 38,216,840,258 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/deu_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/deu_Latn/shard_0000.jsonl.zst) | 69,554,656,901 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/fin_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/fin_Latn/shard_0000.jsonl.zst) | 23,291,593,084 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/ita_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/ita_Latn/shard_0000.jsonl.zst) | 62,987,398,652 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/spa_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/spa_Latn/shard_0000.jsonl.zst) | 108,787,273,231 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/swe_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower72b/swe_Latn/shard_0000.jsonl.zst) | 27,289,776,505 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/dan_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/dan_Latn/shard_0000.jsonl.zst) | 22,116,794,582 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/fra_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/fra_Latn/shard_0000.jsonl.zst) | 73,522,273,086 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/hun_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/hun_Latn/shard_0000.jsonl.zst) | 30,071,758,879 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/isl_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/isl_Latn/shard_0000.jsonl.zst) | 17,377,316,373 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/nld_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/nld_Latn/shard_0000.jsonl.zst) | 36,572,704,177 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/nno_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/nno_Latn/shard_0000.jsonl.zst) | 16,772,177,807 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/nob_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/nob_Latn/shard_0000.jsonl.zst) | 21,941,589,238 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/pol_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/pol_Latn/shard_0000.jsonl.zst) | 44,761,598,659 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/por_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/por_Latn/shard_0000.jsonl.zst) | 64,550,511,314 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/ron_Latn/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/ron_Latn/shard_0000.jsonl.zst) | 30,336,160,945 |
| [`https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/ukr_Cyrl/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/nemotron-cc-tower+-0.1/release/parallel/tower9b/ukr_Cyrl/shard_0000.jsonl.zst) | 34,182,171,112 |
| [`https://data.openeurollm.eu/prelude/baby/olmo-mix-1124/release/arxiv/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/olmo-mix-1124/release/arxiv/shard_0000.jsonl.zst) | 21,735,915,323 |
| [`https://data.openeurollm.eu/prelude/baby/olmo-mix-1124/release/pes2o/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/olmo-mix-1124/release/pes2o/shard_0000.jsonl.zst) | 104,527,250,996 |
| [`https://data.openeurollm.eu/prelude/baby/olmo-mix-1124/release/wiki/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/olmo-mix-1124/release/wiki/shard_0000.jsonl.zst) | 6,125,158,754 |
| [`https://data.openeurollm.eu/prelude/baby/starcoder-0.0.0/release/shard_0000.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/starcoder-0.0.0/release/shard_0000.jsonl.zst) | 70,564,696,583 |
| [`https://data.openeurollm.eu/prelude/baby/starcoder-0.0.0/release/shard_0001.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/starcoder-0.0.0/release/shard_0001.jsonl.zst) | 79,472,911,202 |
| [`https://data.openeurollm.eu/prelude/baby/starcoder-0.0.0/release/shard_0002.jsonl.zst`](https://data.openeurollm.eu/prelude/baby/starcoder-0.0.0/release/shard_0002.jsonl.zst) | 51,257,371,969 |
</details>

## Data Packing

Overall design principles and some terminology are documented through
the [general description of OpenEuroLLM training data collection](https://github.com/OpenEuroLLM/training-data-collection/blob/main/README.md).
The `baby` data collection is the first implementation of this process,
where the bulk of processing parameters already are made explicit through
per-dataset `metadata.yaml` files, but some configuration aspects merely
reflect the defaults setting (at the time) of the software involved.
For the central tool; the OpenEuroLLM Training Data Packer, its
[`baby` release version](https://github.com/OpenEuroLLM/training-data-packer/tree/baby)
was used.
