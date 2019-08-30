#!/usr/bin/env python3
# ./day5-lunch t_data.ctab

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

for i, line in enumerate (open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split()
    chromosome = fields[1]
    t_name = fields[5]
    if fields[2] == "-":
        new_prom_start = int(fields[4]) - 500 
        new_prom_end = int(fields[4]) + 500
        
    if fields[2] == "+":
        new_prom_start = int(fields[3]) - 500
        new_prom_end = int(fields[3]) + 500 
    
    if new_prom_start < 0:
        new_prom_start = 0
        
    print(chromosome, new_prom_start, new_prom_end, t_name, sep="\t") 
       

#saved as t_data.bed now!  
     
#+ strand +/- region of beginning
#- strand +/- region at end

