#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

#sorting and joining done in unix
# sort -k 1,1 pcafile.eigenvec > sorted_pca_eigenvec
# sort -k 1,1 integrated_call_samples.panel > sorted_int
#
# join sorted_int sorted_pca_eigenvec > joined_files


sample = np.genfromtxt("joined_files", dtype = None, encoding = None, names = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"])


#a_list = joinpca['col1']
#b_list = joinpca['col2']
#c_list = joinpca['col3']
#d_list = joinpca['col4']
#e_list = joinpca['col5']
#f_list = joinpca['col6']
#g_list = joinpca['col7']
#h_list = joinpca['col8']

pop = sample['col2']
supop = sample['col3']
sex = sample['col4']
pca1 = sample['col6']
pca2 = sample['col7']

#pop = []
#supop = []
#sex = []
#pca1 = []
#pca2 = []

#POPULATION
fig, ax = plt.subplots()

plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title("PCA1 vs PCA2 Distinguished by Population")



for line in np.unique(pop):
    popc = np.where(pop == line)
    ax.scatter(pca1[popc], pca2[popc])
   # plt.legend((pca1[popc], pca2[popc]))
    
#plt.show()
plt.savefig("ex3_a.png")




#SUPERPOPULATION
fig, ax = plt.subplots()

plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title("PCA1 vs PCA2 Distinguished by Superpopulation")


for line in np.unique(supop):
    supopc = np.where(supop == line)
    ax.scatter(pca1[supopc], pca2[supopc])
    plt.legend(pca1[supopc], pca2[supopc])
    
#plt.show()
plt.savefig("ex3_b.png")





#SEX
fig, ax = plt.subplots()

plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title("PCA1 vs PCA2 Distinguished by Sex")

for line in np.unique(sex):
    sexl = np.where(sex == line)
    ax.scatter(pca1[sexl], pca2[sexl])
    plt.legend(pca1[sexl], pca2[sexl])
    
#plt.show()
plt.savefig("ex3_c.png")
