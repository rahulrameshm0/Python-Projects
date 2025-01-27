import random
while True:
    user_input = input("Roll the dice? (y/n): ")
    random_number1 = random.randint(1,15)
    random_number2 = random.randint(1,15)
    if user_input == "y":
        print(f"({random_number1}, {random_number2})")
        continue
    elif user_input == "n":
        print("Thank you for playing!")
        break
    else:
        print("invalid choice!")
