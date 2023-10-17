# class node:
#     def __init__(self,val=0):
#         self.val=val
#         self.next=None
# class sll:
#     def __init__(self):
#         self.head=None
#     def insert_at_beginning(self,data):
#         if self.head==None:
#             self.head=node(data)
#         else:
#             curr=self.head
#             while(curr.next):
#                 curr=curr.next
#             new=node(data)
#             curr.next=new
#     def display(self):
#         temp=self.head
#         while(temp):
#             print(temp.val,end=" → ")
#             temp=temp.next
#     def delete_at_beginning(self):
#         if self.head==None:
#             return 
#         temp=self.head
#         self.head=self.head.next
#         temp.next=None
#         return temp.val
#     def delete_at_end(self):
#         if self.head==None:
#             return 
#         temp=self.head
#         while(temp.next.next):
#             temp=temp.next
#         temp.next=None
#         return temp.val
# o1=sll()
# l=[1,2,3,4]
# for i in l:
#     o1.insert_at_beginning(i)
# print(o1.display())
# print(o1.delete_at_end())
# print(o1.delete_at_beginning())
# print(o1.insert_at_beginning(10))
# print(o1.display())
#--------------------------------------------------------
# class node:
#     def __init__(self,val=0):
#         self.prev=None
#         self.val=val
#         self.next=None
# class dll:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insert_at_beginning(self,data):
#         if self.head==None:
#             self.head=node(data)
#             self.tail=self.head
#         else:
#             newNode=node(data)
#             self.head.prev=newNode
#             newNode.next=self.head
#             self.head=newNode
#     def display(self):
#         temp=self.head
#         while(temp):
#             print(temp.val,end=" ⇆ ")
#             temp=temp.next
#     def delete_at_beginning(self):
#         if self.head==None:
#             return 
#         temp=self.head.val
#         self.head=self.head.next
#         self.head.prev=None
#         return temp
#     def delete_at_end(self):
#         if self.head==None:
#             return 
#         temp=self.tail.val
#         self.tail=self.tail.prev
#         self.tail.next=None
#         return temp
#     def reverse(self):
#         temp=self.head
#         while(temp):
#             temp.prev,temp.next=temp.next,temp.prev
#             temp=temp.prev
#         self.head,self.tail=self.tail,self.head
# o1=dll()
# l=[1,2,3,4]
# for i in l:
#     o1.insert_at_beginning(i)
# print(o1.display())
# print(o1.delete_at_end())
# print(o1.delete_at_beginning())
# print(o1.insert_at_beginning(10))
# print(o1.display())
# print(o1.reverse())
# print(o1.display())
#--------------------------------------------------------
