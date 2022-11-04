# a='my name is ashwini'
# i=0
# while i<len(a):
#     j=0
#     n=a[i]
#     while j<len(n):
#         if n[j].upper():
#             n=str(n[j][0].upper())
#             print(n[j].lower(),end="")
#             j+=1
#         else:
#             print(a[i],end="")
        # i+=1

a='my name is ashwini'
i=0
while i<len(a):
    j=0
    n=a[i]
    while j<len(n):
        if n.isalpha:
            print(n[j].upper(),end="")
            j+=1
        else:
            print(a[i],end="")
        i+=1
        
