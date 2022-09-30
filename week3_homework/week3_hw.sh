#!/bin/bash

#Step 1
bwa index sacCer3.fa

#Step 2
for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
 	bwa mem \
 	-R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" \
 	-t 4 \
 	-o ${SAMPLE}.sam \
 	sacCer3.fa ${SAMPLE}.fastq
done

#Step 3a
for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
 		samtools sort -@4 -O bam -o ${SAMPLE}.bam ${SAMPLE}.sam
done

#Step 3b
for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
  		samtools index -b ${SAMPLE}.bam
done

#Step 4
freebayes -f sacCer3.fa -L bam_files.txt --genotype-qualities -p 1 > fb.vcf

#Step 5
vcffilter -f 'QUAL > 0.99' fb.vcf > yeast_filt.vcf

#Step 6
vcfallelicprimitives -k -g yeast_filt.vcf > yeast_filt2.vcf

#Step 7
#ran in command line:
snpeff ann -sequenceOntology R64-1-1.99 yeast_filt2.vcf > ann_vcf.vcf

#Step 8
# in week3_hw.py

