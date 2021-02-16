import csv

cd = {}
# [Total, Ramp]

with open("../normal_tissue_withoutU.csv") as open1:
    for line in open1:
        row = line.split(',')
        ct = row[3] + " in " + row[2]

        if ct not in cd.keys():
            cd[ct] = [1, 0]
        else:
            cd[ct][0] += 1

        if row[6] == 'Y\n':
            cd[ct][1] += 1


headerT = ['tissue', 'total genes', 'total ramps']
headerC = ['cell type', 'total genes', 'total ramps']
with open("spreadCellTypeTotalAndRamp.csv", 'w') as cell_csv_file:
    writerC = csv.writer(cell_csv_file)
    writerC.writerow(headerC)
    for cell, nums in cd.items():
        writerC.writerow([cell, nums[0], nums[1]])
