'''
 Assignment2_1
 Discrription - Astric patterns of a right and left sided triangle  
 this program uses two funtions different funtions to droaw two seperate triangles. 
 Programmed using Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

'''
# defining function1
def pattern1(n):
   
     
    # outer loop handles number of rows
    # n in this case n = 5
    for i in range(0, n):
     
        # inner loop handles number of columns
        # adds the correct spaces in each row
        for j in range(0, i+1):
         
            # prints out the astrics 
            print("* ",end="")
      
        # ends line after each row
        print("")
 
# number of rows (n = 5)
# funtion call
n = 5
pattern1(n)

# defining function2
def pattern2(n):
     
    # number of spaces in rows
    k = 2*n - 2
 
    # outer loop handles number of rows
    for i in range(0, n):
     
        # inner loop handles number of spaces in each row
        # adds the correct spaces in each row
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k or numbers of spaces after each loop
        k = k - 2
     
        # inner loop handles number of columns
        # adds the correct spaces in each row
        for j in range(0, i+1):
         
            # prints out astrics
            print("* ", end="")
     
        # ends line after each row
        print("")
 
# function2 call
pattern2(n)
