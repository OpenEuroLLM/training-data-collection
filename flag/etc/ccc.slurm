#!/bin/bash

#
#
# 

#SBATCH --job-name=ccc
#SBATCH --output=log/%x-%j.out
#SBATCH --partition=small
#SBATCH --account=project_465002530
#SBATCH --time=72:00:00
#SBATCH --mail-type=FAIL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
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

cores=${SLURM_CPUS_ON_NODE:-8};

#
# first argument is the source directory with JSONLines files
#
path=$(realpath -s ${1});
if [ -z "${path}" -o ! -d ${path} ]; then
  echo "ccc.slurm: missing or invalid source directory argument; exit." >&2;
  exit 1;
fi
shift;
path=${path%/};

#
# next argument is the target directory for JSONLines files
#
target=$(realpath -s ${1});
if [ -z "${target}" ]; then
  echo "ccc.slurm: missing or invalid target directory argument; exit." >&2;
  exit 1;
fi
shift;

if [ ! -d ${target} ]; then
  mkdir -p ${target};
fi
export path target;

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] ccc.slurm: root in ${root}; data: ${path}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] ccc.slurm: target: ${target}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] ccc.slurm: using ${cores} cores."

module reset;
module load LUMI parallel;

function run() {
  local input=${1};
  echo ${file};  
  local output="${target}/$(basename ${input})";
  local command="zstdcat ${input} | jq -c"
  command="${command} 'select(.crawl_id|test(\"CC-MAIN-2025|CC-MAIN-2024-[4-9]|CC-MAIN-2024-3[1-9]\"))'"
  command="$command | zstd -z -T2 -o ${output}";
  if [ ! -f ${output} ]; then eval ${command}; fi;
} # run()
export -f run;

parallel="LC_ALL=C parallel --plain --will-cite";
parallel="${parallel} --group --jobs $[${cores} / 2]";

#
# finally, iterate through all the files in this directory
#
cd ${root};
find ${path} -mindepth 1 -maxdepth 1 -name \*.jsonl.zst \
| eval ${parallel} run {} ${target};

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] ccc.slurm: all files processed."
exit 0;
