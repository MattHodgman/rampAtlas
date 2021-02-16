#!/bin/bash
#SBATCH --time=24:00:00   # walltime
#SBATCH -N 1 -n 1 --mem=64G # 1 core on one node, with 64G total memory
#SBATCH -J "consensus_tissue_ramp_final"   # job name
#SBATCH --mail-user=benjamin1225bs@gmail.com   # email address
#SBATCH --mail-type=FAIL


module load python/3.7
python3 tissueRampFinal.py
