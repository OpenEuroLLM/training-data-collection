#!/bin/bash

#
# find dclm-1.0/source -type d -links 2 -exec sbatch etc/count.slurm {} \;
# for i in finepdfs-1.0.0/source/*; do sbatch etc/count.slurm $i; done
# find finephrase-0.0.0/source -type d -links 2 -exec sbatch etc/count.slurm {} \;
# find finewiki-0.0.0/source -type d -links 2 -exec sbatch etc/count.slurm {} \;
# find hplt-4.0/source -type d -links 2 -exec sbatch etc/count.slurm {} \;
# find mixture-vitae-1.0/source -type d -links 2 -exec sbatch etc/count.slurm {} \;
# find nemotron-cc-1.0/source -type d -links 2 -exec sbatch etc/count.slurm {} \;
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

set -x

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

if [ "$1" = "--trial" ]; then
  trial=1;
  shift;
fi

#
# command-line argument is one (source) directory with JSONLines files
#
path=$(realpath -s ${1});
if [ -z "${path}" ]; then
  echo "count.slurm: missing or invalid directory argument; exit." >&2;
  exit 1;
fi

tokenizer="openeurollm/tokenizer-256k";

suffix="${path##${root}/}/";
infix="${suffix#*/}";
infix="${infix%%/*}";
name="${suffix%%/${infix}/*}";
part="${suffix##*/${infix}/}";
part="${part%/}";
metadata="${root}/${name}/metadata.yaml";

if [ ! -f "${metadata}" ]; then
  echo "count.slurm: no metadata for ${root}/${name}; exit." >&2;
  exit 1;
fi

#
# _fix_me_
# we should allow block-local metadata specifications in the next round
#
if [ ${infix} = "release" ]; then
  key="text";
else
  key=$(yq4 ".text" ${metadata});
  if [ -z "${key}" -o "${key}" = "null" ]; then
    echo "count.slurm: unable to determine .text. key; exit." >&2;
    exit 1;
  fi
fi

suffix=$(yq4 ".${infix}.${part}.suffix" ${metadata});
if [ -z "${suffix}" -o "${suffix}" = "null" ]; then
  suffix=$(yq4 ".${infix}.default.suffix" ${metadata});
fi    
if [ -z "${suffix}" -o "${suffix}" = "null" ]; then
  suffix=$(yq4 ".suffix" ${metadata});
fi    
if [ -z "${suffix}" -o "${suffix}" = "null" ]; then
  echo "count.slurm: unable to determine .suffix. value; exit." >&2;
  exit 1;
fi
pattern=$(echo ${suffix} | sed -e 's,\.,\\\\\.,g' -e 's,$,\$,g');

if [ -z "${part}" ]; then
  target="${root}/${name}/counts";
else
  target="${root}/${name}/counts/${part}";
fi
if [ ! -d ${target} ]; then mkdir -p ${target}; fi
target=${target}/${infix}.json;
if [ -e ${target} ]; then rm -f ${target}; fi

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] count.slurm: root in ${root}; data: ${1}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] count.slurm: target: ${target}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] count.slurm: using ${cores} cores."

#
# finally, invoke the statitics code from the Training Data Catalogue
#
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
