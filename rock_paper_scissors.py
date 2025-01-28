import random
emojis = {'r': '🪨', 'p': '📃', 's': '✃'}
lists = ["r", "p", "s"]
computer = 0
user = 0

while True:
    user_input = input("rock, paper or scissors (r/p/s): ")
    computer_choice = random.choice(lists)

    print(f"You chose: {emojis[user_input]}")
    print(f"Computer Chose: {emojis[computer_choice]}")
    if user_input not in lists:
        print("Enter a valid input!")
        continue
    elif (
            (user_input == "r" and computer_choice == "s") or
            (user_input == "s" and computer_choice == "p") or
            (user_input == "p" and computer_choice == "r")):
        print("You win")
        user += 1
    elif(
            (user_input == "s" and computer_choice == "s") or
            (user_input == "p" and computer_choice == "p") or
            (user_input == "r" and computer_choice == "r")):
        print("It's a draw!")
    else:
        print("You lose")
        computer += 1
    print(f"Your point = {user}")
    print(f"Computer point = {computer}")
    should_continue = input("Do you need to continue? (y/n): ").lower()
    if should_continue == "y":
        continue
    elif should_continue == "n":
        print("Thank you for playing")
        break


