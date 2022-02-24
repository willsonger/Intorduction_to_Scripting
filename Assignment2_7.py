'''
 Assignment2_7
 Description - Write a program which takes an integer input from number.
 Check if the number is Armstrong number. Display the result.
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

 Work Cited:
 Author: Tony Gaddis
 Title: Starting Out with Python (5th Edition)   
 and
 Narcissistic number                 
 https://en.wikipedia.org/wiki/Narcissistic_number
'''
# user prompt for imput
number = int(input("Enter a positive number to check if it an armstrong number: "))

# function to check user input
def check_input(num):

    # use length funtion from string to determine the number of digits.
    digit = len(str(num))
    sum = 0
    
    startNum = num
    # calculate each digit in the number while digit is greater than zero.    
    while num>0:
        temp = num%10
        sum += (temp ** digit)
        num = num // 10


    if sum == startNum:
        return True
    else:
        return False

#function call
if check_input(number):

#display results
    print(number,'is armstrong')
else:
    print(number,'is not armstrong')
    

    

