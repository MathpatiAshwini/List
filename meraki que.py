
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