#!/bin/bash
#SBATCH --time=1:00:00   # walltime
#SBATCH -N 1 -n 1 --mem=64G # 1 core on one node, with 64G total memory
#SBATCH -J "consensus stats"   # job name
#SBATCH --mail-user=taylormeurs@gmail.com   # email address
#SBATCH --mail-type=FAIL
bigFile=$1
numTisPair=$2
folder=$3
module load python/3.7
echo ${bigFile}
python3 ../scripts/totalAndRamp.py ../${folder}/${bigFile}
python3 ../scripts/expressionCounts.py ../${folder}/${bigFile}
python3 ../scripts/geneExpressionCounts.py ../${folder}/${bigFile}
python3 ../scripts/bayes3.py ../${folder}/geneExpressionCountsTissueCAI.csv
python3 ../scripts/pairwiseChi.py ../${folder}/tissueTotalAndRamp.csv
python3 ../scripts/chiPercent.py ../${folder}/tissueTotalAndRamp.csv ${numTisPair} ../${folder}/tissuePairwiseChi.csv

