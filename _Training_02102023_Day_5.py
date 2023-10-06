import math as m
# def straight(n):#Printing  1 to n in ascending order
#     if n==0:
#         return
#     straight(n-1)
#     print(n,end = "→")

# def nonstraight(n):# printing 1 to n in descending order
#     if n==0:
#         return
#     print(n,end = "←")
#     nonstraight(n-1)
# n = int(input("Enter a number:"))
# straight(n)
# print()
# nonstraight(n)
#-----------------------------------------
# def check(mat,i,j):#no.of Islands in a binary matrix.
#     if i<0 or j<0 or i>=len(mat) or j>=len(mat) or mat[i][j]==0:
#         return 
#     mat[i][j] = 0
#     check(mat,i,j+1)
#     check(mat,i,j-1)
#     check(mat,i+1,j)
#     check(mat,i-1,j)
# matrix = [[0,0,0,1],[1,1,1,1],[0,1,0,1],[1,0,1,1]]#1=>Land 0=>Water
# islands=0
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if matrix[i][j]==1:
#             islands+=1
#             check(matrix,i,j)
# print("No.of Islands are:",islands)
#-----------------------------------------
# def subset(l,s):
#     if s==0:
#         return True
#     if len(l)==0:
#         return False
#     return subset(l[1:],s-l[0]) or subset(l[1:],s)
# print("Enter a list of integers:")
# l=list(map(int,input().split()))
# lis=sorted(l)
# s=int(input("Enter a target sum to check a subset of it is present in the above list:"))
# if s<l[0]:
#     print(False)
# else:
#     print(subset(l,s))
#-----------------------------------------
# def burntTrees(mat,i,j):
#     if i<0 or j<0 or i>=len(mat) or j>=len(mat) or mat[i][j]==0:
#         return 
#     mat[i][j]=0
#     burntTrees(mat,i,j+1)
#     burntTrees(mat,i,j-1)
#     burntTrees(mat,i+1,j)
#     burntTrees(mat,i-1,j)

# matrix = [[1,0,0,1],[1,0,0,0],[1,0,1,0],[0,1,1,1]]#1=>Tree and 0=>Land
# x,y = map(int,input("Enter the co-ordinates of the burnt tree:").split())
# print("The land Before fire is:")
# for i in matrix:
#     print(*i,sep=" ")
# burntTrees(matrix,x,y)
# print("The land after fire is:")
# for i in matrix:
#     print(*i,sep=" ")
# trees=0
# for i in range(len(matrix)):
#     trees+=matrix[i].count(1)
# print("No.of Burnt trees are:",trees)
#-----------------------------------------
# def judgeSquareSum(c):
#     e=int(m.sqrt(c)+1)
#     for i in range(e):
#         if(m.sqrt(c-i*i)*10==m.ceil(m.sqrt(c-i*i))*10):
#             return True
#     return False
# n=int(input("Enter a number to check if its possible to divide it as x²+y²:"))
# print(judgeSquareSum(n))
#-----------------------------------------
