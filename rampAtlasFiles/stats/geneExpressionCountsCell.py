import sys
import csv

inputFile = sys.argv[1]

rampD = {}
# [RND, RL, RM, RH, NND, NL, NM, NH]
percentD = {}


with open(inputFile) as open1:
    for line in open1:
        row = line.split(',')
        geneName = row[1]
        exp = row[4]
        if geneName not in rampD.keys():
            rampD[geneName] = [0, 0, 0, 0, 0, 0, 0, 0]

        if row[6] == 'Y\n':
            if exp == 'High':
                rampD[geneName][3] += 1
            elif exp == 'Medium':
                rampD[geneName][2] += 1
            elif exp == 'Low':
                rampD[geneName][1] += 1
            elif exp == 'Not detected':
                rampD[geneName][0] += 1
        elif row[6] == 'N\n':
            if exp == 'High':
                rampD[geneName][7] += 1
            elif exp == 'Medium':
                rampD[geneName][6] += 1
            elif exp == 'Low':
                rampD[geneName][5] += 1
            elif exp == 'Not detected':
                rampD[geneName][4] += 1


header = ['gene', "RND", "RL", "RM", "RH", "NND", "NL", "NM", "NH", "R total", "gene total"]

rampTotal = 0
geneTotal = 0
with open("geneExpressionCountsSpreadCellTypeCAI.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    for gene, nums in rampD.items():
        geneTotal = sum(nums)
        rampTotal = sum(nums[0:4])

        writer.writerow([gene, nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], rampTotal, geneTotal])
