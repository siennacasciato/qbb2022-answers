#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA


#Step 1
sequence_file = sys.argv[1]
input_sequences = readFASTA(open(sequence_file))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

scoring_file = sys.argv[2]
alphabet = {}
for line in open(sys.argv[2]):
    fields = line.strip().split()
    for i, char in enumerate(fields):
        alphabet[char] = i
    break
        
score_mat = np.loadtxt(scoring_file, skiprows=1, usecols=range(1,len(alphabet)+1))

gap_penalty = float(sys.argv[3])
# output_file = sys.argv[4]


#Step 2
F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
traceback_matrix = np.empty((len(sequence1)+1, len(sequence2)+1), dtype=str)



# Step 3

#fills in the first column
for i in range(len(sequence1)+1):
    F_matrix[i,0] = i * gap_penalty
    traceback_matrix[i,0] = 'v'

#fills in the first row
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j * gap_penalty
    traceback_matrix[0,j] = 'h'


#fills in entire F matrix, goes through all columns and rows and fills them in
for i in range(1, len(sequence1)+1):
    for j in range(1, len(sequence2)+1):
        d = F_matrix[i-1,j-1] + score_mat[alphabet[sequence1[i-1]], alphabet[sequence2[j-1]]]
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)
        if d == max(d,h,v):
            traceback_matrix[i,j] = 'd'
        elif h == max(d,h,v):
            traceback_matrix[i,j] = 'h'
        else:
            traceback_matrix[i,j] = 'v'

#print(F_matrix)
print(traceback_matrix)


#Step 4
i = len(sequence1)
j = len(sequence2)
sequence1_align = ''
sequence2_align = ''

while(i!=0 or j!=0):
    c_dir = traceback_matrix[i,j]
    if c_dir == 'd':
        sequence1_align = sequence1[i-1] + sequence1_align
        sequence2_align = sequence2[j-1] + sequence2_align
        i-=1
        j-=1
    elif c_dir == 'h':
        sequence1_align = '-' + sequence1_align
        sequence2_align = sequence2[j-1] + sequence2_align
        j-=1
    elif c_dir == 'v':
        sequence1_align = sequence1[i-1] + sequence1_align
        sequence2_align = '-' + sequence2_align
        i-=1
                
#print(sequence1_align)
print(sequence2_align)


#command line input for amino acid sequences: ./week2hw.py needleman-wunsch/CTCF_38_M27_AA.faa needleman-wunsch/BLOSUM62.txt -10

#command line input for DNA sequences: ./week2hw.py needleman-wunsch/CTCF_38_M27_DNA.fna needleman-wunsch/HOXD70.txt -300


