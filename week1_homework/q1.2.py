#!/usr/bin/env python

import scipy.stats
from scipy.stats import poisson
import sys
import numpy as np
import matplotlib.pyplot as plt

slist = [0] * 1000000
#print(slist)

reads = 50000

for i in range(reads):
    #np.random.randint(low = 0, high = 999900)
    start = np.random.randint(low = 0, high = 999900)
    for j in range(start,start+100):
        array = (j, +1)
        print(array)

#print(array)

fig, ax = plt.subplots()
ax.hist(array)
ax.set_xlabel("Genome Position")
ax.set_ylabel("Number of Overlapping Reads")
x = np.arange(0,500000)
y = scipy.stats.poisson.pmf(np.arange(0,500000), 200000)
plt.plot(x, y, 'r-')
#plt.show()

plt.savefig("1.2_hist.png")

