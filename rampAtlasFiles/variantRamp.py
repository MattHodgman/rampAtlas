import re
import sys
import csv
infile = sys.argv[1]
outfile = sys.argv[2]
cell_tissue_type = sys.argv[3].split(".")[0][4:]
geneListFile = sys.argv[4]

rampList = []
geneList = []

# make list of genes found to have a ramp by extRamp's .fa output
with open(infile, 'r') as ramps:
    for line in ramps:
        txt = re.compile("ALLELE_ID=([^;\n]*)")
        geneRegex = txt.search(line)
        try:
            gene = geneRegex.group(1)
            rampList.append(gene)
            ramps.readline()
        except:
            print(line)

# find original genes and map them to their variants
with open(geneListFile, 'r') as glf:
    for line in glf:
        geneList.append(line.strip())

gd = {}
for gene in geneList:
    # depending on how matt names them
    if "ref" in gene:
        gd[gene[:-4]] = []

for origGene in gd.keys():
    for gene in geneList:
        if origGene in gene:
            gd[origGene].append(gene)

header = ["Name", "Ramp", "Same as gene", "cell/tissue type"]
with open(outfile, 'w') as csv_file:
    writerT = csv.writer(csv_file)
    writerT.writerow(header)
    for origGene, variants in gd.items():
        origGeneRamp = (origGene + "_ref") in rampList

        for variant in variants:
            varRamp = variant in rampList
            same = varRamp == origGeneRamp
            writerT.writerow([variant, varRamp, same, cell_tissue_type])
