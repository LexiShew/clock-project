###############################################################################
#
#   generate-clock-heatmap.py
#
#   creates heatmap image of RF clock protein PPI scores.
#   image file: clock-heatmap.png
#
###############################################################################


import seaborn as sns
import pandas as pd

# RF
RF_df = pd.read_csv("clock_RF_score_matrix_unsorted.csv", index_col=0)

RF_heatmap = sns.heatmap(RF_df, cmap=sns.light_palette("seagreen", as_cmap=True))
RF_fig = RF_heatmap.get_figure()
RF_fig.savefig("clock-RF-score-heatmap.png") 

# AF
AF_df = pd.read_csv("clock_AF_score_matrix_unsorted.csv", index_col=0)

AF_heatmap = sns.heatmap(AF_df, cmap=sns.light_palette("seagreen", as_cmap=True))
AF_fig = AF_heatmap.get_figure()
AF_fig.savefig("clock-AF-score-heatmap.png") 