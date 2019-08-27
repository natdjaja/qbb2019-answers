#!/bin/bash

samtools view SRR072893.sam | awk '{print NF}' | sort SRR072893.sam | uniq -c > SRR072893.columns