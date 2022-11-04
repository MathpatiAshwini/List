a=[[2,3,4],[1,2,6,7],[7,8,9,0,1],[2,1,5,12,],[7,8,2,]]
a=[[2,3,4,'',''],[1,2,6,7,''],[7,8,9,0,1],[2,1,'','',''],[7,8,2,'','']]
i=0
b1=[]
while i<len(a):
    j=0
    k=0
    sum=0
    while j<len(a):
        l=a[j][i]
        if type (l)==int:
            sum+=a[j][i]
        if type (l)=='':
            k=k+0
        else:
            k=k+1
        j+=1
    avg=sum/k
    b1.append(avg)
    i=i+1
print(b1)