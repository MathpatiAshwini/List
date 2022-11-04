a=[22,10,3,50]
i=0
j=1
b=[]
while i<len(a):
    n=str(a[i]+j)
    if len(n)>1:
            v=n[0]
            l=int(v)
            b.append(l)
    else:
        h=int(a[2])
        b.append(h)
    i+=1
    j+=1
print(b)
