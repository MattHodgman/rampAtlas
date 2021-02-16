# [Tissue/Cell, Total, Ramp] add percent significant comparisons
# [Tissue/Cell1, Tissue/Cell2, Chi, P]
# total = 34 for cell 43 for tissue

import sys
import math

totAndRamp = sys.argv[1]
numPairs = int(sys.argv[2])
pairwiseFile = sys.argv[3]

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

with open(totAndRamp) as tis_file, open("tissueChiPercentCorrected.csv", 'w') as tis_write:
    header = tis_file.readline().rstrip() + ",significant pairs,percent sig pair\n"
    tis_write.write(header)
    totalPair = numPairs

    for line in tis_file:
        row = line.rstrip().split(',')
        sigPair = 0
        with open(pairwiseFile) as tis_pair:
            for part in tis_pair:
                pair = part.rstrip().split(',')
                print(nCr(numPairs+1,2))
                if row[0] in pair and float(pair[3]) < (.05/(nCr(numPairs + 1, 2))):
                    sigPair += 1
        newLine = line.rstrip() + "," + str(sigPair) + "," + str(round(sigPair/totalPair * 100, 3)) + "\n"
        tis_write.write(newLine)
