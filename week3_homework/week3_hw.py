#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import sys
from vcfParser import parse_vcf

parsedvcf = parse_vcf ('ann_vcf.vcf')
# print(parsedvcf[1])

DP = []
GT = []
AF = []
ANN = []
for line in parsedvcf:
    if line[0] == 'CHROM':
        continue
#plot 3
    for sample_info in line[7:7]:
        if sample_info[6] == '.':
            pass
        else:
            AF.append(int(sample_info[6]))
#plot 4
        if sample_info[41] == '.':
            pass
        else:
            ANN.append(int(sample_info[41]))
            
#plot 1
    for sample_info in line[9:]:
        if sample_info[2] == '.':
            pass
        else:
            DP.append(int(sample_info[2]))
#plot 2
        if sample_info[0] == '.':
            pass
        else:
            GT.append(int(sample_info[0]))
    

#print(DP[:10])

fig, axs = plt.subplots(2, 2)
axs[0,0].hist(DP)
axs[0,0].set_title('Depth Distribution of Variant Genotypes',fontsize=9)
axs[0,0].set_xlabel('Variant Genotype',fontsize=9)
axs[0,0].set_ylabel('Depth Distribution',fontsize=9)
axs[0,1].hist(GT)
axs[0,1].set_title('Quality Distribution of Variant Genotypes',fontsize=9)
axs[0,1].set_xlabel('Variant Genotype',fontsize=9)
axs[0,1].set_ylabel('Quality',fontsize=9)
axs[1,0].hist(AF)
axs[1,0].set_title('Allele Frequency Spectrum of Variants',fontsize=9)
axs[1,0].set_xlabel('Variant Allele',fontsize=9)
axs[1,0].set_ylabel('Frequency',fontsize=9)
axs[1,1].plot(ANN)
axs[1,1].set_title('Predicted Effects of Variants',fontsize=9)
axs[1,1].set_xlabel('Variant',fontsize=9)
axs[1,1].set_ylabel('Effect',fontsize=9)

fig.tight_layout(pad=1.0)
#plt.show()
plt.savefig("subplots.png")
