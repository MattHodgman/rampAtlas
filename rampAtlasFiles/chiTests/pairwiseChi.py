import csv
from scipy.stats import chisquare

td = {}
cd = {}
# [Total, Ramp]

with open("../stats/cellTypeTotalAndRamp.csv") as cell_file, open("../stats/tissueTotalAndRamp.csv") as tissue_file:
    cell_file.readline()
    tissue_file.readline()
    for line in tissue_file:
        row = line.rstrip().split(',')
        td[row[0]] = [int(row[1]), int(row[2])]

    for line in cell_file:
        row = line.rstrip().split(',')
        cd[row[0]] = [int(row[1]), int(row[2])]


# run chi squared tests
tissueResults = []
allTissues = list(td.keys())
allTissues.pop()
popTissues = list(td.keys())

for tis1 in allTissues:
    popTissues.remove(tis1)
    for tis2 in popTissues:
        obs1 = td[tis1][1]
        obs2 = td[tis2][1]
        expPer = (obs1 + obs2) / (td[tis1][0] + td[tis2][0])
        exp1 = expPer * td[tis1][0]
        exp2 = expPer * td[tis2][0]

        chi, p_val = chisquare([obs1, obs2], f_exp=[exp1, exp2])
        tissueResults.append([tis1, tis2, chi, p_val])

cellResults = []
allCells = list(cd.keys())
allCells.pop()
popCells = list(cd.keys())

for cell1 in allCells:
    popCells.remove(cell1)
    for cell2 in popCells:
        obs1 = cd[cell1][1]
        obs2 = cd[cell2][1]
        expPer = (obs1 + obs2) / (cd[cell1][0] + cd[cell2][0])
        exp1 = expPer * cd[cell1][0]
        exp2 = expPer * cd[cell2][0]

        chi, p_val = chisquare([obs1, obs2], f_exp=[exp1, exp2])
        cellResults.append([cell1, cell2, chi, p_val])


headerT = ['tissue1', 'tissue2', 'chi', 'p-val']
headerC = ['cell type 1', 'cell type 2', 'chi', 'p-val']
with open("tissuePairwiseChi.csv", 'w') as tissue_csv_file, open("trashcellTypePairwiseChi.csv", 'w') as cell_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(headerT)
    for tisLine in tissueResults:
        writerT.writerow(tisLine)

    writerC = csv.writer(cell_csv_file)
    writerC.writerow(headerC)
    for cellLine in cellResults:
        writerC.writerow(cellLine)
