#!/usr/bin/env python3

import sys
in_file = open(sys.argv[1])
count = 0
for line in in_file:
    if "NH:i:1" in line:
        count += 1
print(count)