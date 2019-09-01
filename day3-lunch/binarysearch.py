#!/usr/bin/env python3

import sys


protein_coding_genes = {}
genes = []

for i, line in enumerate (open(sys.argv[1])):
    fields = line.split()
    if line.startswith("#"):
        continue 
    if 'gene_biotype "protein_coding"' in line and "3R" in fields[0] and "gene" in fields[2]:
        start = int(fields[3])
        end = int(fields[4])
        gene_name = fields[13]    
        
        protein_coding_genes[(start,end)] = gene_name
        genes.append((start,end))
        
# binary

search_pos = 21378950
search_chr = "3R"
sorted(genes)

lo = 0
hi = len(genes)-1
mid = 0
number_iterations = 0

while lo < hi:
    mid =int((hi+lo)/2)
    number_iterations += 1
    if search_pos < genes[mid][0]:
        genes = genes[:mid]
    elif search_pos > genes[mid][1]:
        genes = genes[(mid+1):]
    else:
        print (genes[mid][2] , number_iterations)
        break
        
    hi=len(genes)-1
gene_name = protein_coding_genes[genes[0]]
print(gene_name)
       
location = list(genes[0])
distance_1 = abs(location[0]-search_pos)
distance_2 = abs(location[1]-search_pos)

if distance_1 > distance_2:
    print(distance_2)
    
else:
    print(distance_1)
print(number_iterations)

