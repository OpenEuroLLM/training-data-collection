# OpenEuroLLM Training Data Collection for the “Baby” Cycle

This directory collects and documents the training data mix for the first
“production” (or “mid-size”) [model cycle](https://docs.google.com/document/d/1gEJGJ30bcDzCcfcxZfpFS3OBHGubCCkoxZ8kpTWrff4/edit?usp=sharing), codenamed `baby`.

## Background Documents

+ Original [roadmap](https://docs.google.com/document/d/1gEJGJ30bcDzCcfcxZfpFS3OBHGubCCkoxZ8kpTWrff4/edit?tab=t.0#heading=h.n1ya4eod21cx) (not fully up-to-date)
+ training data [mixture](https://docs.google.com/document/d/1TM_y3-4rP-K65ePq3R5s74F8aZkGOqwdBbz8GXnaBic/edit?tab=t.0#heading=h.7rq8da2rzj1y) (not fully up-to-date)

## Source Datasets

| **Dataset** | **Part** | **Source Tokens** | **Release Tokens** | **%** | **Shards** |
|-------------|----------|------------------:|-------------------:|------:|-----------:|


## Annotations: Contamination Detection

## Annotations: PII Detection

## Packing: Putting it all Together

## Sanity Checking

The utility script `plan.py` implements some basic consistency checking.
It reads the top-level `datamix.txt` and `metadata.yaml` files for all datasets,
makes sure there is a `release` configuration in the metadata and corresponding
per-part directory trees in the `release/` target directories, in turn that
there are a corresponding `megatron-lm/` directory trees, `release.json` files
below `counts/`, and `megatron-lm.md5` checksums below `md5/`.
The script further confirms that there is an MD5 record per tokenized shard,
that timestamps on checksums are more recent than on the underlying binary files,
and likewise for the `release.json` counts (note that the `ltg_Latn` directory
ended up not included in the `baby` data mix).

```
stoepen@uan02:/scratch/project_465002530/training/collection/baby> ./etc/plan.py --test datamix.txt
plan.py(): 156 part(s) in 11 dataset(s).
plan.py(): no .megatron-lm. directory for hplt-3.0/ltg_Latn.
```

## Mirroring

As data preparation neared completion, the binary tokenized files, checksums,
and counts were mirrored to the OpenEuroLLM strategic allocation on Leonardo:

+ `/leonardo_work/OELLM_prod2026/training/collection/baby`

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

Owing to tight run-time limitations on Leonardo login nodes, MD5 checksum validation
was performed in the budget-free `lrd_all_serial` partition, which is limited to
at most four cpu cores and a wall-time of up to four hours.
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
