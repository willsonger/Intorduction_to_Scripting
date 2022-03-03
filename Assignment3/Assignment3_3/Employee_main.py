'''
 Assignment 3_2
 Discrription - create a employee class object with four arguments
 first, last email. concantanate the three strings into an email address
 with lowercase letters seperating the first and last name with a period.
 Department, Job Title pass it to a list
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)

'''


from Employee import Employee

def main():

    e1 = Employee("Susan" , "Meyers" , "@company.com")
    e1.employee_list()

    e2 = Employee("Mark" , "Jones" , "@company.com")
    e2.employee_list()

    e3 = Employee("Joy" , "Rogers" , "@company.com")
    e2.employee_list()


main()
