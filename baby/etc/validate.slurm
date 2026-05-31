#!/bin/bash

#SBATCH --job-name=validate
#SBATCH --output=log/%x-%j.out
#SBATCH --partition=lrd_all_serial
##SBATCH --account=project_465002530
#SBATCH --time=4:00:00
#SBATCH --mail-type=FAIL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
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
path=$(realpath -s ${1});
if [ -z "${path}" ]; then
  echo "validate.slurm: missing or invalid directory argument; exit." >&2;
  exit 1;
fi
path=${path%/};

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] validate.slurm: root in ${root}; data: ${1}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] validate.slurm: data: ${path}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] validate.slurm: using ${cores} cores."

parallel="parallel --plain --will-cite";
parallel="${parallel} --group --jobs ${cores}";

for file in $(find ${path} -name megatron-lm.md5); do
  echo ${file};
  LC_ALL=C ${parallel} -a ${file} "echo {} | md5sum -c -" \
  | tee ${file%md5}log 2>&1
done;

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] validate.slurm: all files processed."
exit 0;
