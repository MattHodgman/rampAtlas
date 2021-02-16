import re
import os.path


def checkInRamp(tisType, curGene):
    g = re.compile(">" + curGene + "\\s")
    if os.path.isfile("tissueExtRes/" + "high_" + tisType + ".fa_ramps"):
        with open("tissueExtRes/" + "high_" + tisType + ".fa_ramps") as search_file:
            if re.search(g, search_file.read()):
                return 1
    if os.path.isfile("tissueExtRes/" + "high_" + tisType + ".fa_no_ramp"):
        with open("tissueExtRes/" + "high_" + tisType + ".fa_no_ramp") as search_file:
            if re.search(g, search_file.read()):
                return 0
    return -1


tissues = []
with open("../consensus/tissue_list.txt", "r") as tissues_file:
    for line in tissues_file:
        tissues.append(line.strip())

final = open('covid_rampsPractice.csv', 'w')
final.write("gene,tissue,ramp presence\n")
# 1: gene | 2: tissue | 3: ramp

# make covid file of it's "gene names" and human tissues it was tested on to add ramp/not
with open('covid_Nov_4_2020.fasta') as covid_fa:
    line = covid_fa.readline()
    while line != "":
        seq = covid_fa.readline()
        txt = re.compile(">([^\\s]*)")
        geneRegex = txt.search(line)
        gene = geneRegex.group(1)
        for tissueType in tissues:
            inRamp = checkInRamp(tissueType, gene)
            if inRamp == 1:
                line = gene + "," + tissueType + ",Ramp\n"
                final.write(line)
            elif inRamp == 0:
                line = gene + "," + tissueType + ",No ramp\n"
                final.write(line)
            else:
                line = gene + "," + tissueType + ",U\n"
                final.write(line)
        line = covid_fa.readline()

final.close()
