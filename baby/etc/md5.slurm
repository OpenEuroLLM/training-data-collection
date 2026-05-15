#!/bin/bash

#
#
#

#SBATCH --job-name=md5
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
# determine the root of the Training Data Catalogue
#
if [ -d /appl/local/openeurollm/training/catalogue ]; then
  base=/appl/local/openeurollm/training/catalogue;
else
  echo "md5.slurm: missing OpenEuroLLM Training Data Catalogue; exit." >&2;
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
  echo "md5.slurm: missing or invalid directory argument; exit." >&2;
  exit 1;
fi
path=${path%/};

suffix="${path##${root}/}/";
infix="${suffix#*/}";
infix="${infix%%/*}";
name="${suffix%%/${infix}/*}";
part="${suffix##*/${infix}/}";
part="${part%/}";
metadata="${root}/${name}/metadata.yaml";

if [ ! -f "${metadata}" ]; then
  echo "md5.slurm: no metadata for ${root}/${name}; exit." >&2;
  exit 1;
fi

pattern=$(yq4 ".suffix" ${metadata});
if [ -z "${pattern}" -o "${key}" = "null" ]; then
  echo "md5.slurm: unable to determine .suffix. value; exit." >&2;
  exit 1;
fi
export pattern;

if [ -z "${part}" ]; then
  target="${root}/${name}/md5";
else
  target="${root}/${name}/md5/${part}";
fi
if [ ! -d ${target} ]; then mkdir -p ${target}; fi
target=${target}/${infix}.md5;
if [ -e ${target} ]; then rm -f ${target}; fi

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] md5.slurm: root in ${root}; data: ${1}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] md5.slurm: target: ${target}."
echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] md5.slurm: using ${cores} cores."

module reset;
module load LUMI parallel;

function run() {
  local file=${1};
  local target="$(dirname ${file})/.$(basename ${file} ${pattern}).md5";
  local command="md5sum ${file} > ${target}";
  if [ ! -f ${target} ]; then eval ${command}; fi;
} # run()
export -f run;

parallel="LC_ALL=C parallel --plain --will-cite";
parallel="${parallel} --group --jobs ${cores}";

set -x
#
# finally, iterate through all the files in this directory
#
cd ${root};
find ${suffix} -mindepth 1 -maxdepth 1 -name \*${pattern} \
| eval ${parallel} run {} ${target};

cat ${suffix}/.*.md5 | sort -k 2,2 > ${target};

#
# make sure everything is group-readable (and directories searchable)
#
chmod -R g+rX ${root}/${name}/md5;

echo "[$(date +"%Y-%m-%d (%H:%M:%S)")] md5.slurm: all files processed."
exit 0;
