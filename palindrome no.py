n=int(input("Enter number:")) 
temp=n 
rev=0 
while(n>0): 
    dig=n%10 
    rev=rev*10+dig 
    n=n//10 
if(temp==rev): 
    print(temp,"The number is a palindrome!") 
else: 
    print(temp,"The number isn't a palindrome!")


# a=["abc","mom","kook","tamann"] 
# i=0 
# while i<len(a): 
#     n=a[i]
#     r=n[: : -1]
#     if r==a[i]:
#         print(a[i],":-palindrome no")
#     else:
#         print(a[i],":-not palindrome no ")
#     i=i+1


# n=[12,333,453,121,525,900]
# temp=n 
# i=0 
# b=[]
# while i<len(n): 
#     dig=n[i]%10 
#     i=i*10+dig 
#     temp=temp//10 
#     b.append(i)
# if temp==b: 
#     print(b,"palindrome!") 
# else: 
#     print(b," not palindrome!")
