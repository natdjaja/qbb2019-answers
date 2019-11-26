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


hema = open(sys.argv[1])

df = pd.read_csv(hema, sep = "\t", index_col = "gene", header = 0)

cfu = df['CFU'].values
poly = df["poly"].values

Data = {'x':cfu, 'y': poly}

#print(Data)

df6 = pd.DataFrame(Data, columns =['x','y'])

#print(df6)

linky=linkage(df, 'single', 'euclidean')
leaf= leaves_list(linky)
#print(leaf)
df2 = df.iloc[leaf]
#print(df2)

# fig, ax = plt.subplots()
# sns.heatmap(df2)


df3 = df.transpose()
# link2=linkage(df3, 'single', 'euclidean')
link2=linkage(df3, 'average')
leaf2= leaves_list(link2)

df4 = df.iloc[leaf,:]
df5 = df4.iloc[:,leaf2]

fig,ax =plt.subplots()
plt.pcolor(df)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)

fig.savefig("heatmap.png")
plt.close(fig)


label_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
labels = np.array(label_list)
sort_label = labels[leaf2]


ax1 = dendrogram(link2, labels = sort_label)
plt.savefig('dendogram.png')
plt.close(fig)


fig.savefig("plot.png")
plt.close(fig)

kmeans = KMeans(n_clusters=5).fit(df6)
centroids = kmeans.cluster_centers_

fig, ax = plt.subplots()
plt.scatter(df6['x'], df6['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

fig.savefig("kmeans.png")
plt.close(fig)

df_data = pd.read_csv(sys.argv[1], sep='\t', header=0, index_col=0)

# diff_exp_high = ((df_data['poly'] + df_data['int']/2))/((df_data['mid'] + df_data['int']/2))>= 2
# diff_exp_low = ((df_data['CFU'] + df_data['unk']/2))/((df_data['mid'] + df_data['int']/2)) <= 0.5
#
#
# diff_exp_genes = df_data[diff_exp_high | diff_exp_low]

#CFU and unk
#poly and int 
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
       
print(sig_de_genes)


labels = list(kmeans.labels_)
genes = list(df_data.index.values)
goi_index = genes.index(sys.argv[2])
goi_cluster = labels[goi_index]
related_genes = []
for i, gene in enumerate(genes):
	if labels[i] == goi_cluster:
		related_genes.append(gene)
print(related_genes)


# with open('list_of_genes.txt', 'w') as f:
#    for item in related_genes:
#        f.write("%s," % item)
fig.savefig('plot.png')

# Index= ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
# Cols = ['A', 'B', 'C', 'D']
# df = DataFrame(abs(np.random.randn(5, 4)), index=Index, columns=Cols)
#
# sns.heatmap(df, annot=True)
#
#
#
# # df = np.loadtxt(open(sys.argv[1]), dtype = "str", delimiter = "\t")
# # array = np.loadtxt
#
# data = pd.read_csv(open(sys.argv[1]), delimiter = "\t", header=0)
# print(data)

# gene_array = np.random.rand(10, 12)
# ax = sns.heatmap(gene_array, linewidth=0.5)
# plt.show()