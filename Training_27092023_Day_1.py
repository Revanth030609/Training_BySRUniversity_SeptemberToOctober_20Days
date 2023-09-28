import math as m
# class Parent:#Hierarchical
#     def one(one):
#         print("Demo one")
#     def two(two):
#         print("Demo two")
# class Child1(Parent):
#     def one(one):
#         print("Child1 one")
#         super()#How to call one() in Parent??
# class Child2(Parent):
#     def one(one):
#         print("Child2 one")
# obj=Child1()
# obj.two()
# obj.one()
#----------------------------------------------
# class Parent:
#     def __init__(itself):#Constructor of Parent!
#         print("init default constructor of Parent")
#     def __init__(itself,var_1=None):#both init act as muliti behaverial class type.
#         print("init parameterized constructor of Parent",var_1)
#     def __constructor__(init):#Not a constructor but method of Parent class!!
#         print("Constructor of Parent")
#     def one(one):
#         print("Demo one")
#     def two(two):
#         print("Demo two")
# obj=Parent()
# obj.one()
# obj.two()
# obj.__constructor__()
# obj1=Parent(101)
# obj1.one()
#----------------------------------------------
# def isprime(n):#Magical prime numbers like 17 (17==71)
#     if n==2 or n==3:
#         return 1
#     if n%2==0 or n%3==0:
#         return 0
#     for i in range(5,int(m.sqrt(n)),6):
#         if(n%i==0):
#             return 0
#     return 1
# def magicalPrime(s,e):
#     for i in range(s,e+1):
#         rev=str(i)
#         rev=rev[::-1]
#         rev=int(rev)
#         #print(i,rev)
#         if(isprime(i)==1 and isprime(rev)==1):
#             print(i,end=" ")
# start=int(input("Enter start of range:"))
# end=int(input("Enter end of range:"))
# magicalPrime(start,end)
#----------------------------------------------
#neon numbers
#9²=81=>8+1=9==>Neon number
#There are only three numbers 0,1,9 that are neon numbers no other numbers are known as neon other than these three numbers!!
# def is_neon_number(n):
#   square = n * n
#   sum_of_digits = 0
#   while square > 0:
#     sum_of_digits += square % 10
#     square //= 10
#   return sum_of_digits == n
  
# n=int(input("Enter a to check if the given number is neon number or not:"))
# print(is_neon_number(n))

#----------------------------------------------
# H/W
# union Space complexity ==>The space complexity of union a user defined data structure is the maximum size of a member shared by all members!
# real time Examples of oops concepts
# neon numbers ==>https://www.quickstart.com/app-development/10-applications-of-object-oriented-programming/
#----------------------------------------------





