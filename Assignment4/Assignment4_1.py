'''
 Assignment 4_1
 Discrription - This exercise assumes you have
 created the Employee class for Prograaming Exercise 4.
 Create a program that stores Employee objects in a directory.
 Use the employee ID number as the key, The program should
 present a menu thatlets the user perform the following actions:
 *Look up an employee in the dirctory
 *Add a new employee to the directory
 *Change an existing employee's name, department,
 and job title in the directory.
 * Delete an employee from the dictionary
 *quite the program.
 When the program ends, it should pickle the dictionary and save
 it to a file. Each time the program starts, it should try to load
 the pickled directory from the file. If the file does not exist,
 the program should start with an emply dictionary. 
 
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)

'''

import pickle
import os

employee_file = 'employee.pkl'

#define class
class Employee:
# define constructor
    def __init__(self):
        if(os.path.isfile(employee_file)):
            # read the file if it exists
            self.info = pickle.load(open(employee_file, "rb"))
        else:
            #create a file if the file doesn't exist
            self.info = []
            pickle.dump( self.info, open(employee_file, 'wb'))

    def look_up(self, emp_ID):
        for person in self.info:
            for key, value in person.items():
                if key == 'emp_ID' and value == emp_ID:
                    print(person)
                 
                
    #define employee dictonary where ID is the KEY
    def add(self, emp_ID, emp_name, depart, title):
        employee_dic = {
            'emp_ID': emp_ID,
            'emp_name': emp_name,
            'depart': depart,
            'title': title,
            }
        #needs for loop to determin that the key isnt alread in use
        self.info.append(employee_dic)
        pickle.dump( self.info, open(employee_file, "wb"))  

    def chglist(self, emp_ID, emp_name, dept, title):
        employee_dic = {
            'emp_ID': emp_ID,
            'emp_name': emp_name,
            'depart': depart,
            'title': title,
            }
        
        for index, e in enumerate(self.info):
            if e['emp_ID'] == emp_ID:
                self.info.pop(index)
        
        self.info.append(employee_dic)
        pickle.dump( self.info, open(employee_file, "wb")) 
        
    def delist(self, emp_ID):

        for index, e in enumerate(self.info):
            if e['emp_ID'] == emp_ID:
                self.info.pop(index)
                    
                #del employee_dict["emp_ID" , "emp_name" , "depart" , "title"]
        print(self.info)
        pickle.dump(self.info, open(employee_file, "wb"))
       
        
emp = Employee()

msg = '''
===============================================
Enter 1 if you want to look up employee by ID.
Enter 2 if you want to add an employee.
Enter 3 if you want to change an employee.
Enter 4 if you want to delete an employee. 
Enter 5 to quite.
================================================
'''
#print(msg)

while(True):
    print(msg)
    option = input("enter your choice:")
    if option == '5':
        print("program ended")
        break

    emp_ID = input("Enter the employee ID: ")

    if option == '1':
        emp.look_up(emp_ID)
    elif option == '2':
        emp_name = input("Add new employee name: ")
        depart = input("Enter the department: ")
        title = input("Enter the employee title: ")
        emp.add(emp_ID, emp_name, depart, title)
    elif option == '3':
        emp_name = input("Change the employee name: ")
        depart = input("Change the department: ")
        title = input(" Change the employee title: ")
        emp.chglist(emp_ID, emp_name, depart, title)
    elif option == '4':
        emp.delist(emp_ID)
        print("the employee has been removed from the dictionary")
    
         
