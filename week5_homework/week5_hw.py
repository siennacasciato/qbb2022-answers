#!/usr/bin/env python3

#Part 1

#Step 1

samtools view -b -q 10 D2_Sox2_R1.bam -o filt_D2_Sox2_R1.bam
samtools view -b -q 10 D2_Sox2_R1_input.bam -o filt_D2_Sox2_R1_input.bam
samtools view -b -q 10 D2_Sox2_R2.bam -o filt_D2_Sox2_R2.bam
samtools view -b -q 10 D2_Sox2_R2_input.bam -o filt_D2_Sox2_R2_input.bam

#Step 2
macs2 callpeak -t filt_D2_Sox2_R1.bam -c filt_D2_Sox2_R1_input.bam -g 95e6 -n R1 -B
macs2 callpeak -t filt_D2_Sox2_R2.bam -c filt_D2_Sox2_R2_input.bam -g 95e6 -n R2 -B

#Step 3
bedtools intersect -wa -a R1_peaks.narrowPeak -b R2_peaks.narrowPeak > intersect_peaks.narrowPeak

#Step 4
wc -l intersect_peaks.narrowPeak
#output of intersects for Sox2
593 intersect_peaks.narrowPeak

bedtools intersect -wa -a intersect_peaks.narrowPeak -b D2_Klf4_peaks.bed >klf_intersect.narrowPeak
wc -l klf_intersect.narrowPeak
#output of intersects for klf4

wc -l D2_Klf4_peaks.bed
60 D2_Klf4_peaks.bed

41 klf_intersect.narrowPeak
#percent co-localization is 41/60 *100 = 68.3% co-localization

Step 5
in step5.py file


#Part 2

#!/bin/bash
sort -k5,5nr intersect_peaks.narrowPeak > sort_sox2.narrowPeak

head -n 300 sort_sox2.narrowPeak >sort300_sox2.narrowPeak

awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' sort300_sox2.narrowPeak > awk_sox2.narrowPeak

samtools faidx -r awk_sox2.narrowPeak mm10.fa > extract_sox2.fa

meme-chip extract_sox2.fa


#Part 3
cd memechip_out/
cd /Users/cmdb/Downloads/motif_databases/MOUSE
cp HOCOMOCOv11_full_MOUSE_mono_meme_format.meme ~/qbb2022-answers/week5_homework/memechip_out/
cd ~/qbb2022-answers/week5_homework/memechip_out/
tomtom combined.meme HOCOMOCOv11_full_MOUSE_mono_meme_format.meme


