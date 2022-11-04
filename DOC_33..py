# a=['12','67','98','34']
# i=0
# b=[]
# while i<len(a):
#     sum=0
#     j=0    
#     while j<len(str(a[i])):
#         sum=sum+int(a[i][j])
#         j+=1
#     b.append(sum)
#     i+=1
# print(b)

a=[12,67,98,34]
i=0
b=[]
while i<len(a):
    sum=0
    j=0   
    p=str(a[i])
    while j<len(p):
        sum+=int(p[j])
        # b.append(sum)
        j+=1
    b.append(sum)
    i+=1
print(b)