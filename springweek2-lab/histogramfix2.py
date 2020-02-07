#!/usr/bin/env python3

#Simulate the time to fixation under a range of different starting allele frequencies. Produce a plot showing starting allele frequency vs. number of generations to fix. 
#Do (at least) 100 simulations for each and include the variability in your plot.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# s = 0
# N = 100
n1 = 0.75
def simulation(Q, N, s, repetitions=100):
    N = int(2*N) 
    n1 = np.ones(repetitions, dtype=np.uint64) * Q * N 
    T = np.empty_like(n1)
    update = (n1 > 0) & (n1 < N)
    t = 0
    while update.any():
        t += 1
        p = n1 * (1 + s) / (N + n1 * s) 
        n1[update] = np.random.binomial(N, p[update])
        T[update] = t
        update = (n1 > 0) & (n1 < N)
    return n1 == N, T
fixations, times = simulation(Q=0.5, N=1000, s=0, repetitions=1000) #changed pop to 100000
fixation_prob = fixations.mean()
fixation_time = times[fixations].mean()
w, h = plt.rcParams['figure.figsize']
fig, ax = plt.subplots(figsize=(2 * w, h))
sns.distplot(times[fixations], ax=ax)
ax.axvline(times[fixations].mean(), color='k', ls='--')
ax.set(xlabel='Generations to fix', ylabel='Frequency')
plt.show() 