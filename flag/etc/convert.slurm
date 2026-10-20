#!/bin/bash

#SBATCH --job-name=convert
#SBATCH --account=project_465002530
#SBATCH --partition=small
#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=64G
#SBATCH --output=/scratch/project_465002530/users/jhelcl/log/%x-%A-%a.out

set -euo pipefail

COLLECTION_ROOT=/scratch/project_465002530/training/collection/flag

module reset
module load cray-python
source /scratch/project_465002530/users/jhelcl/env/bin/activate

init=false
max_jobs=190
dataset=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --init)     init=true; shift ;;
        --max-jobs) max_jobs=$2; shift 2 ;;
        *)          dataset=$1; shift ;;
    esac
done

if [ -z "$dataset" ]; then
    echo "Usage: $0 [--init] [--max-jobs N] DATASET_NAME" >&2
    exit 1
fi

parquet_base="${COLLECTION_ROOT}/${dataset}/parquet"
if [ -f "${COLLECTION_ROOT}/${dataset}/etc/convert.py" ]; then
  converter="${COLLECTION_ROOT}/${dataset}/etc/convert.py";
else
  converter="${COLLECTION_ROOT}/etc/convert.py";
fi

source_base="${COLLECTION_ROOT}/${dataset}/source"
filelist="${COLLECTION_ROOT}/etc/tmp-filelist.${dataset}.txt"

if $init; then
    mapfile -t all_files < <(find "$parquet_base" -name "*.parquet" -type f | sort)
    total=${#all_files[@]}
    printf '%s\n' "${all_files[@]}" > "$filelist"
    echo "Dataset:  ${dataset}"
    echo "Source:   ${parquet_base}"
    echo "Output:   ${source_base}"
    echo "Files:    ${total}"
    echo "Filelist: ${filelist}"
    exit 0
fi

if [ -z "${SLURM_ARRAY_TASK_ID:-}" ]; then
    echo "Run with --init first, then submit as an array job." >&2
    exit 1
fi

mapfile -t all_files < "$filelist"
total=${#all_files[@]}

n_tasks=$(( total < max_jobs ? total : max_jobs ))

if (( SLURM_ARRAY_TASK_ID > n_tasks )); then
    echo "Task ${SLURM_ARRAY_TASK_ID}: nothing to do (${n_tasks} active tasks for ${total} files)"
    exit 0
fi

start=$(( (SLURM_ARRAY_TASK_ID - 1) * total / n_tasks ))
end=$(( SLURM_ARRAY_TASK_ID * total / n_tasks ))

echo "Task ${SLURM_ARRAY_TASK_ID}: files $((start + 1))-${end} of ${total} (max-jobs=${max_jobs})"

files=("${all_files[@]:${start}:$((end - start))}")

for parquet_file in "${files[@]}"; do
    relative_path="${parquet_file#${parquet_base}/}"
    output_subdir="${source_base}/$(dirname "${relative_path}")"
    mkdir -p "${output_subdir}"

    output_file="${output_subdir}/$(basename "${parquet_file%.parquet}").jsonl.zst"

    if [ -e "${output_file}" ]; then
        echo "skip: $(basename "${output_file}")"
        continue
    fi

    echo "$(date): converting $(basename "${parquet_file}")"
    python "${converter}" \
        --infile  "${parquet_file}" \
        --outfile "${output_file}" \
        --threads "${SLURM_CPUS_PER_TASK}" \
        --compression-level 10 \
        --chunk-size 2000
done

echo "$(date): task ${SLURM_ARRAY_TASK_ID} done"
