#!/bin/bash
#SBATCH --time=1:00:00   # walltime
#SBATCH -N 1 -n 1 --mem=64G # 1 core on one node, with 64G total memory
#SBATCH -J "cell_ext_ramp"   # job name
#SBATCH --mail-user=taylormeurs@gmail.com   # email address
#SBATCH --mail-type=FAIL
name=$1
module load python/3.7
echo ${name}
time python3 ExtRamp.py -i GRCh38_latest_genomic_longest_isoforms.fa -u $name -o tissueExtRes/${name}_ramps -n tissueExtRes/${name}_no_ramp -v
