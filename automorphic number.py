#AUTOMORPHIC NUMBER
'''a number whose square ends with the same number'''
#ex:5-->25
#6-->36
num=int(input("Enter a number: "))
square=num**2
l=len(str(num))
'''while temp_num>0:
    temp_num//=10
    num_digits+=1'''
div=10**l
if square%div==num:
    print(num,"is a automorphic number.")
else:
    print(num"is not an automorphic number.")

    
