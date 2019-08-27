#!/bin/bash

grep "^SRR072893" SRR072893.sam | cut -f 3 | sort | uniq -c > SRR072893.txt
cut -f 3 SRR072893.sam | sort | uniq -c
