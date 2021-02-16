import sys
import numpy as np
import pandas as pd

Bayes = sys.argv[1]
geneNameToChromosome = sys.argv[2]
outputFile = sys.argv[3]

bayesD = {}

with open(Bayes) as open1, open(geneNameToChromosome) as open2, open(outputFile,'w') as open3:
	for line in open1:
		line = line.strip()
		lineList = line.split(",")
		gene = lineList[0]
		pValue = lineList[4]
		bayesD[gene] = pValue	
	open3.write("chrom" + "\t" + "cdsStart" + "\t" + "gene" + "\t" + "p-value" + "\n")
	for line in open2:
		line = line.strip()
		lineList = line.split("\t")
		chrom = lineList[2]
		cdsStart = lineList[6]
		gene = lineList[12]
		if gene in bayesD:
			open3.write(chrom + "\t" + cdsStart + "\t" + gene)
			open3.write("\t" + bayesD[gene] + "\n")
	
	
df = pd.read_csv('txtForManhattan_tissue.txt', sep='\t')
df['-logp'] = - np.log(df['p-value'])
print(df)

