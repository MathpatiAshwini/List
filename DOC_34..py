a=[34.67,12,-94.89,'python',0,'c#']
i=0
t=[]
while i<len(a):
    if type(a[i])==int and a[i]>=0:
        t.append(a[i])
    i+=1
print(t)