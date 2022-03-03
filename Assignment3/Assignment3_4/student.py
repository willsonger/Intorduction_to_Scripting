
'''
 Assignment 3_4
 There are 25 students in class, each taking 6 courses. Maximum points of
 each course is 100.
 1. Create a class for each student which hold name and his/her marks for 6 courses.
 2. For each student, find the total sum of all his course and divide it by 600. This is
 how you find percentage of each student.
 3. Sort the students in order of percentage
 4. Find the average of each course
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

 Work Cited:
 Author: Tony Gaddis
 Title: Starting Out with Python (5th Edition)

'''

import random
#insertion sort fuction for gpa and student
    #from lowest to highest 
def insertionSort(arr1, arr2):
    for i in range(1, len(arr1)):
        key1 = arr1[i]
        key2 = arr2[i]
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
        j = i-1
        while j >=0 and key1 < arr1[j] :
            arr1[j+1] = arr1[j]
            arr2[j+1] = arr2[j]
            j -= 1
        arr1[j+1] = key1
        arr2[j+1] = key2

    
    

#create student classmethod
class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
        
    #create % calculater class method    
    def calc_percent(self):
        total_sum = 0
        print(self.name,"course scores")
        for score in self.courses:
            print(score)
            total_sum += score
            
        print(self.name,"course totals: ",total_sum)
        percent = total_sum/600*100
        return round(percent, 2)

    
student_list = ['Monique Mcintyre', 'Sergio Russo', 'April Lozano', 'Jazmyn Phillips', 'Hailee Dean', 
                 'Zavier Stephens', 'Kyla Graham', 'Samson Mcclain', 'Isaias Burch', 'Lilia Stanton', 
                 'Owen Donovan', 'Dale Small', 'Shyla Gillespie', 'Carina Simon', 'Arnav Cohen', 
                 'Londyn Rios', 'Kiley Silva', 'Karli Lawson', 'Patrick Hendricks', 'Lane Potts',
                 'Cael Jackson', 'Matthias Brennan', 'Hillary Mirandstudenta', 'Dexter Patrick', 'Ayden Spence']


#randomly assign course scores to students 
percent_list = []
for n in student_list:
    score_list = []
    for i in range(6):
        score = random.randrange(60, 100)
        score_list.append(score)
    s = Student(n, score_list)
    percentage = s.calc_percent()
    percent_list.append(percentage)



#insertionSort funtion call
insertionSort(percent_list, student_list)

print()
print("Student name sorted by GPA lowest to highest")
index = 0
for name in student_list:
    print(student_list[index] ,"GPA: ",  percent_list[index])
    index += 1
