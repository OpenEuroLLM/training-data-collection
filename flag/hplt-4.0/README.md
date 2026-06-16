# OpenEuroLLM Training Data Collection (`flag` Cycle): HPLT 4.0

## Data Ingestion

```
mkdir -p hplt-4.0/source;
cd hplt-4.0/source;
for i in $(cat ../../etc/languages.txt); do
  for j in clean noisy; do
    if [ -d ../../../../catalogue/hplt/4.0/$j/$i ]; then
      mkdir -p $j/$i;
    fi;
  done;
done
for i in clean/*_* noisy/*_*; do
  (
    cd $i;
    for j in ../../../../../../catalogue/hplt/4.0/$i/*.jsonl.zst; do
      ln -s $j;
    done
  );
done
for i in clean/*; do
  n=$(grep tokens /appl/local/openeurollm/training/catalogue/hplt/4.0/$i/counts.json \
      | sed -e 's/.*: //g' -e 's/,$//g');
  if [ $n -gt 100000000000 ]; then rm -rf noisy/$(basename $i); fi;
done
```
