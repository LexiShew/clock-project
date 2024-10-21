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
import matplotlib.pyplot as plt

def palette(color="seagreen"):
    return sns.light_palette(color, as_cmap=True)

clock_genes = list(pd.read_csv("./data/clock_uniprot_codes.csv")["gene_name"])
print(clock_genes)

# RF -- clock-clock only
clock_RF_df = pd.read_csv("clock_RF_score_matrix_unsorted.csv", index_col=0)

clock_RF_heatmap = sns.heatmap(clock_RF_df, cmap=palette("blue"))
clock_RF_heatmap.set_title("clock-clock RF")
for tick_label in clock_RF_heatmap.get_yticklabels():
    if tick_label.get_text() not in clock_genes:
        tick_label.set_color("grey")
for tick_label in clock_RF_heatmap.get_xticklabels():
    if tick_label.get_text() not in clock_genes:
        tick_label.set_color("grey")

plt.show()
clock_RF_fig = clock_RF_heatmap.get_figure()
clock_RF_fig.savefig("clock-RF-score-heatmap.png")

# RF -- clock-hallmark
clock_hallmark_RF_df = pd.read_csv("clock_hallmark_RF_score_matrix_unsorted.csv", index_col=0)

clock_hallmark_RF_heatmap = sns.heatmap(clock_hallmark_RF_df, cmap=palette("green"))
clock_hallmark_RF_heatmap.set_title("clock-hallmark RF")
for tick_label in clock_hallmark_RF_heatmap.get_yticklabels():
    if tick_label.get_text() not in clock_genes:
        tick_label.set_color("grey")
for tick_label in clock_hallmark_RF_heatmap.get_xticklabels():
    if tick_label.get_text() not in clock_genes:
        tick_label.set_color("grey")

plt.show()
clock_hallmark_RF_fig = clock_hallmark_RF_heatmap.get_figure()
clock_hallmark_RF_fig.savefig("clock-hallmark-RF-score-heatmap.png")


# AF -- clock-clock only
clock_AF_df = pd.read_csv("clock_AF_score_matrix_unsorted.csv", index_col=0)

clock_AF_heatmap = sns.heatmap(clock_AF_df, cmap=palette("pink"))
clock_AF_heatmap.set_title("clock-clock AF")
for tick_label in clock_AF_heatmap.get_yticklabels():
    if tick_label.get_text() not in clock_genes:
        tick_label.set_color("grey")
for tick_label in clock_AF_heatmap.get_xticklabels():
    if tick_label.get_text() not in clock_genes:
        tick_label.set_color("grey")

plt.show()
clock_AF_fig = clock_AF_heatmap.get_figure()
clock_AF_fig.savefig("clock-AF-score-heatmap.png")

# AF -- clock-hallmark
clock_hallmark_AF_df = pd.read_csv("clock_hallmark_AF_score_matrix_unsorted.csv", index_col=0)

clock_hallmark_AF_heatmap = sns.heatmap(clock_hallmark_AF_df, cmap=palette("purple"))
clock_hallmark_AF_heatmap.set_title("clock-hallmark AF")
for tick_label in clock_hallmark_AF_heatmap.get_yticklabels():
    if tick_label.get_text() not in clock_genes:
        tick_label.set_color("grey")
for tick_label in clock_hallmark_AF_heatmap.get_xticklabels():
    if tick_label.get_text() not in clock_genes:
        tick_label.set_color("grey")

plt.show()
clock_hallmark_AF_fig = clock_hallmark_AF_heatmap.get_figure()
clock_hallmark_AF_fig.savefig("clock-hallmark-AF-score-heatmap.png")