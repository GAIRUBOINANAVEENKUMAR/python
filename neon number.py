#NEON NUMBER
'''
a number is said to be neon when
the number is squared and the sum of result individuals is equal to that number
EX:-9-->81-->8+1=9'''

#program
num=int(input("enter a number"))
square=num**2
s=0
cn=num
while square>0:
    l=square%10
    s+=l
    square//=10
if s==cn:
    print("neon number")
else:
    print("not a neon number")
