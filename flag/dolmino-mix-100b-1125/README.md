# OLMo 3 Dolmino-Mix 100B 1125

## Download

```
git lfs install --skip-smudge
git config --global lfs.concurrenttransfers 16
git clone --verbose --jobs 8 --single-branch --branch main \
  https://huggingface.co/datasets/dolma3_dolmino_mix-100B-1125 git
(
  cd git;
  for i in code-meta-reasoning cranecode program_verifiable stack_edu-fim ; do
    echo $i;
    git lfs pull --include "data/*${i}*"
    cp -pr data/*${i}* ../source
  done
  for i in cranemath dolmino-math megamatt omr-rewrite-fullthoughts tinymath; do
    echo $i;
    git lfs pull --include "data/*${i}*"
    cp -pr data/*${i}* ../source
  done
)
```
