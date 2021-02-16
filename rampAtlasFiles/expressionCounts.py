import csv
import sys

bigFile = sys.argv[1]

tdr = {}
td = {}
# [not det, low, med, high]

with open(bigFile) as open1:
    for line in open1:
        row = line.rstrip().split(',')
        tt = row[2]

        if row[6] == 'Ramp':
            if tt not in tdr.keys():
                tdr[tt] = [0, 0, 0, 0]
 
            if row[7] == 'Not detected':
                tdr[tt][0] += 1
            elif row[7] == 'Low':
                tdr[tt][1] += 1
            elif row[7] == 'Medium':
                tdr[tt][2] += 1
            elif row[7] == 'High':
                tdr[tt][3] += 1

        else:
            if tt not in td.keys():
                td[tt] = [0, 0, 0, 0]

            if row[7] == 'Not detected':
                td[tt][0] += 1
            elif row[7] == 'Low':
                td[tt][1] += 1
            elif row[7] == 'Medium':
                td[tt][2] += 1
            elif row[7] == 'High':
                td[tt][3] += 1


headerT = ['tissue', 'not detected ramp', 'low ramp', 'medium ramp', 'high ramp', 'not detected no ramp',
           'low no ramp', 'medium no ramp', 'high no ramp']

with open("tissueExpressionCountsGTEX.csv", 'w') as tissue_csv_file:
    writerT = csv.writer(tissue_csv_file)
    writerT.writerow(headerT)
    for tis, rnums in tdr.items():
        nnums = td[tis]
        writerT.writerow([tis, rnums[0], rnums[1], rnums[2], rnums[3], nnums[0], nnums[1], nnums[2], nnums[3]])

