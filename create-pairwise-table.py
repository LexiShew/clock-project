###############################################################################
#
#   create-pairwise-table.py
#
#   uses `clock_RF_scores.csv` to create `clock_RF_score_matrix_unsorted.csv`
#   and `clock_RF_score_matrix_sorted.csv`
#
###############################################################################

import pandas as pd

clock_genes_uniprot_df = pd.read_csv("./data/clock_uniprot_codes.csv")
hallmark_genes_uniprot_df = pd.read_csv("./data/hallmark_uniprot_codes.csv")
genes_uniprot_df = pd.concat([clock_genes_uniprot_df, hallmark_genes_uniprot_df])
genes_uniprot_map = dict(zip(genes_uniprot_df["uniprot_code"], genes_uniprot_df["gene_name"]))

# RF -- clock-clock pairs
clock_RF_scores_df = pd.read_csv("clock_RF_scores.csv")

clock_RF_scores_df[['gene_1', 'gene_2']] = clock_RF_scores_df['gene_pairs'].str.split('_', expand=True)

clock_RF_scores_df = pd.pivot_table(clock_RF_scores_df, values="score", index=["gene_1"], columns=["gene_2"])

clock_RF_scores_df.rename(columns=genes_uniprot_map, index=genes_uniprot_map, inplace=True)
clock_RF_scores_df.index.name = None
clock_RF_scores_df.columns.name = None

clock_RF_scores_df.to_csv('clock_RF_score_matrix_unsorted.csv', index=True, index_label=None)

clock_RF_scores_df = clock_RF_scores_df.sort_index(axis=0)
clock_RF_scores_df = clock_RF_scores_df.sort_index(axis=1)
clock_RF_scores_df.to_csv('clock_RF_score_matrix_sorted.csv', index=True, index_label=None)

# RF -- clock-hallmark pairs
clock_hallmark_RF_scores_df = pd.read_csv("clock_hallmark_RF_scores.csv")

clock_hallmark_RF_scores_df[['gene_1', 'gene_2']] = clock_hallmark_RF_scores_df['gene_pairs'].str.split('_', expand=True)

clock_hallmark_RF_scores_df = pd.pivot_table(clock_hallmark_RF_scores_df, values="score", index=["gene_1"], columns=["gene_2"])

clock_hallmark_RF_scores_df.rename(columns=genes_uniprot_map, index=genes_uniprot_map, inplace=True)
clock_hallmark_RF_scores_df.index.name = None
clock_hallmark_RF_scores_df.columns.name = None

clock_hallmark_RF_scores_df.to_csv('clock_hallmark_RF_score_matrix_unsorted.csv', index=True, index_label=None)

clock_hallmark_RF_scores_df = clock_hallmark_RF_scores_df.sort_index(axis=0)
clock_hallmark_RF_scores_df = clock_hallmark_RF_scores_df.sort_index(axis=1)
clock_hallmark_RF_scores_df.to_csv('clock_hallmark_RF_score_matrix_sorted.csv', index=True, index_label=None)


# AF -- clock-clock pairs
clock_AF_scores_df = pd.read_csv("clock_AF_scores.csv")

clock_AF_scores_df[['gene_1', 'gene_2']] = clock_AF_scores_df['gene_pairs'].str.split('_', expand=True)

clock_AF_scores_df = pd.pivot_table(clock_AF_scores_df, values="score", index=["gene_1"], columns=["gene_2"])

clock_AF_scores_df.rename(columns=genes_uniprot_map, index=genes_uniprot_map, inplace=True)
clock_AF_scores_df.index.name = None
clock_AF_scores_df.columns.name = None

clock_AF_scores_df.to_csv('clock_AF_score_matrix_unsorted.csv', index=True, index_label=None)

clock_AF_scores_df = clock_AF_scores_df.sort_index(axis=0)
clock_AF_scores_df = clock_AF_scores_df.sort_index(axis=1)
clock_AF_scores_df.to_csv('clock_AF_score_matrix_sorted.csv', index=True, index_label=None)

# AF -- clock-hallmark pairs
clock_hallmark_AF_scores_df = pd.read_csv("clock_hallmark_AF_scores.csv")

clock_hallmark_AF_scores_df[['gene_1', 'gene_2']] = clock_hallmark_AF_scores_df['gene_pairs'].str.split('_', expand=True)

clock_hallmark_AF_scores_df = pd.pivot_table(clock_hallmark_AF_scores_df, values="score", index=["gene_1"], columns=["gene_2"])

clock_hallmark_AF_scores_df.rename(columns=genes_uniprot_map, index=genes_uniprot_map, inplace=True)
clock_hallmark_AF_scores_df.index.name = None
clock_hallmark_AF_scores_df.columns.name = None

clock_hallmark_AF_scores_df.to_csv('clock_hallmark_AF_score_matrix_unsorted.csv', index=True, index_label=None)

clock_hallmark_AF_scores_df = clock_hallmark_AF_scores_df.sort_index(axis=0)
clock_hallmark_AF_scores_df = clock_hallmark_AF_scores_df.sort_index(axis=1)
clock_hallmark_AF_scores_df.to_csv('clock_hallmark_AF_score_matrix_sorted.csv', index=True, index_label=None)