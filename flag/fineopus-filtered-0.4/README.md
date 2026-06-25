# FineOPUS Filtered Stage 4

## Download

```
git lfs install --skip-smudge
git config --global lfs.concurrenttransfers 16
git clone --verbose --jobs 8 --single-branch --branch main \
  https://huggingface.co/datasets/MaLA-LM/FineOPUS-Filtered-Stage4 parquet
(
  cd parquet;
  for i in *; do
    s=${i%-*}; t=${i#*-}; l=../../../../catalogue/languages;
    if grep $s $l > /dev/null; then
      if grep $t $l > /dev/null; then
        echo "+ $i";
	git lfs pull --include "$i/*"
      else echo "- $i"; \rm -rf ./$i;
      fi;
    else echo "- $i"; \rm -rf ./$i;
    fi;
  done
  \rm -rf .git*;
  for i in *_*-*_*; do
    if [ ${i#eng_Latn-} = $i -a ${i%-eng_Latn} = $i ]; then
      \rm -rf $i;
    fi;
  done
)
```