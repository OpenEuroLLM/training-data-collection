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
Pretraining drew data for [36 distinct languages](language.txt) plus some
code and math from the `baby` data collection (this directory).
Conversely, annealing and context extension availed themselves of data
from the newer
[`flag` training data collection](https://github.com/OpenEuroLLM/training-data-collection/blob/main/flag/README.md), which will be published at the end of 2026.

For Prelude training, the data has undergone
[filtering for benchmark contamination](https://github.com/OpenEuroLLM/decontamination-benchmarks),
[masking of personally identifiable information](https://github.com/OpenEuroLLM/training-data-collection/issues/2)
(PII), and up- and down-sampling towards preset token budgets.
Thus, data statistics below distinguish between _source tokens_ (in the original
dataset), _release tokens_ (in the actual OpenEuroLLM training data collection),
and _token budgets_ in individual training phases.
All token counts are in terms of the
[OpenEuroLLM 256k `v1` Tokenizer](https://huggingface.co/openeurollm/tokenizer-256k).
More detailed statistics are available in machine-readable form for
[pretraining](pretraining.csv), and will be provided for annealing and
context extension over the next few weeks.

** Pretraining**

| **Dataset** | **Part** | **Source Tokens** | **Release Tokens** | **%**| **Token Budget** | **%** |
|-------------|----------|------------------:|-------------------:|-----:|-----------------:|------:|
| `baby/dclm-1.0` | `` | 3,845,395,936,156 | 3,493,015,206,249 | 90.8 | 2,591,976,000,001 | 74.2 |
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
| `baby/starcoder-0.0.0` | `` | 276,861,687,159 | 276,861,687,159 | 100.0 | 576,000,000,001 | 208.0 |

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

## Packing: Data Processing

Overall design principles and some terminology are documented through
the [general description of OpenEuroLLM training data collection](https://github.com/OpenEuroLLM/training-data-collection/blob/main/README.md).
The `flag` data collection is the first implementation of this process,
where the bulk of processing parameters already are made explicit through
per-dataset `metadata.yaml` files, but some configuration aspects also
reflect the defaults setting (at the time) of the software involved.
For the central tool; the OpenEuroLLM Training Data Packer, the
[`baby` release version](https://github.com/OpenEuroLLM/training-data-packer/tree/baby)
was used.
