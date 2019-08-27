#!/usr/bin/env python3

import sys

for line in open("fly.txt"):
    fields = line.rstrip("\n").split()
    if "DROME" in line and "FBgn" in line:
        print(fields[-1], fields[-2])
        
#saved this in parsedfile-day2homework.out

        
    
        
    
        
        
        
        

        
        


        
    


        
    
    

    