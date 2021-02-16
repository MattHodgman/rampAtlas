#!/bin/bash
#SBATCH --time=72:00:00
#SBATCH -N 1 -n 28 --mem=128GB
#SBATCH --job-name="expression_calculation"

echo "Hey what's up"

python3 expression_levels.py GTEx_reformat.csv expression_levels.csv


