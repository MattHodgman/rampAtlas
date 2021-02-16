#!/bin/bash
#SBATCH --time=48:00:00   # walltime
#SBATCH -N 1 -n 1 --mem=64G # 1 core on one node, with 64G total memory
#SBATCH -J "covid_big_file"   # job name
#SBATCH --mail-user=taylormeurs@gmail.com   # email address
#SBATCH --mail-type=FAIL
name=$1
module load python/3.7
echo ${name}
time python3 tissueRampFinal.py
