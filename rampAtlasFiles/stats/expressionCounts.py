import csv

tdr = {}
cdr = {}
td = {}
cd = {}
# [not det, low, med, high]

with open("../normal_tissue_withoutU2.csv") as open1:
    for line in open1:
        row = line.split(',')
        tt = row[2]
        ct = row[3]

        if row[6] == 'Y\n':
            if tt not in tdr.keys():
                tdr[tt] = [0, 0, 0, 0]
            if ct not in cdr.keys():
                cdr[ct] = [0, 0, 0, 0]
 
            if row[4] == 'Not detected':
                tdr[tt][0] += 1
                cdr[ct][0] += 1
            elif row[4] == 'Low':
                tdr[tt][1] += 1
                cdr[ct][1] += 1
            elif row[4] == 'Medium':
                tdr[tt][2] += 1
                cdr[ct][2] += 1
            elif row[4] == 'High':
                tdr[tt][3] += 1
                cdr[ct][3] += 1

        else:
            if tt not in td.keys():
                td[tt] = [0, 0, 0, 0]
            if ct not in cd.keys():
                cd[ct] = [0, 0, 0, 0]
 

            if row[4] == 'Not detected':
                td[tt][0] += 1
                cd[ct][0] += 1
            elif row[4] == 'Low':
                td[tt][1] += 1
                cd[ct][1] += 1
            elif row[4] == 'Medium':
                td[tt][2] += 1
                cd[ct][2] += 1
            elif row[4] == 'High':
                td[tt][3] += 1
                cd[ct][3] += 1


headerT = ['tissue', 'not detected ramp', 'low ramp', 'medium ramp', 'high ramp', 'not detected no ramp',
           'low no ramp', 'medium no ramp', 'high no ramp']
headerC = ['cell type', 'not detected ramp', 'low ramp', 'medium ramp', 'high ramp', 'not detected no ramp',
           'low no ramp', 'medium no ramp', 'high no ramp']

with open("tissueExpressionCounts.csv", 'w') as tissue_csv_file, open("trashcellTypeExpressionCounts.csv", 'w') as cell_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(headerT)
    for tis, rnums in tdr.items():
        nnums = td[tis]
        writerT.writerow([tis, rnums[0], rnums[1], rnums[2], rnums[3], nnums[0], nnums[1], nnums[2], nnums[3]])
    print(cd)
    writerC = csv.writer(cell_csv_file)
    writerC.writerow(headerC)
    for cell, rnums in cdr.items():
        nnums = cd[cell]
        writerC.writerow([cell, rnums[0], rnums[1], rnums[2], rnums[3], nnums[0], nnums[1], nnums[2], nnums[3]])
