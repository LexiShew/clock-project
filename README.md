# Clock Gene Project

# Goal

Eventually this might be used to indicate which proteins in the clock pathway interact and would be good candidates for cancer drug treatment stuff

# To Do

- explain all the freaking output files
- figure out what counts as significant
  - fit to exponential?
- AF predictions?
  - compare to multimer
  - follow their process from AF2
  - get seqs
  - AF3 API
    - pick non-interacting pairs
    - pick interacting pairs

# Files

## Data

- `data/RF_scores`: RoseTTAFold pairwise PPI prediction scores for the entire human proteome
  - downloaded from https://conglab.swmed.edu/humanPPI/humanPPI_download.html, RF2-PPI_scores.zip
  - tab-separated format
- `data/AF_scores`: AlphaFold score predictions for only about 6.7% of the RF data...
  - downloaded from https://conglab.swmed.edu/humanPPI/humanPPI_download.html
  - tab-separated format
- `output/clock_uniprot_codes.csv`: UniProt codes for the 14 core clock genes

## Output

- `output/clock_RF_scores.csv`: the PPI scores for all the pairwise core clock proteins found in `RF_scores`
- `output/clock_RF_score_matrix_unsorted.csv`: matrix of clock genes with their RF scores, non-alphabetized but formatted nicely
- `output/clock_RF_score_matrix_sorted.csv`: matrix of clock genes with their RF scores, alphabetized but icky formatting
- a million other files ugh

## Code

- `data-eploration.ipynb`: where the magic happens

# Dependencies

- pandas
- seaborn
- all the others? idk

# Progress

## 12/18

- added merged DF

## IDK

- made code prettier

## 10/09/24

- got clock protein interaction scores from AlphaFold interaction scores

## 10/08/24

- created the following files:
  - clock_RF_score_matrix_sorted.csv
  - clock_RF_score_matrix_unsorted.csv
  - clock_RF_scores.csv
  - clock_uniprot_codes.csv
  - clock-heatmap.png
  - create-pairwise-table.py
  - generate-clock-heatmap.py
  - get-clock-pairwise-PPI-scores.py
  - get-core-clock-PPI-scores.sh
