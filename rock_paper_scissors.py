import random
emojis = {'r': '🪨', 'p': '📃', 's': '✃'}
lists = ["r", "p", "s"]
def get_user_choice():
    while True:
        user_input = input("rock, paper or scissors (r/p/s): ")
        if user_input in lists:
            return user_input
        else:
            print("Enter a valid input!")
            continue

def display_choices(user_input, computer_choice):
    print(f"You chose: {emojis[user_input]}")
    print(f"Computer Chose: {emojis[computer_choice]}")

def determine_winner(user_input, computer_choice):
    if (
        (user_input == "r" and computer_choice == "s") or
        (user_input == "s" and computer_choice == "p") or
        (user_input == "p" and computer_choice == "r")):
        print("You win")

    elif (
        (user_input == "s" and computer_choice == "s") or
        (user_input == "p" and computer_choice == "p") or
        (user_input == "r" and computer_choice == "r")):
        print("It's a draw!")
    else:
        print("You lose")
def play_game():
    while True:
        user_input = get_user_choice()
        computer_choice = random.choice(lists)
        display_choices(user_input, computer_choice)
        determine_winner(user_input, computer_choice)

        should_continue = input("Do you need to continue? (y/n): ").lower()
        if should_continue == "y":
            continue
        elif should_continue == "n":
            print("Thank you for playing")
            break
        else:
            print("Enter a valid input!")

play_game()