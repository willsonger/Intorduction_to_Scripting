'''
 Assignment 3_2
 Discrription - create a employee class object with 4 variables name, ID_number,
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
    def __init__(self, name, ID_Number, Department, Job_Title):
        self.name = name
        self.ID_Number = ID_Number
        self.Department = Department
        self.Job_Title = Job_Title
        
        
    print("Employee Name:" , "ID_Number" , "Department" , "Job Title")     
    
    def employee_list(self):
        print(self.name, self.ID_Number, self.Department, self.Job_Title)

         
