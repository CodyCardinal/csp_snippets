# Exercise From Fluent Python, 2nd Ed, Chapter 2.An Array of Sequences

# import the array type
from array import array
from random import random

# create an array of double-precision floats from any iterable object, use a generator expression
floats = array('d', (random() for i in range(10**7)))
# inspect the last number in the array
print(floats[-1])

# save the array to a binary file
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# create an empty array of doubles
floats2 = array('d')

# read 10m numbers from the binary file
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

# inspect the last number in the array
print(floats2[-1])

# verify the contents of the arrays match
floats2 == floats

# OUTPUT
# 0.7172038483089084
# 0.7172038483089084
# True
