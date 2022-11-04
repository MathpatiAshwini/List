list=[4,6,4,3,3,4,3,4,3,8,1,1,1,1]
l1=[]
i=0
while i<len(list):
    v=list.count(i)
    if v>3:
        if l1.count(i)==0:
            l1.append(i)
    i=i+1
print(l1)

list=[4,6,4,3,3,4,3,6,6]
l1=[]
i=0
while i<len(list):
    v=list.count(i)
    if v>2:
        if l1.count(i)==0:
            l1.append(i)
    i=i+1
print(l1)
a=[4,6,4,3,3,4,3,4,6,6]
# [4,3]
i=0
b=[]
while i<len(a):
    v=a.count(i)
    if v>2:
        b.append(i)
    i=i+1
print(b)
