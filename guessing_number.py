import random
count = 10
while 0 < count:
    try:
        user_input = int(input("Enter a number: "))
        random_number = random.randint(1, 100)
        if user_input > random_number:
            count -= 1
            if count == 0:
                print("You lose!")
            else:
                print(f"Try again. too high!, you have {count} attempts left!")
        elif user_input < random_number:
            count -= 1
            if count == 0:
                print("You lose!")
            else:
                print(f"Try again. too low!, you have {count} attempts left!")
        else:
            print("Congratulation, you guessed the right number!")
            break

    except ValueError:
        print("Enter a valid number!")

