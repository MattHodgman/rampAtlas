with open("rna_tissue_hpa.csv") as old, open("noZero", 'w') as newF:
    for line in old:
        row = line.rstrip().split(",")
        if row[5] != "0.0":
            newF.write(line)

