#!/usr/bin/env python
# coding: utf-8

# ## CSV Module



import csv
from pathlib import Path

# Read CSV and process it
myfile = Path(input('Enter your CSV: '))
if not myfile.is_file:
    print('Something wrong with this file: {}'.format(myfile))
else:
    with open(myfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                full_name = row[0]
                try:
                      first_name = full_name.split(', ')[1].split(' (')[0]
                except IndexError as ie:
                      print(f'Probably incorrect value {full_name}')
                else:
                    print(f'\tUser {first_name} is assigned the VM {row[1]}')
                    print(f'\tUser {full_name} is assigned the VM {row[1]}')
                    line_count += 1
        print(f'Processed {line_count} lines.')

# ## JSON Module



import json
with open(r'ancilliaryFiles/input.json') as input_file:
    result = json.loads(input_file.read())
    
# You can dump dictionaries as jsons
my_dict = {str(x): x**3 for x in range(10)}
json.dumps(my_dict)

# A function to check whether a key is present in a json string
def find_key(elm, key):
    if key in elm.keys():
        return True
    else:
        return False

def iterate_elements(root, search_string):
    for value in root.values():
        if isinstance(value, dict):
            iterate_elements(value, search_string)
        else:
            if value == search_string:
                print('Found')
                return True

iterate_elements(result, "markup")

# You can write json to a file
with open("json_output.txt", 'w') as f_out:
    f_out.write(json.dumps(result, indent=4))

# ## XML Module



from xml.etree import ElementTree as et

# Read XML file and print it
root = et.parse(r'ancilliaryFiles/input.xml').getroot()

for child in root:
    print(child.tag, child.text, child.attrib)

# ## UI Module



# default GUI development module
import tkinter
tkinter._test()




