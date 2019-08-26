#!/usr/bin/env python3

import sys
in_file = open(sys.argv[1])

for i, line in enumerate(in_file):
    fields = line.split("\t")
    if i <= 9:
        print(fields[2])


       