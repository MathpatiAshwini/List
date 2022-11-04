# list=[]
# if len(list) == 0:
# 	print(list,'List is empty')
# else:
# 	print(list,'List there is elemants')

# list=[]
# i=0
# a=[]
# while i<1:
#     if list==a:
#         print(list,"is empty")
#     else:
#         print(list,"elemants is there")
#     i=i+1


a="LAXMI"
b="ASHWINI"
b=""
i=0
while i<len(a):
    j=0
    while j<len(b):
        if a[i]!="l":
            print(a[i],end="")
            j+=1
        if b[j]!="a":
            print(b[j],end="")
        else:
            print(a[i],b[j],end="")
        i+=1
    
