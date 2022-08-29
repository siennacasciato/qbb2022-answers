#QBB2022 - Day 1 - Lunch Exercises  Submission
1. I'm excited to learn how to analyze biological data using coding.

2.
b. Average of 62 exons per gene. 

wc exons.chr21.bed 
   13653   40959  327672 exons.chr21.bed
wc genes.chr21.bed 
     219     657    5256 genes.chr21.bed

(13653 exons / 219 genes = 62 exons)

c. Find how many exons are in each gene. Store the number of exons in a new file (mkdir exons). List the exons in numerical order (sort -n). Use head 110. Use tail on the output to find the median.

3. 
b.

305 chr21	1
 678 chr21	2
  79 chr21	3
 377 chr21	4
 808 chr21	5
 148 chr21	6
1050 chr21	7
 156 chr21	8
 654 chr21	9
  17 chr21	10
  17 chr21	11
  30 chr21	12
  62 chr21	13
 228 chr21	14
 992 chr21	15
 
 The first column is the number of regions, and the last column is the state.
 
 sort -nk 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | uniq -f 3 -c | cut -f 1,4
 
 
 c. We would need to look at the length of each gene for each state by substracting the start and end points of each gene. Add together the lengths of each gene that are in the same state for each state to determine which state makes up the largest piece of the genome.
