# a=[23,14,56,12,19,9,15,25,31,42,43]
# sum=0
# sum2=0
# for i in a:
#     if i%2==0:
#         sum+=i
#     else:
#         sum2+=i
# print("sum of even number is =",sum)
# print("sum of even number is =",sum2)


l=["p","q"]
# [p1,p2,p3,p4,p5,q1,q2,q3,q4,q5]
i=0
b=[]
while i<len(l):
    j=1
    while j<=5:
        k=str(j)
        k=l[i]+k
        b.append(k)
        j+=1
    i+=1
print(b)