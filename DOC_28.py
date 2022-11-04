a=[1,1,2,3,4,5,1,2]
# o/p [2,3,4,5,2]
i=0  
m=[]
while i<len(a):
   if a[i]==1:
    m.append(a[i])
    i+=1
print(m