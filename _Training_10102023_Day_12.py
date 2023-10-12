# class Solution:#804. Unique Morse Code Words
#     def uniqueMorseRepresentations(self, l: List[str]) -> int:
#         d={ 'a':'.-', 'b':'-...',
#                     'c':'-.-.', 'd':'-..', 'e':'.',
#                     'f':'..-.', 'g':'--.', 'h':'....',
#                     'i':'..', 'j':'.---', 'k':'-.-',
#                     'l':'.-..', 'm':'--', 'n':'-.',
#                     'o':'---', 'p':'.--.', 'q':'--.-',
#                     'r':'.-.', 's':'...', 't':'-',
#                     'u':'..-', 'v':'...-', 'w':'.--',
#                     'x':'-..-', 'y':'-.--', 'z':'--..'}
#         def mapp(f):
#             temp=""
#             for i in f:
#                 temp+=d[i]
#             return temp
#         l=list(map(lambda x:mapp(x),l))
#         res=set(l)
#         return len(res)
#-----------------------------------------------------------------
# def result(le,ri):#Merge sort
#     x=[]
#     i,j=0,0
#     while i<len(le) and j<len(ri):
#         if le[i]<ri[j]:
#             x.append(le[i])
#             i+=1
#         else:
#             x.append(ri[j])
#             j+=1
#     x.extend(le[i:])
#     x.extend(ri[j:])
#     return x
# def merge(l):
#     if len(l)<=1:
#         return l
#     mid=len(l)//2
#     le=l[:mid]
#     ri=l[mid:]
#     le=merge(le)
#     ri=merge(ri)
#     r=result(le,ri)
#     return r   
# l=list(map(int,input().split()))
# print(merge(l))
#-----------------------------------------------------------------
