# feedback.txt
## day1-lunch

Looks great. Not important, but a tip for formatting code in markdown is that you can put single-line code in backticks, e.g.:
`sort -nk 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | uniq -f 3 -c | cut -f 1,4`

Also, for both 3b and 4b, how would you avoid printing the extraneous information (e.g., the sample names) in the tallied results?

For 5e, each line of the VCF record both the overall allele frequency (AF) and the superpopulation-specific allele frequencies (EUR_AF, AFR_AF, etc.)--note that the substring "AF=" is part of both.

Think a bit more about what question 5f is asking--note that "AFR_AF" is present in every single line. But how would you extract just that part of each line?
