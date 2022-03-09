'''
 Assignment 4_3
 Discrription - Write a python script to generate and print a
 dictionary that contains a number (between 1 and n) in the
 form (x,x^2x).
 Department, Job Title pass it to a list
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)

'''
#user input
n = input("Input a number to set the range of numbers to be square: ")
num = int(n)
#static  
#num = 15

#create dictionary
dic = {}
#for loop to calculate the square of numbers in range
for i in range(num):
    x = i+1
    dic[x] = (x, x*x)
    
print(" \n The square root of the nebers with in the range are : ", dic)
