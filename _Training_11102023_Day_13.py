import numpy as np
# digi=input()#17. Letter Combinations of a Phone Number
# def combination(digi):
#     d={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
#     res=[]
#     def doing(i,curr):
#         if(len(digi)==len(curr)):
#             res.append(curr)
#         for c in d[digi[i]]:
#             doing(i+1,curr+c)
#     doing(0,"")
#     return res
# if(digi):
#     print(combination(digi))
#------------------------------------------------------
# M = 9
# def puzzle(a):
#     for i in range(M):
#         for j in range(M):
#             print(a[i][j],end = " ")
#         print()
# def solve(grid, row, col, num):
#     for x in range(9):
#         if grid[row][x] == num:
#             return False
             
#     for x in range(9):
#         if grid[x][col] == num:
#             return False
#     startRow = row - row % 3
#     startCol = col - col % 3
#     for i in range(3):
#         for j in range(3):
#             if grid[i + startRow][j + startCol] == num:
#                 return False
#     return True
 
# def Suduko(grid, row, col):
 
#     if (row == M - 1 and col == M):
#         return True
#     if col == M:
#         row += 1
#         col = 0
#     if grid[row][col] > 0:
#         return Suduko(grid, row, col + 1)
#     for num in range(1, M + 1, 1): 
     
#         if solve(grid, row, col, num):
         
#             grid[row][col] = num
#             if Suduko(grid, row, col + 1):
#                 return True
#         grid[row][col] = 0
#     return False
# grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
#         [0, 1, 0, 0, 0, 4, 0, 0, 0],
#         [4, 0, 7, 0, 0, 0, 2, 0, 8],
#         [0, 0, 5, 2, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 9, 8, 1, 0, 0],
#         [0, 4, 0, 0, 0, 3, 0, 0, 0],
#         [0, 0, 0, 3, 6, 0, 0, 7, 2],
#         [0, 7, 0, 0, 0, 0, 0, 0, 3],
#         [9, 0, 3, 0, 0, 0, 6, 0, 4]]
# if (Suduko(grid, 0, 0)):
#     puzzle(grid)
# else:
#     print("Solution does not exist :(")
#------------------------------------------------------
# def can_i_place_My_Cows(arr, min_dist, cows):
#     last = arr[0]
#     count = 1
#     for i in range(1, len(arr)):
#         if abs(last - arr[i]) >= min_dist:
#             count += 1
#             last = arr[i]
#     if count >= cows:
#         return True
#     else:
#         return False
# def solve(arr, cows):
#     limit = max(arr)-min(arr)
#     for i in range(1, limit+1):
#         if can_i_place_My_Cows(arr, i, cows) == True:
#             continue
#         else:
#             return i-1
# arr = list(map(int,input("Enter the cattles distances from a start point:\n").split()))
# cows = int(input("Enter the no.of cows:"))
# result = solve(arr, cows)
# print("The minimum distance between two cows is:",result)
#------------------------------------------------------


