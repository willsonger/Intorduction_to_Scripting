'''
 Assignment2_2
 Discription: Execute following steps:
 Take two integer inputs from users (one number is n, other number is r) 
 Programmed in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)
'''                   
# user input for variable N and R
print("Enter the Value of n: ", end="")
N = int(input())
print("Enter the Value of r: ", end="")
R = int(input())

# Find the factorial for N
factNumber = N
loop_counter_1 = 1
result_fact_number_n = 1

while loop_counter_1 <= factNumber:
    result_fact_number_n = result_fact_number_n * loop_counter_1
    loop_counter_1 += 1
#print(result_fact_number_n)


# Find the Factorial for R 

factNumber = R
loop_counter_1 = 1
result_fact_number_r = 1
while loop_counter_1 <= factNumber:
    result_fact_number_r = result_fact_number_r * loop_counter_1
    loop_counter_1 += 1
#print(result_fact_number)


#find the factorial for N-R
factNumber = N-R
loop_counter_1 = 1
result_fact_number_n_r = 1
while loop_counter_1 <= factNumber:
    result_fact_number_n_r = result_fact_number_n_r * loop_counter_1
    loop_counter_1 += 1
#print(result_fact_number)


#calculate the value of Combination(nCr = n!/r!(n-r)!) and Permutation (nPr = n!/(n-r)!)

     
#print(permutation)
if N > R:
    combination = result_fact_number_n/(result_fact_number_r * result_fact_number_n_r)
    print(combination)
    permutation = result_fact_number_n/result_fact_number_n_r
    print(permutation)
else:
    print("invalid")
