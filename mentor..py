a="LAXMI"
b="ASHWINI"
b=""
i=0
while i<len(a):
    j=0
    while j<len(b):
        if a[i]!="l":
            print(a[i],end="")
            j+=1
        if b[j]!="a":
            print(b[j],end="")
        else:
            print(a[i],b[j],end="")
        i+=1
    

