'''
 Assignment2_5
 Discrription - Find all the prime numbers between [2 50] and print them. Use loops
 Programmed using Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

'''

list = [ i for i in range(2,50)]

primeNumberList =[2,3]
# indexing variable set to zero
for num in range(3,len(list)):
    flag_check = False
    for temp in range(0,num):
        if list[num]%list[temp] == 0 :
            flag_check = True
    if flag_check == False:
        primeNumberList.append(list[num])

print ("these are the prime numbers between 1 and 50:", primeNumberList)
