#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt
# read depth distribution
# less -S output.ann.vcf
dp_list = []
qual_value = []
allele_list = []
predicted = {}
for line in open(sys.argv[1]):
   if line.startswith("#"):
       continue
   column = line.rstrip("\t").split()
   info = column[7]
   info_2 = info.split(";")[7]
   dp = info_2.split("=")[1]
   dp_list.append(dp)
# genotype quality distribution
   qual_dist = int(float(column[5]))
   qual_value.append(qual_dist)
#print(qual_value)
#./plotvariant.py output.ann.vcf
#the allele frequency spectrum of your identified variants
#AF 3
   allele = column[3]
   #print(allele)
   allele_freq = info.split(";")[3]
   allele_val = allele_freq.split("=")[1]
   allele_list.append(allele_val)
#print(allele_list)
# prediction
   #print(len(column))
   #prediction = column[41]
   prediction_2= info.split(";")[41]
   prediction_val = prediction_2.split("=")[1]
   prediction_3 = prediction_val.split("|")[1]
   if prediction_3 in predicted:
       predicted[prediction_3] += 1
   else :
       predicted[prediction_3] = 1
#Graphing
#print(range(len(predicted)))
# print(list(predicted.values()))
fig,ax = plt.subplots(2,2)
#ax[0,0].hist(dp_list, bin = 100)
#ax[0,1].hist(qual_value, bin = 1000 , range = [0,5000])
#ax[1,0].hist(allele_list, bin = 100)
#ax[1,1].hist(predicted)
ax[0,0].hist(dp_list, bins = 100)
ax[0,1].hist(qual_value, bins = 1000 , range = [0,5000])
ax[1,0].hist(allele_list, bins = 100)
# last one specify your x and y vlaue
values = list(predicted.values())
calling = list(range(len(predicted)))
plt.bar(calling,values, align = 'center' )
#print(list(predicted.keys()))
plt.xticks(calling,list(predicted.keys()), rotation = 'vertical', size = 5 )
ax[0,0].set_xlabel("Variant")
ax[0,0].set_ylabel("Read Depth")
ax[0,1].set_xlabel("Variant")
ax[0,1].set_ylabel("Quality")
ax[1,0].set_xlabel("Variant")
ax[1,0].set_ylabel("Freq")
ax[1,1].set_xlabel("Variant")
ax[1,1].set_ylabel("Impact")
ax[0,0].set_title("Read Depth")
ax[0,1].set_title("Quality")
ax[1,0].set_title("Allele Freq")
ax[1,1].set_title("Impact")
fig. savefig("plot.png")
plt.close(fig)
#run ./plotvariant.py output.ann.vcf