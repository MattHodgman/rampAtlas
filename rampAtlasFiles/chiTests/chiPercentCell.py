# [Tissue/Cell, Total, Ramp] add percent significant comparisons
# [Tissue/Cell1, Tissue/Cell2, Chi, P]
# total = 34 for cell 43 for tissue

with open("../stats/spreadCellTypeTotalAndRamp.csv") as cell_file, open("spreadCellChiPercent.csv", 'w') as cell_write:
    header = cell_file.readline().rstrip() + ",significant pairs,percent sig pair\n"
    cell_write.write(header)
    totalPair = 65

    for line in cell_file:
        row = line.rstrip().split(',')
        sigPair = 0
        with open("spreadCellTypePairwiseChi.csv") as cell_pair:
            for part in cell_pair:
                pair = part.rstrip().split(',')
                if row[0] in pair and float(pair[3]) < .05:
                    sigPair += 1
        newLine = line.rstrip() + "," + str(sigPair) + "," + str(round(sigPair/totalPair * 100, 3)) + "\n"
        cell_write.write(newLine)

