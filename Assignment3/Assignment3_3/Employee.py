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



class Employee:
# define constructor
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
        
        
        
    def employee_list(self):
        print(self.first.lower()+"."+self.last.lower()+self.email)
