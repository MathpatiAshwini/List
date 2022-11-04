a=[['R','A','N','I'],['S','H','A','R','M','A']]
i=0
b=[]
while i<len(a):
    n=a[i]
    j=0
    while j<len(a[i]):
        m=a[i][j]
        b.append(m)
        j+=1
    i+=1
print(b)
