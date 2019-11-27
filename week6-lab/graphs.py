#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt 
import numpy as np

# first figure 

ER4_count = 0
G1E_count = 0

g1e = {}
er4 = {}

ER4_binding = open(sys.argv[1])
G1E_binding = open(sys.argv[2])


for line in open(sys.argv[1]):
    ER4_count += 1
       
for line in open(sys.argv[2]):   
    G1E_count += 1        
       
ER4_features = open(sys.argv[3])
G1E_features = open(sys.argv[4])

for line in open(sys.argv[3]):
    col = line.rstrip("\n").split("\t")
    g1e.setdefault(col[3], 0)
    g1e[col[3]] += 1
       
for line in open(sys.argv[4]):
    col = line.rstrip("\n").split("\t")
    er4.setdefault(col[3], 0)
    er4[col[3]] += 1     
   
x_value = np.arange(len(er4))
width = 0.3

fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(20, 10))
axes = axes.flatten()
axes[0].bar(x=["ER4_count", "G1E_count"], height = [ER4_count,G1E_count])
axes[0].set_xlabel(" CTCF Binding Sites")
axes[0].set_ylabel("Number of Sites")
axes[1].bar(x= x_value - width/2, height = list(er4.values()), width = width, color = "blue", label = "ER4")
axes[1].bar(x= x_value + width/2, height = list(g1e.values()), width = width, color = "red", label = "G1E")
axes[1].set_xticks(x_value)
axes[1].set_xticklabels(er4.keys())
axes[1].legend()
axes[1].set_xlabel("Features")
axes[1].set_ylabel("Number of Sites")

fig.savefig("image.png")
plt.close(fig)