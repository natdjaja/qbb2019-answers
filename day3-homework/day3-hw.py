#!/usr/bin/env python3

"""
Count all kmer in a FASTA file
"""

from fasta import FASTAReader
import sys

reader1 = FASTAReader(open(sys.argv[1]))
reader2 = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

kmer_positions = dict()

for ident, sequence in reader1:
    sequence = sequence.upper()
    
    for i in range(0, len(sequence)-k+1):
        kmer=sequence[i:i+k]
        if kmer in kmer_positions:
            kmer_positions[kmer].append((ident,i))
        else:
            kmer_positions[kmer] = [(ident,i)]
            
for ident, sequence in reader2:
    sequence = sequence.upper()
    for j in range(0, len(sequence)-k+1):
        kmer=sequence[j:j+k]
        if kmer in kmer_positions:
            key = kmer_positions[kmer]
            for ident,i in key:
                print(ident, i, j, kmer) 
        





