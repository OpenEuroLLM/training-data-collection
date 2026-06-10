# OpenEuroLLM Training Data Collection for the “Baby” Cycle

This directory collects and documents the training data mix for the first
“production” (or “mid-size”) [model cycle](https://github.com/OpenEuroLLM/training-data-collection/blob/main/README.md), codenamed `baby`.

Training data preparation was carried out on LUMI.
Select parts of the collection are mirrored to Leonardo,
viz. the tokenized binary files for training with Megatron-LM,
document and token counts, and MD5 checksums.

+ LUMI: `/scratch/project_465002530/training/collection/baby/`
+ Leonardo: `/leonardo_work/OELLM_prod2026/training/collection/baby/`

## Background Documents

+ Original [roadmap](https://docs.google.com/document/d/1gEJGJ30bcDzCcfcxZfpFS3OBHGubCCkoxZ8kpTWrff4/edit?tab=t.0#heading=h.n1ya4eod21cx) (not fully up-to-date)
+ training data [mixture](https://docs.google.com/document/d/1TM_y3-4rP-K65ePq3R5s74F8aZkGOqwdBbz8GXnaBic/edit?tab=t.0#heading=h.7rq8da2rzj1y) (not fully up-to-date)

## Source Datasets

| **Dataset** | **Part** | **Source Tokens** | **Release Tokens** | **%** | **Shards** |
|-------------|----------|------------------:|-------------------:|------:|-----------:|
| `dclm-1.0` |  | 38,967,683,732 | 3,493,015,206,249 | 8,963.9 | 100 |
| `finemath-0.0.0` | `finemath-4plus` | 10,684,233,758 | 10,616,534,301 | 99.4 | 1 |
| `finepdfs-1.0.0` | `als_Latn` | 2,353,482,366 | 2,353,482,366 | 100.0 | 1 |
| `finepdfs-1.0.0` | `bos_Latn` | 5,627,374,893 | 3,999,982,671 | 71.1 | 1 |
| `finepdfs-1.0.0` | `bul_Cyrl` | 7,943,829,750 | 5,338,256,924 | 67.2 | 1 |
| `finepdfs-1.0.0` | `cat_Latn` | 11,084,337,859 | 4,970,649,678 | 44.8 | 1 |
| `finepdfs-1.0.0` | `ces_Latn` | 25,735,988,104 | 4,376,190,666 | 17.0 | 1 |
| `finepdfs-1.0.0` | `dan_Latn` | 11,723,952,358 | 3,881,030,351 | 33.1 | 1 |
| `finepdfs-1.0.0` | `deu_Latn` | 154,018,911,871 | 9,251,990,551 | 6.0 | 1 |
| `finepdfs-1.0.0` | `ekk_Latn` | 2,912,687,889 | 2,912,687,889 | 100.0 | 1 |
| `finepdfs-1.0.0` | `ell_Grek` | 16,495,925,964 | 8,574,937,950 | 52.0 | 1 |
| `finepdfs-1.0.0` | `eng_Latn` | 1,316,304,236,277 | 1,131,370,937,441 | 86.0 | 12 |
| `finepdfs-1.0.0` | `eus_Latn` | 2,696,420,052 | 2,696,420,052 | 100.0 | 1 |
| `finepdfs-1.0.0` | `fin_Latn` | 13,197,482,048 | 4,492,674,627 | 34.0 | 1 |
| `finepdfs-1.0.0` | `fra_Latn` | 168,589,430,004 | 13,418,209,758 | 8.0 | 1 |
| `finepdfs-1.0.0` | `gle_Latn` | 300,703,698 | 300,703,698 | 100.0 | 1 |
| `finepdfs-1.0.0` | `glg_Latn` | 1,737,198,341 | 1,737,198,341 | 100.0 | 1 |
| `finepdfs-1.0.0` | `hrv_Latn` | 10,440,955,240 | 4,171,379,082 | 40.0 | 1 |
| `finepdfs-1.0.0` | `hun_Latn` | 28,761,473,161 | 4,318,410,781 | 15.0 | 1 |
| `finepdfs-1.0.0` | `isl_Latn` | 3,125,767,392 | 3,125,767,392 | 100.0 | 1 |
| `finepdfs-1.0.0` | `ita_Latn` | 81,555,508,409 | 10,568,898,395 | 13.0 | 1 |
| `finepdfs-1.0.0` | `kat_Geor` | 5,335,467,829 | 5,335,467,829 | 100.0 | 1 |
| `finepdfs-1.0.0` | `lit_Latn` | 5,341,006,388 | 4,236,671,358 | 79.3 | 1 |
| `finepdfs-1.0.0` | `lvs_Latn` | 4,229,372,445 | 4,229,372,445 | 100.0 | 1 |
| `finepdfs-1.0.0` | `mkd_Cyrl` | 1,655,260,079 | 1,655,260,079 | 100.0 | 1 |
| `finepdfs-1.0.0` | `mlt_Latn` | 737,732,814 | 737,732,814 | 100.0 | 1 |
| `finepdfs-1.0.0` | `nld_Latn` | 43,632,511,070 | 6,974,685,720 | 16.0 | 1 |
| `finepdfs-1.0.0` | `nno_Latn` | 340,874,944 | 340,874,944 | 100.0 | 1 |
| `finepdfs-1.0.0` | `nob_Latn` | 9,974,679,166 | 3,572,054,890 | 35.8 | 1 |
| `finepdfs-1.0.0` | `pol_Latn` | 41,724,854,569 | 4,967,277,451 | 11.9 | 1 |
| `finepdfs-1.0.0` | `por_Latn` | 94,299,880,209 | 10,196,322,891 | 10.8 | 1 |
| `finepdfs-1.0.0` | `ron_Latn` | 20,365,874,849 | 4,501,111,002 | 22.1 | 1 |
| `finepdfs-1.0.0` | `slk_Latn` | 10,722,613,075 | 3,982,747,128 | 37.1 | 1 |
| `finepdfs-1.0.0` | `slv_Latn` | 7,058,209,834 | 4,519,441,551 | 64.0 | 1 |
| `finepdfs-1.0.0` | `spa_Latn` | 214,982,410,543 | 14,906,029,302 | 6.9 | 1 |
| `finepdfs-1.0.0` | `srp_Cyrl` | 10,096,061,037 | 3,931,458,254 | 38.9 | 1 |
| `finepdfs-1.0.0` | `swe_Latn` | 21,917,786,744 | 4,580,527,164 | 20.9 | 1 |
| `finepdfs-1.0.0` | `tur_Latn` | 15,429,740,155 | 7,224,451,098 | 46.8 | 1 |
| `finepdfs-1.0.0` | `ukr_Cyrl` | 24,556,069,044 | 3,677,449,138 | 15.0 | 1 |
| `finepdfs-edu-1.0.0` | `als_Latn` | 472,332,224 | 472,318,823 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `bos_Latn` | 981,965,136 | 981,906,549 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `bul_Cyrl` | 1,245,739,246 | 1,245,658,103 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `cat_Latn` | 1,148,874,840 | 1,148,760,642 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `ces_Latn` | 4,076,220,329 | 4,075,729,681 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `dan_Latn` | 1,685,264,681 | 1,685,048,727 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `deu_Latn` | 16,814,852,514 | 16,811,365,622 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `ekk_Latn` | 406,649,970 | 406,620,025 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `ell_Grek` | 2,338,140,100 | 2,338,025,715 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `eng_Latn` | 141,839,278,641 | 141,823,476,237 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `eus_Latn` | 295,150,093 | 295,128,097 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `fin_Latn` | 1,960,226,158 | 1,960,054,642 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `fra_Latn` | 17,538,489,293 | 17,536,229,598 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `glg_Latn` | 235,935,307 | 235,918,227 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `hrv_Latn` | 1,631,281,189 | 1,631,173,114 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `hun_Latn` | 4,870,661,193 | 4,870,393,233 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `isl_Latn` | 249,999,161 | 249,974,399 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `ita_Latn` | 10,213,000,226 | 10,211,705,449 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `kat_Geor` | 872,572,518 | 872,567,315 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `lit_Latn` | 877,919,983 | 877,866,294 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `lvs_Latn` | 556,807,151 | 556,754,028 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `mkd_Cyrl` | 265,851,572 | 265,841,124 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `mlt_Latn` | 96,357,755 | 96,353,648 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `nld_Latn` | 4,900,246,544 | 4,899,584,616 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `nno_Latn` | 41,136,949 | 41,133,601 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `nob_Latn` | 1,300,940,922 | 1,300,810,558 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `pol_Latn` | 7,533,696,810 | 7,533,155,804 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `por_Latn` | 12,838,655,867 | 12,837,399,189 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `ron_Latn` | 4,438,041,427 | 4,437,834,181 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `slk_Latn` | 1,842,001,862 | 1,841,843,297 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `slv_Latn` | 617,331,653 | 617,268,590 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `spa_Latn` | 28,472,950,718 | 28,471,094,450 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `srp_Cyrl` | 1,921,150,029 | 1,921,081,318 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `swe_Latn` | 3,274,257,693 | 3,273,919,321 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `tur_Latn` | 2,447,914,948 | 2,447,801,974 | 100.0 | 1 |
| `finepdfs-edu-1.0.0` | `ukr_Cyrl` | 4,784,078,683 | 4,783,929,387 | 100.0 | 1 |
| `hplt-3.0` | `als_Latn` | 10,529,092,443 | 12,735,389,362 | 121.0 | 1 |
| `hplt-3.0` | `bos_Latn` | 27,695,837,667 | 16,161,519,161 | 58.4 | 1 |
| `hplt-3.0` | `bul_Cyrl` | 42,713,367,493 | 21,564,996,135 | 50.5 | 1 |
| `hplt-3.0` | `cat_Latn` | 21,035,306,449 | 18,286,495,183 | 86.9 | 1 |
| `hplt-3.0` | `ces_Latn` | 93,521,314,847 | 25,468,238,167 | 27.2 | 1 |
| `hplt-3.0` | `dan_Latn` | 55,465,847,872 | 17,141,293,788 | 30.9 | 1 |
| `hplt-3.0` | `deu_Latn` | 548,693,366,012 | 73,753,387,702 | 13.4 | 1 |
| `hplt-3.0` | `ekk_Latn` | 17,670,864,848 | 15,367,416,308 | 87.0 | 1 |
| `hplt-3.0` | `ell_Grek` | 103,562,684,310 | 37,558,069,994 | 36.3 | 1 |
| `hplt-3.0` | `eus_Latn` | 2,537,717,669 | 2,524,688,658 | 99.5 | 1 |
| `hplt-3.0` | `fin_Latn` | 63,971,845,965 | 20,801,858,025 | 32.5 | 1 |
| `hplt-3.0` | `fra_Latn` | 625,713,569,595 | 97,075,568,612 | 15.5 | 1 |
| `hplt-3.0` | `gle_Latn` | 827,777,248 | 540,275,521 | 65.3 | 1 |
| `hplt-3.0` | `glg_Latn` | 2,993,652,432 | 2,714,057,143 | 90.7 | 1 |
| `hplt-3.0` | `hrv_Latn` | 30,263,415,562 | 17,945,430,519 | 59.3 | 1 |
| `hplt-3.0` | `hun_Latn` | 90,780,586,862 | 28,297,539,442 | 31.2 | 1 |
| `hplt-3.0` | `isl_Latn` | 4,816,712,669 | 3,646,579,138 | 75.7 | 1 |
| `hplt-3.0` | `ita_Latn` | 297,646,358,391 | 66,197,515,208 | 22.2 | 1 |
| `hplt-3.0` | `kat_Geor` | 44,120,800,610 | 52,616,153,752 | 119.3 | 1 |
| `hplt-3.0` | `lit_Latn` | 22,728,917,285 | 16,026,793,669 | 70.5 | 1 |
| `hplt-3.0` | `ltg_Latn` | 18,785,225 | 0 | 0.0 | 0 |
| `hplt-3.0` | `lvs_Latn` | 18,704,139,033 | 18,321,525,857 | 98.0 | 1 |
| `hplt-3.0` | `mkd_Cyrl` | 4,808,723,524 | 4,346,615,370 | 90.4 | 1 |
| `hplt-3.0` | `mlt_Latn` | 752,134,448 | 1,135,757,682 | 151.0 | 1 |
| `hplt-3.0` | `nld_Latn` | 168,278,087,959 | 36,248,296,138 | 21.5 | 1 |
| `hplt-3.0` | `nno_Latn` | 1,420,558,546 | 1,292,495,298 | 91.0 | 1 |
| `hplt-3.0` | `nob_Latn` | 44,588,677,570 | 15,464,897,198 | 34.7 | 1 |
| `hplt-3.0` | `pol_Latn` | 221,631,136,292 | 41,260,411,594 | 18.6 | 1 |
| `hplt-3.0` | `por_Latn` | 327,821,314,241 | 73,454,333,231 | 22.4 | 1 |
| `hplt-3.0` | `ron_Latn` | 98,113,338,882 | 29,435,322,570 | 30.0 | 1 |
| `hplt-3.0` | `slk_Latn` | 33,059,373,007 | 17,727,473,039 | 53.6 | 1 |
| `hplt-3.0` | `slv_Latn` | 17,563,684,478 | 15,736,901,668 | 89.6 | 1 |
| `hplt-3.0` | `spa_Latn` | 692,156,868,974 | 135,827,129,796 | 19.6 | 1 |
| `hplt-3.0` | `srp_Cyrl` | 9,022,705,657 | 9,741,790,076 | 108.0 | 1 |
| `hplt-3.0` | `swe_Latn` | 101,847,772,616 | 24,880,794,250 | 24.4 | 1 |
| `hplt-3.0` | `tur_Latn` | 149,012,480,113 | 34,137,289,154 | 22.9 | 1 |
| `hplt-3.0` | `ukr_Cyrl` | 75,602,173,611 | 26,922,263,959 | 35.6 | 1 |
| `megamath-0.0.0` | `megamath-text-code-block` | 48,138,848,818 | 22,617,868,611 | 47.0 | 1 |
| `megamath-0.0.0` | `megamath-web-pro` | 14,183,867,585 | 14,147,469,034 | 99.7 | 1 |
| `nemotron-cc-1.0` | `high/actual` | 565,924,264,266 | 564,839,963,667 | 99.8 | 6 |
| `nemotron-cc-1.0` | `medium/actual` | 2,063,798,579,550 | 1,422,938,530,652 | 68.9 | 15 |
| `nemotron-cc-1.0` | `medium-high/actual` | 515,465,110,905 | 514,882,927,275 | 99.9 | 5 |
| `nemotron-cc-opus-1.1` | `bos_Latn` | 98,924,620,356 | 15,835,112,548 | 16.0 | 1 |
| `nemotron-cc-opus-1.1` | `bul_Cyrl` | 123,243,592,462 | 19,703,429,671 | 16.0 | 1 |
| `nemotron-cc-opus-1.1` | `cat_Latn` | 124,353,668,852 | 18,649,234,302 | 15.0 | 1 |
| `nemotron-cc-opus-1.1` | `ces_Latn` | 95,432,402,395 | 20,025,898,029 | 21.0 | 1 |
| `nemotron-cc-opus-1.1` | `ell_Grek` | 154,930,307,068 | 29,413,843,575 | 19.0 | 1 |
| `nemotron-cc-opus-1.1` | `est_Latn` | 114,680,244,889 | 16,044,451,640 | 14.0 | 1 |
| `nemotron-cc-opus-1.1` | `eus_Latn` | 102,052,460,721 | 13,264,550,716 | 13.0 | 1 |
| `nemotron-cc-opus-1.1` | `gle_Latn` | 126,261,928,559 | 15,141,676,602 | 12.0 | 1 |
| `nemotron-cc-opus-1.1` | `glg_Latn` | 109,875,137,469 | 14,278,104,366 | 13.0 | 1 |
| `nemotron-cc-opus-1.1` | `hrv_Latn` | 108,210,878,830 | 17,304,087,826 | 16.0 | 1 |
| `nemotron-cc-opus-1.1` | `kat_Geor` | 1,038,476,846,679 | 134,893,665,792 | 13.0 | 1 |
| `nemotron-cc-opus-1.1` | `lav_Latn` | 170,792,299,748 | 23,896,163,384 | 14.0 | 1 |
| `nemotron-cc-opus-1.1` | `lit_Latn` | 114,912,176,393 | 16,077,774,646 | 14.0 | 1 |
| `nemotron-cc-opus-1.1` | `mkd_Cyrl` | 125,518,960,998 | 16,309,028,426 | 13.0 | 1 |
| `nemotron-cc-opus-1.1` | `mlt_Latn` | 134,951,009,011 | 17,525,783,725 | 13.0 | 1 |
| `nemotron-cc-opus-1.1` | `slk_Latn` | 113,218,597,419 | 16,976,795,960 | 15.0 | 1 |
| `nemotron-cc-opus-1.1` | `slv_Latn` | 112,583,053,500 | 15,755,875,225 | 14.0 | 1 |
| `nemotron-cc-opus-1.1` | `sqi_Latn` | 174,219,266,179 | 24,382,901,025 | 14.0 | 1 |
| `nemotron-cc-opus-1.1` | `srp_Cyrl` | 130,924,280,324 | 18,340,879,465 | 14.0 | 1 |
| `nemotron-cc-opus-1.1` | `tur_Latn` | 117,196,064,386 | 25,772,235,052 | 22.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower72b/deu_Latn` | 81,859,660,544 | 40,908,201,584 | 50.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower72b/fin_Latn` | 93,248,682,940 | 16,772,759,993 | 18.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower72b/ita_Latn` | 82,285,655,894 | 38,649,527,598 | 47.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower72b/spa_Latn` | 91,611,305,219 | 74,160,222,685 | 81.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower72b/swe_Latn` | 89,681,716,339 | 18,818,693,253 | 21.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/dan_Latn` | 87,700,534,458 | 14,909,078,386 | 17.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/fra_Latn` | 102,377,460,080 | 53,198,987,987 | 52.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/hun_Latn` | 99,853,552,237 | 21,958,584,496 | 22.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/isl_Latn` | 97,348,571,405 | 12,640,575,704 | 13.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/nld_Latn` | 93,648,923,682 | 25,263,854,475 | 27.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/nno_Latn` | 90,132,244,358 | 11,711,911,758 | 13.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/nob_Latn` | 84,161,194,674 | 14,301,375,643 | 17.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/pol_Latn` | 83,828,958,663 | 26,806,679,868 | 32.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/por_Latn` | 90,185,273,844 | 43,266,618,560 | 48.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/ron_Latn` | 100,047,217,252 | 21,994,268,814 | 22.0 | 1 |
| `nemotron-cc-tower+-0.1` | `parallel/tower9b/ukr_Cyrl` | 102,496,405,840 | 20,484,876,350 | 20.0 | 1 |
| `olmo-mix-1124` | `arxiv` | 22,325,465,870 | 22,287,607,951 | 99.8 | 1 |
| `olmo-mix-1124` | `pes2o` | 60,351,920,673 | 60,336,371,648 | 100.0 | 1 |
| `olmo-mix-1124` | `wiki` | 3,836,025,828 | 3,819,092,981 | 99.6 | 1 |
| `starcoder-0.0.0` |  | 78,051,681 | 276,861,687,159 | 354,715.9 | 3 |


## Per-language breakdown (To be reviewed)

| Language       | Release Tokens   |
|----------------|------------------|
| eng_Latn       | 7,355,314,114,101 |
| spa_Latn       | 253,364,476,233   |
| kat_Geor       | 193,717,854,688   |
| fra_Latn       | 181,228,995,955   |
| pol_Latn       | 80,567,524,717    |
| ell_Grek       | 77,884,877,234    |
| nld_Latn       | 73,386,420,949    |
| tur_Latn       | 69,581,777,278    |
| ron_Latn       | 60,368,536,567    |
| hun_Latn       | 59,444,927,952    |
| ukr_Cyrl       | 55,868,518,834    |
| ces_Latn       | 53,946,056,543    |
| swe_Latn       | 51,553,933,988    |
| bul_Cyrl       | 47,852,340,833    |
| fin_Latn       | 44,027,347,287    |
| cat_Latn       | 43,055,139,805    |
| hrv_Latn       | 41,052,070,541    |
| slk_Latn       | 40,528,859,424    |
| dan_Latn       | 37,616,451,252    |
| lit_Latn       | 37,219,105,967    |
| bos_Latn       | 36,978,520,929    |
| slv_Latn       | 36,629,487,034    |
| nob_Latn       | 34,639,138,289    |
| srp_Cyrl       | 33,935,209,113    |
| sqi_Latn       | 24,382,901,025    |
| lav_Latn       | 23,896,163,384    |
| lvs_Latn       | 23,107,652,330    |
| mkd_Cyrl       | 22,576,744,999    |
| isl_Latn       | 19,662,896,633    |
| mlt_Latn       | 19,495,627,869    |
| glg_Latn       | 18,965,278,077    |
| eus_Latn       | 18,780,787,523    |
| ekk_Latn       | 18,686,724,222    |
| est_Latn       | 16,044,451,640    |
| gle_Latn       | 15,982,655,821    |
| als_Latn       | 15,561,190,551    |
| nno_Latn       | 13,386,415,601    |
| ltg_Latn       | 0                 |
|------|---------|
| code           | 276,861,687,159   |
| math           | 47,381,871,946    |
| **Total**      | **9,761,315,067,743** |

## Annotations: Contamination Detection

https://github.com/OpenEuroLLM/decontamination-benchmarks

## Annotations: PII Detection

https://github.com/OpenEuroLLM/training-data-collection/issues/2

## Packing: Putting it All Together

https://github.com/OpenEuroLLM/training-data-packer/blob/main/README.md

## Sanity Checking

The utility script `plan.py` implements some basic consistency checking.
It reads the top-level `datamix.txt` and `metadata.yaml` files for all datasets,
makes sure there is a `release` configuration in the metadata and corresponding
per-part directory trees in the `release/` target directories, in turn that
there are a corresponding `megatron-lm/` directory trees, `release.json` files
below `counts/`, and `megatron-lm.md5` checksums below `md5/`.
The script further confirms that there is an MD5 record for each tokenized shard,
that timestamps on checksums are more recent than on the underlying binary files,
and likewise that `release.json` counts are more recent than the corresponding
data files.
```
stoepen@uan02:/scratch/project_465002530/training/collection/baby> ./etc/plan.py --test datamix.txt
plan.py(): 156 part(s) in 11 dataset(s).
plan.py(): no .megatron-lm. directory for hplt-3.0/ltg_Latn.
```

## Mirroring

As data preparation neared completion, the binary tokenized files, checksums,
and counts have been mirrored to the OpenEuroLLM strategic allocation on Leonardo:

+ `/leonardo_work/OELLM_prod2026/training/collection/baby/`

With moderate amounts of parallelization, data transfer took on the order of
two days:

```
for i in $(cat etc/paths.txt); do
  ssh -xt data.leonardo.cineca.it rclone \
    --config ${HOME}/.config/rclone/rclone.conf -v copy \
    sftp:/scratch/project_465002530/training/collection/baby/${i}/ \
    /leonardo_work/OELLM_prod2026/training/collection/baby/${i}/ \
    --sftp-ssh \"/bin/ssh -F ${HOME}/.ssh/config lumi\" \
  | tee -a $(dirname ${i})/megatron-lm.log 2>&1;
done
```

```
for i in $(sed 's,megatron-lm,md5,g' etc/paths.txt); do \
  ssh -xt data.leonardo.cineca.it rclone \
    --config ${HOME}/.config/rclone/rclone.conf -v copy \
    sftp:/scratch/project_465002530/training/collection/baby/${i}/ \
    /leonardo_work/OELLM_prod2026/training/collection/baby/${i}/ \
    --sftp-ssh \"/bin/ssh -F ${HOME}/.ssh/config lumi\" \
  | tee -a $(dirname ${i})/md5.log 2>&1;
done
```

```
for i in $(sed 's,megatron-lm,counts,g' etc/paths.txt); do \
  ssh -xt data.leonardo.cineca.it rclone \
    --config ${HOME}/.config/rclone/rclone.conf -v copy \
    sftp:/scratch/project_465002530/training/collection/baby/${i}/ \
    /leonardo_work/OELLM_prod2026/training/collection/baby/${i}/ \
    --sftp-ssh \"/bin/ssh -F ${HOME}/.ssh/config lumi\" \
  | tee -a $(dirname ${i})/counts.log 2>&1;
done
```

Owing to tight run-time limitations on Leonardo login nodes, MD5 checksum validation
(using `etc/validate.slurm`)
was performed in the budget-free `lrd_all_serial` partition, which is limited to
at most four cpu cores and a maximum wall-time of up to four hours.
Validating the largest of the individual datasets, DCLM-baseline 1.0 and Nemotron-CC 1.0,
took on the order of two and 1.5 hours, respectively.

```
for f in $(find */md5 -name megatron-lm.md5); do
  i=$(wc -l $f | awk '{print $1}'); l=${f%md5}log;
  if [ ! -f $l ]; then echo "missing log: $f";
  else
    j=$(grep ": OK" $l | wc -l);
    if [ $i -ne $j ]; then echo "mismatch: $f ($i vs $j)"; fi;
  fi;
done
```
