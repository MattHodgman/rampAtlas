import csv
from scipy.stats import chisquare

td = {}
cd = {}
# [Total, Ramp, RND, RL, RM, RH, NND, NL, NM, NH]
# [0,     1,    2,   3,   4, 5,  6,   7,  8,   9

with open("geneExpressionCountsCellTypeCAI.csv") as cell_file, open("geneExpressionCountsTissueCAI.csv") as tissue_file:
    cell_file.readline()
    tissue_file.readline()

    for line in tissue_file:
        row = line.rstrip().split(',')
        rnd, rl, rm, rh = int(row[1]), int(row[2]), int(row[3]), int(row[4])
        nnd, nl, nm, nh = int(row[5]), int(row[6]), int(row[7]), int(row[8])
        fiveP = .05 * int(row[10])

        if rnd + nnd > fiveP and rl + nl > fiveP and rm + nm > fiveP and rh + nh > fiveP:
            td[row[0]] = [int(row[10]), int(row[9]), rnd, rl, rm, rh, nnd, nl, nm, nh]

    for line in cell_file:
        row = line.rstrip().split(',')
        rnd, rl, rm, rh = int(row[1]), int(row[2]), int(row[3]), int(row[4])
        nnd, nl, nm, nh = int(row[5]), int(row[6]), int(row[7]), int(row[8])
        fiveP = .05 * int(row[10])
        

        if rnd + nnd > fiveP and rl + nl > fiveP and rm + nm > fiveP and rh + nh > fiveP:
            cd[row[0]] = [int(row[10]), int(row[9]), rnd, rl, rm, rh, nnd, nl, nm, nh]

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
    if weightedAvg < resultList[3] < resultList[4]:
        resultList.append(resultList[4] - weightedAvg)
    else:
        resultList.append(-1)
    tissueResults.append(resultList)

cellResults = []
for gene, nums in cd.items():
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
    if weightedAvg < resultList[3] < resultList[4]:
        resultList.append(resultList[4] - weightedAvg)
    else:
        resultList.append(-1)
    cellResults.append(resultList)

header = ['gene', 'P(R|ND)', 'P(R|L)', 'P(R|M)', 'P(R|H)',  "H-AVG(ND,L)"]
with open("tissueBayes2.csv", 'w') as tissue_csv_file, open("cellTypeBayes2.csv", 'w') as cell_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(header)
    for tisLine in tissueResults:
        writerT.writerow(tisLine)

    writerC = csv.writer(cell_csv_file)
    writerC.writerow(header)
    for cellLine in cellResults:
        writerC.writerow(cellLine)
