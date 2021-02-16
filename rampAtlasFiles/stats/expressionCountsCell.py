import csv

cdr = {}
cd = {}
# [not det, low, med, high]

with open("../normal_tissue_withoutU.csv") as open1:
    for line in open1:
        row = line.split(',')
        ct = row[3] + " in " + row[2]

        if row[6] == 'Y\n':
            if ct not in cdr.keys():
                cdr[ct] = [0, 0, 0, 0]
 
            if row[4] == 'Not detected':
                cdr[ct][0] += 1
            elif row[4] == 'Low':
                cdr[ct][1] += 1
            elif row[4] == 'Medium':
                cdr[ct][2] += 1
            elif row[4] == 'High':
                cdr[ct][3] += 1

        else:
            if ct not in cd.keys():
                cd[ct] = [0, 0, 0, 0]
 

            if row[4] == 'Not detected':
                cd[ct][0] += 1
            elif row[4] == 'Low':
                cd[ct][1] += 1
            elif row[4] == 'Medium':
                cd[ct][2] += 1
            elif row[4] == 'High':
                cd[ct][3] += 1


headerC = ['cell type', 'not detected ramp', 'low ramp', 'medium ramp', 'high ramp', 'not detected no ramp',
           'low no ramp', 'medium no ramp', 'high no ramp']

with open("speadCellTypeExpressionCounts.csv", 'w') as cell_csv_file:
    writerC = csv.writer(cell_csv_file)
    writerC.writerow(headerC)
    for cell, rnums in cdr.items():
        nnums = cd[cell]
        writerC.writerow([cell, rnums[0], rnums[1], rnums[2], rnums[3], nnums[0], nnums[1], nnums[2], nnums[3]])
