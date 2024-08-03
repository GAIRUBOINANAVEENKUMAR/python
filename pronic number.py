#PRONIC NUMBER
'''
a  number which is formed by mu6ltiplication of two consecutive numbers
is called pronic number
'''
#EX:-2,6,12,20,24...
#1*2=2
#2*3=6

#program - check given number is abstract or not
n=int(input("enter a number"))
m=1
l=[]
for i in range(1,n):
    l.append(i)
print(l)
i=0
while i<n:
    if l[i]*l[i+1]==n:
        print("pronic number")
    else:
        print("not pronic number")
    
    
