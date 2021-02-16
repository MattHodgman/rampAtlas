import csv
from scipy.stats import chisquare
import sys

geneExpCount = sys.argv[1]

td = {}
# [Total, Ramp, RND, RL, RM, RH, NND, NL, NM, NH]
# [0,     1,    2,   3,   4, 5,  6,   7,  8,   9

with open(geneExpCount) as tissue_file:
    tissue_file.readline()

    for line in tissue_file:
        row = line.rstrip().split(',')
        rnd, rl, rm, rh = int(row[1]), int(row[2]), int(row[3]), int(row[4])
        nnd, nl, nm, nh = int(row[5]), int(row[6]), int(row[7]), int(row[8])
        fiveP = .05 * int(row[10])

        if rnd + nnd > fiveP and rl + nl > fiveP and rm + nm > fiveP and rh + nh > fiveP:
            td[row[0]] = [int(row[10]), int(row[9]), rnd, rl, rm, rh, nnd, nl, nm, nh]


# run bayes theorem
tissueResults = []

# [gene, r|nd, r|l, r|m, r|h, h-(l+nd)/2]
for gene, nums in td.items():
    resultList = [gene]
    totalGene = nums[0]
    totalRamp = nums[1]
    for exp in range(4):
        if totalRamp == 0:
            resultList.append(0)
        else:
            pRampGivenExpression = (((nums[exp + 2]) / totalRamp) * (totalRamp / totalGene)) / (
                        (nums[exp + 2] + nums[exp + 6]) / totalGene)
            resultList.append(pRampGivenExpression)

    rnd, rl, nnd, nl = nums[2], nums[3], nums[6], nums[7]
    weightedAvg = (resultList[1] * (rnd + nnd) + resultList[2] * (rl + nl)) / (rnd + rl + nnd + nl)
    resultList.append(weightedAvg)
    resultList.append(resultList[4] - weightedAvg)
    if weightedAvg < resultList[3] < resultList[4]:
        resultList.append("middle")
    elif weightedAvg == resultList[3] or weightedAvg == resultList[4]:
        resultList.append("equal")
    elif resultList[3] > resultList[4]:
        resultList.append("more")
    else:
        resultList.append("less")

    exph = (totalRamp / totalGene) * (nums[5] + nums[9])
    expl = (totalRamp / totalGene) * (rl + nl + rnd + nnd)
    if exph == 0 or expl == 0:
        resultList.append(-1)
        resultList.append(-1)
    else:
        chi, p_val = chisquare([nums[5], (rnd + rl)], f_exp=[exph, expl])
        resultList.append(chi)
        resultList.append(p_val)

    resultList.append(totalRamp)
    resultList.append(totalGene)
    tissueResults.append(resultList)

header = ['gene', 'P(R|ND)', 'P(R|L)', 'P(R|M)', 'P(R|H)', 'weighted avg ND & L', "H-AVG(ND,L)", 'pos of medium',
        'chiValue', 'chi p_val', 'totalRamp', 'totalGene']

with open("tissueBayes3.csv", 'w') as tissue_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(header)
    for tisLine in tissueResults:
        writerT.writerow(tisLine)

