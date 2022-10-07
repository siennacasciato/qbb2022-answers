#!/usr/bin/env python3

#Step 2
#PCA ran in command line:
#plink --vcf genotypes.vcf --pca 10 --out pcafile

import numpy as np
import matplotlib.pyplot as plt

# plinkpca = np.genfromtxt("pcafile.eigenvec", dtype = None, encoding = None, names = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12"])
#
# a_list = plinkpca['col1']
# b_list = plinkpca['col2']
# pca1 = plinkpca['col3']
# pca2 = plinkpca['col4']
# pca3 = plinkpca['col5']
# pca4 = plinkpca['col6']
# pca5 = plinkpca['col7']
# pca6 = plinkpca['col8']
# pca7 = plinkpca['col9']
# pca8 = plinkpca['col10']
# pca9 = plinkpca['col11']
# pca10 = plinkpca['col12']
#
# fig, ax = plt.subplots()
# ax.scatter(pca1, pca2)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# #plt.show()
# plt.savefig("q2.png")


#Step 3

# plink --vcf genotypes.vcf --pca 10 --out pcafile
# plink --freq --vcf genotypes.vcf --out affile

# allele_freq = np.genfromtxt("affile.frq", dtype = None, encoding = None, names = ["CHR", "SNP", "A1", "A2", "MAF", "NCHROBS"])

# print(allele_freq)

# fig, ax = plt.subplots()
# ax.hist(allele_freq['MAF'][1:].astype(float),bins=50)
# plt.xlabel('SNP')
# plt.ylabel('Frequency')
# #plt.show()
# plt.savefig("AF.png")


#Step 4
# plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar pcafile.eigenvec --allow-no-sex --out CB1908_gwas_results
# plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar pcafile.eigenvec --allow-no-sex --out GS451_gwas_results


#Step 5

#qmplot -I CB1908_gwas_results.assoc.linear -T CB1908_IC50 -M ID --dpi 300 -P 1e-5 -O manhattan --display

import pandas as pd
import matplotlib.pyplot as plt
from qmplot import manhattanplot

#if __name__ == "__main__":
df = pd.read_table("CB1908_gwas_results.assoc.linear", header=int(['CHR'][1:], ['SNP'][1:], ['BP'][1:], ['A1'][1:], ['TEST'][1:], ['NMISS'][1:], ['BETA'][1:], ['STAT'][1:], ['P'][1:]):
    df = df.dropna(how="any", axis=0)
    
#ax = manhattanplot(data=df)
#plt.show()
#plt.savefig("CB1908_manhattan.png")



# CB1908_man = np.genfromtxt("CB1908_gwas_results.assoc.linear", dtype = None, encoding = None, names = ["CHR", "SNP", "BP", "A1", "TEST", "NMISS", "BETA", "STAT", "P"])
# gt_rows = np.where(CB1908_man['TEST']=='ADD')
# CB1908_subset = CB1908_man[gt_rows]
# #print(CB1908_subset)
#
# CB1908_log = -np.log10(float(CB1908_man[8]))

#CB1908_len = range(len(CB1908_subset))
#CB1908_group = CB1908_subset.groupby(('CHR'))