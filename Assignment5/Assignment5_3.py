'''
 Assignment 5_3
 Discrription - 
 1. Count all letters, digits and symbols in: str1 = "P@#yn26at^&i5ve"
 2. Remove special symbols and punctuation from string: str1 = "/*Jon is
    @developer & musician"
 3. Remove ‘-‘and replace with space in : str1 = Emma-is-a-data-scientist
 4. Write a program to remove all consonants from “Hello, have a good day”
 Department, Job Title pass it to a list
 Programming in Python 
 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

 Work Cited:
 Author: Tony Gaddis
 Title: Starting Out with Python (5th Edition)

'''
str1 = "P@#yn26at^&i5ve"

lowcase=0
upcase=0
numb=0
specialC=0

for character in str1:
    if character.islower():
        lowcase=lowcase+1
    elif character.isupper():
        upcase=upcase+1
    elif character.isdigit():
        numb=numb+1
    else:
        specialC=specialC+1
        
    total = lowcase + upcase + numb + specialC    
print("Question 1 \n")        
print("number of lower case: ", lowcase)
print("number of upper case: ", upcase)
print("number of digits: ", numb)
print("number of special characters: ", specialC) 
print("Total number of characters in the string is: ", total)
print("=================================================================")
print("Question 2 \n") 


str1 = "/*Jon is@developer & musician"

for c in ['/', '*','@','&' ]:
    str1 = str1.replace(c,'')
    print(str1)
print("=================================================================")
print("Question 3 \n") 

str1 = "Emma-is-a-data-scientist"

str1= str1.replace('-', ' ')
print(str1)

print("=================================================================")
print("Question 4 \n") 

str1 = "Hello, have a good day"
new_str = ""                          
for c in str1:
    #c = c.lower()
    if c not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        new_str = new_str + c

print(new_str)



 
