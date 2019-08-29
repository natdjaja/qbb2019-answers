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

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm = {name1: ctab1.loc[:,"FPKM"], 
        name2: ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm)

#print(df)

goi = np.log2(df.loc[:,name1] + 1) 
goi2 = np.log2(df.loc[:,name2] + 1)


fig, ax = plt.subplots()
ax.scatter (goi, goi2, alpha=0.3)
ax.set_title("Scatterplot")
ax.set_xlabel("Log2 FPKM {}".format(name1))
ax.set_ylabel("Log2 FPKM {}".format(name2))

fig.savefig("name1vsname2.png")


plt.close(fig)



#
#
# for i, line in enumerate(open(sys.argv[1])):
#     if i == 0:
#         continue
#     fields = line.rstrip("\n").split("\t")
#     exons.append(int(fields[6]))
#     lengths.append(int(fields[7]))
#
#
#

#
