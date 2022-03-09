'''
 Assignment 5_5
 Discrription - 1. Create a class “student” which holds firstname(string), lastname(string), email(string),
 all_course(list of numbers)
 2. Use regular expression to extract firstname (without spaces), lastname (without spaces),
 email (without spaces), and all_courses from the file provided (students.txt).
 3. Create an object for each student and save the data.
 4. From previous assignment, take the list of 25 students and append to the file.
 5. After appending sort all the students (25 students from previous assignment + 10 students
 from students.txt file) on first name and save it a new file.
 Please be careful with title line from students.txt. The title line or first line should be ignored. For
 sorting you can use in build method such as .sort().
 
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

 Work Cited:
 Author: Tony Gaddis
 Title: Starting Out with Python (5th Edition)

'''
import re
# create student class with assigned values, 
class Student:
    def __init__(self, fName, lName, email, course):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.course = course
        
    def write_data(self):
        return '{} {} {} {},{},{},{},{},{}\n'.format(
            self.fName, self.lName, self.email, *self.course) 
        # the * of self.course means extracting the list into 6 values

# open student.txt file and read data set
with open('student.txt', 'r') as file:
    contents = file.readlines()
    
pattern = re.compile(r'(\w+) (\w+) (\S+) (\d+),(\d+),(\d+),(\d+),(\d+),(\d+)')
# pattern: word word string digits digits digits digits digits digits
students = []

# define pattern placement for object values
for row in contents[1:]:
    segments = pattern.match(row)
    f_name = segments.group(1)
    l_name = segments.group(2)
    email = segments.group(3)
    c1 = segments.group(4)
    c2 = segments.group(5)
    c3 = segments.group(6)
    c4 = segments.group(7)
    c5 = segments.group(8)
    c6 = segments.group(9)
    course = [c1, c2, c3, c4, c5, c6]
    s = Student(f_name, l_name, email, course)
    students.append(s)

with open('oldStudentFile.txt', 'r') as file:
    contents = file.readlines()

for row in contents[1:]:
    segments = pattern.match(row)
    f_name = segments.group(1)
    l_name = segments.group(2)
    email = segments.group(3)
    c1 = segments.group(4)
    c2 = segments.group(5)
    c3 = segments.group(6)
    c4 = segments.group(7)
    c5 = segments.group(8)
    c6 = segments.group(9)
    course = [c1, c2, c3, c4, c5, c6]
    s = Student(f_name, l_name, email, course)
    students.append(s)

# Sorted students list to be rewritting in new_students file
sorted_students = sorted(students, key = lambda x:x.fName)
with open("new_students.txt", "w") as file:
    for s in sorted_students:
        file.write(s.write_data())
