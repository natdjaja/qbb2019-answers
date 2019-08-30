#!/usr/bin/env python3

"""
Usage ./02-timecourse.py <t_name> <samples.csv>, <FPKMs>
Create a timecourse of a given transcript for females

./timecourse.py FBtr0331261 ~/qbb2019/data/samples.csv all.csv

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

def get_fpkm_data(fpkms,columns):
    fpkms = fpkms.drop(fpkms.columns[list(columns)],axis=1)
    fpkms = fpkms.drop(columns="gene_name")
    return fpkms

def get_replicate_fpkm_data(ctab_data_dir,metadata_file,sex_):
    fpkm = [ ]
    for i, line in enumerate(open(metadata_file)):
        if i == 0:
            continue
        fields = line.split(",")
        srr_id = fields[0]
        sex = fields[1]
        if sex != sex_:
            continue
        stage = fields[2]
        ctab_path = os.path.join(ctab_data_dir, srr_id, 
                                "t_data.ctab")
    
       # print(ctab_path)
        df = pd.read_csv(ctab_path, sep="\t", 
                          index_col="t_name")
        fpkm.append(df.loc["FBtr0331261","FPKM"])
    return fpkm

t_name = sys.argv[1] # tname
samples = pd.read_csv(sys.argv[2])# samples csv
fpkm_file = sys.argv[3] #all csv
df = pd.read_csv(fpkm_file, index_col="t_name")


fpkms1 = get_fpkm_data(df,range(9,17))
fpkms2 = get_fpkm_data(df,range(1,9))

samples = pd.read_csv(sys.argv[2]) #samples csv

#fpkms = pd.read_csv(sys.argv[3], index_col="t_name")

my_data = (fpkms1.loc[t_name,:])
my_data2 = (fpkms2.loc[t_name,:])


male_rep_data = get_replicate_fpkm_data(sys.argv[5],sys.argv[4],"male")
female_rep_data = get_replicate_fpkm_data(sys.argv[5],sys.argv[4],"female")

print(male_rep_data)
print(female_rep_data)


fig, ax = plt.subplots()
ax.plot(range(8),my_data, color="blue", label='male')
ax.plot(range(8),my_data2, color="red", label='female')
ax.plot(range(4,8),male_rep_data,'x', color="blue")
ax.plot(range(4,8),female_rep_data,'x', color="red")
ax.set_title("Sxl")
ax.set_xlabel("Developmental Expression")
ax.set_xticks([0,1,2,3,4,5,6,7])
ax.set_xticklabels(['10', '11', '12', '13', '14A', '14B', '14C', '14D'], rotation=90)
ax.set_ylabel("mRNA Abundance (FPKM)")
plt.legend(loc='upper left')
plt.show()
fig.savefig("timecourse.png")
plt.close(fig)








