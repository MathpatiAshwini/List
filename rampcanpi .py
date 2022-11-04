a=[10,10,2,3,2,2,3,40]
i=0
b=[]
while i<len(a) :
    if a[i]==a[i]:
        a=['12','67','98','34']
i=0
b=[]
while i<len(a):
    sum=0
    j=0    
    while j<len(str(a[i])):
        sum=sum+int(a[i][j])
        j+=1
    b.append(sum)
    i+=1
print(b)