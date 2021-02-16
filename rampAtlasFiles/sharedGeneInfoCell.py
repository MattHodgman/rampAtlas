import csv

tissueGeneDict = {}
# tis = {genes}
rampGeneDict = {}
# tis = {genes with ramps}

with open("normal_tissue_withoutU.csv") as fullList:
    for line in fullList:
        row = line.split(',')
        tissueType = row[3].lower() + " in " + row[2]

        if tissueType not in tissueGeneDict.keys():
            tissueGeneDict[tissueType] = {row[1]}
        else:
            tissueGeneDict[tissueType].add(row[1])
        if row[6] == 'Y\n':
            if tissueType not in rampGeneDict.keys():
                rampGeneDict[tissueType] = {row[1]}
            else:
                rampGeneDict[tissueType].add(row[1])

resultLists = []

tissueList = list(rampGeneDict.keys())
tissueList.sort()
print(tissueList)
tissueList2 = [tis for tis in tissueList]
for tis1 in tissueList:
    for tis2 in tissueList2:
        ramp1 = rampGeneDict[tis1] & tissueGeneDict[tis2]
        ramp2 = rampGeneDict[tis2] & tissueGeneDict[tis1]
        common = len(ramp1 & ramp2)
        total = len(ramp1 | ramp2)
        preTotal = len(rampGeneDict[tis1] | rampGeneDict[tis2])
        if total > 900:
            resultLists.append([tis1, tis2, (common / total), common, total, preTotal])
    tissueList2.pop(0)

header = ['cell in tissue 1', 'cell in tissue 2', 'percent common ramps', 'ramps in common', 'any gene with ramp', 'total ramps no cut']

with open("sharedGeneInfoCellCap.csv", 'w') as tissue_csv_file:
    writer = csv.writer(tissue_csv_file)
    writer.writerow(header)
    for result in resultLists:
        writer.writerow(result)

