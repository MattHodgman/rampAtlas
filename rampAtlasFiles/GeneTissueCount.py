import csv
tissues = ["N/A", "adipose tissue", "adrenal gland", "appendix", "bone marrow", "breast", "bronchus", "cartilage",
           "caudate", "cerebellum", "cerebral cortex", "cervix| uterine", "choroid plexus", "colon", "dorsal raphe", "duodenum",
           "endometrium 1", "endometrium 2", "epididymis", "esophagus", "eye", "fallopian tube", "gallbladder", "hair",
           "heart muscle", "hippocampus", "hypothalamus", "kidney", "lactating breast", "liver", "lung", "lymph node",
           "nasopharynx", "oral mucosa", "ovary", "pancreas", "parathyroid gland", "pituitary gland", "placenta",
           "prostate", "rectum", "retina", "salivary gland", "seminal vesicle", "skeletal muscle", "skin", "skin 1",
           "skin 2", "small intestine", "smooth muscle", "soft tissue 1", "soft tissue 2", "sole of foot", "spleen",
           "stomach 1", "stomach 2", "substantia nigra", "testis", "thymus", "thyroid gland", "tonsil",
           "urinary bladder", "vagina"]
td = {}

for tis in tissues:
    td[tis] = [0, 0, 0]

with open('normal_tissue.csv') as csv_file:
    for line in csv_file:
        row = line.rstrip().split(",")
        if row[5] != "Uncertain":
            if row[4] == "High":
                td[row[2]][0] += 1
            elif row[4] == "Medium":
                td[row[2]][1] += 1
            elif row[4] == "Low":
                td[row[2]][2] += 1

header = ['tissue', 'high', 'medium', 'low']
with open("tissueCounts.csv", 'w') as cohen_csv_file:
    writer = csv.writer(cohen_csv_file)
    writer.writerow(header)
    for tissue, counts in td.items():
        writer.writerow([tissue, counts[0], counts[1], counts[2]])
