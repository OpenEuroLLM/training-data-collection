
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
    --config ${HOME}/.config/rclone/rclone.conf -v sync \
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
    --config ${HOME}/.config/rclone/rclone.conf -v sync \
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

```bash
for i in $(cat etc/parts.txt); do
  rclone -v --transfers 8 --checkers 16 sync \
    $i lumi-465002530-public:baby-collection/$i; done

for i in $(sed 's,/release,/pii,g' etc/parts.txt); do
  rclone -v --transfers 8 --checkers 16 sync \
    $i lumi-465002530-public:baby-collection/$i; done

for i in $(sed 's,/release,/contamination,g' etc/parts.txt); do
  rclone -v --transfers 8 --checkers 16 sync \
    $i lumi-465002530-public:baby-collection/$i; done
```
