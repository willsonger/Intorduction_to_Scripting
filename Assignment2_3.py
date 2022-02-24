'''
 Assignment2_3
 Discrription - Given a list, sort them
 using loop and print the new list.
 List = [20, 68, 41, 88, 16,
 40, 65, 97, 85]
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)

'''

# predefined list
list = [20, 68, 41, 88, 16, 40, 65, 97, 85]



print ("The unsorted numbers of the list are:",list)

# indexing veriable set to zero
i=0 

# outer loop to determine the length of list
#inner loop compares value placement of the number
for i in range(i,len(list)):
    for j in range(i+1,len(list)):	
        if (list[i]>list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp

print ("The sorted numbers of the list are:",list)	
