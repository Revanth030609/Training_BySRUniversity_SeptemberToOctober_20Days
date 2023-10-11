# def binary(n,t):#try list=1 3 5 6 and target=5
#     def search(s,e):
#         mid=s+(e-s)//2
#         if(n[mid]<=t and e-s==0):
#             return mid
#         if(n[mid]<t):
#             return search(mid+1,e)
#         elif(n[mid]>t):
#             return search(s,mid-1)
#     return search(0,len(n)-1)

# nums=list(map(int,input().split()))
# target=int(input())
# print(binary(nums,target))
#-----------------------------------------------------
# def bin(n,limit=1e-6):# Limit is tolerance.
#     if n<0:
#         raise ValueError("Cannot compute the square of Negative numbers!")
#     if n<1:
#         left,right=n,1
#     else:
#         left,right=0,n
#     while abs(left-right)>limit:
#         mid=(left+right)/2
#         mid_sqr=mid*mid
#         if mid_sqr<n:
#             left=mid
#         else:
#             right=mid
#     return (left+right)/2
# n=int(input("Enter a number for its square root:"))
# res=bin(n)
# print(f"The square root of {n} is {res}")
#-----------------------------------------------------
# def peakIndexInMountainArray(arr):
#     s=0
#     size=len(arr)-1
#     while(s<size):
#         if(arr[s]>arr[s+1]):
#             return s
#         s+=1
# arr=list(map(int,input("Enter a list of numbers which is a mountain:\n").split()))
# print("The peak of the array mountain is at index:",peakIndexInMountainArray(arr))
#-----------------------------------------------------
# def palindromes(s):
#     res=[]
#     size=len(s)
#     def check(f,l):
#         while(s[f]!=s[l] and f>=0 and l<=size-1):
            
# s=input("Enter a string to check if it has a inner palindrome:")
# size=len(s)
# print(palindromes(s))
#-----------------------------------------------------
# def fun(l,st,en):#852 leetcode
#     while(st<en):
#         mid=(st+en)//2
#         if l[mid]>l[mid+1] and l[mid]>l[mid-1]:
#             en=mid
#             return l[mid]
#         else:
#             st=mid+1
# l=list(map(int,input().split()))
# print(fun(l,0,len(l)-1))
#------------------------------------------------------
# def binary_search_ceil(arr, target):
#   low = 0
#   high = len(arr) - 1
#   while low <= high:
#     mid = (low + high) // 2
#     if arr[mid] == target:
#       return mid
#     elif arr[mid] < target:
#       low = mid + 1
#     else:
#       high = mid - 1
#   return high

# def binary_search_floor(arr, target):
#   low = 0
#   high = len(arr) - 1
#   while low <= high:
#     mid = (low + high) // 2
#     if arr[mid] == target:
#       return mid
#     elif arr[mid] < target:
#       low = mid + 1
#     else:
#       high = mid - 1
#   return low
# arr=list(map(int,input("Enter an sorted array:\n").split()))
# target=int(input("Enter a search number:"))
# print(f"{binary_search_ceil(arr, target)},{binary_search_floor(arr, target)}")
#------------------------------------------------------
# def solve(arr):#Two pointer sum.
#     p1 = 0
#     p2 = len(arr)-1
#     while p1<p2:
#         sum = arr[p1] + arr[p2]
#         if sum == target:
#             return (arr[p1], arr[p2])
#         elif sum < target:
#             p1 += 1
#         else:
#             p2 -= 1
#     return False
    
# arr = [2,3,4,5,6]
# target = 17
# result = solve(arr)
# print(result)
#------------------------------------------------------
