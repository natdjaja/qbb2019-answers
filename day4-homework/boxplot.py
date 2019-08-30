#!/usr/bin/env python3

"""
Usage ./01-boxplot.py <gene_name> <FPMKs.csv>

Boxplot all transcripts for a given gene name

less -S ~/qbb2019/data/samples.csv to see samples
"""
# Sxl all.csv

import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv(fpkm_file, index_col="t_name")

goi = df.loc[:,"gene_name"] == gene_name
fpkms1 = df.drop(df.columns[list(range(9,17))],axis=1)
fpkms1 = fpkms1.drop(columns="gene_name")

#goi2 = df.loc[:,"gene_name"] == gene_name
fpkms2 = df.drop(df.columns[list(range(1,9))],axis=1)
fpkms2 = fpkms2.drop(columns="gene_name")


# for i, line in enumerate(open(metadata)):
#     if i == 0:
#         continue
#     fields = line.rstrip("\n").split(",")
 
fig,(ax1, ax2) = plt.subplots(2)
ax1.boxplot(fpkms1.loc[goi,:].T)
ax2.boxplot(fpkms2.loc[goi,:].T)
ax1.set_title("Female Boxplot")
ax1.set_xticks([1,2,3,4,5,6,7,8])
ax1.set_xticklabels(['female_10', 'female_11', 'female_12', 'female_13', 'female_14A', 'female_14B', 'female_14C', 'female_14D'], rotation=45)
ax1.set_ylabel("Gene Expression")
ax2.set_title("Male Boxplot")
ax2.set_xlabel("")
plt.xticks([1,2,3,4,5,6,7,8], ['male_10', 'male_11', 'male_12', 'male_13', 'male_14A', 'male_14B', 'male_14C', 'male_14D'], rotation=45)

ax2.set_ylabel("Gene Expression")
plt.subplots_adjust(hspace = 0.8)
fig.savefig("boxplot.png")
plt.close(fig)


#fields 2-9 male
#fields 10-17 female