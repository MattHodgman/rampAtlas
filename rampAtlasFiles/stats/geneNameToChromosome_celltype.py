import sys

geneNameToChromosome = sys.argv[1]
outputFile = sys.argv[2]

genesRead = set()

with open(geneNameToChromosome) as open1, open(outputFile,"w") as open2:
	for line in open1:
		line = line.strip()
		lineList = line.split("\t")
		inputGene = lineList[12]
		if inputGene not in genesRead:
			open2.write(line)
			open2.write("\n")
			genesRead.add(inputGene)
				
