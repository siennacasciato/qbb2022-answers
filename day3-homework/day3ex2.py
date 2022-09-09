#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plinkpca = np.genfromtxt("pcafile.eigenvec", dtype = None, encoding = None, names = ["col1", "col2", "col3", "col4", "col5"])

a_list = plinkpca['col1']
b_list = plinkpca['col2']
c_list = plinkpca['col3']
d_list = plinkpca['col4']
e_list = plinkpca['col5']

fig, ax = plt.subplots()
ax.scatter(c_list, d_list)
plt.xlabel('PC1')
plt.ylabel('PC2')

ax.scatter(c_list,e_list)
plt.xlabel('PC1')
plt.ylabel('PC3')

plt.show()
plt.savefig("ex2_a.png")



