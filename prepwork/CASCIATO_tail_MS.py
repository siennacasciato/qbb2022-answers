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

# This is a good start. You appear to get using sys.argv and what you need
# to do to ensure you're not trying to get an item that doesn't exist in the
# list. Your first for loop is going to print every line in the file. Your 
# second will throw an error. I understand your logic in trying to reverse
# the lines and then print out the first "n_lines" lines. However "reverse" 
# isn't a function on its own. It can be called from a list to reverse the list.
# You need to save all of the lines in a list and then reverse it. So first,
# you need to create an empty list and then append each line to that list.
# It is also really important to get into the habit of commenting your code so
# you and others can understand what you were trying to do sometime in the
# future. Overall, you're on the right track. Keep it up! - Mike