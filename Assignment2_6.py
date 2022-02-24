list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,21,23,24,25,26,
        27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,56,47,48,49,50]

print ("these are the prime numbers between 1 and 50:")

# indexing variable set to zero
i=0
num=list



for num in range(i,len(list)):
    for j in range(i+1,len(list)):
        if num%i == 0:
        #if (list[i]>list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp

print ("The sorted numbers of the list are:",list)

'''
for i in range(i,len(list)):
    i


    f list[i]> 1:

        for i in range(i,num):
            if num%i == 0:

                break
            else:
                print(num)
	
'''
