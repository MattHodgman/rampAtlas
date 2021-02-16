# gene, tissue, ramp presence

import sys

tissueFile = sys.argv[1]
bigFile = sys.argv[2]

tissues = []
with open(tissueFile) as allTis:
    for line in allTis:
        tissues.append(line.rstrip())

rampUse = {}
allGenes = {}
difDict = {}
for tissue in tissues:
    rampUse[tissue] = 0
    allGenes[tissue] = 0

with open(bigFile) as allLines:
    allLines.readline()
    for line in allLines:
        row = line.rstrip().split(",")
        allGenes[row[1]] += 1
        if row[2] == "Ramp":
            rampUse[row[1]] += 1
        if row[0] not in difDict.keys():
            difDict[row[0]] = set([row[2]])
        else:
            difDict[row[0]].add(row[2])

geneTot = 0
genesWithDif = 0

for gene in difDict.keys():
    geneTot += 1
    if len(difDict[gene]) == 2:
        genesWithDif += 1
print("total " + str(geneTot))
print("dif " + str(genesWithDif))
print("percent " + str(genesWithDif/geneTot))
print("\n")
print("tissue,total,ramps")
for tissue in tissues:
    print(tissue + "," + str(allGenes[tissue]) + "," + str(rampUse[tissue]))


