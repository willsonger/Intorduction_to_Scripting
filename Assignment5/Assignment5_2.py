'''
 Assignment 5_2
 Discrription - write a program with a funtion that accepts a
string as an argument and returns the number
of vowles that the string contains. The
application should have another funtion
that accepts a string as an argument and returns
the number of consonants that the string contains
The application should let the user enter a string,
and should let the user enter a string, and should
display the number of vowels and the number of
consonants it contains
 Department, Job Title pass it to a list
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)

'''

def vowel(string):
    count = 0
    for s in string:
        s=s.lower()
        if s in ['a', 'e', 'i', 'o', 'u' ]:
            count += 1
            
    return count
    
def consonant(string):
    count = 0
    for s in string:
        s=s.lower()
        if s not in ['a', 'e', 'i', 'o', 'u' ]:
            count += 1
            
    return count
    
    
string = input('Please enter a string: ')
string = string.replace(' ', '')

v = vowel(string)

c = consonant(string)

print(string, ': ' 'num of vowel: ', v, 'num of consonant: ', c)






































