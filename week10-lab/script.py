#!/usr/bin/env python3

import sys 
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import seaborn as sns
from sklearn.cluster import KMeans
import scipy.stats as sp

df_data = pd.read_csv(sys.argv[1], sep='\t', header=0, index_col=0)
diff_exp_high = ((df_data['CFU'] + df_data['unk'])/2)/((df_data['poly'] + df_data['int'])/2) >= 2
diff_exp_low = ((df_data['CFU'] + df_data['unk'])/2)/((df_data['poly'] + df_data['int'])/2) <= 0.5
diff_exp_genes = df_data[diff_exp_high | diff_exp_low]
# for gene_name, row in diff_exp_genes.iterrows():
#     sample1 = [row['CFU'], row['unk']]
#     sample2 = [row['poly'], row['int']]
#     print(gene_name, stats.ttest_ind(sample1, sample2).pvalue)
cfu1 = list(diff_exp_genes["CFU"].values)
poly1 = list(diff_exp_genes["poly"].values)
int1 = list(diff_exp_genes["int"].values)
unk1 = list(diff_exp_genes["unk"].values)
gene_name1 = list(diff_exp_genes.index.values)
l = len(gene_name1)
# print(l)
# print(gene_name1)
sig_de_genes = []
for i in range(l):
    early = [cfu1[i], unk1[i]]
    late = [poly1[i], int1[i]]
    t, p  = (sp.ttest_rel(early, late))
    if p < 0.05:
        sig_de_genes.append(gene_name1[i])
        # print(i)
print(sig_de_genes)

