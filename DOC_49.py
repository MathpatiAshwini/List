a=['s','d','f','s','d','f','s','f','k','o','p','i','w','e','k','c']
i=0
b=[]
while i<len(a):
    if a[i]=='f':
        b=i
    elif a[i]=="c":
        c=i
    elif a[i]=="k":
        d=i
    elif a[i]=="w":
        e=i
    i+=1
print("last occurrence of f in the list",b)
print("last occurrence of c in the list",c)
print("last occurrence of k in the list",d)
print("last occurrence of w in the list",e)