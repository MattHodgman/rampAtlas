#!/bin/bash
#SBATCH --time=1:00:00   # walltime
#SBATCH -N 1 -n 1 --mem=64G # 1 core on one node, with 64G total memory
#SBATCH -J "hpa stats"   # job name
#SBATCH --mail-user=taylormeurs@gmail.com   # email address
#SBATCH --mail-type=FAIL
bigFile=$1
numTisPair=$2
module load python/3.7
echo ${bigFile}
python3 ../scripts/totalAndRamp.py ../hpa/${bigFile}
python3 ../scripts/expressionCounts.py ../hpa/${bigFile}
python3 ../scripts/geneExpressionCounts.py ../hpa/${bigFile}
python3 ../scripts/bayes3.py ../hpa/geneExpressionCountsTissueCAI.csv
python3 ../scripts/pairwiseChi.py ../hpa/tissueTotalAndRamp.csv
python3 ../scripts/chiPercent.py ../hpa/tissueTotalAndRamp.csv ${numTisPair} ../hpa/tissuePairwiseChi.csv

