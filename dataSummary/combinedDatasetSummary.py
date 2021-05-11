import sys

cosnensusFile = sys.argv[1]
fantomFile = sys.argv[2]
gtexFile = sys.argv[3]
hpaFile = sys.argv[4]
fullAnalysis = sys.argv[5]

# 1 = same as consensus
# 0 = different from consensus
# -1 = not found in file

# make ramp and no ramp sets for each file
cRamp = set()
cNoRamp = set()
gRamp = set()
gNoRamp = set()
hRamp = set()
hNoRamp = set()
fRamp = set()
fNoRamp = set()

# row[1] = gene, row[2] = tissue, row[6] = ramp presence
with open(gtexFile) as gFile:
    for line in gFile:
        row = line.rstrip().split(",")
        if row[6] == "Ramp":
            gRamp.add((row[1], row[2]))
        else:
            gNoRamp.add((row[1], row[2]))

with open(hpaFile) as hFile:
    for line in hFile:
        row = line.rstrip().split(",")
        if row[6] == "Ramp":
            hRamp.add((row[1], row[2]))
        else:
            hNoRamp.add((row[1], row[2]))

with open(fantomFile) as fFile:
    for line in fFile:
        row = line.rstrip().split(",")
        if row[6] == "Ramp":
            fRamp.add((row[1], row[2]))
        else:
            fNoRamp.add((row[1], row[2]))


def isRampMatch(searchTuple, rampPres, fileRamp, fileNoRamp):
    if rampPres == "Ramp":
        if searchTuple in fileRamp:
            return 1
        elif searchTuple in fileNoRamp:
            return 0
        else:
            return -1
    else:
        if searchTuple in fileRamp:
            return 0
        elif searchTuple in fileNoRamp:
            return 1
        else:
            return -1


header = "Gene,Genename,Tissue,NX,Expressionbin,Cosnensusramppresence,fantomRamp,gtexRamp,hpaRamp,Totalsupport%,Totalmatches,TotalFiles\n"
with open(cosnensusFile) as cFile, open(fullAnalysis, "w") as finalFile:
    finalFile.write(header)
    for line in cFile:
        row = line.rstrip().split(",")
        finalRow = [row[0], row[1], row[2], row[5], row[7], row[6]]
        sTuple = (row[1], row[2])
        finalRow.append(isRampMatch(sTuple, row[6], fRamp, fNoRamp))
        finalRow.append(isRampMatch(sTuple, row[6], gRamp, gNoRamp))
        finalRow.append(isRampMatch(sTuple, row[6], hRamp, hNoRamp))
        totFiles = 0
        totMatches = 0
        for i in range(6, 9):
            if finalRow[i] != -1:
                totFiles += 1
                totMatches += finalRow[i]
        if totFiles != 0:
            finalRow += [totMatches/totFiles, totMatches, totFiles]
        else:
            finalRow += [0, 0, 0]
        finalRow = [str(element) for element in finalRow]
        finalFile.write(",".join(finalRow))
        finalFile.write("\n")

