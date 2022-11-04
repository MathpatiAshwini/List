b="my8 name8 is8 archana8"
i=0
a=""
while i<len(b):
    if b[i].isalpha()==True or b[i]==" ":
        a=a+b[i] 
    i+=1
print(a)

a="LAXMI"
b="ASHWINI"
i=0
while i<len(b):
    j=0
    while j<len(b):
        if a[i].islower():
            print(a[i],end="")
            j+=1
        if b[j][0].upper():
            print(b[j],end="")
        else:
            print(a[i],b[j],end="")
        i+=1
    

a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
b=[]
sum2=0
while i<len(a):
    sum=0
    j=0
    n=a[i]
    while j<len(n):
        sum+=n[j]
        sum2+=n[j]
        j+=1
        # b.append(sum)
    i+=1
    b.append(sum)
print(b)
print(sum2)