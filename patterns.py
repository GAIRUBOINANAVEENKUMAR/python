n=int(input("Enter a number:-"))
for i in range(n):
    for j in range(n):
        if i<=j:
            if i+j<=n-1:
                print("*",sep=" ",end=" ")
    print()
        
