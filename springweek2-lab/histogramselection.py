#!/usr/bin/env python3
# under selection , yaxis time to fixation and x axis is selction coffiecnet with increase in selction time for fixation decreases
# iterate through selection coeffienct 
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# s = 0 selction coffiencent 
N = 100
n1 = 0.5
def simulation(q,N, s, repetitions=1000):
    N= 2*int(N)
    n1 = np.ones(repetitions, dtype=np.uint64) * (q * N)
    # n1 = np.ones(repetitions, dtype=np.uint64) * (p* N)
    T = np.empty_like(n1)
    update = (n1 > 0) & (n1 < N)
    t = 0
    while update.any():
        t += 1
        n0 = N - n1
        p = n1 * (1 + s) / (n0+ n1 * (1+s))
        n1[update] = np.random.binomial(N, p[update])
        T[update] = t
        update = (n1 > 0) & (n1 < N)
    return n1 == N, T
coeff= [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
times2 = []
for value in coeff:
    fixations, times = simulation(N=100, s= value, q= 0.5, repetitions=1000)
    fixation_prob = fixations.mean()
    fixation_time = times[fixations].mean()
    times2.append(fixation_time)
w, h = plt.rcParams['figure.figsize']
fig, ax = plt.subplots(figsize=(2 * w, h))
plt.plot(coeff,times2)
# ax.axvline(times[fixations].mean(), color='k', ls='--')
ax.set(xlabel='selection coff', ylabel='time to fixation')
sns.despine()
plt.show()