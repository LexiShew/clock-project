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

df = pd.read_csv("clock_RF_score_matrix_unsorted.csv", index_col=0)

heatmap = sns.heatmap(df, cmap=sns.light_palette("seagreen", as_cmap=True))
fig = heatmap.get_figure()
fig.savefig("clock-heatmap.png") 