# class parent:
#     def parent1(self):
#         print("parent1")
#     def parent2(self):
#         print("parent2")
# class child1:
#     def child11(self):
#         print("child11")
#     def child12(self):
#         print("child12")
# class child2:
#     def child21(self):
#         print("child21")
#     def child22(self):
#         print("child22")
# p=parent()
# c1=child1()
# c2=child2(c1)
# c2.child11()
#--------------------------------
# class Solution:#5. Longest Palindromic Substring
#     def longestPalindrome(self, s: str) -> str:
#         def check(f, l, size):
#             while f >= 0 and l < size and s[f] == s[l]:
#                 f -= 1
#                 l += 1
#             return s[f + 1 : l]
#         size = len(s)
#         if size <= 1:
#             return s
#         res = ""
#         for i in range(size):
#             palindrome1 = check(i, i, size)
#             if len(palindrome1) > len(res):
#                 res = palindrome1
#             palindrome2 = check(i, i + 1, size)
#             if len(palindrome2) > len(res):
#                 res = palindrome2
#         return res
#------------------------------------------------------
# s1 = input("Enter a string:")
# s2 = input("Enter another string:")
# res = []
# for i in range(len(s1)):
#     for j in range(i+1,len(s1)):
#         ans = ""
#         for k in range(i,j+1):
#             ans+=s1[k]
#         res.append(ans)
# ans = ""
# for i in res:
#     if i in s2:
#         if len(i)>len(ans):
#             ans = i
# print("The longest common subsequence is:",ans)
#------------------------------------------------------

