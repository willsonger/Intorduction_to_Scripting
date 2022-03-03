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

from car import car

#this is the main fuction

def main():
    my_car = car(2022, "Corvette", 0)
    #print("my_car after instantiating:\n", my_car)

    # Display my car before acceleration.
    print('This is my car at ideal:', my_car.getSpeed())

    # Acceleration 5 times
    print('my car is accelerating')

    for count in range(5):
        target_speed = 20 * count
        my_car.setSpeed(target_speed)
        print("current speed: ", my_car.getSpeed())

    # deceleration 5 times
    times = 5
    current_speed = my_car.getSpeed()
    each_deceleration = current_speed / times
    print ("car is braking: ")
    for i in range(times):
        current_speed = current_speed - each_deceleration
        my_car.setSpeed(current_speed)
        print ("Current speed: ", my_car.getSpeed())
        
main()
