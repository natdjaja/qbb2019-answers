#!/usr/bin/env python3

"""
Usage: ./03-MAplot.py <ctab1> <ctab2>
"""

import sys 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import os

name1=sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2=sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm={name1 : ctab1.loc[:,"FPKM"], 
      name2 : ctab2.loc[:,"FPKM"]}

df=pd.DataFrame(fpkm)
df += 1

r=df.loc[:,name1]
g=df.loc[:,name2]

a = 0.5*np.log2(r*g)

m=np.log2(r/g)

fig, ax = plt.subplots()
ax.set_title("MA Plot")
ax.set_xlabel(str(sys.argv[1]))
ax.set_ylabel(str(sys.argv[2]))
ax.scatter(a, m, alpha = 0.2)

fig.savefig("MA.png")
plt.close(fig)