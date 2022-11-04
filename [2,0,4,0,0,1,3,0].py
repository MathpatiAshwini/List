# a=[2,0,4,0,0,1,3,0]
# # o/p[2,4,3,0,0,0,0]
# print("[",a[0],a[2],a[6],a[1],a[3],a[4],a[7],"]")


a="ashwini"
b=" "
i=0
while i<len(a):
    n=a[i]
    b+="'"
    b+=n
    b+="'"
    b+=","
    i=i+1
print([b])