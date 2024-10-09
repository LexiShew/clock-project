###############################################################################
#
#   create-pairwise-table.py
#
#   uses `clock_RF_scores.csv` to create `clock_RF_score_matrix_unsorted.csv`
#   and `clock_RF_score_matrix_sorted.csv`
#
###############################################################################

import pandas as pd

clock_RF_scores_df = pd.read_csv("clock_RF_scores.csv")

clock_RF_scores_df[['gene_1', 'gene_2']] = clock_RF_scores_df['gene_pairs'].str.split('_', expand=True)

clock_RF_scores_df = pd.pivot_table(clock_RF_scores_df, values="score", index=["gene_1"], columns=["gene_2"])

clock_genes_uniprot_df = pd.read_csv("clock_uniprot_codes.csv")
clock_genes_uniprot_map = dict(zip(clock_genes_uniprot_df["uniprot_code"], clock_genes_uniprot_df["gene_name"]))

clock_RF_scores_df.rename(columns=clock_genes_uniprot_map, index=clock_genes_uniprot_map, inplace=True)
clock_RF_scores_df.index.name = None
clock_RF_scores_df.columns.name = None

clock_RF_scores_df.to_csv('clock_RF_score_matrix_unsorted.csv', index=True, index_label=None)

clock_RF_scores_df = clock_RF_scores_df.sort_index(axis=0)
clock_RF_scores_df = clock_RF_scores_df.sort_index(axis=1)
clock_RF_scores_df.to_csv('clock_RF_score_matrix_sorted.csv', index=True, index_label=None)