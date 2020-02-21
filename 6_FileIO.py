#!/usr/bin/env python
# coding: utf-8



# Open files for reading using this
f = open('ancilliaryFiles/TestFile.txt')
# Make sure you close the file after you are done with it.
f.close()



# Open files for writing using this
f = open('Writing.txt', 'w')
# Make sure you close the file after you are done with it.
f.close()



# The above methods are not nice if there is an exception between file open and file close.
# The file might remain open and there will be resource leak.
# There is a better way which will automatically close the file if something goes wrong.
# This opens the file and stores the file handle in file_handle to be used inside the block
with open('ancilliaryFiles/TestFile.txt') as file_handle:
    # You can get the entire contents of a file as a string like so
    contents = file_handle.read()
    print(contents)



with open('ancilliaryFiles/TestFile.txt') as file_handle:
    # You can get the contents of a file line by line like so.
    # This is useful when you want to read a file larger than your memory
    for line in file_handle:
        print(line.strip())
        # Here strip will remove the end of line character from the line
        # Because print will add its own.



# input.txt contains pixel values in (R, G, B) format
# Let's change the paranthesis to *** so that the output is ***R, G, B***
with open('ancilliaryFiles/input.txt') as file_handle:
    contents = file_handle.read()
    contents = contents.replace('(', '***').replace(')', '*'*3)
    print(contents)



# input.txt contains pixel values in (R, G, B) format
# Let's find the pixel with the maximum red value
with open('ancilliaryFiles/input.txt') as file_handle:
    max_red = -1
    for line in file_handle:
        # There is a lot going on in this list comprehension. Take a moment to understand this.
        pixel_values = [int(p.strip()) for p in line.strip().replace('(', '').replace(')', '').split(',')]
        if pixel_values[0] > max_red:
            max_red = pixel_values[0]
    print("Max red value is {}".format(max_red))



# You can open multiple files like this.
# Let's open input.txt, add 30 to all the values and store the result in output.txt
# Since RGB values go from 0 to 255 anything that goes beyond 255 is clamped to 255.
with open('output.txt', 'w') as out_file, open('ancilliaryFiles/input.txt') as in_file:
    for line in in_file:
        pixel_values = [int(p.strip()) for p in line.strip().replace('(', '').replace(')', '').split(',')]
        pixel_values = [255 if p + 30 > 255 else p + 30 for p in pixel_values]
        out_file.write("({}, {}, {})\n".format(*pixel_values))



# Let's change a file in place. We use the r+ mode for this
with open('ancilliaryFiles/inplace.txt', 'r+') as file_handle:
    contents = file_handle.read()
    print('We will replace all the ??? and *** with something.')
    contents = contents.replace('***', 'Orange').replace('???', 'Blue')
    # Let's go to the beginning of the file
    file_handle.seek(0)
    file_handle.write(contents)



# Use help function to get help on functions.
# It will print the docstring.
help(file_handle.seek)

# ## File open modes
# 
# |Mode |Description |
# |---:|:---|
# |`r` |Open text file for reading.<br>The stream is positioned at the beginning of the file. |
# |`r+` |Open for reading and writing.<br>The stream is positioned at the beginning of the file. |
# |`w` |Truncate file to zero length or create text file for writing.<br>The stream is positioned at the beginning of the file. |
# |`w+` |Open for reading and writing.<br>The file is created if it does not exist, otherwise it is truncated.<br>The stream is positioned at the beginning of the file. |
# |`a` |Open for writing.<br>The file is created if it does not exist.<br>The stream is positioned at the end of the file.<br>Subsequent writes to the file will always end up at<br>the then current end of file, irrespective of any intervening<br>fseek(3) or similar. |
# |`a+` |Open for reading and writing.<br>The file is created if it does not exist.<br>The stream is positioned at the end of the file.<br>Subsequent writes to the file will always end up<br>at the then current end of file, irrespective of any<br>intervening fseek(3) or similar. |
# |`t` | Open text file. To be used with `r`, `w`, or `a`. |
# |`b` |Open binary file. To be used with `r`, `w`, or `a`. |
# |`x` |Open file exclusively. To be used with `r`, `w`, or `a`.|




