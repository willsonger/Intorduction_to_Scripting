'''
 Assignment 3_1
 Discrription - Car Class Object car accelerates and decelerates
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)

'''
#define class  
class car:
   

# initialize car methode with arguments year, model, speed    
    def __init__(self, year, model, speed):
        self.__year = year
        self.__model = model
        self.__speed = speed


# define year method        
    def setYear(self, year):
        self.__year = year

    def getYear(self):
        return self.__year

# define model method
    def setMake(self, model):
        self.__model = model

    def getModel(self):
        return self.__Model

# define speed method
    def setSpeed(self,inp_speed):
        if self.__speed < 0:
           print("invalid input, speed must be greater then zero")
        else:
           self.__speed = inp_speed

    def getSpeed(self):
        return self.__speed

# define string 
    def __string__(self):
        return "year : " + self.__year + ", Model :" + \
            self.__model + ", speed =" + str(self.__speed)


 

   
