import csv
import sys
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

totAndRamp = sys.argv[1]

td = {}
# [Total, Ramp]

with open(totAndRamp) as tissue_file:
    tissue_file.readline()
    for line in tissue_file:
        row = line.rstrip().split(',')
        td[row[0]] = [int(row[1]), int(row[2])]


# run z tests
tissueResults = []
allTissues = list(td.keys())
allTissues.pop()
popTissues = list(td.keys())

for tis1 in allTissues:
    popTissues.remove(tis1)
    for tis2 in popTissues:
        ramp1 = td[tis1][1]
        ramp2 = td[tis2][1]
        gene1 = td[tis1][0]
        gene2 = td[tis2][0]
        count = np.asarray([ramp1, ramp2])
        nobs = np.asarray([gene1, gene2])
        stat, P = proportions_ztest(count, nobs)


        tissueResults.append([tis1, tis2, stat, P])


headerT = ['tissue1', 'tissue2', 'z-statistic', 'p-val']
with open("pairwiseZ.csv", 'w') as tissue_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(headerT)
    for tisLine in tissueResults:
        writerT.writerow(tisLine)

