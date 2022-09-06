#!/bin/bash

# Set env
VINA="/home/ubuntu/req/vina"
VINA_GPU="/home/ubuntu/usr/Vina-GPU/Vina-GPU"
OBABEL="~/anaconda3/envs/vina/bin/obabel"

# Set input arguments
#INPUT_PROTEIN="example/6imo/6imo_protein.pdb"
#INPUT_LIGAND="example/6imo/6imo_ligand.mol2"
INPUT_PREFIX="/home/ubuntu/VINA_screening/example/"
OUTPUT_PREFIX="/home/ubuntu/alg"
TAG="test"
#/home/ubuntu/VINA_screening/example/6imo/*.sdf
files="${INPUT_PREFIX}????"
for file in $files;do
  echo $file
  name=${file##*/}
  for idx in `seq 1 10`;do
      /home/ubuntu/VINA_screening/run_vina.py -r ${file}/*.pdb \
                    -l ${file}/*.sdf \
                    -d "${OUTPUT_PREFIX}/${name}" \
                    -t "${TAG}_${idx}" \
                    --obabel ${OBABEL} \
                    --vina ${VINA} \
                    --device CPU
  done
done