#

## Data Ingestion

```
mkdir fineweb2-hq;
cd fineweb2-hq;
git clone --verbose --jobs 8 --single-branch --branch main \
  https://huggingface.co/datasets/epfml/FineWeb2-HQ parquet
(
  cd parquet;
  for i in ces_Latn dan_Latn deu_Latn ell_Grek fra_Latn \
           hun_Latn ita_Latn nld_Latn pol_Latn por_Latn \
	   spa_Latn swe_Latn tur_Latn; do
    echo $i;
    git lfs pull --include "$i/*";
  done;
  \rm -rf arb_Arab cmn_Hani fas_Arab ind_Latn jpn_Jpan rus_Cyrl vie_Latn .git*
)
```
