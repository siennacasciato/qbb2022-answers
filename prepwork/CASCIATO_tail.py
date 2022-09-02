#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys
filename = sys.argv[1]
if len(sys.argv) > 2:  
    n_lines = int(sys.argv[2])
else:
    n_lines = 10
for i, line in enumerate(open(filename)):
    print(line.strip('\r\n'))
for i, line in reverse(open(filename)):
    if i < n_lines:
        print(line.strip('\r\n'))