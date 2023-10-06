import math as m
# n=int(input("Enter the magic matrix size:"))#Magic Matrix
# matrix=[[0]*n for i in range(n)]# Here it won't get error since we are repeating 0 a variable not a list
### matrix=[[0]*n]*n #Here list is shared among 3 rows so error occours [0]*n we are repeating this a list.
# def magicMatrix(i,j,counter):
#     if(counter>n*n):
#         return 
#     else:
#         if(i<0 and j==n):
#             i=0
#             j=n-2
#         elif(i<0):
#             i=n-1
#         elif(j==n):
#             j=0
#         elif(matrix[i][j]!=0):
#             i+=1
#             j-=2
#             magicMatrix(i,j,counter)
#     if(matrix[i][j]==0):
#         matrix[i][j]=counter
#         magicMatrix(i-1,j+1,counter+1)
# magicMatrix(n//2,n-1,1)
# # OR # #
# def generate(n):
#     mm=[[0]*n for i in range(n)]
#     def fill(i,j,counter):
#         if counter>(n*n):
#             return mm
#         if i<0 and j==n:
#             i=0
#             j=n-2
#         else:
#             if i<0:
#                 i=n-1
#             if j==n:
#                 j=0
#         if mm[i][j]:
#             i-=1
#             j-=2
#             return fill(i,j,counter)
#         mm[i][j]=counter
#         return fill(i-1,j+1,counter+1)
#     return fill(n//2,n-1,1)
# matrix=generate(n)
# print("The magic matrix is:",*matrix,sep='\n')
#------------------------------------------------------------------
# l=list(map(int,input().split()))
# d={}
# res=[]
# for i in l:
#     if i not in d.keys():
#         d[i]=1
#     else:
#         d[i]+=1
# for i in d:
#     if d[i]>1:
#         res.append(i)
# print("Duplicate elements are:",res)
#------------------------------------------------------------------
# s="Hello2 how1 are3 you4"
# d={'1':"",'2':"",'3':"",'4':"",'5':"",'6':"",'7':"",'8':"",'9':""}
# l=s.split(" ")
# for i in l:
#     d[i[-1]]=i[:-1]
# st=""
# for i in d:
#     if(d[i]!=""):
#         st+=" "+d[i]
# s=s[1:]
# print("-"+s+"-")
#------------------------------------------------------------------
# def solveNQueens(n):
#     state= [["0"] * n for i in range(n)]
#     res=[]
#     visited_cols=set()
#     visited_diagonals=set()
#     visited_antidiagonals=set()
#     def backtrack(r):
#         if r==n:                
#             res.append(["".join(row) for row in state])
#             return
#         for c in range(n):
#             diff=r-c
#             _sum=r+c
#             if not (c in visited_cols or diff in visited_diagonals or _sum in visited_antidiagonals):                    
#                 visited_cols.add(c)
#                 visited_diagonals.add(diff)
#                 visited_antidiagonals.add(_sum)
#                 state[r][c]='Q' 
#                 backtrack(r+1) 
#                 visited_cols.remove(c)
#                 visited_diagonals.remove(diff)
#                 visited_antidiagonals.remove(_sum)
#                 state[r][c]='0'                                
#     backtrack(0)
#     return res
# s=solveNQueens(4)
# for i in s:
#     for j in i:
#         print(" ".join(list(j)))
#     print()
#------------------------------------------------------------------