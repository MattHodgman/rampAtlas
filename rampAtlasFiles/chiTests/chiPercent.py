# [Tissue/Cell, Total, Ramp] add percent significant comparisons
# [Tissue/Cell1, Tissue/Cell2, Chi, P]
# total = 34 for cell 43 for tissue

with open("../stats/spreadCellTypeTotalAndRamp.csv") as cell_file, open("cellChiPercentCorrected.csv", 'w') as cell_write:
    header = cell_file.readline().rstrip() + ",significant pairs,percent sig pair\n"
    cell_write.write(header)
    totalPair = 65

    for line in cell_file:
        row = line.rstrip().split(',')
        sigPair = 0
        with open("spreadCellTypePairwiseChi.csv") as cell_pair:
            for part in cell_pair:
                pair = part.rstrip().split(',')
                if row[0] in pair and float(pair[3]) < (.05/2145):
                    sigPair += 1
        newLine = line.rstrip() + "," + str(sigPair) + "," + str(round(sigPair/totalPair * 100, 3)) + "\n"
        cell_write.write(newLine)


with open("../stats/tissueTotalAndRamp.csv") as tis_file, open("tissueChiPercentCorrected.csv", 'w') as tis_write:
    header = tis_file.readline().rstrip() + ",significant pairs,percent sig pair\n"
    tis_write.write(header)
    totalPair = 43

    for line in tis_file:
        row = line.rstrip().split(',')
        sigPair = 0
        with open("tissuePairwiseChi.csv") as tis_pair:
            for part in tis_pair:
                pair = part.rstrip().split(',')
                if row[0] in pair and float(pair[3]) < (.05/946):
                    sigPair += 1
        newLine = line.rstrip() + "," + str(sigPair) + "," + str(round(sigPair/totalPair * 100, 3)) + "\n"
        tis_write.write(newLine)
