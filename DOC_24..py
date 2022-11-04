a=[1,2,3,1,2,2]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)

# a=int(input("enetr the number:-"))
# b=[]
# i=0
# while i<a:
#     x=int(input("enetr the number:-"))
#     b.append(x)
#     n=x
#     r=n%1000
#     m=r%100
#     y=m%10
#     i=i+1
#     print('"',n-r,"+",r-m,"+",m-y,"+",y,'"')
