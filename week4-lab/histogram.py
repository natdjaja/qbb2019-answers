#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

freq = []
for i, line in enumerate( open(sys.argv[1]) ):
    if i == 0:
        continue
    fields = line.rstrip("\n").split()
    if float(fields[4]) > 0:
        freq.append( float(fields[4]) )

# print( len(fpkms) )

# my_data = np.log2( fpkms )

mu = 0
sigma = 1

x = np.linspace( -0.05, 0.05 )
print(x) 
print( type(x) )
y = stats.norm.pdf( x, mu, sigma )

fig, ax = plt.subplots()
ax.hist( freq, bins=10000, density=True )
ax.plot( x, y )
fig.savefig("freq.png")
plt.close(fig)