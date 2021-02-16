#!/usr/bin/env python3

import sys
from Bio import SeqIO

def get_next_semicolon(description):
    '''
    Returns the index of the next ';' in the gene description
    '''
    try:
        return description.index(';')
    except ValueError:
        return len(description)
    
# return list of nucleotides that the reference could mutate to
def get_nucleotide_mutations(ref_nucleotide):
    nucleotides = ['A','C','G','T']
    nucleotides.remove(ref_nucleotide.upper())
    return nucleotides

for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
    
    # get sequence info
    seq = str(seq_record.seq)
    description = seq_record.description
    geneName = description[description.find("gene=") + 5 : description.find("gene=") + 5 + get_next_semicolon(description[description.find("gene=") + 5 : ])]  # get gene name
    
    # parse nucleotides after start codon
    s = ''
    n = 3
    for ref_nucleotide in seq[3:]:
        seq_list = list(seq)
        for nucleotide in get_nucleotide_mutations(ref_nucleotide):
            print('>' + description[:-1] + '_' + str(n + 1) + ref_nucleotide.upper() + '>' + nucleotide + ';')
            #print('ALLELE_ID=' + geneName + '_ref_' + str(n + 1) + ref_nucleotide.upper() + '>' + nucleotide + ';')
            seq_list[n] = nucleotide
            print(s.join(seq_list))
            seq_list = list(seq)
        n += 1
