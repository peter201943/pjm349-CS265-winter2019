#!/usr/bin/env python3
#
#Peter J. Mangelsdorf
#
#for each student:
#    get name
#    get scores
#    average = +/scores
#    return (name, average)
#for each student:
#    print info
#
#Use command line arguments
#


#(0) Imports
import sys

#(1) Globals
students = []
student_data = ""
student_file = None

#(3) Exception Function, bugs user until valid filepath specified.
def try_again():
    done = False
    global student_file
    while (not done):
        file_name = input("Student File Location: ")
        try:
            student_file = open(file_name)
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
        student_file = sys[1].open()
    except:
        print("Invalid File Path")
        try_again()
        
#(4) Get Info On Student
student_data = student_file.readlines()
for line in student_data:
    line_split = line.split(",")
    name = line_split[0]
    average = 0
    for score in line_split[1:]:
        if (score != ""):
            average = average + int(score)
    average = average/len(line_split)
    student = [name, average]
    students.append(student)

#(5) Print Student Info
for student in students:
    print(str(student[0]) + "," + str(student[1]))

