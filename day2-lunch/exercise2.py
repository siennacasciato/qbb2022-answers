#!/usr/bin//env python3
import sys

from bedfile import parse_bed

ex2 = parse_bed("hg38_gencodev41_chr21.bed")

#print(ex2)

#exon_list = open("parse_bed").readlines(10)

exons = []

for line in ex2:
    exons.append(line[9])

#print(exons)

#get median
exons.sort()
#print(exons)
print(exons[len(exons)//2])

#median exon is 4















#def parse_bed(fname):
#    fs = open(fname, mode = 'r')
#    bed = []
#    data_types = [str, int, int, str, int, str, int, int, int, int]
#    for line in fs:
#        fields = line.rstrip().split("\t")
#        for i in range(min(len(data_types),len(fields))):
#            fields[i] = data_types[i](fields[i])
#            try: 
#                if fields[i] != ".":
#                    fields[i] = data_types[i](fields[i])
 #       bed.append(fields[:min(len(data_types),len(fields))])
  #      chrom = fields[0]
   #     start = int(fields[1])
    #    end = int(fields[2])
     #   exon = int(fields[10])
        
     #   bed.append([chrom,start,end,exon])
        

#finding the median

#taking out only the exons column
#exon_list = open("hg38_gencodev41_chr21.bed").readlines(10)

#in terminal
#sort -n exon_list
#head -n 110 exon_list
#tail exon_list

        
        
        
        
        
        #except:
            #print(f"line {h} is malformed", file = sys.stderr)
        #fs.close
        #return bed
#if __name__ == "__main__":
    #bed = hg38_gencodev41_chr21(sys.argv[1])
    
    #print bed

#file for genes and exons is the hg38_gencodev41_chr21.bed file

#load the hg bed file
#find the median number of exons for genes in that hg bed file