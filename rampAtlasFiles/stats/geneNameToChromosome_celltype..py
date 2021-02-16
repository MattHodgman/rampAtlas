import sys
import pandas as pd
import numpy as np

geneNameToChromosome = sys.argv[1]
outputFile = sys.argv[2]

genesRead = set()

df = pd.read_csv('geneNameToChromosome.txt', sep='\t')
df['-logp'] = - np.log(df['p-value'])

with open(geneNameToChromosome) as open1, open(outputFile,"w") as open2:
	for line in open1:
		line = line.strip()
		lineList = line.split("\t")
		inputGene = lineList[12]
		if inputGene not in genesRead:
			open2.write(line)
			open2.write("\n")
			genesRead.add(inputGene)
