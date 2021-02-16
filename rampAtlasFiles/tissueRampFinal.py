import re
import os.path
tissues = ["adrenal gland", "appendix", "bone marrow", "breast", "bronchus",
           "caudate", "cerebellum", "cerebral cortex", "cervix| uterine", "colon", "duodenum",
           "endometrium 1", "endometrium 2", "epididymis", "esophagus", "fallopian tube", "gallbladder",
           "heart muscle", "hippocampus", "kidney", "liver", "lung", "lymph node",
           "nasopharynx", "oral mucosa", "pancreas", "parathyroid gland", "placenta",
           "prostate", "rectum", "salivary gland", "seminal vesicle", "skin 1",
           "skin 2", "small intestine", "soft tissue 1", "spleen",
           "stomach 1", "stomach 2", "testis", "thyroid gland", "tonsil",
           "urinary bladder", "vagina"]
tissuesNoSpace = ["adrenal_gland", "appendix", "bone_marrow", "breast", "bronchus",
           "caudate", "cerebellum", "cerebral_cortex", "cervix_uterine", "colon", "duodenum",
           "endometrium_1", "endometrium_2", "epididymis", "esophagus", "fallopian_tube", "gallbladder",
           "heart_muscle", "hippocampus", "kidney", "liver", "lung", "lymph_node",
           "nasopharynx", "oral_mucosa", "pancreas", "parathyroid_gland", "placenta",
           "prostate", "rectum", "salivary_gland", "seminal_vesicle", "skin_1",
           "skin_2", "small_intestine", "soft_tissue_1", "spleen",
           "stomach_1", "stomach_2", "testis", "thyroid_gland", "tonsil",
           "urinary_bladder", "vagina"]


def checkInRamp(tisType, curGene):
    g = re.compile("gene=" + curGene + "[;\n]")
    if os.path.isfile("tissueExtRes/" + tisType + ".fa_ramps"):
        with open("tissueExtRes/" + tisType + ".fa_ramps") as search_file:
            if re.search(g, search_file.read()):
                return 1
    if os.path.isfile("tissueExtRes/" + tisType + ".fa_no_ramp"):
        with open("tissueExtRes/" + tisType + ".fa_no_ramp") as search_file:
            if re.search(g, search_file.read()):
                return 0
    return -1


final = open('normal_tissue_final_2.csv', 'w')
# 1: gene | 2: tissue | 3: cell type | 4: expression | 5: certainty
with open('normal_tissue.csv') as tissue_csv:
    for line in tissue_csv:
        row = line.rstrip().split(",")
        print(row[1])
        if row[5] == "Uncertain" or row[2] not in tissues:
            line = line.rstrip() + ",U\n"
            final.write(line)
        else:
            tissueType = tissuesNoSpace[tissues.index(row[2])]
            inRamp = checkInRamp(tissueType, row[1])
            if inRamp == 1:
                line = line.rstrip() + ",Y\n"
                final.write(line)
            elif inRamp == 0:
                line = line.rstrip() + ",N\n"
                final.write(line)
            else:
                line = line.rstrip() + ",U\n"
                final.write(line)

final.close()
