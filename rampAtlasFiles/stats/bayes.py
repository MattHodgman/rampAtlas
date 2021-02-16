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
        # add 1 to all 8 categories (N and R for ND L M H), add 8 to total and 4 to ramp total
        td[row[0]] = [int(row[10])+8, int(row[9])+4, int(row[1])+1, int(row[2])+1, int(row[3])+1, int(row[4])+1,
                      int(row[5])+1, int(row[6])+1, int(row[7])+1, int(row[8])+1]

    for line in cell_file:
        row = line.rstrip().split(',')
        cd[row[0]] = [int(row[10])+8, int(row[9])+4, int(row[1])+1, int(row[2])+1, int(row[3])+1, int(row[4])+1,
                      int(row[5])+1, int(row[6])+1, int(row[7])+1, int(row[8])+1]

    print(cd["ACO2"])
    print(cd["DHX8"])
    print(td["ADAT1"])
    print(td["TTC33"])
# run bayes theorem
tissueResults = []
for gene, nums in td.items():
    resultList = [gene]
    totalGene = nums[0]
    totalRamp = nums[1]
    for exp in range(4):
        pRampGivenExpression = (((nums[exp+2])/totalRamp) * (totalRamp/totalGene)) / ((nums[exp+2] + nums[exp+6])/totalGene)
        resultList.append(pRampGivenExpression)
    tissueResults.append(resultList)

cellResults = []
for gene, nums in cd.items():
    resultList = [gene]
    totalGene = nums[0]
    totalRamp = nums[1]
    for exp in range(4):
        pRampGivenExpression = (((nums[exp+2])/totalRamp) * (totalRamp/totalGene)) / ((nums[exp+2] + nums[exp+6])/totalGene)
        resultList.append(pRampGivenExpression)
    cellResults.append(resultList)

header = ['gene', 'P(R|ND)', 'P(R|L)', 'P(R|M)', 'P(R|H)']
with open("tissueBayes.csv", 'w') as tissue_csv_file, open("cellTypeBayes.csv", 'w') as cell_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(header)
    for tisLine in tissueResults:
        writerT.writerow(tisLine)

    writerC = csv.writer(cell_csv_file)
    writerC.writerow(header)
    for cellLine in cellResults:
        writerC.writerow(cellLine)
