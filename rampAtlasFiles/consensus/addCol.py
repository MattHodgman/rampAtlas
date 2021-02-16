import sys

inFile = sys.argv[1]

with open(inFile) as file1, open("rampOrNotClean2.csv", "w") as file2:
    for line in file1:
        row = line.split(",")
        r1 = ",".join(row[0:3])
        r2 = ",".join(row[3:])
        rcomb = r1 + ",,," + r2
        file2.write(rcomb)

