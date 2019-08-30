#!/usr/bin/env python3

"""
Usage: ./001-metadata.py <metadata.csv> <ctab_dir> 
<ctab_dir> eg ~/qbb2019-answers/results/stringtie

Create all.csv with FPKMs

t_name, gene_name, sample1, ... sample


./allfpkms.py ~/qbb2019/data/samples.csv ../results/stringtie/

"""

import sys
import os
import pandas as pd

metadata = sys.argv[1]
ctab_dir = sys.argv[2]

fpkms = {}

for i, line in enumerate(open(metadata)):
    if i == 0:
        continue
    fields = line.rstrip("\n").split(",")
    srr_id = fields[0]
    sex = fields[1]
    stage = fields[2]
    ctab_path = os.path.join(ctab_dir, srr_id, 
                            "t_data.ctab")
    
   # print(ctab_path)
    df = pd.read_csv(ctab_path, sep="\t", 
                      index_col="t_name")
    if i == 1:
        fpkms["gene_name"] = df.loc[:,"gene_name"]
    fpkms [sex + "_" + stage] = df.loc[:,"FPKM"]

df_fpkms = pd.DataFrame(fpkms)
print(df_fpkms.describe())
pd.DataFrame.to_csv(df_fpkms, "all.csv")
