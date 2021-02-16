#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:31:51 2020

@author: matthodgman
"""
import re
import itertools
from Bio import SeqIO

ref_genome = 'GRCh38_latest_genomic_longest_isoforms.fa'
gene_dict = {'' ; {}}
#gene_dict = {'EXTL3' : {'417795' : '1970A>G', '417794' : '1382C>T', '417796' : '1015C>T'}}
'''
gene_dict = {'LYRM4' : {'102450' : '203G>T'}, 
             'PMPCB' : {'523138' : '523C>T', '523140' : '524G>A', '523141' : '530T>G', '523139' : '601G>C', '523142' : '1265T>C'},
             'ANK3' : {'918004' : '11033del', '88648' : '10995del', '872695' : '4365_4368del ', '802576' : '2659C>T'},
             'NHLRC2' : {'599377' : '442G>T', '599378' : '601_602del'},
             'LMAN1' : {'8065' : '1356del', '8064' : '796del', '8062' : '89dup', '8066' : '2T>C'},
             'POFUT1' : {'574378' : '289C>T', '56808' : '430G>T', '56809' : '482del'}}
'''

def get_next_semicolon(description):
    '''
    Returns the index of the next ';' in the gene description
    '''
    try:
        return description.index(';')
    except ValueError:
        return len(description)
    
def applyVariant(seq, effects):
    '''
    changes the gene sequence to include the variant
    '''
    
    for effect in effects:
        # standard nucleotide swap
        if re.search('\d+(?=[GTCA])', effect):
            location = int(re.search('\d+(?=[GTCA])', effect).group(0))
            ref = re.search('(?<=\d)[GTCA]*(?=>)', effect).group(0)
            var = re.search('(?<=>)[GTCA]*', effect).group(0)
            
            if seq[location - 1] == ref: # make sure reference nucleotides match
                seq = seq[:location - 1] + var + seq[location:] # apply nucleotide switch
            else:
                print('reference nucleotides do not match.', effect, seq)
            
        # single deletion
        elif re.search('(?<!.)\d+(?=del)', effect):
            location = int(re.search('\d+(?=del)', effect).group(0))
            seq = seq[:location - 1] + seq[location:] # remove nucleotide
        
        # range deletion 
        elif re.search('\d+(?=_)', effect):
            location_start = int(re.search('\d+(?=_)', effect).group(0))
            location_end = int(re.search('(?<=_)\d+(?=del)', effect).group(0))
            seq = seq[:location_start - 1] + seq[location_end:]
        
        # duplicate
        elif re.search('\d+(?=dup)', effect):
            location = int(re.search('\d+(?=dup)', effect).group(0))
            seq = seq[:location] + seq[location - 1] + seq[location:]
    
    return seq

# find every gene in the reference genome
for gene in gene_dict.keys():
    fasta_lines_to_write = []
    for seq_record in SeqIO.parse(ref_genome, "fasta"):
        description = seq_record.description # get gene description
        
        geneName = description[description.find("gene=") + 5 : description.find("gene=") + 5 + get_next_semicolon(description[description.find("gene=") + 5 : ])]  # get gene name
        
        # check if it is wanted gene
        if geneName == gene:
            seq = seq_record.seq # get gene sequence
    
            # make variant fasta descriptions and sequences
            # make every combination of variants
            for L in range(0, len(gene_dict[gene].keys())+1):
                for subset in itertools.combinations(gene_dict[gene].keys(), L):
                    
                    # make variant description
                    if len(subset) > 0:
                        description_var = description + ";ALLELE_ID=" + gene + "_"
                        # format variant list
                        for variant in subset:
                            description_var = description_var + variant + "_"
                        description_var = description_var[:-1] + ";"
                    else:
                        description_var = description + ";ALLELE_ID=" + gene + "_ref;"
                    
                    # apply variants to sequence
                    effects = []
                    for variant in subset:
                        effect = gene_dict[gene][variant]
                        effects.append(effect)
                    seq_var = applyVariant(seq, effects)
                    fasta_lines_to_write.append(description_var)
                    fasta_lines_to_write.append(seq_var)

    # write fasta file
    f = open(gene + ".fa", "a")
    for line in fasta_lines_to_write:
        f.write(str(line))
        f.write('\n')
    f.close()   
