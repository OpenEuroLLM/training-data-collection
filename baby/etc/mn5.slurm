#!/bin/bash

#SBATCH --job-name=mn5
#SBATCH --output=log/%x-%j.out
#SBATCH --partition=small
#SBATCH --account=project_465002530
#SBATCH --mail-type=FAIL
#SBATCH --time=8:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=4G

#
# determine our root directory, where the SLURM script resides
#
if [ -n "${SLURM_JOB_ID}" ]; then
  script=$(scontrol show job ${SLURM_JOB_ID} \
  | awk '/^ *Command=/ {sub(/^ *Command=/, "", $1); print $1;}');
  path=$(dirname ${script});
  root="${path%/etc}";
else
  path=$(dirname $0);
  if [ "${path#./}" != "${path}" ]; then
    path="$(pwd)/${path#./}";
  fi
  if [ "${path#/}" = "${path}" ]; then
    if [ "${path}" = "." ]; then
      path="$(pwd)";
    else 
      path="$(pwd)/${path}";
    fi
  fi
  root="${path%/etc}";
fi
root=$(realpath ${root});

cores=${SLURM_CPUS_ON_NODE:-4};

#
# command-line argument is one dataset directory
#
path=${1};
if [ -z "${path}" -o ! -d ${path} ]; then
  echo "mn5.slurm: missing or invalid directory argument; exit." >&2;
  exit 1;
fi
path=${path%/};
path=${path/megatron-lm};

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] mn5.slurm: root in ${root}; data: ${1}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] mn5.slurm: data: ${path}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] mn5.slurm: using ${cores} cores."

module load lumio;
rclone -v --transfers 16 --checkers 32 --config ${HOME}/.config/rclone/bsc.conf \
  --sftp-ssh "ssh uiop429521@transfer2.bsc.es" copy \
  ${path}/megatron-lm \
  sftp:/gpfs/projects/ehpc533/training/collection/baby/${path}/megatron-lm
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] mn5.slurm: all files processed."
exit 0;
