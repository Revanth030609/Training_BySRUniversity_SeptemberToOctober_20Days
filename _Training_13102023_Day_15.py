# def knap(W,wt,val,n):#Knap sack 1/0 using dynamic programming.
#     dp=[[0 for x ion range(W+1)] for x in range(n+1)]
#     for i in range(n+1):
#         for w in range(W+1):
#             if i==0 or w==0:
#                 dp[i][w]=0
#             elif wt[i-1]<=w:
#                 dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
#             else:
#                 dp[i][w]=dp[i-1][w]
#             return dp[n][W]
#---------------------------------------------------------------
# def coinchange(l,tar):
#     dp = [[float('inf') for j in range(tar+1)] for i in range(len(l)+1)]
#     for i in range(tar+1):
#         dp[1][i] = i//l[0]
#     for i in range(len(l)+1):
#         for j in range(tar+1):
#             if i==0 or j==0:
#                 continue
#             if l[i-1]>j:
#                 dp[i][j]=dp[i-1][j]
#             else:
#                 dp[i][j] = min(1+dp[i][j-l[i-1]],dp[i-1][j])
#     return dp[len(l)][tar]
# l = list(map(int,input("Enter the coins list:").split()))
# tar = int(input("Enter the target amount:"))
# print(coinchange(l,tar))
#---------------------------------------------------------------
# l = list(map(int,input("Enter a list:\n").split()))#189 rotate array
# k = int(input("Enter the rotation factor:"))
# if k>len(l):
#     k = k%len(l)
# while k!=0:
#     t = l[0]
#     j=1
#     while j<len(l):
#         l[j-1] = l[j]
#         j+=1
#     l[j-1] = t
#     k-=1
# print("The rotated list is:\n",l)
#---------------------------------------------------------------





