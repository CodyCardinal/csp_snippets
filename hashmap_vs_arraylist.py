#setup
from array import array
from random import random,randint
import timeit

new_dict_data = {random():random()}
new_array_data = random()
randomnum = randint(1,10**7)

# For each HashMap(Dictionary) and Array List:
# compare runtime of lookup, insertion, and removal of items.

print("Test Create Array")
array_floats = array('d', (random() for i in range(10**7)))
%timeit array_floats = array('d', (random() for i in range(10**7)))
print(f"Array Length {len(array_floats)}")

print("Test Create Dictionary")
dict_floats = {x:x*random() for x in range(10**7)}
%timeit dict_floats = {x:x*random() for x in range(10**7)}
print(f"Dict Length {len(dict_floats)}")

print("Test Lookup in Array")
%timeit array_floats[randomnum]

print("Test Lookup in Dict")
%timeit dict_floats[randomnum]

print("Test insertion into Array")
array_floats.append(new_array_data)
%timeit array_floats.append(new_array_data)

print("Test insertion into Dict")
dict_floats.update(new_dict_data)
%timeit dict_floats.update(new_dict_data)

print("Test Removal from Array")
%timeit array_floats.pop(randomnum)

print("Test Removal from Dict")
%timeit dict_floats.pop(randomnum, None)

# Reference: https://towardsdatascience.com/faster-lookups-in-python-1d7503e9cd38