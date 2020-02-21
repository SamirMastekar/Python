#!/usr/bin/env python
# coding: utf-8



# This is how you define a function.
# This function takes 0 arguments and returns None.
def hello_world():
    print("Hello World!")
    
# This is how you call a function.
hello_world()

# This function takes 2 variables as arguments
# returns None.
def print_greater(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        print("Invalid inputs")
    else:
        if x > y:
            print(x)
        else:
            print(y)

# This function takes 2 arguments and returns
# the larger of the two
def return_greater(x, y):
    if x > y:
        return x
    else:
        return y
    

greater = return_greater(y=10, x=20)
print(greater)



# To enforce types use isinstance(<variable>, <datatype>)



greater = return_greater(34, 45)
print(greater)

if return_greater(34, 45):
    print("Non None")
if not print_greater(34, 45):
    print("None")



def square(x):
    return x**2

# This function takes a list and returns its square
# as another list.
# You can call a function from a function.
# This is called nesting.
def square_list(my_list):
    res = []
    for elem in my_list:
        res.append(square(elem))
    return res

sq_lst = square_list([5, 10, 15, 20])
print(sq_lst)



# This is how you add a docstring to document the function.
def add(x, y):
    """
    This function adds two numbers and returns the sum
    """
    print("x is {} and y is {}".format(x, y))
    return x + y

add(5, 6)
# You can call functions by specifying the input arguments
# as keywords like so. The order does not matter.
add(y=5, x=6)

# The docstring can be accessed directly via the
# __doc__ python internal attribute
print(add.__doc__)



# Recursion.
# Prints the n-th fibonacci number
# 1, 1, 3, 5, 8, 13, 21, 34, 55, 89...
def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



fibonacci(6)



# Another example of recursion is Binary search
my_list = list(range(0, 100, 5))
def binary_search(input_list, n):
    print(f"Looking at {input_list}")
    list_len = len(input_list)
    if list_len == 0:
        print("Not Found")
        return
    if list_len == 1:
        if n == input_list[0]:
            print("Found")
            return
    mid = list_len // 2
    if n == input_list[mid]:
        print("Found")
        return
    elif n > input_list[mid]:
        binary_search(input_list[mid+1:], n)
    else: # n < input_list[mid]
        binary_search(input_list[:mid], n)

print(my_list)
binary_search(my_list, 86)



# A function can take Variable number of arguments
def add(*input_numbers):
    res_sum = 0
    for num in input_numbers:
        res_sum = res_sum + num
    return res_sum

print(add(5, 6))
print(add(1, 2, 3))
print(add(3,4,5,6,7,8))
print(add(10))



# A function can take variable number of
# keyword arguments.
# The name of the input variable kwargs is a convention.
# You can call it bunny if you want.
def varkwargs(**kwargs):
    return kwargs

varkwargs(color="Blue", car="BMW")



# You can mix the arguement types
# here x is called as a positional argument
def mixed_args(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

varargs(1, 4, 'asd')
varkwargs(big="foot", small=4)

mixed_args(0, 1, 'test', code="Python")



# Sorting of lists using custom functions
# in place sorting

my_list = ['###_job2', 'ABC_job1', 'DEF_job3']

# This function takes an element of my_list and returns a value
# which will be used for sorting. For us this is the job ID.
def sort_by_jobs(value):
    job_id = int(value.split('_job')[1])
    return job_id

# sort using custom keys
l1 = sorted(my_list, key=sort_by_jobs)
l2 = my_list[:]
l2.sort(key=sort_by_jobs)
print(l1)
print(l2)
print(l1 == l2)



def calc(a, b, **kwargs):
    if kwargs['operation'] == '+':
        return a + b

def calc_parse(user_val):
    op1, op, op2 = user_val.split(' ')
    return calc(int(op1), int(op2), operation=op)

# Using the inbuilt eval function to evaluate the string
# as python code
def better_calc(user_val):
    # something better here
    return eval(user_val)

print(calc_parse('1 + 2'))
