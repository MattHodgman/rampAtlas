import csv

td = {}
cd = {}
# [Total, Ramp]

with open("../normal_tissue_withoutU2.csv") as open1:
    for line in open1:
        row = line.split(',')
        tt = row[2]
        ct = row[3]
        if tt not in td.keys():
            td[tt] = [1, 0]
        else:
            td[tt][0] += 1

        if ct not in cd.keys():
            cd[ct] = [1, 0]
        else:
            cd[ct][0] += 1

        if row[6] == 'Y\n':
            td[tt][1] += 1
            cd[ct][1] += 1


headerT = ['tissue', 'total genes', 'total ramps']
headerC = ['cell type', 'total genes', 'total ramps']
with open("tissueTotalAndRamp.csv", 'w') as tissue_csv_file, open("trashcellTypeTotalAndRamp.csv", 'w') as cell_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(headerT)
    for tis, nums in td.items():
        writerT.writerow([tis, nums[0], nums[1]])

    writerC = csv.writer(cell_csv_file)
    writerC.writerow(headerC)
    for cell, nums in cd.items():
        writerC.writerow([cell, nums[0], nums[1]])
