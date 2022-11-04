a=[1,2,3,4,5,6,7,8,9,10]
i=0
c=[]
while i<len(a)-1:
    n=a[i+1]-a[i]
    c.append(n)
    i=i+1
print(c)
