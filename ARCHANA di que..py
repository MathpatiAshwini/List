a=["archana","devika"]
b=["singh","raj"]
i=0
v=[]
w=0
while i<len(a):
    j=0
    while j<len(b):
        if w<len(a):
            c=a[j][0].upper() 
            m=b[j][0].upper()
            v.append(c)
            v.append(m)
            j+=1
        i+=1
print(v)