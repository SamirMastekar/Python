#!/usr/bin/env python
# coding: utf-8

# # Inbuilt modules

# ### Importing modules and using their functionality



# A module can be imported like this
import math

# You can import only specific functionality from a module like this
from math import ceil, floor

# A module can be imported with an alias like this
import math as m

# You can import every symbol from a module like this but avoid doing this!!!!
from math import *



# Use functionality
print(math.sqrt(2))
print(ceil(2.2))
print(floor(3.8))
print(m.sqrt(3))



# Check what is available in this module
dir(math)
# OR
dir('math') # without loading the module

# Check what a function does using help
help(math.isinf)
# OR
help('math.isinf') # without loading the module and/or the functionality

# ## String Module



import string



# You have a lot of attributes in the string module like these
string.ascii_letters # All letters a-z and A-Z
string.ascii_uppercase # Only A-Z
string.digits # 0-9
string.whitespace # All possible white space characters



# Joining a list of strings with a separator
my_str_list = ["Str1", "Str2", "Str3", "Str4"]
str_to_put_between_elems = '****'
joined_str = str_to_put_between_elems.join(my_str_list)
print(joined_str)

# ## Random Module



import random



# You can choose at random from the given inputs like so
random.choice(("Heads", "Tails"))



# Program to roll a 6 sided dice and if we get 
def roll():
    bonus = 0
    chances = 0
    while True:
        value = random.choice(range(1,7))
        chances += 1
        if value == 6:
            print('You got lucky! Extra chance')
            bonus += 1
            continue
        else:
            break
    return chances, bonus

for x in range(500):
    print('In {} rolls, you had {} extra chances!'.format(*roll()))



# Random strings
from string import ascii_lowercase

chars50 = [random.choice(ascii_lowercase) for i in range(50)]
''.join(chars50)

# ## Pretty Printer Module



# Use this for formatting your output properly
# In short - human readable format
from pprint import pprint



my_dict = {str(x): x**2 for x in range(10)}
pprint(my_dict)
