""""special number
A two digit number whose sum of
addition and multiplication
of individual digits is equal to that number
Ex:- 49,89 """
n=int(input("enter a number"))
s=0
m=1
cn=n
while n>0:
    l=n%10
    s+=l
    m*=l
    n=n//10
su=s+m
if su==cn:
    print("special number")
else:
    print("not a special number")
