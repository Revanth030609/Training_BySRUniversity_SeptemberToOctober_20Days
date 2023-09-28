import math as m
# lemon=input("Enter no.of lemons:")
# print("Enter a valid Lemon count!!") if not(lemon.isnumeric()) else print(f"You will have sufficient lemons when you buy {21-lemons} no.of lemons") if (lemon<=21) else print(f"You have {lemon-21} no.of extra lemons!")
#---------------------------------------------
size=int(input("Enter the column size of matrix:"))
# one={"rowC":0,"columnC":0,"diagonalL":0,"diagonalR":0}
# zero={"rowC":0,"columnC":0,"diagonalL":0,"diagonalR":0}
# matrix=list(map(int,input().split(" ")))
# matrix = [list(row) for row in zip(*[iter(matrix)]*size)]
# print(matrix)
# dr=size-1
# dl=0
# s=[0,0,0,0]
# for lis in matrix:
#     if(sum(lis)==size):
#         one["rowC"]+=1
#     elif(sum(lis)==0):
#         zero["rowC"]+=1
#     one["diagonalR"]+=lis[dr]
#     one["diagonalL"]+=lis[dl]
#     zero["diagonalR"]+=lis[dr]
#     zero["diagonalL"]+=lis[dl]
#     dr-=1
#     dl+=1
#     s=[x + y for x, y in zip(s,lis)]
# one["diagonalR"]//=size
# one["diagonalL"]//=size
# zero["diagonalR"]//=size 
# zero["diagonalL"]//=size
# for i in s:
#     if(i==0):
#         zero["columnC"]+=1
#     elif(i==size):
#         one["columnC"]+=1
# print("Zero==>",zero,"\nOne==>",one)
#---------------------------------------------
# Input="Hello, how is your family?!"
# Output=""#output :ylima, fru oy siwo holleH?!
# for i in range(len(Input)):
#     if(Input[i].isalpha()):
#         Output+="X"
#     else:
#         Output+=Input[i]
# j=0
# Input=list(Input)#Since we converted it into list easy to traverse and takes 1.02 sec for conversion (i.e., form str to list to str) which is faster since we are doing it ones!!
# Output=list(Output)
# for i in range(len(Input)-1,-1,-1):
#     while(Output[j]!="X"):
#         j+=1
#     if(Input[i].isalpha()):
#         Output[j]=Input[i]
#         j+=1
# print("".join(Output))
#---------------------------------------------
# Input="Hello, how is your family?!"
# Output=""#output :ylima, fru oy siwo holleH?!
# for i in range(len(Input)):
#     if(Input[i].isalpha()):
#         Output+="X"
#     else:
#         Output+=Input[i]
# j=0
# for i in range(len(Input)-1,-1,-1):
#     while(Output[j]!="X"):
#         j+=1
#     if(Input[i].isalpha()):
#         Output=Output[:j] + Input[i] + Output[j+1:]#Slower method due to this line time for ones it takes 0.3 sec!
#         j+=1
# print(Output)
#---------------------------------------------
# i=int(m.sqrt(40))+1
# while(i*i<=100):#perfect squares btw 40 to 100
#     print(f"{i}==>{i*i}")#O(√n)
#     i+=1

    
    
    
    
    
    
    
    
    
    
