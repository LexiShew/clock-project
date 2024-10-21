Clock Gene Project
==================

# Goal
Eventually this might be used to indicate which proteins in the clock pathway interact and would be good candidates for cancer drug treatment stuff

# To Do
* like actually write README
* turn in to Jupyter NB?
* figure out what cancer hallmarks are
* document files...

* plot hist of RF and AF values
* AF3
    * compare to multimer
    * follow their process from AF2
    * get seqs
    * AF3 API
        * pick non-interacting pairs
        * pick interacting pairs

# Files
## Data
* `RF_scores`: all pairwise PPI scores for the entire human proteome? maybe?
    * downloaded from https://conglab.swmed.edu/humanPPI/humanPPI_download.html, RF2-PPI_scores.zip
    * tab-separated format

## Helper files
* `clock_uniprot_codes.csv`: UniProt codes for the 14 core clock genes
* `clock_RF_scores.csv`: the PPI scores for all the pairwise core clock proteins found in `RF_scores` 
* `clock_RF_score_matrix_unsorted.csv`: matrix of clock genes with their RF scores, non-alphabetized but formatted nicely
* `clock_RF_score_matrix_sorted.csv`: matrix of clock genes with their RF scores, alphabetized but icky formatting 

## Scripts
* `get-clock-pairwise-PPI-scores.py`: creates `clock_RF_scores.csv` from `RF_scores`
* `create-pairwise-table.py`: uses `clock_RF_scores.csv` to create `clock_RF_score_matrix_unsorted.csv` and `clock_RF_score_matrix_sorted.csv`
* `generate-clock-heatmap.py`: creates heatmap image of RF clock protein PPI scores
* `get-core-clock-PPI-scores.sh`: runs everything to get heatmap
    * run with `sh get-core-clock-PPI-scores.sh`

## Output
* `clock-heatmap.png`: heatmap of RF scores between core clock proteins

## Miscellaneous
`clock_RF_score_matrix_unsorted_pretty.txt`: readable version of `clock_RF_score_matrix_unsorted.csv`
`clock_RF_score_matrix_sorted_pretty.txt`: readable version of `clock_RF_score_matrix_sorted.csv`

# Dependencies
* pandas
* seaborn

# Progress
## 10/09/24
* got clock protein interaction scores from AlphaFold interaction scores  

## 10/08/24
* created the following files:
    * clock_RF_score_matrix_sorted.csv
    * clock_RF_score_matrix_unsorted.csv
    * clock_RF_scores.csv
    * clock_uniprot_codes.csv
    * clock-heatmap.png
    * create-pairwise-table.py
    * generate-clock-heatmap.py
    * get-clock-pairwise-PPI-scores.py
    * get-core-clock-PPI-scores.sh