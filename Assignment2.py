#!/usr/bin/env python
# coding: utf-8

# Given a path from `sys.argv`, find out recursively the size of all files using `Path.glob` and `os.stat`. Print out the single largest file along with its size on the console.
# 
# Bonus: Launch the explorer window to show that file to user.  
# Hint - Use `os.system(f'explorer /select,{largest_file_name}')`

# In[1]:


from pathlib import Path
import sys
import os
import pprint

# In[3]:


# We will use input for jupyter but you can use sys.argv[1] when writing a py file
# p = Path(sys.argv[1])
input_path = input("Type in a path: ")

p = Path(input_path)

file_list = list(p.parent.glob("*.*"))

file_size_dict = {x:os.stat(x).st_size for x in file_list if Path.is_file(x)}

# In[4]:


largest_file_size = -1
for file_name, file_size in file_size_dict.items():
    if file_size > largest_file_size:
        largest_file_size = file_size
        largest_file_name = file_name

# In[5]:


print(largest_file_name, largest_file_size, 'bytes')

# In[6]:


os.system(f'explorer /select,{largest_file_name.resolve()}')




