#!/usr/bin/env python
# coding: utf-8



# Numbers
3
4.0
5.2342

# Write multiline comments with
# a '#' on each line
# Using IDEs or other editors you can convert
# multiple lines to comments automatically



# Math is as you would expect
1 + 1.0 + 0.34
-2 * 4
3 / 4
3 - -6 # This is not readable so better to write it as 3 - (-6)



# Integer division uses // and rounds down
# / always returns floats no matter what the operands are (ints or floats)
1 // 2
4 // -2
3 // 1.2



# Modulo operator
7 % 3



# Exponentiation
2**4



# Precedence with parentheses
(5 + (1 + 4) ) * 5



# You can round floating point number to the nearest integer using round()
round(5.523) # returns 6
round(5.123) # returns 5



# Boolean primitives
True
False



# Boolean operators
True and False
True or False
not True



# Boolean as ints
# This is a bad practice so avoid doing this
print(True + True)
print(True * 8)
False - 5



# Comparing Boolean and Ints
# This is a bad practice so avoid doing this
0 == False
1 == True
5 == True
-2 != False



# Cast int to bool
# This is a bad practice so avoid doing this
bool(3)
print(bool(-6))
bool(0)
0 and 2
-5 or 0
1 and 2



# Compare numbers
1 == 2
2 < 3
3 <= 4
1 < 2 <= 3 # Chain comparisons. This is equivalent to 1 < 2 and 2 <= 3
1 != 0



# Strings. Single and double quotes are equivalent
"This is a string"
'This is also a string'

# Multiple strings can be written like this
# It is a shorthand for string concatenation
print("This is the first line."
"This is the second line.")

# Multiline strings can also be written like this
"""
This is a multiline string.
We can write as many lines as we want.
Go ahead, write a lot of lines.
It will be considered as a single string.
""";
# Use semi-colons to suppress output



# When you want to print quotes use different quotes for the string
# or use escape characters \
print("This is 'a' string")
print('This is "also" a string')
print("This is \"a\" string")



# String operators +, [], *
# String concatenation can be done using +
print("This is" + "a string")
# String elements can be accessed using [index]
# Index starts at 0 for the start of the string
# and -1 for the end of the string
print("This is a string"[0])
print("This is a string"[-4])
print("This is a string"[5])
# You can split the string
print("This, is, a, string".split(','))
# You can remove leading and trailing white spaces from string using strip
print("   **Removing leading and trailing spaces.**   ".strip())
# You can print the same string multiple times using * operator
print("How many times?"*5)



# Length of a string
len("This is a string")



# String formatting
print("{} can be {}".format("This", "formatted"))
print("Printing {0}. {0} again. Something different {1}".format("This", "now"))
print("My favourite colour is {colour}".format(colour="Red"))
print("This %s style of %s" % ("is the old", "formatting"))

# A new way to format strings in Python 3.6+
my_name = "Vishal"
my_surname = "Sontakke"
print(f"My name is {my_name}")



# Empty data structures return False on casting
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(None)) # None vs empty



# Empty data structures are different from the None object
None == ""




