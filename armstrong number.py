#armstrong numbers
'''
armstrong number is a number that is equal
to the sum of cube of its digits'''
#ex:-153,370,8208,1634
#1^3+5^3+3^3=153
#note:-power= length of number

#program
n=int(input("enter a number"))
st=str(n)
power=len(st)
s=0
cn=n
while n>0:
    k=n%10
    po=k**power
    s+=po
    n//=10
if s==cn:
    print("armstrong number")
else:
    print("not a armstrong number")
    
