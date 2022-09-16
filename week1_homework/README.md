#Week 1 Lab Assignment

1.1:
1Mbp x 5x = 5Mbp of data
5Mbp / 100bp = 50,000 reads

1Mbp x 15x = 15Mbp of data
15Mbp / 100bp = 150,000 reads


1.2:
see uploaded .png file.

1.3:
1,000 bp to 7,000 bp had not been sequenced. It does not match Poisson expectations because we expect Poisson distribution to be normal (form a bell shaped curve), which was not seen in the histogram produced.

1.4:
50,000 bp to 550,000 bp had not been sequenced. The Poisson distribution does not match the expectations because the distribution should show a bell shaped curve, but in the histogram it does not.


2.1:
```
grep -c '>' contigs.fasta
```
4 contigs were produced.

2.2:
```
less -S contigs.fasta.fai 
```
105830+47860+ 41351+39426 = 234467

length of contigs = 234467

2.3:
```
sort -k 2 -n contigs.fasta.fai
```
size of largest contig is 105830

2.4:
```
sort -k 2 -n | tail -2 contigs.fasta.fai
```
size of contig N50 is 41351


3.1:
```
dnadiff ./asm/ref.fa asm/contigs.fasta
less -S out.report
```
average identity of my assembly is 99.9955, compared to the reference which was also 99.9955.

3.2:
```
nucmer ./asm/ref.fa asm/contigs.fasta
show-coords -r -c -l out.delta > nucmer.coords
less -S nucmer.coords
```
the length of the longest alignment is from 3 bp to 26789 bp.

3.3:
```
less -S out.report 
```
there is 1 insertion in my assembly compared to the 5 insertions in the reference. There are no deletions in the assembly.


4.1:
```
show-coords -o out.delta > nucmer.coords
less -S nucmer.coords 
```
the position of the insertion in the assembly is in the region between 26787bp and 27500bp in node 3.

4.2:
```
less -S nucmer.coords 
```
the novel insertion is 713bp long.
27500-26787 = 713

4.3:
```
samtools faidx /Users/cmdb/qbb2022-answers/week1_homework/asm/contigs.fasta NODE_3_length_41351_cov_20.528098:26787-27500
```
insertion DNA sequence:
```
>NODE_3_length_41351_cov_20.528098:26787-27500
CCGCCCATGCGTAGGGGCTTCTTTAATTACTTGATTGACGCATGCCCCTCGTTCTACATG
TCTAGCTTCGTAACTGCCCCGATTTATACAGGAGCATATGCGTTTCGTAGTGCCGGGAAT
GCATACCAAAGGGCTCACGGCGGGTACGCCACAATGGCTCAAGTCGAAAATGAATCGAAG
ACAACAAGGAATACCGTACCCAATTACTCAAGGACCTCATACACCATCCCATGCTACTTA
TCTACAGACATACACGCCAGCACCCAGCAACCAAAGCACACCGACGATAAGACTACAATC
GCGATAAGCACAACTTACATTAGGAGGCCCGGCAAATCTTGACGGCGTTAAGTCCGACAC
GAATACCCCCCGACAAAAGCCTCGTATTCCGAGAGTACGAGAGTGCACAAAGCACCAAGG
CGGGGCTTCGGTACATCCACCAGTAGTCCCGTCGTGGCGGATTTTCGTCGCGGATGATCC
GAGGATTTCCTGCCTTGCCGAACACCTTACGTCATTCGGGGATGTCATAAAGCCAAACTT
AGGCAAGTAGAAGATGGAGCACGGTCTAAAGGATTAAAGTCCTCGAATAACAAAGGACTG
GAGTGCCTCAGGCATCTCTGCCGATCTGATTGCAAGAAAAAATGACAATATTAGTAAATT
AGCCTATGAATAGCGGCTTTAAGTTAATGCCGAGGTCAATATTGACATCGGTAG
```

4.4:
```
./asm/dna-decode.py -d --input insert.fasta
```
The decoded message :  Congratulations to the 2021 CMDB @ JHU class!  Keep on looking for little green aliens..

