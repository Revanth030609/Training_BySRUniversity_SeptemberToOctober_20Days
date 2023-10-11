# def maxProfit(prices):#Greedy Algorithm.Here min and max are kept track of!
#     size=len(prices)
#     small=prices[0]#121. Best Time to Buy and Sell Stock
#     profit_max=0
#     for i in range(size):
#         if(small>prices[i]):
#             small=prices[i]
#         temp=prices[i]-small
#         if(profit_max<temp):
#             profit_max=temp
# return profit_max
#----------------------------------------------------------
# class Solution:#122. Best Time to Buy and Sell Stock II
#     def maxProfit(self, prices: List[int]) -> int:
#         size=len(prices)
#         small=prices[0]
#         profit_max=0
#         f=0
#         for i in range(size-1):
#             if(small>prices[i]):
#                 small=prices[i]
#             if(prices[i]>prices[i+1]):
#                 profit_max+=prices[i]-small+temp
#                 small=prices[i]
#             if(prices[i]<prices[i+1]):
#                 temp=prices[i+1]-small
#         if f:
#             return profit_max+temp
#         else:
#             return profit_max
#----------------------------------------------------------
# knapsack=int(input("Enter the knapsack size:"))
# profits=list(map(int,input("Enter the profits of items:\n").split()))
# weights=list(map(int,input("Enter the weights of items:\n").split()))
# size=len(profits)
# pairs=list(zip(weights,profits))
# pairs.sort(key=lambda x:x[1]/x[0],reverse=True)
# max_profit=0

# for i in range(size):
#     if(x[0]<=knapsack):
#         max_profit+=x[1]
#         knapsack-=x[0]
#     else:
#         max_profit+=knapsack*(x[1]/x[0])
#         break
# print(f"The knapsack of size {knapsack} will have a maximium profit of:{max_profit}")
#----------------------------------------------------------
# class Solution:#34. Find First and Last Position of Element in Sorted Array
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left, right = 0, len(nums) - 1
#         first, last = -1, -1
        
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 first = mid
#                 last = mid
#                 while first > 0 and nums[first - 1] == target:
#                     first -= 1
#                 while last < len(nums) - 1 and nums[last + 1] == target:
#                     last += 1
#                 return [first, last]
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return [first, last]
#----------------------------------------------------------
# class Solution:#2141. Maximum Running Time of N Computers.
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         batteries.sort()
#         total = sum(batteries)
#         while batteries[-1] > total//n:
#             n -= 1
#             total -= batteries.pop()
#         return total//n
#----------------------------------------------------------
# c=int(input())
# wt=list(map(int,input().split()))
# p=list(map(int,input().split()))
# l=list(zip(wt,p))
# l.sort(key=lambda y:y[1]/y[0],reverse=True)
# print(l)
# maxpr=0
# for weight,pro in l:
#     if weight<c:
#         maxpr+=pro
#         c-=weight
#     else:
#         maxpr+=c*(pro/weight)
#         break
# print(maxpr)
#----------------------------------------------------------



