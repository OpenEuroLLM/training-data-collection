#!/bin/bash

#
# for i in hplt-3.0/source/*_*; do sbatch etc/count $i; done
#

#SBATCH --job-name=count
#SBATCH --output=log/%x-%j.out
#SBATCH --partition=small
#SBATCH --account=project_465002530
#SBATCH --time=72:00:00
#SBATCH --mail-type=FAIL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=128
#SBATCH --mem-per-cpu=2G

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
# determine the root of the Training Data Catalogue
#
if [ -d /appl/local/openeurollm/training/catalogue ]; then
  base=/appl/local/openeurollm/training/catalogue;
else
  echo "count.slurm: missing OpenEuroLLM Training Data Catalogue; exit." >&2;
  exit 1;
fi

module reset;
module load cray-python;
source ${base}/local/bin/activate;

#
# command-line argument is one (source) directory with JSONLines files
#
path=$(realpath -s ${1});
if [ -z "${path}" ]; then
  echo "count.slurm: missing or invalid directory argument; exit." >&2;
  exit 1;
fi

pattern="\\.jsonl\\.zst\$";
tokenizer="openeurollm/tokenizer-256k";
key="text";
suffix="${path##${root}/}";
name="${suffix%%/source/*}";
part="${suffix##*/source/}";
target="${root}/${name}/counts/${part}";
if [ ! -d ${target} ]; then mkdir -p ${target}; fi
target=${target}/source.json;
if [ -e ${target} ]; then rm -f ${target}; fi

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] count.slurm: root in ${root}; data: ${1}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] count.slurm: target: ${target}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] count.slurm: using ${cores} cores."

python -c "
import sys;
sys.path.append(\"${base}/etc\");
import counts;
counts.count_directory(\"${path}\", pattern = \"${pattern}\", cores = ${cores}, tokenizer = \"${tokenizer}\", key = \"${key}\", target = \"${target}\", force = True);
"

#
# make sure everything is group-readable (and directories searchable)
#
chmod -R g+rX ${root}/${name}/counts;

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] count.slurm: all files processed."
exit 0;
