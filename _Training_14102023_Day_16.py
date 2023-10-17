# def primes(s,r):
#     l = [True for i in range(r+1)]
#     l[0] = False
#     l[1]=False
#     l[2] = True
#     for i in range(r+1):
#         if l[i]==True:
#             j=i+1
#             while j<r+1:
#                 if l[j]==True and j%i==0:
#                     l[j]=False
#                 j+=1       
#     return l
# ans = primes(3,100)
# for i in range(3,len(ans)):
#     if ans[i]:
#         print(i,end=" ")
#---------------------------------------------------------------
# def sumtar(l,tar,i,j):#Using Sliding window concept finding target sum possible or not!
#     if l[i]==tar:
#         return [l[0]]
#     j = 0
#     cs = l[i]
#     while j<len(l)-1:
#         if cs==tar:
#             return l[i:j+1]
#         elif j<len(l) and cs<tar:
#             j+=1
#             cs+=l[j]
#         elif cs>tar:
#             cs-=l[i]
#             i+=1
#     return None

# l = list(map(int,input("Enter a list of integers:").split()))
# tar = int(input("Enter a target sum:"))
# print(sumtar(l,tar,0,0))
#---------------------------------------------------------------

