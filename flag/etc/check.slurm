#!/bin/bash

#SBATCH --job-name=check
#SBATCH --account=project_465002530
#SBATCH --partition=small
#SBATCH --time=8:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
#SBATCH --output=/scratch/project_465002530/users/jhelcl/log/%x-%A-%a.out

set -euo pipefail

COLLECTION_ROOT=/scratch/project_465002530/training/collection/flag

module reset
module load cray-python
source /scratch/project_465002530/users/jhelcl/env/bin/activate

max_jobs=190
dataset=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --max-jobs) max_jobs=$2; shift 2 ;;
        *)          dataset=$1; shift ;;
    esac
done

if [ -z "$dataset" ]; then
    echo "Usage: $0 [--max-jobs N] DATASET_NAME" >&2
    exit 1
fi

if [ -z "${SLURM_ARRAY_TASK_ID:-}" ]; then
    echo "Submit as an array job." >&2
    exit 1
fi

filelist="${COLLECTION_ROOT}/etc/tmp-filelist.${dataset}.txt"

mapfile -t all_files < "$filelist"
total=${#all_files[@]}

n_tasks=$(( total < max_jobs ? total : max_jobs ))

if (( SLURM_ARRAY_TASK_ID > n_tasks )); then
    echo "Task ${SLURM_ARRAY_TASK_ID}: nothing to do (${n_tasks} active tasks for ${total} files)"
    exit 0
fi

start=$(( (SLURM_ARRAY_TASK_ID - 1) * total / n_tasks ))
end=$(( SLURM_ARRAY_TASK_ID * total / n_tasks ))
(( end > total )) && end=$total

echo "Task ${SLURM_ARRAY_TASK_ID}: files $((start + 1))-${end} of ${total} (max-jobs=${max_jobs})"

python -u "${COLLECTION_ROOT}/etc/check.py" "$filelist" --start "$start" --end "$end"
