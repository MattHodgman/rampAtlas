import re
import sys

openfile = sys.argv[1]

genes = []
tissues = []
expressions = []
# row[1] = genename
# row[2] = tissue name
# row[3] = NX (expression)

with open(openfile) as tissue_file, open("../GRCh38_latest_genomic_longest_isoforms.fa") as genome:
    tissue_file.readline()
    for line in tissue_file:
        row = line.rstrip().split(',')
        genes.append([row[1], float(row[3]), row[2]])
        tissues.append(row[2])
        expressions.append(float(row[3]))
    tissues = set(tissues)
    tissues = list(tissues)
    expressions.sort()
    highGeneIndex = expressions[int((3/4)*len(expressions))]
    #lowGeneIndex = expressions[int((1/4)*len(expressions))]
    #print(lowGeneIndex)

    outputList = []
    for tissue in tissues:
        outputList.append('highGenesByTissue/' + tissue + '.fa')
    for out in outputList:
        open(out, "w").close()

    highGenes = {}
    for gene in genes:
        if gene[0] not in highGenes.keys():
            highGenes[gene[0]] = []
    for gene in genes:
        if gene[1] >= highGeneIndex:
            highGenes[gene[0]].append(gene[2])

    print("high genes found")
    
    geneList = []
    for line in genome:
        txt = re.compile("gene=([^;\n]*)")
        geneRegex = txt.search(line)
        gene = geneRegex.group(1)
        strToWrite = line + genome.readline()
        geneList.append(gene)

        if gene in highGenes.keys():
            for tissue in highGenes[gene]:
                file = open(outputList[tissues.index(tissue)], "a")
                file.write(strToWrite)
                file.close()

#print([val for val in geneList if val in highGenes.keys()])

