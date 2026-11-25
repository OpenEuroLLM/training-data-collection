# Notes on Dataset Preparation

## Background

For maximum flexibility with token selection based on BSC-edu scores, Alex Shvets (BSC) broke up the
original `release/` data shards from HPLT 4.0 into close to 3000 smaller files, each representing a
bracket of BSC-edu levels in discretized intervals of 0.1 points.
In this scheme, for example, `clean/nob_Latn/shard_0000_00.jsonl.zst` comprises all documents with a
BSC-edu score in the interval [0, 0.1[ (i.e. below 0.1).
Stephan Oepen tokenized this data using the standard `flag` production cycle.

## On-Demand Merging

Unfortunately, it turned out that Megatron-LM data loading chokes on very small token shards.  Therefore,
Alex and Stephan collaborated on identifying the minimum size threshold, which (in late 2026) appears to
be around 133k tokens.
Stephan then identified the minimal set of merges from within a list of per-language token shards ranked
by BSC-edu levels, so as to combine adjacent shards to yield a minimum of 150k tokens.
These merges are recorded in [`etc/merges.txt](etc/merges.txt) and computed from
[`etc/merge.py](etc/merge.py).
From this data, Stephan created a forest of merge directories below `megatron-lm/openeurollm-256k/cleanm`.

```bash
cd megatron-lm/openeurollm-256k/cleanm;
egrep clean ../../../etc/merges.txt \
| while read line; do
  language=$(echo $line | awk -F, '{ print $2; }');
  count=$(echo $line | awk -F, '{ print $3; }');
  bucket=$(echo $line | awk -F, '{ print $4; }');
  target=$language/${count}_${bucket};
  if [ ! -d $target ]; then mkdir -p $target; fi;
  for j in $(echo $line | awk -F, '{ print $5; }'); do
    b=${j%.info.json}_text_document;
    ln -s ../../../$b.bin $target;
    ln -s ../../../$b.idx $target;
  done;
done
```

He then used the Megatron-LM `merge_datasets.py` tool to create merged shards.
For example, `cleanm/spa_Latn/merge_0001_37_text_document` is the result of merging the six individual
tokens shards soft linked below `cleanm/spa_Latn/0001_37/`.
In total, there were 38 merges, comprising 119 original token shards.

To complete the `cleanm` variant of this bite-sized HPLT 4.0 version, organized by BSC-edu scores, the
original files that did not require merging were soft-linked from the parallel `clean/` directory tree.
