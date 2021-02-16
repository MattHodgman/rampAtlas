import sys

inFile = sys.argv[1]

with open(inFile) as file1, open("rampOrNotClean.csv", "w") as file2:
    for line in file1:
        row = line.rstrip().split(",")
        if len(row) > 6:
            if row[8] == "No ramp":
                r1 = ",".join(row[0:4])
                r1 += ",No ramp\n"
                r2 = ",".join(row[4:])
                r2 += "\n"
                file2.write(r1)
                file2.write(r2)
            elif row[8] == "Ramp":
                r1 = ",".join(row[0:4])
                r1 += ",Ramp\n"
                r2 = ",".join(row[4:])
                r2 += "\n"
                file2.write(r1)
                file2.write(r2)
        else:
            file2.write(line)

