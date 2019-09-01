#!/usr/bin/env python3

#!/usr/bin/env python3

import sys

genes = []
dictionary = {}

for i, line in enumerate (open(sys.argv[1])):
    fields = line.split()
    if line.startswith("#"):
        continue 
    if 'gene_biotype "protein_coding"' in line and "3R" in fields[0]:
        start = int(fields[3])
        end = int(fields[4])
        gene_name = (fields[13])    
        genes.append((start,end,gene_name))
        actual_gene_name = fields[13]
        dictionary[fields[3]] = actual_gene_name
        dictionary[fields[4]] = actual_gene_name
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
        break
        
    hi=len(genes)-1
       
location = list(genes[0])
distance_1 = abs(location[0]-search_pos)
distance_2 = abs(location[1]-search_pos)

if distance_1 > distance_2:
    print("Gene name is ", genes[mid][2], "Distance is ", distance_2, "Number of iterations is ", number_iterations)
else:
    print("Gene name is ", genes[mid][2], "Distance is ", distance_1, "Number of iterations is ", number_iterations)


