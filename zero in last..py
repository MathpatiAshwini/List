a=[1,2,0,5,6,3,0,0]
i=0
b=[]
while i<len(a):
    if a[i]==0:
        a.sort()
        a.pop()
    i+=1
print(a)