#!/usr/bin/env python
# coding: utf-8

# ## OS module



import os



# You can get the current working directory (cwd)
os.getcwd()

# You can change the cwd to another directory
# use r before strings when it contains path
# it stands for raw-string
path_to_change_to = r"D:\workdir"
print(f"Before chdir: cwd = {os.getcwd()}")
os.chdir(path_to_change_to)
print(f"After chdir: cwd = {os.getcwd()}")

# You can change the permissions of a file
help(os.chmod)



# you can launch things similar to cmd like so
return_value = os.system('calc.exe')
print(f'Command exited with code {return_value}')

# You can get a dictionary of environment variables
env_dict = os.environ

# To delete a file use
os.unlink(r'C:\Users\u5ffoo\PycharmProjects\PythonTraining\input.txt')



# To get the statistics of a file like size, date created, date modified etc.
os.stat(r"D:\path\to\your\file.ext")

# ## SYS Module



import sys



# Get input arguments to a script as a list
# first argument is always the script name
print(sys.argv)



# Get system information
print(sys.getdefaultencoding())
print(sys.executable)
print(sys.maxsize) # max size of an integer on this machine
print(sys.copyright)

# ## Pathlib Module



from pathlib import Path



# Initialize a path object to point to your file
p = Path(r"C:\path\to\your\file.ext")
# Or simply use a blank argument for current working directory
p = Path()



# To get the absolute path of the file or folder
p.resolve()



# To check if the path object points to a file or directory
p.is_file()
p.is_dir()



# In order to get a list of all files of a certain type in this folder
# "**/" will enable recursive search
list_of_files = p.glob('**/*.txt')



# To get the parts of the path
p.parts
# To get the file extension
p.suffix
# To get the file name
p.stem
# To get multiple extensions like tar.gz as a list
p.suffixes

# ## Subprocess Module

# In[1]:


import subprocess
# synchronous call using run

# you can call a dummy process which writes to both streams.
# it is available in stdout and stderr
myproc = subprocess.run('py demo_file.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(myproc.stdout, myproc.stderr, myproc.returncode)

# asynchronous call using Popen
myprocess = subprocess.Popen(r'ping localhost -n 2',
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
                          
# iterate over readline until it returns an empty byte string
for line in iter(myprocess.stdout.readline, b''):
        decodedLine = line.decode("utf-8")
        print(f"*** {decodedLine.strip()}")

# get the exit code
returncode = myprocess.wait()
print(f'The process finished with exit code {returncode}')




