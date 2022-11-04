# a=[1,2,3,4,5,6] 
# b=a[::-1]
# i=0
# m=[]
# while i<len(a)/2:
#     n=b[i],a[i]
#     m.append(n)
#     i=i+1
# print(m)
a="dog"
# o/p[d,do,dog,o,og,gd]
i=0
b=[]
while i<len(a):
    j=0
    while j<3:
        b.append(a[j])
        j+=1
    i+=1
    print(b)
