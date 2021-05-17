import re
import os.path
import sys

covidFile = sys.argv[1]

tissues = []
with open("../consensus/tissue_list.txt", "r") as tissues_file:
    for line in tissues_file:
        tissues.append(line.strip())

covidGenes = set()
with open(covidFile) as covid_fa:
    line = covid_fa.readline()
    while line != "":
        covidGenes.add(line)
        covid_fa.readline()
        line = covid_fa.readline()

tissueRampsDict = {}
tissueNoRampDict = {}
for tissue in tissues:
    tissueRampsDict[tissue] = set()
    tissueNoRampDict[tissue] = set()

for tissue in tissues:
    if os.path.isfile("tissueExtRes/" + tissue + ".fa_ramps"):
        with open("tissueExtRes/" + tissue + ".fa_ramps") as ramp_file:
            line = ramp_file.readline()
            while line != "":
                tissueRampsDict[tissue].add(line)
                ramp_file.readline()
                line = ramp_file.readline()

for tissue in tissues:
    if os.path.isfile("tissueExtRes/" + tissue + ".fa_no_ramp"):
        with open("tissueExtRes/" + tissue + ".fa_no_ramp") as no_ramp_file:
            line = no_ramp_file.readline()
            while line != "":
                tissueNoRampDict[tissue].add(line)
                line = no_ramp_file.readline()

final = open('covid_ramps_better.csv', 'w')
uncertain = open('unclassified_covid_ramps.csv', 'w')

final.write("gene,tissue,ramp presence\n")
uncertain.write("gene,tissue,ramp presence\n")
# 1: gene | 2: tissue | 3: ramp

for tissue in tissues:
    ramps = tissueRampsDict[tissue].intersection(covidGenes)
    for gene in ramps:
        line = gene[1:-1] + "," + tissue + ",Ramp\n"
        final.write(line)
    no_ramps = tissueNoRampDict[tissue].intersection(covidGenes)
    for gene in no_ramps:
        line = gene[1:-1] + "," + tissue + ",No ramp\n"
        final.write(line)
    classified_seq = ramps.union(no_ramps)
    unclassified_seq = covidGenes.difference(classified_seq)
    for gene in unclassified_seq:
        line = gene[1:-1] + "," + tissue + ",Uncertain\n"
        uncertain.write(line)

uncertain.close()
final.close()
