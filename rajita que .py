# a=[[8,3,4],[1,5,9],[6,7,2]]
a=[[1,2,1],[4,5,6],[10,13]]
i=0
b=[]
while i<len(a):
    n=a[i]
    j=0
    sum=0
    while j<len(n):
        sum+=a[i][j]
        j=j+1
    i=i+1
    b.append([sum])
print(b)
