#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str]
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        try:
        #if True:
            for j in range(min(len(field_types), len(fields))):
                if fields[j]== ".":
                    continue
                print(i)
                fields[j] = field_types[j](fields[j])
            if fieldN >= 9:
                Rgb = fields[8].split(",")
                for j in range(len(Rgb)):
                    Rgb[j] = int(Rgb[j])
                fields[8] = Rgb
            if fieldN > 10:
                size = fields[10].rstrip(",").split(",")
                print(size)
                for j in range(len(size)):
                    size[j] = int(size[j])
                    print(size[j])
                fields[10] = size
                print(f"Line {i} appears malformed", file=sys.stderr)      
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    return bed
if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    print(bed[0])