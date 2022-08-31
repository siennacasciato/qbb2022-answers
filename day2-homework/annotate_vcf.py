#QBB2022 - Day 2 - Homework Exercises Submission

import sys
from vcfParser import parse_vcf

parsed_dbSNP = parse_vcf('dbSNP_snippet.vcf')
parsed_rsnip = parse_vcf('random_snippet.vcf')

#for i in range(10):
#    print(parsed_dbSNP[i])

dbsnp = {}
for line in parsed_dbSNP:
    if line[0] == 'CHROM':
        continue
    chrom = line[0]
    pos = line[1]
    ref = line[3]
    IDs = line[2]

    dbsnp[pos] = IDs


#for k,v in dbsnp.items():
#    print(k,v)


for i in parsed_rsnip:
    if i[1] in dbsnp:
        #print('yes')
        i[2] = dbsnp[i[1]]
        print(i[0:4])
    else:
        continue
	




