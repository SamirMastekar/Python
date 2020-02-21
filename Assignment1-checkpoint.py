#!/usr/bin/env python
# coding: utf-8

# ### 1. FizzBuzz
# Given a list `mylist`, produce a list of results where each element:
# if it is divisible by 3 print `"Fizz"`
# if it is divisible by 5 print `"Buzz"`
# if it is divisible by 3 and 5 print `"FizzBuzz"`
# if `NOTA`, print `None`
# 
# #### Example:
# `In: [1, 3, 5]`  
# `Out: [None, "Fizz", "Buzz"]`
# 
# `In: []`  
# `Out: []`
# 
# `In: [3, 5, 15, 45]`  
# `Out: ["Fizz", "Buzz", "FizzBuzz", "FizzBuzz"]`

# In[1]:


mylist = [3, 4, 5, 15, 40, 25, 12, 8]
res = []
for elem in mylist:
    div_by_3 = elem % 3 == 0
    div_by_5 = elem % 5 == 0
    if div_by_3 and not div_by_5:
        res.append('Fizz')
    elif div_by_5 and not div_by_3:
        res.append('Buzz')
    elif div_by_3 and div_by_5:
        res.append('FizzBuzz')
    else:
        res.append(None)

for i in range(len(mylist)):
    print(f"{mylist[i]} \t {res[i]}")

# ### 2. Calculator
# 
# Ask for input of type `'operand1 operation operand2'` and print the result of operation.
# If user gives empty input, stop with a message `"Exiting!"` else ask for the input again.
# 
# #### Example:
# `In: Enter operand 1, operation, operand2: 1 + 4`  
# `Out: 5`
# 
# `In: Enter operand 1, operation, operand2: 2.2 + 4`  
# `Out: 6.2`
# 
# `In: Enter operand 1, operation, operand2:`  
# `Out: Exiting!`

# In[4]:


while True:
    print("Welcome to the simple calculator. To exit simply give an empty input.")
    exp = input("Enter operand1 operation operand2: ")
    if exp == "":
        print("Exiting!")
        break
    exp_split = exp.split()
    operand1 = float(exp_split[0])
    operation = exp_split[1]
    operand2 = float(exp_split[2])
    if operation == '+':
        print(f"Result {operand1 + operand2}")
    elif operation == '-':
        print(f"Result {operand1 - operand2}")
    elif operation == '*':
        print(f"Result {operand1 * operand2}")
    elif operation == '/':
        print(f"Result {operand1 / operand2}")
    else:
        print("Invalid operation please try again.")

# ### 3. Squares
# Given a list `mylist`, create a list which contains the squares of each element of `mylist`.
# 
# #### Example:
# `In: [10, 3 ,50]`  
# `Out: [100, 9, 2500]`



mylist = list(range(1, 11))
squares = []
for elem in mylist:
    squares.append(elem**2)

for i in range(len(mylist)):
    print(f"{mylist[i]} \t {squares[i]}")




