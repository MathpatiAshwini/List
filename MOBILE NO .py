a=[(123456789)]
# o/p(123)456-789
i=0
b=[]
while i<len(a):
    if i<3:
        b.append(a[i])
    elif i>=3 and i<6:
        b.append(a[i])
    else:
        b.append(a[i])
    i+=1
print(b)