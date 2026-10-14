#!/bin/bash

#SBATCH --job-name=textify
#SBATCH --account=project_465002530
#SBATCH --partition=small
#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=64G
#SBATCH --array=1-120
#SBATCH --output=/scratch/project_465002530/users/jhelcl/log/%x-%A-%a.out

set -euo pipefail

COLLECTION_ROOT=/scratch/project_465002530/training/collection/flag
DATASET=openthoughts-3
SRC_DIR="${COLLECTION_ROOT}/${DATASET}/raw/data"
OUT_DIR="${COLLECTION_ROOT}/${DATASET}/source/data"
CONVERTER="${COLLECTION_ROOT}/${DATASET}/etc/textify.py"

module reset
module load cray-python
source /scratch/project_465002530/users/jhelcl/env/bin/activate

mkdir -p "${OUT_DIR}"

printf -v shard "%05d" $((SLURM_ARRAY_TASK_ID - 1))
infile="${SRC_DIR}/train-${shard}-of-00120.jsonl.zst"
outfile="${OUT_DIR}/train-${shard}-of-00120.jsonl.zst"

if [ ! -e "${infile}" ]; then
    echo "Task ${SLURM_ARRAY_TASK_ID}: input file not found: ${infile}" >&2
    exit 1
fi

if [ -e "${outfile}" ]; then
    echo "skip: $(basename "${outfile}") already exists"
    exit 0
fi

echo "$(date): converting $(basename "${infile}")"
python "${CONVERTER}" \
    --infile  "${infile}" \
    --outfile "${outfile}" \
    --threads "${SLURM_CPUS_PER_TASK}" \
    --compression-level 10 \
    --chunk-size 2000

echo "$(date): task ${SLURM_ARRAY_TASK_ID} done"
