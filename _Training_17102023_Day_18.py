import collections as coll
#--------------------------------------------------------------
# class node:
#     def __init__(self,val=0):
#         self.prev=None
#         self.val=val
#         self.next=None
# class cdll:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insert_at_end(self,data):
#         if self.head==None:
#             self.head=node(data)
#             self.tail=self.head
#             self.tail.next=self.head
#             self.head.prev=self.tail
#         else:
#             newNode=node(data)
#             newNode.next=self.head
#             newNode.prev=self.tail
#             self.tail.next=newNode
#             self.tail=newNode
#             self.head.prev=self.tail
#     def insert_at_beginning(self,data):
#         if self.head==None:
#             self.head=node(data)
#             self.tail=self.head
#             self.tail.next=self.head
#             self.head.prev=self.tail
#         else:
#             newNode=node(data)
#             newNode.next=self.head
#             self.head.prev=newNode
#             self.head=newNode
#             self.tail.next=self.head
#             self.head.prev=self.tail
#     def display(self):
#         print(" ⇆",self.head.val,end=" ⇆ ")
#         temp=self.head.next
#         while(temp!=self.head):
#             print(temp.val,end=" ⇆ ")
#             temp=temp.next
#     def delete_at_beginning(self):
#         if self.head==None:
#             return 
#         temp=self.head.val
#         self.head=self.head.next
#         self.head.prev=self.tail
#         self.tail.next=self.head
#         return temp
#     def delete_at_end(self):
#         if self.head==None:
#             return 
#         temp=self.tail.val
#         self.tail=self.tail.prev
#         self.tail.next=self.head
#         self.head.prev=self.tail
#         return temp
# o1=cdll()
# l=[1,2,3,4]
# for i in l:
#     o1.insert_at_beginning(i)
# print(o1.display())
# print(o1.delete_at_end())
# print(o1.delete_at_beginning())
# print(o1.insert_at_beginning(-1))
# print(o1.display())
#--------------------------------------------------------------
#Stack is a linear data structure where insertion and retrivel is implemented one end only either bottom or top.--Monotonic stack where we insert elts in sorted order while insertion.
#Queue is a linear data structure where insertion is done on one end and deleted from other end.
#--------------------------------------------------------------
# def removeDuplicates(s):#1047. Remove All Adjacent Duplicates In String.
#     st=coll.deque()
#     for i in s:
#         if not st:
#             st.append(i)
#         elif i==st[-1]:
#             st.pop()
#         else:
#             st.append(i)
#     return "".join(st)
# s=input("Enter a string of small alphabets:")
# print("After deleting common letters adjacent to each other the resulting string is:",removeDuplicates(s))
#--------------------------------------------------------------
# def minLength(s):#2696. Minimum String Length After Removing Substrings
#     st=coll.deque()
#     for i in s:
#         if not st:
#             st.append(i)
#         elif st[-1]=="A" and i=="B":
#             st.pop()
#         elif st[-1]=="C" and i=="D":
#             st.pop()
#         else:
#             st.append(i)
#     return len(st)
# s=input("Enter a string in only capital letters:")
# print("The length of string after deleting AB and CD combinations is:",minLength(s))
#--------------------------------------------------------------
# def removeStars(s):#2390. Removing Stars From a String
#     st=coll.deque()
#     for i in s:
#         if not st:
#             st.append(i)
#         elif i=="*":
#             st.pop()
#         else:
#             st.append(i)
#     return "".join(st)
# s=input("Enter a string with * in them:")
# print("The resulting string after removing letters whenever * occoured is:",removeStars(s))
#--------------------------------------------------------------
# def isValid(s):#20. Valid Parentheses
#     st=coll.deque()
#     d={")":"(","}":"{","]":"["}
#     for i in s:
#         if i=="(" or i=="{" or i=="[":
#             st.append(i)
#         if i==")" or i=="}" or i=="]":
#             if(not st):
#                 return False
#             elif(d[i]==st[-1]):
#                 st.pop()
#             else:
#                 return False
#     return not st
# s=input("Enter a string of brackets (),{},[] to check valid parenthesis:")
# print(isValid(s))
#--------------------------------------------------------------
#641. Design Circular Deque
# class MyCircularDeque:

#     def __init__(self, k: int):
#         self.q = []
#         self.k = k
        
#     def insertFront(self, value: int) -> bool:
#         if len(self.q) < self.k:
#             self.q = [value] + self.q
#             return True
#         return False

#     def insertLast(self, value: int) -> bool:
#         if len(self.q) < self.k:
#             self.q.append(value) #push in last
#             return True
#         return False
        
#     def deleteFront(self) -> bool:
#         if len(self.q) > 0:
#             self.q.pop(0)
#             return True
#         return False

#     def deleteLast(self) -> bool:
#         if len(self.q) > 0:
#             self.q.pop()
#             return True
#         return False

#     def getFront(self) -> int:
#         if len(self.q) > 0:
#             front = self.q[0]
#             return front
#         return -1

#     def getRear(self) -> int:
#         if len(self.q) > 0:
#             last = self.q[-1]
#             return last
#         return -1
        
#     def isEmpty(self) -> bool:
#         if len(self.q) == 0:
#             return True
#         return False
        
#     def isFull(self) -> bool:
#         if len(self.q) == self.k:
#             return True
#         return False
#--------------------------------------------------------------
# class TreeNode:#94. Binary Tree Inorder Traversal
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         l=[]
#         def inOrder(root):
#             if(root==None):
#                 return 
#                 #DFS Preorder Traversal
#             inOrder(root.left)
#             l.append(root.val)
#                 #DFS Inorder Traversal
#             inOrder(root.right)
#                 #DFS Postorder Traversal
#         inOrder(root)
#         return l
#--------------------------------------------------------------
#BFS (Level order) traversal.
# class node():
#     def __init__(self,val):
#         self.left=None
#         self.val=val
#         self.right=None
# root=node(1)
# root.left=node(2)
# root.right=node(3)
# root.left.right=node(4)
# root.right.left=node(5)
# root.right.right=node(6)
# q=[]
# BFS_Traversal=[]
# q.append(root)
# while(q):
#     temp=q.pop(0)
#     BFS_Traversal.append(temp.val)
#     if(temp.left):
#         q.append(temp.left)
#     if(temp.right):
#         q.append(temp.right)
# print("The BFS traversal is:\n",*BFS_Traversal,sep=" ")
#--------------------------------------------------------------