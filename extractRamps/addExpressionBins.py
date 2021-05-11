import sys

csvFile = sys.argv[1]
newFile = sys.argv[2]

with open(csvFile) as genes_fa:
    genes_fa.readline()
    line = genes_fa.readline()
    expressions = []
    while line != "":
        row = line.rstrip().split(',')
        expressions.append(float(row[5]))
        line = genes_fa.readline()
expressions.sort()
#lowToHighExp = [value for value in expressions if value != 0]
lowGeneMinNX = expressions[int((1 / 4) * len(expressions))]
medGeneMinNX = expressions[int((1 / 2) * len(expressions))]
highGeneMinNX = expressions[int((3 / 4) * len(expressions))]

print(medGeneMinNX)
print(highGeneMinNX)

with open(csvFile) as old_file, open(newFile, "w") as new_file:
    header = old_file.readline()
    new_file.write(header)
    line = old_file.readline()
    while line != "":
        row = line.rstrip().split(',')
        if float(row[5]) >= highGeneMinNX:
            new_file.write(line.rstrip() + ",High\n")
        elif float(row[5]) >= medGeneMinNX:
            new_file.write(line.rstrip() + ",Medium\n")
        elif float(row[5]) >= lowGeneMinNX:
            new_file.write(line.rstrip() + ",Low\n")
        else:
            new_file.write(line.rstrip() + ",Not detected\n")
        line = old_file.readline()

