#!/usr/bin/env python
# coding: utf-8



# Simple variable assignment
fiveFloat = 5.0
fiveInt = 5
fiveString = "Five"



# Printing using string formatting
print(f"This evaluates to TEN = {fiveFloat + fiveInt}")



# Checking type of data
print(type(fiveFloat))
print(type(fiveInt))
type(fiveString)
fiveFloat = "Five"
type(fiveFloat)



# Results of operations can be assigned back to a new variable
x = 10
y = 15
z = x + y
print(z)



# Input from console
input_string = input("What is your name? ")
print(f"Okay, your name is {input_string}")

# Inputs are always strings. To take numbers as inputs,
# cast them to int or float as per need
num1 = 54
num2 = input("Enter another number: ")
print(num1 + float(num2))



# Lists
empty_li = []
# A more readable way to create lists
empty_li = list()



# Creating some lists
some_li = [1, 4, 6]
# List can contain items of different types
other_li = [1, [1, 2, 3], 'Four']
# You can create a list with a single element
one_li = [1]
print(other_li[1][0])



# Appending at the end of the list
some_li.append(2)
some_li.append(-3)



# Remove last element using pop and store it in the variable
print(f"Before popping {some_li}")
last_elem = some_li.pop()
print(f"After popping {some_li}")
print(f"Popped element {last_elem}")



# Accessing elements of a list.
# Important: Lists start at index 0 and end at (length - 1)
some_li[0]
some_li[-1]
some_li[2]
print(some_li)
# You can obtain custom slices of the list.
# This always returns new lists and keeps the original list unmodified.
print(some_li[1:4])
print(some_li[1:4:2])
# The format for slicing is as follows
# some_li[start index : end index : step]



# Some more examples of slicing
some_li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(some_li)
print(some_li[::4])
print(some_li[1::2])
# Reversing a list is easy with slicing
# just use a step of -1
print(some_li[::-1])

# ## Assignment
# Find the middle two elements of a list



some_li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List: {some_li} has {len(some_li)} elems")
mid_idx = (len(some_li) + 1) // 2
print(f"Middle index {mid_idx}")
print(some_li[mid_idx-1:mid_idx+1])



# Removing elements at a certain index
del some_li[3]
# Removing a specific element if it exists
some_li.remove(8)
# del some_li[3] is equivalent to some_li.remove(some_li[3])

# Removing elements from nested lists
other_li = [1, [1, "2", 3], 'Four']
del other_li[1][1] # Will delete "2" from the nested list
# How do you delete an elem from nested list?



# Shallow copy
old_li = [1,2,3,4,5]
new_li = old_li # Both the lists now point to the same memory
print(old_li)
print(new_li)
old_li.append(10)
print(old_li)
print(new_li)
new_li is old_li



# Deep copy
old_li = [1,2,3,4,5]
new_li = old_li[:] # Both the lists now have their own copy of the data
print(old_li)
print(new_li)
old_li.append(10)
print(old_li)
print(new_li)
new_li is old_li



# Inserting elements at certain indices
some_li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(some_li)
some_li.insert(3, "InsertedValue")
print(some_li)



# Concatenating
some_li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li = [10, 20, 30]
some_li = some_li + li # Using the + operator
some_li.extend([1, 2, 3]) # Using the extend function



# Check for existence
100 in some_li # only tells whether the element exists or not
idxOf10 = some_li.index('10') # Gives the index if the element exists or raises ValueError



# obtaining the length of the list
len(some_li)



# Tuples
# Again it can contain items of different types
tup = ()
# Create empty tuple in a more readable format
tup = tuple()
tup = (1, 2)
tup = (1, 2, 3)
tup = (1, 2, 3, 4)
tup = (1, 2, "Three")



# Most operations that can be performed on Lists can be performed on Tuples as well
tup[0]
len(tup)
2 in tup
tup.index('Three')
tup[1:4:2] # Slicing works as well. Returns a new tuple

# You cannot delete elements from a tuple unlike lists.
# This is because tuples are immutable (cannot be changed)
# While lists are mutable (can be changed)



# Unpacking tuples into exactly the same number of variables
a, b = (1, 3)
print(a)
print(b)
tup = ('a', 'b', 'c', 'd')
# Unpacking tuples into a list and single variables
a, *b, c = 1, 2, 3, 4, 5
print(a, c)



