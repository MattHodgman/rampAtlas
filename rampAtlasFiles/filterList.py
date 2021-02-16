
s = []
output = open('filteredPercentExpected.csv', 'w')
with open("coolGeneSet.csv", 'r') as mySet, open("percentExpected.csv", 'r') as myList:
    for line in mySet:
        s.append(line.rstrip())
    print(s)
    for line in myList:
        row = line.split(',')
        print(line)
        if row[0] in s:
            output.write(line)

output.close()
