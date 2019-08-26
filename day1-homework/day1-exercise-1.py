#!/usr/bin/env python3

import sys
in_file = open(sys.argv[1])
count = 0
for line in in_file:
    fields = line.split("\t")
    # splits into fields
    if fields[2] == "*":
        #gets rid of fields with * refer to RNAME
        continue
    count += 1
    #counts and adds 1
        
print(count)
