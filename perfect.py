#check perfect or not
#perfect number=sum of divisors
#ex:-6,28,496
#6-1,2,3
n=int(input("enter a number"))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print("perfect number")
else:
    print("not a perfect number")
