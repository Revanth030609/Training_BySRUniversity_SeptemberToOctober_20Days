import sys
import turtle
# def fun2(a,b):
#     if b==0:
#         return 1
#     else:
#         return fun(a,fun2(a,b-1))
# def fun(x,y):
#     if y==0:
#         return 0
#     return x+fun(x,y-1)
# print(fun2(2,3))#2³==>8
#-----------------------------------------
# s=input("Enter a string for checking if it a palindrome:")
# last=len(s)-1   #O(n/2)
# for first in range(0,(last//2)):
#     if(s[first]!=s[last]):    #Analyse!
#         print("Not a palindrome!")
#         sys.exit(0)
#     #print(first,last)
#     last-=1
# #print(first,last)   
# print("It is a palindrome!")
# # OR # #
# s=input("Enter a string for checking if it a palindrome:")
# i=0
# j=len(s)-1
# while(i<j):#Works for both odd and even strings!
#     if(s[i]!=s[j]):
#         print("Not a palindrome!")
#         break
#     i+=1
#     j-=1
# else: #if it's not breaking out of the above loop this else is executed!!
#     print("A palindrome!")
# # Using Recursion # #
# s=input("Enter a string for checking if it a palindrome:")
# def palindrome(s,first,last):
#     if(s[first]!=s[last]):
#         return 0
#     if(first>=last):
#         return 1
#     return palindrome(s,first+1,last-1)
# if(palindrome(s,0,len(s)-1)):
#     print("Is a Palindrome")
# else:
#     print("Is not a palindrome")
#-----------------------------------------
# size=int(input("Enter the binary square matrix size:"))
# l=[]
# for i in range(size):
#     l.append(list(map(int,input().split()))
# def check(l,i,j,n):
#     if(l[i][j]==0):
#         return 
#     if (l[i][j]==1):
#         l[i][j]=0
#     if i<n-1:
#         check(l,i+1,j,n)
#     if i>0:
#         check(l,i-1,j,n)
#     if j<n-1:
#         check(l,i,j+1,n)
#     if j>0:
#         check(l,i,j-1,n)
# count=0
# for i in range(size):
#     for j in range(size):
#         if(l[i][j]==1):
#             count+=1
#             check(l,i,j,size)
# print("Total no.of Islands:",count)
#-----------------------------------------
# t=turtle.Turtle()
# t.circle(100)
#-----------------------------------------







