#!/bin/usr/env phyton3

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
targetsequence = {}
extension = {}
#for target name, store extension that goes with it

for ident, sequence in reader1:
    sequence = sequence.upper()
    targetsequence[ident] = sequence
    # extension[ident] = list(extendedkmer)
    
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
                targetseq = targetsequence[ident]
                lengthtarget = len(targetseq)
                lengthquery = len(sequence)
                extendright = True
                extendedkmer = kmer 
                while True:
                    if extendright:
                        if targetseq[i+k+1] == sequence[j+k+1]:
                            i += 1
                            j += 1
                            extendedkmer += sequence[j+k+1]
                        else:
                        extendright = False
                    else:
                       # we would add extensions here 
                        break
                    if lengthtarget == i+k or lengthquery == j+k:
                        extendright = False
                                                            
                                
                print(ident, i, j, kmer) 
        





