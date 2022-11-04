a=[6,1,3,5,6,3,1]
i=0
b=[]
d=1
while i<len(a):
    if a[i] not in b:
        # h=d*a[i]
        # b.append(h*a[d])
        b.append(a[i])
    i=i+1
print(b)

# l=[6,1,3,5]
# i=0
# p=1
# while i<len(l):
#     p=p*l[i]
#     i=i+1
# print(p)



# b=[]
# for i in list:
#     if i not in b:
#         b.append(i)
# print(b)
# p=1
# for j in b:
#     p=p*j
# print(p)
