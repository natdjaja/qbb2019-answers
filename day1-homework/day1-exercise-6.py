#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
count = 0
for i, line in enumerate(in_file):
    fields = line.split("\t")
    if (fields[2] == "2L") and (int(fields[3]) > 10000) and (int(fields[3]) < 20000):
        count += 1
    
print(count)


