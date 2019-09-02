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

mean_H3K4me3 = pd.read_csv(sys.argv[3], sep="\t", header=None, index_col=0 )

mean_H3K9me3 = pd.read_csv(sys.argv[4], sep="\t", header=None, index_col=0 )


histone_md = {"FPKM": ctab.loc[:, "FPKM"], 
        "H3K4me1": mean_H3K4me1.iloc[:, -1],
        "H3K4me3": mean_H3K4me3.iloc[:, -1],
        "H3K9me3": mean_H3K9me3.iloc[:, -1]}
        
histone_df = pd.DataFrame(histone_md)
histone_df["logFPKM"] = np.log(histone_df["FPKM"]+1)


model = sm.formula.ols(formula= "logFPKM ~ H3K4me1 + H3K4me3 + H3K9me3 ", data= histone_df)

ols_results= model.fit()


fig, ax = plt.subplots()
ax.hist(ols_results.resid, bins=100, range=(-10,10))
plt.xlabel("Residual")
plt.ylabel("Freq")
plt.title("FPKM & Histone Mod Residual")
fig.savefig("loglinearregression.png")
plt.close(fig)
    