# a=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# even=0
# odd=0
# while i<len(a):
#     if a[i]%2==0:
#         even+=1
#     else:
#         odd+=1
#     i+=1
# print("even number is the list",even)
# print("odd number is the list ",odd)

a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
while i<len(a):
    if a[i]%2==0:
        print("even",a[i])
    else:
        print("odd",a[i])
    i+=1

