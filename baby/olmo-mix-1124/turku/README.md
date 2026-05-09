This direcctory contains a copy of parts of Olmo-Mix 1124 prepared by the
TurkuNLP team, with some minor local modifications (to be recovered and
documented).

The files have been copied into the “baby” training data collection from:

  /scratch/project_462000963/datasets/allenai/

  drwxrws--- 2 galicato project_462000963 4096 Oct 21  2025 ./arxiv
  drwxrws--- 2 galicato project_462000963 4096 Oct 17  2025 ./pes2o
  drwxrws--- 2 galicato project_462000963 4096 Apr 13 10:45 ./Wiki

For increased uniformity and compatibility with the original Olmo-Mix release,
a few renamings have been applied

+ arxiv/*.json -> *.jsonl
+ Wiki -> wiki
+ wiki/*.json -> *.jsonl

Additionally, all JSONLines files have been compressed using: zstd -z --rm.
