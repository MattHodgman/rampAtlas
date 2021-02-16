import re
import os.path

tissues = []
with open("tissue_list.txt", "r") as tissues_file:
    for line in tissues_file:
        tissues.append(line.strip())

genes = set()
badGenes = []
lineDict = {}
for tissue in tissues:
    lineDict[tissue] = {}
with open('rna_tissue_gtex.csv') as genes_fa:
    header = genes_fa.readline().rstrip()
    line = genes_fa.readline()
    while line != "":
        row = line.rstrip().split(',')
        genes.add(row[1])
        if row[1] not in lineDict[row[2]].keys():
            lineDict[row[2]][row[1]] = line.rstrip()
        else:
            lineDict[row[2]][row[1]] += ("," +  line.rstrip())
            #print(row[2] + " " + row[1])
            badGeneFirstCopy = lineDict[row[2]][row[1]].split(',')[0]
            badGenes.append((badGeneFirstCopy, row[0]))

        line = genes_fa.readline()
print(set(badGenes))

tissueRampsDict = {}
tissueNoRampDict = {}
for tissue in tissues:
    tissueRampsDict[tissue] = set()
    tissueNoRampDict[tissue] = set()

for tissue in tissues:
    if os.path.isfile("tissueExtRes/" + tissue + ".fa_ramps"):
        with open("tissueExtRes/" + tissue + ".fa_ramps") as ramp_file:
            line = ramp_file.readline()
            while line != "":
                txt = re.compile("gene=([^;\n]*)")
                geneRegex = txt.search(line)
                gene = geneRegex.group(1)
                tissueRampsDict[tissue].add(gene)
                ramp_file.readline()
                line = ramp_file.readline()

for tissue in tissues:
    if os.path.isfile("tissueExtRes/" + tissue + ".fa_no_ramp"):
        with open("tissueExtRes/" + tissue + ".fa_no_ramp") as no_ramp_file:
            line = no_ramp_file.readline()
            while line != "":
                txt = re.compile("gene=([^;\n]*)")
                geneRegex = txt.search(line)
                gene = geneRegex.group(1)
                tissueNoRampDict[tissue].add(gene)
                line = no_ramp_file.readline()

final = open('rampOrNot.csv', 'w')
uncertain = open('unclassified_sequences_rampOrNot.csv', 'w')

# final is file with all info plus ramp presence
final.write(header + ",ramp presence\n")
# uncertain is file of sequences that could not be classified by extRamp
uncertain.write(header + ",ramp presence\n")

for tissue in tissues:
    ramps = tissueRampsDict[tissue].intersection(genes)
    for gene in ramps:
        if gene in lineDict[tissue].keys():
            line = lineDict[tissue][gene] + ",Ramp\n"
            final.write(line)
    no_ramps = tissueNoRampDict[tissue].intersection(genes)
    for gene in no_ramps:
        if gene in lineDict[tissue].keys():
            line = lineDict[tissue][gene] + ",No ramp\n"
            final.write(line)
    classified_seq = ramps.union(no_ramps)
    unclassified_seq = genes.difference(classified_seq)
    for gene in unclassified_seq:
        if gene in lineDict[tissue].keys():
            line = lineDict[tissue][gene] + ",Uncertain\n"
            uncertain.write(line)

uncertain.close()
final.close()
