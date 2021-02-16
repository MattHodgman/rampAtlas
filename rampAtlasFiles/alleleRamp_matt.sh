#!/bin/bash
#SBATCH --time=72:00:00   # walltime
#SBATCH -N 1 -n 1 --mem=64G # 1 core on one node, with 64G total memory
#SBATCH -J "tissue_allele_ext_ramp"   # job name
tissue=$1
module load python/3.7
echo ${tissue}
python3 ExtRamp.py -i clinVar/all_random_mutations.fa -a tissue_tAI_values/${tissue} -o alleleExtRes/${tissue}_ramps_random_mutations -v
python3 variantRamp.py alleleExtRes/${tissue}_ramps_random_mutations alleleCSVs/${tissue}_allele_ramps_random_mutations.csv ${tissue} clinVar/allele_id_list_random_mutations
