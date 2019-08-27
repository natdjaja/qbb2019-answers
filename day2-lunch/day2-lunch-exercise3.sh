#!/bin/bash

sort SRR072893.sam | cut -f 1 | uniq -c > SRR072893.txt