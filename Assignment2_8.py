'''
 Assignment2_8
 Description - Create a function to find Fibonacci
 number. Take a integer input from user and
 print Fibonacci number for the corresponding index
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

 Work Cited:
 Author: Tony Gaddis
 Title: Starting Out with Python (5th Edition)

 https://en.wikipedia.org/wiki/Fibonacci_search_technique

'''
# create funtion 
def fib_Num(n):

# set initial values in variables a to 0 b to 1
    a = 0
    b = 1
    
# print a value if term is equal to one.     
    if n <= 1:
        print(a)
# while in loop if num is less than or equal to
# one add it to the next sequential number
    else:
        print(b)

        for i in range(2,n):
            c = a+b
            a = b
            b = c
# print while in loop            
            print(c)
m = int(input("enter a number :"))
#print ("The sorted numbers of the list are:",list)
fib_Num(m)

