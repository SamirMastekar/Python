#!/usr/bin/env python
# coding: utf-8



mylist = list(range(1, 11))



# Lists can be created in another way called as list comprehension
res = [x**2 for x in mylist]

# the above list is equivalent to
res = []
for x in mylist:
    res.append(x**2)



# To get squares of only the even numbers from the list
res = [x**2 for x in mylist if x % 2 == 0]

# this is equivalent to
res = []
for x in mylist:
    if x % 2 == 0:
        res.append(x**2)



# Some more examples of list comprehensions
natural_numbers = [x + 1 for x in range(10)]
even_numbers = [x for x in range(10) if x % 2 == 0]
into_ten = [x * 10 for x in even]



# Sets, Dictionaries, and Tuples can also be created using comprehension

# Example of set
# Set of charactes in my_string which are not a,b,c, or d
my_string = 'abcdefghiiabcde'
res = {x for x in my_string if x not in 'abcd'}

# Create a dictionary where keys are numbers and values are their cubes
square_dict = {x: x**3 for x in mylist}

# Create tuples as well
res = (x for x in range(10))

# You can create nested lists using list comprehension as well
res = [[x,y] for x in mylist for y in mylist]
