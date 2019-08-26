#!/usr/bin/env python3

import sys
in_file = open(sys.argv[1])

count = 0
total_MAPQ = 0

for line in in_file:
    fields = line.strip().split("\t")
    total_MAPQ += int(fields[4])
    count += 1

average = float(total_MAPQ)/float(count)

print(average)
