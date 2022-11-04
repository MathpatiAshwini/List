a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
c=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        c+=1
    i=i+1
print(b)
print(c)
