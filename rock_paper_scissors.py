import random
lists = ["r", "p", "s"]
while True:
    user_input = input("rock, paper or scissors (r/p/s): ")
    computer_choice = random.choice(lists)
    if user_input == "r" and computer_choice == "r":
        print("You chose: Rock 🪨\nComputer Choose: Rock 🪨\nIt's a draw!")
    elif user_input == "r" and computer_choice == "p":
        print("You chose: Rock 🪨\nComputer Choose: Paper 📃\nYou lose!")
    elif user_input == "p" and computer_choice == "r":
        print("You chose: Paper 📃\nComputer Choose: Rock 🪨\nYou win!")
    elif user_input == "p" and computer_choice == "s":
        print("You chose: Paper 📃\nComputer Choose: scissors ✁\nYou lose!")
    elif user_input == "p" and computer_choice == "p":
        print("User choice: Paper 📃\nComputer Choose: paper 📃\nit's a draw!")
    elif user_input == "s" and computer_choice == "p":
        print(f"User choice: Scissors ✄\nComputer Choice: Paper 📃\nYou win!")
    elif user_input == "r" and computer_choice == "s":
        print(f"User choice: Rock 🪨\nComputer Choice: Scissors ✄\nYou win!")
    elif user_input == "s" and computer_choice == "r":
        print(f"User choice: scissors ✄ \nComputer Choice: Rock 🪨\nYou lose!")
    elif user_input == "s" and computer_choice == "s":
        print(f"User choice: scissors ✄\nComputer Choice: Scissors ✃\nIt's a draw!")
    else:
        print("Enter a valid input!")
    should_continue = input("Do you need to continue? (y/n): ").lower()
    if should_continue == "y":
        continue
    elif should_continue == "n":
        print("Thank you for playing")
        break


