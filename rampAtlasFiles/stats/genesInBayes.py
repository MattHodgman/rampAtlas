import sys

geneNameToChromosome = sys.argv[1]
bayes = sys.argv[2]
outputFile = sys.argv[3]

bayesGeneL = []
chromosomeGeneL = []
count = 0

with open(bayes) as open1:
	for line in open1:
		line = line.strip()
		lineList = line.split(",")
		gene = lineList[0]
		bayesGeneL.append(gene)

with open(geneNameToChromosome) as open2, open(outputFile) as open3:
	for line in open2:
		line = line.strip()
		lineList = line.split("\t")
		inputGene = lineList[12]
		chromosomeGeneL.append(inputGene)
	chromosomeGeneL = list(dict.fromkeys(chromosomeGeneL))
		
for gene in bayesGeneL:
	for toCompare in chromosomeGeneL:
		if gene == toCompare:			
			bayesGeneL.remove(gene)

with open(outputFile,'w') as open3:
	for gene in bayesGeneL:
		open3.write(str(gene))
		open3.write("\n")
		count = count + 1

print(count)
