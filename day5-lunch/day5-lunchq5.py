#!/usr/bin/env python3


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy


#FBrtr0302347
ctab = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
mean_H3K4me1 = pd.read_csv(sys.argv[2], sep="\t", header=None, index_col=0 )
# print( mean_H3K4me1.iloc[:,4] )
mean_H3K4me3 = pd.read_csv(sys.argv[3], sep="\t", header=None, index_col=0 )
# print( mean_H3K4me3.iloc[:,4] )
mean_H3K9me3 = pd.read_csv(sys.argv[4], sep="\t", header=None, index_col=0 )
# print( mean_H3K9me3.iloc[:,4] )

histon_md = {"FPKM": ctab.loc[:, "FPKM"], 
        "H3K4me1": mean_H3K4me1.iloc[:, -1],
        "H3K4me3": mean_H3K4me3.iloc[:, -1],
        "H3K9me3": mean_H3K9me3.iloc[:, -1]}

histone_df = pd.DataFrame(histon_md)


model = sm.formula.ols(formula= "FPKM ~ H3K4me1 + H3K4me3 + H3K9me3 ", data= histone_df)

ols_results= model.fit()
# print(ols_result.summary())

fig, ax = plt.subplots()
ax.hist(ols_results.resid, bins=1000, range=(-50,50))
plt.xlabel("Residual")
plt.ylabel("Freq")
plt.title("FPKM & Histone Mod Residual")
fig.savefig("linearregression.png")
plt.close(fig)
    