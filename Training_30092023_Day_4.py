import sys
# a=(input("Enter an Alphabet for it's position:")
# if(ord(a)>96):
#     print(ord(a)-96)
# else:
#     print(ord(a)-64)
#------------------------------------------------------
# a=input("Enter an alphabet:")
# pos=int(input("Enter the number for shifting the alphabet:"))
# pos%=26
# if(ord(a)>96 and ord(a)<123):
#     print(chr(((ord(a)-97+pos)%26)+97))
# elif(ord(a)>64 and ord(a)<91):
#     print(chr(((ord(a)-65+pos)%26)+65))
#------------------------------------------------------
# n=int(input("Enter the pattern length:"))
# for i in range(1,n+1):
#     print("* "*i)
#------------------------------------------------------
# n=int(input("Enter the pattern length:"))
# for i in range(n):#The below n and this n are different!!
#     n-=1
#     print("* "*n,end="")
#     print(" "*i)
#------------------------------------------------------
# n=int(input("Enter the pattern length:"))
# for i in range(n-1):
#     print(" "*(n-i)+"* "*(i+1))
# for i in range(n):
#     print(" "*(i+1)+"* "*(n-i))
#------------------------------------------------------
# n=int(input("Enter the pattern length:"))
# for i in range(n):
#     print((str(i+1)+" ")*(i+1))
#------------------------------------------------------
# n=int(input("Enter the pattern length:"))
# #  a=1
# #  for i in range(n):
# #      print((i+1)*a)
# #      a=a+(10**(i+1))
# # # or # #
# for i in range(1,n+1):
#     print(((10**i)//9)*(i))
#------------------------------------------------------
# def fib(n):
#     if(n==1 or n==2):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# n=int(input("Enter the fibonacci series length you want:"))
# for i in range(1,n+1):
#     print(fib(i),end=" ")
#------------------------------------------------------
# class node:
#     def __init__(self,x):
#         self.data=x
#         self.next=None
# class singleLinkedList:
#     def __init__(self):
#         self.head=None
#     def create(self,x):
#         if(self.head==None):
#             self.head=node(x)
#             self.tail=self.head
#         else:
#             temp=self.head
#             while(temp.next!=None):
#                 temp=temp.next
#             temp.next=node(x)
#             self.tail=temp
#     def traverse(self):
#         temp=self.head
#         while(temp!=None):
#             print(temp.data,end="-->")
#             temp=temp.next
#         print(None)
#     def add_at_front(self,x):
#         if(self.head==None):
#             self.head=node(x)
#         else:
#             temp=node(x)
#             temp.next=self.head
#             self.head=temp
#     def mid_element(self):
#         if(self.head==None):
#             print("None")
#         else:
#             temp1=self.head
#             temp2=self.head
#             while(temp2!=None):
#                 temp1=temp1.next
#                 temp2=temp2.next.next
#             print("The mid element is:",temp1.data)
#     def add_at_end(self,x):
#         if(self.head==None):
#             self.head=node(x)
#         else:
#             temp=node(x)
#             self.tail.next=temp
#             self.tail=temp
# print("#### Single Linked List ####")
# a=singleLinkedList()
# while(True):
#     print("------------------------------------------------------")
#     print("0-Exit\n1-Create\n2-Traverse and display\n3-Add at front\n4-Display Mid element\n5-Add at end")
#     choice=int(input("Enter your choice:"))
#     if(choice==0):
#         break
#     elif(choice==1):
#         size=int(input("Enter the no.of elements you want to insert in the linked list:"))
#         print(f"Enter the {size} no.of integers:")
#         l=list(map(int,input().split(" ")))
#         for i in l:
#             a.create(i)
#         print(f"Successfully created {size} node in the single linked list.") 
#     elif(choice==2):
#         print("The existing linked list traversal is:")
#         a.traverse()
#     elif(choice==3):
#         a.add_at_front(int(input("Enter an integer to insert at front of the linked list:")))
#         print("Successfully inserted!")
#     elif(choice==4):
#         a.mid_element()
#     elif(choice==5):
#         a.add_at_end(int(input("Enter an integer to insert at end of the linked list:")))
#         print("Inserted Successfully at the end!")
#     else:
#         print("Invald choice please try again!!")
#------------------------------------------------------

    






