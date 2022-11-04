d=int(input("enter the length of time:"))
c=str(d)
b=int(c)
if len(c)>0:
    x=c[:2]
    if int(x)<=12:
        print(c[:2],":",c[2:4],":",c[4:],"pm")
    else:
        print((c[:2])-12,":",c[2:4],":",c[4:],"am")
else:
    print("wrong length")
