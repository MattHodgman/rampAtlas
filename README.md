# rampAtlas
Code used to retrieve, organize, and analyze data for the Ramp Atlas.  
  
All datasets downloaded from the Human Protein Atlas were modified into Comma Seperated Values files (CSVs).  
Each dataset was formatted "Gene, Gene Name, Tissue, na, na, Normalized Expression"  
After processeing, the final files also included ", Ramp Presence, Expression Bin"  
These files will be reffered to as "Ramp Presence CSV" in the following input/output explanations.
  
  
**Extract Ramps Directory**  
*highGenes.py*  
input: original dataset CSV  
output: files containing all genes in the top expression quartile for every tissue/cell-type  
  
*rampOrNot.py* and *covidRampOrNot.py*  
input: *rn it hard codes input so prolly change that* original CSV  
output: original CSV with added "Ramp Presence" column  
  
*splitDoubleLines.py*  
input: *rn it hard codes input so prolly change that* output of rampOrNot.py  
output: genes represented by multiple isoforms in a single tissue/cell-type are seperated one line per isoform  
  
*addExpressionBins.py*  
input: output CSV file from splitDoubleLines.py; name for new output file  
output: original CSV file with added Ramp Presence and Expression Bin columns. Expression bins are based on 
quartile of expression, labeled Not detected, Low, Medium, and High  
  
*removeConflictingIsoforms.py*  
input: output of addExpressionBins.py  
output: the input CSV with all isoforms with conflicting ramp presence for the same gene removed. This is the final Ramp Presence CSV  
  
   
**Data Summary Directory**  
*geneAndRampTotal.py*  
input: Ramp Presence CSV  
output: total counts of genes and ramps per tissue and cell type, useful for dataset-wide chi-squared tests and pairwise z-tests  
  
*combinedDatasetSummary.py*  
input: cosnensus Ramp Presence CSV; FANTOM5 Ramp CSV; GTEx Ramp CSV; HPA Ramp CSV; name of output file  
output: CSV of "Gene, Genename, Tissue, NX, Expression bin, Cosnensus ramp presence, FANTOM5 Ramp, GTEx Ramp, HPA Ramp, Total support %, Total matches, Total files" where total files is the number of datasets including that gene in that tissue, total matches is the number of datasets with ramp presence consistent with the consensus dataset, and Total support % = Total matches / Total files 
  
*rampCountByExpressionAndTissues.py*  
input: Ramp Presence CSV  
output: counts of ramps across expression bins (Not detected, low, med, high) for each tissue/cell-type  
  
*rampCountByExpressionAndGenes.py*  
input: Ramp Presence CSV  
output: counts of ramps across expression bins (Not detected, low, med, high) for each gene  
  
  
**Z-Test Directory**  
*pairwiseZTest.py*  
input: output of geneAndRampTotal.py   
output: 
  
  
*ZTestSummary.py*  
input: output of geneAndRampTotal.py; number of tissue/cell-type pairs (number of tissues-1 FANTOM5=44, GTEx=33, HPA=42, consensus=61, cell=65); output of pairwiseZtest.py  
output: CSV of "Tissue, Total genes, Total ramps, Significant pairs, Percent significant pairs"  
