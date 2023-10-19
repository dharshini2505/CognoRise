import random
while True:
    print("0.ROCK")
    print("1.PAPER")
    print("2.SCISSOR")
    user_choice = int(input("Enter your Choice(0/1/2): "))
    if user_choice >=3 or user_choice <0 :
        print ("Invalid choice ,try again")
    else:
        computer_choice=random.randint(0,2)
        print("Computer choice =",computer_choice )
        if computer_choice == user_choice :
            print("match draw")
        elif computer_choice == 0 and user_choice == 2:
            print("You Lose")
        elif computer_choice == 2 and user_choice == 0:
            print("You Win")
        elif computer_choice > user_choice:
            print("You Lose")
        elif computer_choice < user_choice:
            print("You Win")
            
        count=input("dou you want to continue \n 1.YES 2. NO :")
        while count.lower() not in ("1","2"):
            count=input("Please Enter the Correct Input \n 1.YES 2. NO")
        if count == "2":
            print()
            print("Thank you.")
            break

