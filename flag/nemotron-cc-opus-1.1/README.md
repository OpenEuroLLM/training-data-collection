#

## Data Ingestion

```
mkdir -p nemotron-cc-opus-1.1/source;
cd nemotron-cc-opus-1.1/source;
for i in ../../../../catalogue/nemotron-cc-opus/1.1/openeurollm/*_*;
  do mkdir ${i##*/};
done
for i in *_*; do
  (
    cd $i;
    for j in ../../../../../catalogue/nemotron-cc-opus/1.1/openeurollm/$i/*.jsonl.gz; do
      ln -s $j;
    done
  );
done
```