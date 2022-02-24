'''
 Assignment2_4
 Discription: Write a program that calculates
 the sum of a list and the sum of odd and
 even numbers within the list using a loop. 
 Programmed in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)
'''

# predefined list
list = [20, 68, 41, 88, 16, 40, 65, 97, 85]
#total variable set to zero
total=0

# i index for loop, simple addition of elements 
for i in range(0,len(list)):
    total=total+list[i]

print ("The sum of all the numbers in the list is: ",total)

#variables
even_lst= []
odd_lst=[]
sum_even = 0
sum_odd = 0

# in index for list
# if i is divisable by 2 append to even list
# else append to the odd list
for i in list:
    if  i%2 == 0:
        even_lst.append(i)
        sum_even = sum_even + i
    else:
        odd_lst.append(i)
        sum_odd = sum_odd + i
print ("the sum of all the even numbers in the list is: ",sum_even) 
print ("the sum of all the odd numbers in the list is:  ",sum_odd)
#print(sum_even)

