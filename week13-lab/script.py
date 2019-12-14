#!/usr/bin/env python2

import sys
import numpy as np
f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
input1 = []
fieldstuple = ()
v1 = [0] * 7000
v2 = [0] *7000
rna_index = []
rna_expression = {}
for i, line in enumerate(f1):
    if i == 0: 
        continue 
    fields = line.rstrip('\n').split('\t')
    if int(fields[1]) >= 5000000 and int(fields[1]) <= 40000000:
        index1 = (int(fields[1]) - 5000000) / 5000
        rna_index.append(index1)
        rna_expression[index1] = float(fields[-2])
activity_index = []
activity_value= {}
for i, line in enumerate(f2):
    if i == 0: 
        continue 
    fields = line.rstrip('\n').split('\t')
    if int(fields[1]) >= 5000000 and int(fields[1]) <= 40000000:
        index2 = (int(fields[1]) - 5000000) / 5000
        activity_index.append(index2)
        activity_value[index2] = float(fields[-2])
import hifive
import numpy
hic = hifive.HiC('PROJECT_FNAME', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)        
interaction_activity = {}
for index1 in rna_index:
    int_act = 0
    for index2 in activity_index:
        int_act += float(activity_value[index2])* data[index1][index2]
    interaction_activity[index1] = int_act
rna_expression_list = []
interaction_activity_list = []
for index in rna_index:
    rna_expression_list.append(float(rna_expression[index]))
    interaction_activity_list.append(interaction_activity[index])
rna_array = numpy.array(rna_expression_list)
interaction_activity_array = numpy.array(interaction_activity_list)
R_value = numpy.corrcoef(rna_array, interaction_activity_array)[0, 1]
#print "R coefficient =" , R_value
print(data)