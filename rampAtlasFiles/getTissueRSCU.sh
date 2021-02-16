#! /usr/local/bin/bash

TISSUELIST="cellTypeGenes_list"
module load python/3.7
while read -r TISSUE
 do 
    python3 ExtRamp_modified.py -i cellTypeGenes/${TISSUE} -u GRCh38_latest_genomic_longest_isoforms.fa -o garbage_tissue_out/${TISSUE} > cellTypeGenes_tAI_values/tAI_${TISSUE}.csv
done < "$TISSUELIST"


