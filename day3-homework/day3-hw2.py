#!/usr/bin/env python3

"""
Count all kmer in a FASTA file
"""
# ./day3-hw2.py droYak2_seq.fa subset.fa 11 > extended.out

from fasta import FASTAReader
import sys

reader1 = FASTAReader(open(sys.argv[1])) #target subset
reader2 = FASTAReader(open(sys.argv[2])) #query which is droyak
k = int(sys.argv[3])

kmer_positions = dict()
#key is kmer
#value is ident,i (sequence,start of target)
targetsequence = {}
#key is ident (sequence)
#value is targetseq
extension = {}
#key targetseq
#value is the extension


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
            for ident,i in kmer_positions[kmer]:
                
                targetseq = targetsequence[ident] #ident is key, value is targetseq
                lengthtarget = len(targetseq) #print out targetseq length
                lengthquery = len(sequence) #print out sequence from reader2 query
                extendright = True #so it goes right
                extendedkmer = kmer #new variable for kmer
                j = 0
                while True:
                    if extendright:
                        if sequence[j+k+1] == targetseq[+k+1]:
                            i += 1
                            j += 1
                            extendedkmer += targetseq[j+k+1]
                        else:
                            extendright = False
                            extension[extendedkmer] = (targetseq)
                            break
                    if lengthtarget == i+k or lengthquery == j+k:
                        extendright = False
                        break  
sorted(extendedkmer, reverse = True, key = len)
for extendedkmer in extension:
        print(extendedkmer)
                        
        





