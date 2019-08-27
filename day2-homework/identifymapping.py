#!/usr/bin/env python3

import sys

map = {}

for line in open(sys.argv[1]):
    fields = line.rstrip("\n").split()
    key = fields[0]
    map[key] = fields[1]
#for gene in map:
print(map)
    

for line in open(sys.argv[2]):
     fields = line.rstrip("\n").split()
     if fields[8] in map:
         print(line + map[fields[8]])
     elif fields[8] not in map and sys.argv[3] == "nothing":
         print("nothing")
     elif fields[8] == " ":
         continue
    
         

         
         
         
         
         
# in terminal $ ./identifymapping.py parsedfile-day2homework.out ../results/stringtie/SRR072893/t_data.ctab

    
    

    

    


