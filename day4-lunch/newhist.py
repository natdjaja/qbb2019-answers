#!/usr/bin/env python3

#!/usr/bin/env python3

"""
Use ./newhist.py ../results/stringtie/SRR072893/t_data.ctab <ctab>

Plot FPKM

Use a = 0.5, skew_mu = 4, skew_sigma = 2
"""


import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append(float(fields[11])) 

print(len(fpkms))

my_data =np.log2(fpkms)
mu = 0
sigma = 1

x_1 = np.linspace( -15, 15, 100)
y = stats.norm.pdf( x_1, mu, sigma)

#print(y)
#print(type(y))
    
fig, ax = plt.subplots()
ax.set_title("FPKM Histogram")
ax.set_xlabel("FPKMS")
ax.set_ylabel("Frequency")
ax.text(0.05, 0.95, "a = 0.5, skew_mu = 4, skew_sigma = 2" , transform=ax.transAxes, fontsize=12,
        verticalalignment='top')

a = float(sys.argv[2])
skew_mu = float(sys.argv[3])
skew_sigma = float(sys.argv[4])
z = stats.skewnorm.pdf( x_1, a, skew_mu, skew_sigma)


# r = stats.skewnorm.rvs(a, size=1000)
# ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)

ax.hist(my_data, bins=100, density=True)
ax.plot(x_1, y)
ax.plot(x_1, z)
fig.savefig("fpkms.png")
plt.close(fig)


#for fig, ax = plt.subplots()
#we can put ax1,ax2 to print different graphs, not overlay






