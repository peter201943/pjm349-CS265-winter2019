#!/usr/bin/env python3
#
#Peter J. Mangelsdorf
#
#split on space
#store in entry
#sort numerically
#
#Use command line arguments
#


#(0) Imports
import sys

#(1) Globals
ids = {}
id_data = ""
id_file = None

#(3) Exception Function, bugs user until valid filepath specified.
def try_again():
    done = False
    global id_file
    while (not done):
        file_name = input("ID File Location: ")
        try:
            id_file = open(file_name)
            done = True
        except:
            print("Invalid File Path")
            done = False

#(2) Get File Location from User. Behaves interactively.
if (len(sys.argv) == 0):
    print("No File Specified")
    try_again()
else:
    try:
        id_file = sys[1].open()
    except:
        print("Invalid File Path")
        try_again()
        
#(4) Get Info On People's ID
id_data = id_file.readlines()
for line in id_data:
    line_split = line.split(" ")
    name = str(line_split[1:])
    my_id = line_split[0]
    ids[my_id] = name

#(5) Sort ID Info and Print
for id_key, name_value in sorted(ids.items()):
    print("{} {}".format(id_key, name_value))






