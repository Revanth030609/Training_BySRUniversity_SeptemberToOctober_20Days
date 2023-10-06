# print("Enter the list your want to sort using quick sort:")
# l=list(map(int,input().split()))
# def quickSort(l):
#     def swapper(l,s,e):
#         pi=l[e]
#         i=s-1
#         for j in range(s,e):
#             if(l[j]<pi):
#                 i+=1
#                 l[i],l[j]=l[j],l[i]
#         l[i+1],l[e]=l[e],l[i+1]
#         return i+1
#     def sort(l,s,e):#Worst case occours when dividing of the list is imbalenced either totally left or right skewed!==>O(n²)!
#         if(s<e):#Best case and Average case occours when division of list is exactly at mid and balenced gives O(n*logn)!
#             pi=swapper(l,s,e)
#             sort(l,s,pi-1)
#             sort(l,pi+1,e)
#     return sort(l,0,len(l)-1)
# quickSort(l)
# print("The sorted list is:\n",l)
#-------------------------------------------------------
# def binary_search(array, target):
#   low = 0
#   high = len(array) - 1
#   while low <= high:
#     mid = (low + high) // 2
#     if array[mid] == target:
#       return mid
#     elif array[mid] < target:
#       low = mid + 1
#     else:
#       high = mid - 1
#   return -1
# array = list(map(int,input("Enter a list of integers:").split()))
# target = int(input("Enter a search key:"))

# index = binary_search(array, target)

# if index != -1:
#   print(f"The target element {target} is found at index {index}.")
# else:
#   print(f"The target element {target} is not found in the array.")
#-------------------------------------------------------
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
#-------------------------------------------------------


