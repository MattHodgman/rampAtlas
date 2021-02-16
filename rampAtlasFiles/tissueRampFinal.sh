#!/bin/bash
#SBATCH --time=10:00:00   # walltime
#SBATCH -N 1 -n 1 --mem=64G # 1 core on one node, with 64G total memory
#SBATCH -J "final"   # job name
#SBATCH --mail-user=taylormeurs@gmail.com   # email address
#SBATCH --mail-type=FAIL
module load python/3.7
time python3 tissueRampFinal.py
