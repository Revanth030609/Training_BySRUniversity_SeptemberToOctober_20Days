# import sys
# l=list(map(int,input("Enter a list of whole numbers form 0-9 only:\n").split()))
# count=[0 for i in range(10)]
# for i in l:
#     if(i not in {0,1,2,3,4,5,6,7,8,9}):
#         print("Error:You entered an invalid number in the list for count sort.(i.e., you entered a number(s) which are not 0 to 9)!!")
#         sys.exit(0)
#     count[i]+=1
# for i in range(1,10):
#     count[i]+=count[i-1]
#-----------------------------------------------
# def fun(a):
#     return a*a
# l=[1,2,3,4]
# l=list(map(fun,l))#map takes each elt and send to fun and finally create a map obj which we converted into a list obj/variable.
#-----------------------------------------------
# l=[[1,2,3],[4,5,6],[7,8,9]]
# lis=list(map(lambda a:sum(a),l))#list(map(lambda a:sorted(a),l)) # you can't use a.sort() here since it wont return anything.
# print(lis)
#-----------------------------------------------
# l=[1,2,3,4,5,6]
# lis=list(filter(lambda a:a%2==0,l))# try a%2 ?
# print(lis)
#-----------------------------------------------
# def som(lis,f,l):#sum of list with divide and conquer!
#     if(l-f==1):
#         return lis[f]+lis[l]
#     if(l-f==0):
#         return lis[f]
#     mid=f+(l-f)//2
#     return som(lis,f,mid)+som(lis,mid+1,l)
# l=list(map(int,input("Enter a list of integers:\n").split()))
# print("Sum of integers in list is:",som(l,0,len(l)-1))
#-----------------------------------------------
# def maxx(l):
#     def logic(s,e):
#         if(s-e==1):
#             return l[s] if l[s]>l[e] else l[e]
#         if(s-e==0):
#             return l[s]
#         mid=s+(e-s)//2
#         left=logic(s,mid)
#         right=logic(mid+1,e)
#         return left if left>right else right
#     return logic(0,len(l)-1)
# l=list(map(int,input("Enter a list of integers:\n").split()))
# print("The largest element in the list is:",maxx(l))
#-----------------------------------------------
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while arr[j] < arr[j-1] and j > 0:
#             arr[j-1], arr[j] = arr[j], arr[j-1]
#             j = j-1
#     return arr
    
# size=int(input())
# arr = list(map(int,input().split(", ")))
# print(arr)
# ans = insertion_sort(arr)
# print(*ans,sep="->",end=" ")
#-----------------------------------------------
# def bubble(arr):
#     size=len(arr)
#     for i in range(size):
#         for j in range(size-i-1):
#             if(arr[j]>arr[j+1]):
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# size=int(input())
# arr = list(map(int,input().split(", ")))
# ans = bubble(arr)
# print(*ans,sep="->")
#-----------------------------------------------






