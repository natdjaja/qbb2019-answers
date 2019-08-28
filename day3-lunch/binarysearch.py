#!/usr/bin/env python3

import sys

genes = []

for i, line in enumerate (open(sys.argv[1])):
    fields = line.split()
    if line.startswith ("#"):
        continue
    if 'gene_biotype "protein_coding"' in line and "3R" in fields[0]:
        start = fields[3]
        end = fields[4]
        gene_name = fields[13]    
        entry = (int(start), int(end), gene_name)
        genes.append((entry))
# print(genes)


#binary


search_pos = 21378950
search_chr = "3R"
    
lo = 0
hi = len(genes)-1
mid = 0
number_iterations = 0

while (lo <= hi):
    mid = int((hi+lo)/2)
    number_iteractions = number_iterations + 1
    if (search_pos < genes[mid][0]):
        hi = mid
    elif (search_pos > genes[mid][1]):
        lo = mid
    else:
        print(genes[mid][2], number_iterations)
        break
    if hi-lo == 1:
        break
        
        
    # print(lo,mid,hi)
    

  