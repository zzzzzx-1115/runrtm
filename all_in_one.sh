#!/bin/bash

# Set env
VINA="/home/ubuntu/req/vina"
VINA_GPU="/home/ubuntu/usr/Vina-GPU/Vina-GPU"
OBABEL="/home/ubuntu/anaconda3/envs/vina/bin/obabel"
VINA_PY="/home/ubuntu/VINA_screening/run_vina.py"
CONVERTER="/home/ubuntu/runrtm/pdb2sdf.py"
RTM_PY="/home/ubuntu/runrtm/rtm.py"
RTM_ORIGIN="/home/ubuntu/RTMScore/example/rtmscore.py"
SORTER="/home/ubuntu/runrtm/get_highest_scores.py"
NUMBER="5"

# Set input arguments

INPUT_PREFIX="/home/ubuntu/VINA_screening/example"
OUTPUT_PREFIX="/home/ubuntu/alg_apo"
SDF_PREFIX="/home/ubuntu/ligand_sdf_apo"
RTM_PREFIX="/home/ubuntu/all_scores_pocket_apo"
TAG="test"
RESULT_PREFIX="/home/ubuntu/ranked_scores_pocket_apo"

####run vina
files="${INPUT_PREFIX}/????"
for file in $files;do
  echo $file
  name=${file##*/}
  for idx in `seq 1 10`;do
      python ${VINA_PY} -r ${file}/*_aligned.pdb \
                    -l ${file}/*.mol2 \
                    -d "${OUTPUT_PREFIX}/${name}" \
                    -t "${TAG}_${idx}" \
                    --obabel ${OBABEL} \
                    --vina ${VINA} \
                    --device CPU
  done
done

####covert results of vina (.pdb) to .sdf

python ${CONVERTER} -f ${OUTPUT_PREFIX} -o ${SDF_PREFIX}

###compute rtmscores

for file in $files; do
  name=${file##*/}
  echo $name
  python ${RTM_PY} -p ${INPUT_PREFIX} -l ${SDF_PREFIX} -n ${name} --rtm_loc ${RTM_ORIGIN} -o ${RTM_PREFIX} --gen_pocket -rl "${INPUT_PREFIX}/${name}/${name}_ligand.sdf"
done

###get top n results
foos="${RTM_PREFIX}/*.csv"
for foo in ${foos}; do
  python ${SORTER} -i ${foo} -o ${RESULT_PREFIX} -n ${NUMBER}
done
