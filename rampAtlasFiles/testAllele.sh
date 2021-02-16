#!/bin/bash
#SBATCH --time=1:00:00   # walltime
#SBATCH -N 1 -n 1 --mem=64G # 1 core on one node, with 64G total memory
#SBATCH -J "tissue_allele_ext_ramp"   # job name
#SBATCH --mail-user=taylormeurs@gmail.com   # email address
#SBATCH --mail-type=FAIL
tissue=$1
module load python/3.7
echo ${tissue}
python3 ExtRamp.py -i GRCh38_latest_genomic_longest_isoforms.fa -a tissue_tAI_values/${tissue} -o alleleExtRes/${tissue}_ramps
python3 testVariantRamp.py alleleExtRes/${tissue}_ramps alleleCSVs/${tissue}_allele_ramps.csv ${tissue} clinVar/allele_id_list
