a=['2','t','u','6','2','d','6','d','u','1','2']
i=0
b=[]
while i<len(a):
    if a[i] in b:
        print(a[i],end="")
    else:
        b=a[i]
        print(b,end="")
    i+=1