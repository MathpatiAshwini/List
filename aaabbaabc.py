# a="aaabbaabc"
# # o/p['a','b','a','b','c']
# b=[]
# i=0
# while i<len(a):
#     count=0
#     k=a[i]
#     c=[]
#     j=0
#     while j<len(a):
#         l=a[j]
#         if k==l:
#           count+=1
#         j+=1
#     c.append(k)
#     c.append(count)
#     if c not in b:
#       b.append(c)
#     i+=1
# print(b)




# a="aaabbaabc"
# # o/p['a','b','a','b','c']
# b=[]
# i=0
# while i<len(a):
#     k=a[i]
#     j=1
#     while j<len(k):
#         # b.append(a[i])
#         j+=1
#     b.append(a[i])
#     i+=1
# print(b)



# a="aaabbaabc"
# # o/p['a','b','a','b','c']
# b=[]
# i=0
# while i<len(a)-5:
#     k=a[i]
#     j=0
#     while j<len(k):
#         if a[i].isalpha:
#             b.append(a[i-4])
#             j+=1
#         i+=1
# print(b)