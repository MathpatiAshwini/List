a=[1,2,3,4,5,6]
i=0
b=len(a)
c=[]
while i<b-1:
    d=[]
    j=i
    while j<i+1:
        d.append(a[j])
        d.append(a[j+1])
        j+=1
    c.append(d)
    i+=1
print(c)

    
