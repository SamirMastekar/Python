#!/usr/bin/env python
# coding: utf-8



# if-elif-else
var = 20

# Indentations are extremely important!!!
# Do not mix Tabs and Spaces in a single python file.
if var > 10:
    print("var is greater than 10")
elif var < 10:
    print("var is less than 10")
else:
    print("var is equal to 10")



# You can have as many elifs as you want
option = 3

if option == 1:
    print("Choosing option 1")
elif option == 2:
    print("Choosing option 2")
elif option == 3:
    print("Choosing option 3")
elif option == 4:
    print("Choosing option 4")
else:
    print("Invalid option. Try again.")



# Advanced, can be skipped
# Equivalent to C's ternary operator (var > 10) ? 5 : 4
var1 = 5 if var > 10 else 4
print(var1)



# for loops

# Looping over lists
for i in [1, 3, 5, 6]:
    print(i)
    
some_dict ={'one': 1,
            'two': 2,
            'three': 3,
            1: 'four'}

# Looping over dicts: Method #1
for key, val in some_dict.items():
    print(key, val)
    
# Looping over dicts: Method #2
for item in some_dict.items():
    print(item[0], item[1]) # item[0] is the key. item[1] is the value.

# Looping for a set number of times
for i in range(5): # Loops 5 times starting at 0 and ending at 4 not including 5
    print(i)
    
for i in range(4, 10):
    print(i)

# You can jump as well
for i in range(4, 10, 3):
    print(i)



# while loops
x = 10
# Do something while something is true
while x > 0:
    print(x)
    x += 1

# ## Assignment
# Given a word count the instances of all the characters in it.



# Counting the number of occurrances of individual letters in a word
word = input("Enter the word: ")
res = dict()
for char in word:
    print(char, end=" ")
    if char in res:
        res[char] = res[char] + 1 # equivalent to res[char] += 1
    else:
        res[char] = 1
    print(res)
print(res)
