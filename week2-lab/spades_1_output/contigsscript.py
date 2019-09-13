#!/usr/bin/env python3

"""
python script to compute the number of contigs, minimum/maximum/average contig length, and N50
"""

# from fasta import FASTAReader
import sys

class FASTAReader(object):
    
    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False
    
    def next(self):
        
        if self.eof:
            return None, None
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            
        #If reach this point, ident is set correctly
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append(line.strip())
        sequence = "".join(sequences)
        return ident, sequence 

def N50(contig):
    contig.sort()
    halfway = float(sum(contig_lengths)) / 2
    counter = 0
    for contiglength in contig:
        counter += contiglength 
        if counter >= halfway:
            return(contiglength)
        
     
for i in range(1, len(sys.argv)):
    contig_file = open(sys.argv[i])
    contig_reader = FASTAReader(contig_file)
        
    contig_counter = 0
    contig_lengths = []
        
    while True:
        ident, sequence = contig_reader.next()
        if not ident is None:
            contig_counter += 1
            contig_lengths.append(len(sequence))  
        else:
            break

            
avgcontigs = sum(contig_lengths)/len(contig_lengths)   
lengthcontigs = sorted(contig_lengths, reverse = True)
     
print("The minimum number is ", min(contig_lengths), 
"the maximum number is ", max(contig_lengths), 
"the average is ", avgcontigs,
"the N50 is ", N50(contig_lengths))     
    
   
    
      
