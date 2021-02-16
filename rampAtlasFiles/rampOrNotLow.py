import sys

args = sys.argv
genes = []
with open("normal_tissue.csv", 'r') as geneFile:
    for line in geneFile:
        genes.append("gene=" + line.lstrip().split(",")[1] + ";")

genes = list(set(genes))
print(len(genes))

lowGeneRamp = []
lowGeneNoRamp = []
for gene in genes:
    tisExp = {}
    ramp = []
    noRamp = []
    with open("normal_tissue.csv", 'r') as normTissue:
        for line in normTissue:
            row = line.rstrip().split(",")
            if row[1] == gene[5:-1]:
                if row[3] in tisExp.keys():
                    tisExp[row[3]].append(row[4])
                else:
                    tisExp[row[3]] = [row[4]]

    valid = True
    for exp in tisExp.values():
        if ("High" in exp and "Low" in exp) or ("High" in exp and "Medium" in exp):
            valid = False
    
    if valid:
        for filename in args[1:]:
            with open(filename, 'r') as file:
                for line in file:
                    if "txt" in filename:
                        if gene in line:
                            noRamp.append(filename.split(".")[0][10:])
                    elif "fasta" in filename:
                        if gene in line:
                            ramp.append(filename.split(".")[0][10:])
        if len(ramp) != 0 and len(noRamp) != 0:                    
            print(gene[5:-1])
            print("no ramp: ")
            print(set(noRamp))
            if len(noRamp) != 0:
                lowGeneNoRamp.append(gene[5:-1])
            print("ramp: ")
            print(set(ramp))
            if len(ramp) != 0:
                lowGeneRamp.append(gene[5:-1])

print("genes no ramps")
print(lowGeneNoRamp)
print("genes ramps")
print(lowGeneRamp)

