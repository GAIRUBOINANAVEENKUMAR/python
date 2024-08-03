import random
guess_number=random.randint(1,100)
User_Name=input("Enter Your Name: ")
user_guess=int(input("What number you are guessing: "))
for i in range(5):
    if(guess_number==user_guess):
        print(f"Congratulations {User_Name} You Won The Game!!!")
        break
    elif(guess_number>user_guess):
        print("Your Guess is Below To My Number")
        user_guess=int(input("What number you are guessing: "))
    else:
        print("Your Guess is Above To My Number")
        user_guess=int(input("What number you are guessing: "))
else:
    print(f"Sorry{User_Name} You Lost The Game...!")
    print(f"My Number is {guess_number}")
    
        
        
        
