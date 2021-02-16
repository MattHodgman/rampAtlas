import re
import sys
infile = sys.argv[1]
rampList = []
with open(infile, 'r') as ramps:
    for line in ramps:
        txt = re.compile("ALLELE_ID=([^;\n]*)")
        geneRegex = txt.search(str(line))
        gene = geneRegex.group(1)
        rampList.append(gene)
        ramps.readline()
    print(rampList)
