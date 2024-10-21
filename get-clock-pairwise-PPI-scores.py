###############################################################################
#
#   get-clock-pairwise-PPI-scores.py
#
#   creates `clock_RF_scores.csv` from `RF_scores`
#
###############################################################################

import pandas as pd

clock_genes_uniprot_df = pd.read_csv("./data/clock_uniprot_codes.csv")
hallmark_genes_uniprot_df = pd.read_csv("./data/hallmark_uniprot_codes.csv")

clock_codes = clock_genes_uniprot_df["uniprot_code"] 
hallmark_codes = hallmark_genes_uniprot_df["uniprot_code"]
clock_pairs = [str(first_code) + "_" + str(second_code)
               for first_code in clock_codes
               for second_code in clock_codes]
clock_hallmark_pairs = [str(first_code) + "_" + str(second_code)
                                    for first_code in clock_codes
                                    for second_code in hallmark_codes] + \
                        [str(first_code) + "_" + str(second_code)
                                for first_code in hallmark_codes
                                for second_code in clock_codes]


RF_scores_df = pd.read_csv("./data/RF_scores", sep='\t', header=None)
AF_scores_df = pd.read_csv("./data/AF_scores", sep='\t', header=None)

# RF scores -- pairwise clock genes
clock_pairs_RF_scores_df = RF_scores_df[RF_scores_df[0].isin(clock_pairs)] 
clock_pairs_RF_scores_df.columns = ("gene_pairs", "score")
clock_pairs_RF_scores_df.sort_values(by=["gene_pairs"])

clock_pairs_RF_scores_df.to_csv('clock_RF_scores.csv', index=False)

# RF scores -- clock-hallmark pairs
clock_hallmark_pairs_RF_scores_df = RF_scores_df[RF_scores_df[0].isin(clock_hallmark_pairs)] 
clock_hallmark_pairs_RF_scores_df.columns = ("gene_pairs", "score")
clock_hallmark_pairs_RF_scores_df.sort_values(by=["gene_pairs"])

clock_hallmark_pairs_RF_scores_df.to_csv('clock_hallmark_RF_scores.csv', index=False)

# AF scores
clock_pairs_AF_scores_df = AF_scores_df[AF_scores_df[0].isin(clock_pairs)] 
clock_pairs_AF_scores_df.columns = ("gene_pairs", "score")
clock_pairs_AF_scores_df.sort_values(by=["gene_pairs"])

clock_pairs_AF_scores_df.to_csv('clock_AF_scores.csv', index=False)

# AF scores -- clock-hallmark pairs
clock_hallmark_pairs_AF_scores_df = AF_scores_df[AF_scores_df[0].isin(clock_hallmark_pairs)] 
clock_hallmark_pairs_AF_scores_df.columns = ("gene_pairs", "score")
clock_hallmark_pairs_AF_scores_df.sort_values(by=["gene_pairs"])

clock_hallmark_pairs_AF_scores_df.to_csv('clock_hallmark_AF_scores.csv', index=False)
