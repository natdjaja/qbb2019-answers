#!/usr/bin/env python3

"""
Use ./newhist.py ../results/stringtie/SRR072893/t_data.ctab <ctab>
Plot FPKM
Use a = 0.9, skew_mu = 3, skew_sigma = 1.9
"""


import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue #skip header
    fields = line.rstrip("\n").split("\t") #strip lines and fields to get rid of white spaces
    if float(fields[11]) > 0: #prints the integer of the fpkms only if it's bigger than 0
        fpkms.append(float(fields[11])) #add the fpkm to our new list of fpkms

#print(len(fpkms))

my_data = np.log2(fpkms) #log of data to make it cleaner
mu = 0 #point at which 50% of values exist
sigma = 1 #std dev

x_1 = np.linspace( -15, 15, 100) #100 is the number of bins
y = stats.norm.pdf( x_1, mu, sigma) 

#print(y)
#print(type(y))
    
fig, ax = plt.subplots()
ax.set_title("FPKM Histogram")
ax.set_xlabel("FPKMS")
ax.set_ylabel("Frequency")
ax.text(0.05, 0.95, "a = 0.9, skew_mu = 3, skew_sigma = 1.9" , transform=ax.transAxes, fontsize=12,
        verticalalignment='top')

a = float(sys.argv[2]) #degree of skew
skew_mu = float(sys.argv[3]) #new mu user can input as arg
skew_sigma = float(sys.argv[4]) #sigma user can input as arg
z = stats.skewnorm.pdf( x_1, a, skew_mu, skew_sigma) #new line for skewnorm, with old x, new a, new mu, new sigma
#user for skewnorm must follow this output
# r = stats.skewnorm.rvs(a, size=1000)

ax.hist(my_data, bins=100, density=True) #histogram will be plotted here
ax.plot(x_1, y) #plot for curve fit, normal dist
ax.plot(x_1, z) #plot for skewnorm. same as norm but with new arg
fig.savefig("fpkms.png") #save as this file
plt.close(fig) #have to close the fig

