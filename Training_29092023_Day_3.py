import math as m
# a=int(input("Enter a number to check if it is even or odd:"))
# if(a&1==0):#Even or odd using bitwise operator!
#     print(f"{a} is even.")
# else:
#     print(f"{a} is odd.")
#----------------------------------------------
# a=int(input("Enter a number to check how many bits are set bits:"))
# t=a
# c=0
# while(t):
#     c+=1
#     t=t&(t-1)
# print(f"In {a} there are {c} set bits in it's binary format.")
#----------------------------------------------
# smallest number greater than n(count) with exactly 1 bit difference in the binary form!
# a=a=int(input("Enter a number:"))
# print(a|a+1)
#----------------------------------------------
#check if the ith bit is 1 or not!
# a=int(input("Enter a number:"))
# pos=int(input("Enter the ith bit you want to check if it's set (ie., on or 1) bit or not:"))
# if(a&(1<<(pos-1))):
#     print(f"Yes the bit number {pos} is set in {a}.")
# else:
#     print(f"NO the bit number {pos} is not set in {a}.")
#----------------------------------------------
# check if the number is in the power of 2 or not
# a=int(input("Enter a number to check if it's a powers of 2 or not:"))
# res=m.log2(a)
# if(2**res == 2**int(m.log2(a))):
#     print(f"The number {a} is a power of 2")
# else:
#     print(f"The number {a} is not a power of 2")
# # OR # #
# c=0
# while(a):
#     c+=1
#     n=n&(n-1)# For powers of 4 use==>"n=n&(n-3)"
# if(c==1):
#     print("True")
# else:
#     print("False")
#----------------------------------------------
# a=[1,2,3,4,6,7]#missing number in the list
# x=0
# for i in range(len(a)+2):
#     x^=i
# for i in range(len(a)):
#     x^=a[i]
# print("Missing number is ",x)
#----------------------------------------------
# def factorial(n):#Factorial using recursion 
#     if(n==1 or n==0):
#         return n
#     else:
#         return n*factorial(n-1)
# a=int(input("Enter a number for its factorial:"))
# print(f"The factorial of {a} is {factorial(a)}")
#----------------------------------------------
# def fibonacci(f1,f2,n):#Fibonacci series using recursion
#     if(n==0):
#         return
#     else:
#         print(f1,end=" ")
#         n-=1
#         fibonacci(f2,f1+f2,n)
# n=int(input("Enter the fibonacci series length:"))
# fibonacci(0,1,n)
#----------------------------------------------
#print(m.ceil(2.1) , m.floor(2.1))
#----------------------------------------------
#def TowerOfHanoi(n , source, destination, auxiliary):
#    if n==1:
#        print ("Move disk 1 from source",source,"to destination",destination)
#        return
#    TowerOfHanoi(n-1, source, auxiliary, destination)
#    print ("Move disk",n,"from source",source,"to destination",destination)
#    TowerOfHanoi(n-1, auxiliary, destination, source)
#n = 4
#TowerOfHanoi(n,'A','B','C')




