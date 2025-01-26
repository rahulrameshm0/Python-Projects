import random

user_choice = int(input("Enter your choice: 0 is for Rock, 1 is for paper, 2 is for scissor: "))
if user_choice >=3 or user_choice < 0:
    print("You have entered the wrong number")
else:
    computer_choice = random.randint(0, 1)
    print("computer chose: ")
    print(computer_choice)
    if computer_choice == user_choice:
        print("Its a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You Win")

