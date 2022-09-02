# Feedback day2-lunch

Overall, this looks good. It would be much easier to read with some spaces breaking up the code into functional blocks and comments to explain the logic. There are also several checks that are not being performed. 

1. You need to check that Rgb is equal to zero or has three values. 
2. You are missing splitting up fields[11], which you could do reusing the code you use to split fields[10].
3. You also need to check that fields[10] and fields[11] both have the same number of elements as the number in fields[9].

Finally, I know it was done for debugging purposes, but you need to uncomment the `try` and `except` statements. Otherwise the code will fail if it encounters a value that is of an inappropriate data type.

You look like you're gaining comfort with Python, for loops, and lists. Keep it up!