# list=[3,4,5,20,5,25,1,3]
# print(list.count(5))

# (without using count method)
# numbers=[50,40,23,70,56,12,5,10,7]
# index=0
# while index<len(numbers):
#     index+=1
# print(index)


# c=20
# d=40
# e=0
# while c<=d:
#     e=e+1
#     c=c+1
# print(e)

# list=[50,40,23,70,56,12,5,10,7]
# more=20
# less=40
# i=0
# while i<len(list):
#     if list[i]>20 and list[i]<40:
#         print(list[i],"between 20 to 40" )
#     i=i+1
#     print()


a=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
c=0
p=0
i=0
b=[]
n=[]
while i<len(a):
    if a[i]!=a[i+1]:
        c+=1
        b.append(c)
    else:
        p+=1
        n.append(p)
    i+=1
print(b)
print(n)