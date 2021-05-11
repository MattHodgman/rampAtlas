# rampAtlas
Code used to retrieve, organize, and analyze data for the Ramp Atlas.  
  
All datasets downloaded from the Human Protein Atlas were modified into Comma Seperated Values files (CSVs).  
Each dataset was formatted "Gene, Gene Name, Tissue, na, na, Normalized Expression"  
After processeing, the final files also included ", Ramp Presence, Expression Bin"  
  
  
**Extract Ramps Directory**  
*highGenes.py*  
input: original dataset csv  
output: files containing all genes in the top expression quartile for every tissue/cell type  
  
*rampOrNot.py* and *covidRampOrNot.py*  
input: *rn it hard codes input so prolly change that* original CSV  
output: original CSV with added "Ramp Presence" column  
  
*splitDoubleLines.py*  
input: *rn it hard codes input so prolly change that* output of rampOrNot.py  
output: genes represented by multiple isoforms in a single tissue are seperated one line per isoform  
  
*addExpressionBins.py*  
input: output CSV file from splitDoubleLines.py and name for new output file  
output: original CSV file with Ramp Presence and Expression Bin columns. Expression bins are based on 
quartile of expression, labeled Not detected, Low, Medium, and High  
  
*removeConflictingIsoforms.py*  
input: output of addExpressionBins.py which is the full CSV after processing  
output: same CSV but without any isoforms with conflicting ramp presence for the same gene  
  
   
**Data Summary Directory**  
*geneAndRampTotal.py*  
input:   
output:   
  
*combinedDatasetSummary.py*  
input:   
output:   
  
*rampCountByExpressionAndTissues.py*  
input:   
output:   
  
*rampCountByExpressionAndGenes.py*  
input:   
output:   
  
  
**Z-Test Directory**  
*pairwiseZTest.py*  
input:   
output:   
  
*ZTestSummary.py*  
input:   
output:   
