import csv
import sys

bigFile = sys.argv[1]

td = {}
# [Total, Ramp]

with open(bigFile) as open1:
    open1.readline()
    for line in open1:
        row = line.split(',')
        tt = row[2]
        if tt not in td.keys():
            td[tt] = [1, 0]
        else:
            td[tt][0] += 1

        if row[6] == 'Ramp':
            td[tt][1] += 1


headerT = ['tissue', 'total genes', 'total ramps']
with open("tissueTotalAndRamp.csv", 'w') as tissue_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(headerT)
    for tis, nums in td.items():
        writerT.writerow([tis, nums[0], nums[1]])

