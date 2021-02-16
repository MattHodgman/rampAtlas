import re
tissues = ["adrenal gland", "appendix", "bone marrow", "breast", "bronchus",
           "caudate", "cerebellum", "cerebral cortex", "cervix| uterine", "colon", "duodenum",
           "endometrium 1", "endometrium 2", "epididymis", "esophagus", "fallopian tube", "gallbladder",
           "heart muscle", "hippocampus", "kidney", "liver", "lung", "lymph node",
           "nasopharynx", "oral mucosa", "pancreas", "parathyroid gland", "placenta",
           "prostate", "rectum", "salivary gland", "seminal vesicle", "skin 1",
           "skin 2", "small intestine", "soft tissue 1", "spleen",
           "stomach 1", "stomach 2", "testis", "thyroid gland", "tonsil",
           "urinary bladder", "vagina"]
tissuesNoSpace = ["adrenal_gland", "appendix", "bone_marrow", "breast", "bronchus",
           "caudate", "cerebellum", "cerebral_cortex", "cervix_uterine", "colon", "duodenum",
           "endometrium_1", "endometrium_2", "epididymis", "esophagus", "fallopian_tube", "gallbladder",
           "heart_muscle", "hippocampus", "kidney", "liver", "lung", "lymph_node",
           "nasopharynx", "oral_mucosa", "pancreas", "parathyroid_gland", "placenta",
           "prostate", "rectum", "salivary_gland", "seminal_vesicle", "skin_1",
           "skin_2", "small_intestine", "soft_tissue_1", "spleen",
           "stomach_1", "stomach_2", "testis", "thyroid_gland", "tonsil",
           "urinary_bladder", "vagina"]
gd = {}
td = {}

for tissue in tissuesNoSpace:
    td[tissue] = set()

# 1: gene | 2: tissue | 3: cell type | 4: expression | 5: certainty
with open('normal_tissue.csv') as csv_file:
    for line in csv_file:
        row = line.rstrip().split(",")
        cellType = "_".join(row[3].split())
        if row[5] != "Uncertain":
            if row[4] == "High":
                if row[2] in tissues:
                    td[tissuesNoSpace[tissues.index(row[2])]].add(cellType)
                    if row[1] in gd.keys():
                        if tissues.index(row[2]) in gd[row[1]].keys():
                            gd[row[1]][tissues.index(row[2])].append(cellType)
                        else:
                            gd[row[1]][tissues.index(row[2])] = [cellType]
                    else:
                        gd[row[1]] = {tissues.index(row[2]): [cellType]}

# outputList = []
# for tissueIndex in range(len(tissuesNoSpace)):
#     for cellType in td[tissues[tissueIndex]]:
#         outputList.append(open('cellTypeGenes/' + tissuesNoSpace[tissueIndex] + '/' + cellType + '.fa', 'w'))

outputDict = {}
for tissue in td.keys():
    outputDict[tissue] = {}

for tissue in td.keys():
    for cellType in td[tissue]:
        outputDict[tissue][cellType] = (open('cellTypeGenes/' + tissue + '__' + cellType + '.fa', 'w'))

print(outputDict)
genelist = []
with open('GRCh38_latest_genomic_longest_isoforms.fa', 'r') as genome:
    for line in genome:
        txt = re.compile("gene=([^;\n]*)")
        geneRegex = txt.search(line)
        gene = geneRegex.group(1)
        genelist.append(gene)
        strToWrite = line + genome.readline()

        if gene in gd.keys():
            tisDict = gd[gene]
            for tis, ctList in tisDict.items():
                for ct in ctList:
                    outputDict[tissuesNoSpace[tis]][ct].write(strToWrite)

print(genelist)
print(gd.keys())
print([value for value in genelist if value in gd.keys()])
for tis, cellTypeList in outputDict.items():
    for ct in cellTypeList:
        outputDict[tis][ct].close()
