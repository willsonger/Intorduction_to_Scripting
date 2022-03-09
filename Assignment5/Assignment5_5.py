'''
 Assignment 5_5
 Discrription - Given a string “this is the string for the class”
 1. Convert the above string to “This Is The String For The Class” using a loop
 2. Convert the above string to “ThisIsTheStringForTheClass” using a loop
 3. Convert the above string to “Thi$ I$ $tring for the Cla$$” using a loop
 4. Convert the above string to “This is the String for the Class” using a loop
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

 Work Cited:
 Author: Tony Gaddis
 Title: Starting Out with Python (5th Edition)

'''
import re

#Convert the above string to “This Is The String For The Class” using a loop
str1 = "this is the string for the class"

print("Original string:\n",str1)
print("=====================================")
print("part 1")


#passing str1 using a for loop for part 1 through part 4
print("\nAfter capitalizing each first letter:")
result = ' '.join(word.capitalize() for word in str1.split())
print(result)

print("\npart 2")
print("=====================================")
#2. Convert the above string to “ThisIsTheStringForTheClass” 

print('After removing all spaces using RegEx:\n', re.sub(r"\s+", "", result), sep='')

print("\npart 3")
print("=====================================")
#3. Convert the above string to “Thi$ I$ $tring for the Cla$$” 

print('After replacing all S with $ \n')
str_new = result.lower().replace('s', '$')
print(str_new)


print("\npart 4")
print("============================https://www.onlinegdb.com/online_python_compiler#tab-stdin=========")
# 4. Convert the above string to “This is the String for the Class” using a loop

