import csv
from scipy.stats import chisquare

cd = {}
# [Total, Ramp]

with open("../stats/spreadCellTypeTotalAndRamp.csv") as cell_file:
    cell_file.readline()
    for line in cell_file:
        row = line.rstrip().split(',')
        cd[row[0]] = [int(row[1]), int(row[2])]


# run chi squared tests
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


headerC = ['cell type 1', 'cell type 2', 'chi', 'p-val']
with open("spreadCellTypePairwiseChi.csv", 'w') as cell_csv_file:
    writerC = csv.writer(cell_csv_file)
    writerC.writerow(headerC)
    for cellLine in cellResults:
        writerC.writerow(cellLine)
