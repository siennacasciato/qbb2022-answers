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