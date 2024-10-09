###############################################################################
#
#   get-clock-pairwise-PPI-scores.py
#
#   creates `clock_RF_scores.csv` from `RF_scores`
#
###############################################################################

import pandas as pd

clock_genes_uniprot_df = pd.read_csv("clock_uniprot_codes.csv")

codes = clock_genes_uniprot_df["uniprot_code"]
clock_pairs = [str(first_code) + "_" + str(second_code)
               for first_code in codes
               for second_code in codes]

RF_scores_df = pd.read_csv("RF_scores", sep='\t', header=None)
AF_scores_df = pd.read_csv("AF_scores", sep='\t', header=None)

# RF scores
clock_pairs_RF_scores_df = RF_scores_df[RF_scores_df[0].isin(clock_pairs)] 
clock_pairs_RF_scores_df.columns = ("gene_pairs", "score")
clock_pairs_RF_scores_df.sort_values(by=["gene_pairs"])

clock_pairs_RF_scores_df.to_csv('clock_RF_scores.csv', index=False)

# AF scores
clock_pairs_AF_scores_df = AF_scores_df[AF_scores_df[0].isin(clock_pairs)] 
clock_pairs_AF_scores_df.columns = ("gene_pairs", "score")
clock_pairs_AF_scores_df.sort_values(by=["gene_pairs"])

clock_pairs_AF_scores_df.to_csv('clock_AF_scores.csv', index=False)
