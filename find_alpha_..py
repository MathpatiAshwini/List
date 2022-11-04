str="ashwini123mathpati"
i=0
b=[]
p=""
while i<len(str):
    if str[i].isalpha():
        b.append(str[i])
    i+=1
p="".join(b)
print(p)