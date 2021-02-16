import re
import os.path


def checkInRamp(tisType, curGene):
    g = re.compile("gene=" + curGene + "[;\n]")
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
with open("tissue_list.txt", "r") as tissues_file:
    for line in tissues_file:
        tissues.append(line.strip())

final = open('consensus_ramp.csv', 'w')
final.write("Gene,Genename,Tissue,NX,Ramp Presence\n")
# 1: gene | 2: tissue | 3: ramp

# make covid file of it's "gene names" and human tissues it was tested on to add ramp/not
with open('rna_tissue_consensus.csv') as covid_csv:
    covid_csv.readline()
    for line in covid_csv:
        line = line.strip()
        gene = line.split(",")[1]
        tissue = line.split(",")[2]
        #txt = re.compile(">([^\\s]*)")
        #geneRegex = txt.search(line)
        #gene = geneRegex.group(1)
        inRamp = checkInRamp(tissue, gene)
        if inRamp == 1:
            line = line.rstrip() + ",Ramp\n"
            final.write(line)
        elif inRamp == 0:
            line = line.rstrip() + ",No ramp\n"
            final.write(line)
        else:
            line = line.rstrip() + ",Uncertain\n"
            final.write(line)

final.close()
