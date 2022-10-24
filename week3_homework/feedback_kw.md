# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 1 + 0.5 + 1 + 1 + 1 + 0.25 + 1 = 8.75 points out of 10 possible points

1. Index genome

  * good! --> +1

2. align reads

  * very good! --> +1

3. sort bam files and index sorted bam files (0.5 points each)

  * great! --> +1

4. variant call with freebayes

  * fantastic! --> +1

5. filter variants

  * I see what you're going for here, but you want to use `QUAL > 20` as your filter criteria. [A PHRED score of 20 corresponds to a base call accuracy of 99%](https://en.wikipedia.org/wiki/Phred_quality_score)
  * --> +0.5

6. decompose complex haplotypes

  * great! --> +1

7. variant effect prediction

  * good! --> +1

8. python plotting script

  * for the allele frequency, I'm wondering if the `line[7:7]` is the issue for why that panel is blank? See this example list below that I made and indexed using command line python:
  ```
  >>> test_line = [1,2,3,4,5,6,7,8]
  >>> test_line[7]
  8
  >>> test_line[7:7]
  []
  ```
  * I'm not entirely sure why the annotation list is blank, but you want the annotation to be a string rather than an integer. The annotations should be a bar plot where the x-axis is some string/phrase and the y-axis is a count for the number of times you see that string/phrase
  * Also, you don't want to plot the genotype (GT), you want to plot the genotype quality (GQ)
  * --> +1

9. 4 panel plot (0.25 points each panel)

  * 2 of the panels are blank, and 1 is not plotting what was asked for --> +0.25

10. 1000 line vcf

  * good! --> +1
