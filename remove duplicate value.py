a=['a','s','h','w','i','n','i','m','a','t','h','p','a','t','i']
i=0
b=[]
c=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        c=c+1
    i=i+1
print(b)
print(c)