# You can swap easily because for tuples the () are not mandatory
a, c = c, a
print(a, c)



# Dictionaries
empty_dict = {}
# A better way to create empty dictionaries
empty_dict = dict()
# Create dictionaries manually
some_dict ={'one': 1,
            'two': 2,
            'three': 3,
            1: 'four'}



# Access dictionaries by keys rather than indices
# Dictionaries are unordered data structures
print(some_dict['two'])
print(some_dict[1])
print(some_dict)
print(some_dict['five'])



# Invalid vs Valid keys
# Keys should be an immutable datatype
# Values can be anything
invalid_dict = {[1,2]: 'first'}
valid_dict = {(1,2): 'first'}



# Lookup
some_dict['one']
# If the key does not exist then it will throw KeyError



# Get keys and values as lists
list(some_dict.keys())
list(some_dict.values())



# Existence of keys
'1' in some_dict

# A safe way to get the value of a specific key
# If key exists returns the value
some_dict.get('one')
# If it does not then returns the None object
# It takes an optional argument which specifies
# what to return in case the key is not found
# if you do not want it to return None.
# Use shift+tab with cursor inside get() to obtain documentation
some_dict.get('seven')


some_dict ={'one': 1,
            'two': 2,
            'three': 3,
            1: 'four'}

# You can add keys in 2 ways
# If the key 'five' does not exist it will create a new key
# and assign 7 to it.
# If it exists it will update the value to 7
some_dict['five'] = 7
# Another way to create a new key if one does not exist
# is to use the setdefault method
# It works exactly like above
some_dict.setdefault('five', 5)
some_dict.setdefault('five', 6)



# Updating Dictionaries with other dictionaries
# Updates existing keys and adds non-existent keys
some_dict.update({'six': 6, 123: "One_Two_Three"})



# Removing keys
del some_dict['five']



# To get all the key value pairs as a list of tuples from a dictionary
result_items = list(res.items())
# collection of key,value
print(result_items)
# 0th entry's key
print(result_items[0][0])
# 0th entry's value
print(result_items[0][1])



# Sets
empty_set = set()
some_set = {1, 1, 2, 3, 3, 4, 4}



# Invalid vs Valid set elements
invalid_set = {[1, 2], [2, 3]}
valid_set = {(1, 2), (2, 3)}
# Because sets have unique elements and is an ordered data structures
# we cannot have mutable elements



# Adding to sets
some_set.add(6)
some_set.add(3)
# Removing elements from a set
some_set.remove(5) # Removes the element 5



# Set operations
other_set = {1, 4, 8, 10}
print(some_set, other_set)
print(other_set & some_set) # Set intersection
print(other_set | some_set) # Set union
print(other_set - some_set) # Set difference (remove from other_set what is present in some_set)
print(some_set - other_set) # Set difference the other way
print(other_set ^ some_set) # Symmetric set difference
print(other_set >= some_set) # Proper set containment
print(other_set < some_set) # Improper set containment



# Existence of elements
3 in some_set



# Counting the number of occurrances of individual letters in a word
word = input("Enter the word: ")
res = dict()
for char in word:
    if char in res:
        res[char] = res[char] + 1 # equivalent to res[char] += 1
    else:
        res[char] = 1

print(res)



# Given a name in the following format:
# <first_name> <middle_name> <last_name1> <last_name2> ... <last_name<N>>
# Output
# <last_name<N>>, <first_name> <middle_name> <last_name1> ... <last_name<N-1>>
name = input("Enter your name: ")
print(name.split())
*first_names, last_name = name.split()
# Print takes a keyword argument called end which specifies what character
# is to be printed after printing the input string. By default it is set to
# the new line character '\n'
print(f"{last_name},", end=' ')
for f_name in first_names:
    print(f_name, end=' ')



print("There is a star at the end of this sentence", end='*')
print("It is indeed present")



# Sorting of lists
# in place sorting
my_list = list(range(10, 0, -1))
my_list.sort()

# sort into a new list using the sorted function
my_list = list(range(10, 0, -1))
sorted_list = sorted(my_list)

# Sort in reverse using the reverse keyword argument
my_list = list(range(10))
sorted_list = sorted(my_list, reverse=True)
my_list.sort(reverse=True)




