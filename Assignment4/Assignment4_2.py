'''
 Assignment 4_2
 Discrription - Design a program that asks the user to enter a series of
 20 numbers. This program should store the numbers in a list then display
 the following data: lowest number, highest number, total sum, and list average. 
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)

'''

# create list
numList = []

#set total to zero
total = 0

#Set the range of numbers to 20
for i in range(20):
    #user input of 20 numbers append to list and total the sum of list 
    number = int(input("Enter a random number " + str(i + 1) + ": "))
    numList.append(number)
    total += number

#solve output using min and max function
print("\n" 'The lowest number is', min(numList))
print('The highest number is', max(numList))
print('The total is', total)
print('The average is', total / 20)

exit()
