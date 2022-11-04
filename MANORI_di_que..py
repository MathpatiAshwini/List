# Sample Input 0
# 07:05:45PM
# Sample Output 0
# 19:05:45
# Example: s="12:01:00PM", return=> "12:01:00"
        #  s="12:01:00AM", return=>"00:01:00"
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# s="12:01:00PM"
# print("00"+s[2:8]+"am")
# s="07:05:45PM"
# print("19"+s[2:8]+"am")

d=int(input("enter the length of time:"))
c=str(d)
# b=int(c)
if d=="07:05:45":
    x=c[:2]
    if int(x)<=12:
        print("19",c[2:4],":",c[4:],"pm")
    else:
        print((c[:2])-12,":",c[2:4],":",c[4:],"am")
else:
    print("wrong length")