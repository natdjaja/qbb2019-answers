#!/usr/bin/env python3

"""
Usage: ./newscatter.py <ctab>
Compare num_exons vs length
"""
# run this in the terminal
#./00-scatter.py ../results/stringtie/SRR072893/t_data.ctab

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

name1 = sys.argv[1].split(os.sep)[-2] #arg and we look at second to last column
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name") #pandas can only read csv type files

name2 = sys.argv[2].split(os.sep)[-2] #arg and we look at second to last column again
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm = {name1: ctab1.loc[:,"FPKM"], #our new dictionary. name1 or 2 for arg. locate in file only fpkm column
        name2: ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm) #new var that reads data frame as fpkm

#print(df)

fpkmss1 = np.log2(df.loc[:,name1] + 1) #this will call in the value associated with the key of "name"
fpkmss2 = np.log2(df.loc[:,name2] + 1)

m, b = np.polyfit(fpkmss1, fpkmss2, 1) #our slope and b for our graph
x = [fpkmss1.min(), fpkmss2.max()] #min and max aka range for our x, you can do this in any order i think

fig, ax = plt.subplots() #plot graphs
ax.scatter (fpkmss1, fpkmss2, s=3, alpha=0.2, color="red") #scatterplot with fpkm1 and fpkm2, size3, red color
ax.plot(x, [(m*x1+b) for x1 in x], 
    color="blue") #plot the line for best fit
ax.set_title("Scatterplot of FPKMs")
ax.set_xlabel("Log2 FPKM {}".format(name1))
ax.set_ylabel("Log2 FPKM {}".format(name2))


fig.savefig("ndscatterplot.png")

plt.close(fig)


# polyfit = np.polyfit(goi, goi2, 1)
# poly1d = np.poly1d(polyfit)
# xp = np.linspace(0, 14, 100)
# ax.plot(xp, poly1d(xp))
