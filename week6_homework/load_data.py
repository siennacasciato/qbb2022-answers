#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def main():
    in1_fname = sys.argv[1]
    in2_fname = sys.argv[2]
    bin_fname = sys.argv[3]
    out_fname = sys.argv[4]
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    # in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
    
    
    # print(data1)
    #
    # filtered = [11170245,12070245]
    # filtered = []
    #
    # for value in filtered:
    #     if value > 12070245:
    #         continue
    #     if value < 11170245:
    #         continue
    
    data1['F1'] = data1['F1']-(start_bin+1)
    data1['F2'] = data1['F2']-(start_bin+1)
    data2['F1'] = data2['F1']-(start_bin+1)
    data2['F2'] = data2['F2']-(start_bin+1)
    
    #print(data2)
    
    data1['score'] = numpy.log(data1['score'])
    data2['score'] = numpy.log(data2['score'])
    
    data1_mat = square_matrix(data1)
    data2_mat = square_matrix(data2)
    
    vmax = max(numpy.amax(data1_mat), numpy.amax(data2_mat))
    
    fig, axes = plt.subplots(ncols=3)
    axes[0].imshow(-data1_mat, cmap = 'magma', interpolation = 'nearest', vmax=0, vmin=-vmax)
    plt.show()
    
    

def square_matrix(data):
    N = numpy.max(data['F1'])
#command line output: 140
    bmat = numpy.zeros((N+1,N+1))
         
    for row in data:
        bmat[row[0], row[1]] = row[2]
        bmat[row[1],row[0]] = row[2]
    return bmat
        
    






if __name__ == "__main__":
    main()

