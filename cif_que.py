a=[]
b=[0]
i=0
c=[]
while i<len(b):
    if b[i] not in c:
        print([b[i]])
    else:
        print(a[i])
    i+=1
    