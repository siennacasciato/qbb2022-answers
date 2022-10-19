# Week 1 Genome Assembly -- Feedback

1 + 0.75 + 0.25 + 1 + 1 + 1 + 0.75 + 1 + 1 + 0.5 = 8.25 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)

  * To store where your reads are simulated in the genome, you want to use the `slist` variable that you created at the beginning of the script. Then when you have `array = (j, +1)`, you want to reference the `j` location in `slist` and add one to that location, so something like `slist[j] += 1` instead of the `array = (j, +1)`.
  * --> +0.75

3. Question 1.2, 1.4 plotting script(s)

  * You want to plot your `slist` variable which will have counts for the number of reads overlapping each genomic position.
  * Your x-axis won't be the Genomic Position, it'll instead be the number of overlapping reads. Your y-axis will be the number of genomic positions
  * For your y variable from `scipy.stats.poisson.pmf`, you want to use lambda equal to the coverage you're simulating (5 or 15) rather than 200000 or 400000.
  * Additionally, for your y variable, in order to change it from probability of observing a coverage of 0, 1, 2, etc..., to the frequency count of observing that coverage for number of genomic positions you're considering, you'll want to multiply the y variable by the number of genomic locations total  (1 million)
  * --> +0.25

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * Once you change your code to edit and plot `slist`, the histograms should look more like you expect.
  * --> +1


5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * Once you have the new histograms, your observations will change. You can also use your `slist` and `y` variables. For `slist`, you can count how many of the list elements are equal to 0. And you just want the first `y` variable element.
  * --> +1

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.25, not quite, you specifically, want to order the contigs by length, largest to smallest, and then sum to find the contig whose length is shorter than or equal to other contigs larger than it, such that the sum of these contigs is half the genome length.

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33

  9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

    * position of insertion in assembly --> this doesn't match with what I would expect, I know you said how you found it, but have you considered that you want between, not including those end positions?
    * length of novel insertion --> +0.5; length should be end - beginning plus 1, otherwise it doesn't count the end. like if you're counting from 1 to 10, there are 10 numbers, but 10-1 is only 9.

  10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

    * DNA sequence of encoded message --> +0.25, code is the right idea
    * secret message --> +0.25, code is the right idea

  Your commands and given output, as you have them written down, would not produce the correct output message. We're okay with you working with other people, but we want to make sure that you also understand the commands that you're running. If your code isn't working, you're always welcome to reach out for help, either from classmates or from the TAs. So, if you really did get the correct output, please correct the commands you used, but if you were having trouble getting that output, let us know and we can help.
