l=[1,2,3,4,5,6]
i=0
b=[]
while i<len(l):
    n=l[i+1],l[i-1]
    b.append(n)
    i+=1
print(b)