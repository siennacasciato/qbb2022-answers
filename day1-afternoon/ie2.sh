#goal: number of SNPs in the 1000 genomes file that intersects each gene and how many unique genes are represented.

genefile=/Users/cmdb/data/bed_files/genes.bed
vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf

bedtools intersect -a $genefile -b $vcffile > intersect_out_ie2.bed
