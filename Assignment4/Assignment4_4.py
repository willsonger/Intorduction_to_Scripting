'''
 Assignment 4_4
 Discrription - Question 4:
1. Generate a random list of size 100 using for loop. The range is [0 to 20]
2. Write a function to find the second largest numbers in the list without sorting the list
3. Remove repeating elements in the list Department, Job Title pass it to a list
 
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)


'''
import random

randlist = []

for i in range(0,100):
    x = random.randint(1,20)
    randlist.append(x)

print("\nThis is a random set of 100 numbers within the range of 1 and 20\n", randlist)

new_list = []
for n in set(randlist):
    new_list.append(n)
print("\nThis is the list of random numbers with all the duplicates removed\n" , new_list)
