#QBB2022 - Day 1 - Homework Exercises Submission

Exercise 1

1. Error message:
```
Considering  A
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  C
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  G
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  T
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
 ```
add -v nuc$nuc, delete $ in later $nuc

 #!/bin/bash

 #USAGE: bash exercise1.sh input_VCF

```
 for nuc in A C G T
 do
   echo "Considering " $nuc
   awk '/^#/{next} {if ($4 == $nuc) {print $5}}' $1 | sort | uniq -c
 done
```


Output from working script:
awk -v nuc=$nuc '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c




Exercise 2:

I chose to use state 2 because it is a transcription start site, which would be close to promoter regions of the genome. I used bedtools to intersect the vcf file and the chromHMM file in order to only use data from the vcf file that matched the data in the chromHMM file. I used awk to only print the lines with genes in state 2. 

awk code:
```
awk '{if ($4 == 2) {print}}' "chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed" > twofile
```

Bedtools code:
```
chromfile=/Users/cmdb/qbb2022-answers/day1-homework/twofile
vcffile=/Users/cmdb/qbb2022-answers/day1-homework/random_snippet.vcf

bedtools intersect -a $vcffile -b $chromfile > intersect_out_exercise2.vcf
```
```
awk  '/^#/{next} {if ($4 == "C") {print $5}}' intersect_out_exercise2.vcf | sort | uniq -c
   7 A
   4 G
  24 T
```
Last, I ran awk again to identify the most common alternate cytosine reference allele for the variants in the promoter like regions. I found that thymine is the most common alternate allele. This makes sense because transition mutations are common. Transition mutations are where a purine is changed to another purine (A to G or G to A) or when a pyrimidine is changed to another pyrimidine (C to T or T to C). It makes sense that thymine was the most common alternate allele to cytosine because a transition mutation was likely occurring.


Exercise 3:

The first line of the exercise3 script is printing the lines 1 and 2 in the file and putting them into a new created file called variants.bed.
The second line is sorting the lines by field and numerically in the genes.bed file. The output of this is then being put into a new created file called genes.sorted.bed.
The third line is using bedtools to find the closest matches between the files varients.bed and genes.sorted.bed.

First error message:
Error: unable to open file or unable to determine types for file variants.bed

- Please ensure that your file is TAB delimited (e.g., cat -t FILE).
- Also ensure that your file has integer chromosome coordinates in the 
  expected columns (e.g., cols 2 and 3 for BED).

Correct the script by making it tab delimited.

Second error message:
Error: Sorted input specified, but the file variants.bed has the following out of order record

Correct the script by sorting.


Corrected script:
```
awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed
```


10293 variants
```
sort -k 7 variants | uniq -cf 6 | wc
     200    1600   12047
```
200 unique genes.

on average: 51 variants connected to a gene on average.
(10293/200=51)

git add README.md exercise1.sh
git commit -m "edited script and answers for day 1 hw exercise 1"
git push	





 
 
