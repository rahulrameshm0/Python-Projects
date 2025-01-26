import random
import art
print(art.art)
print("Let me think of a number between 1 to 50")
level = input("Choose the level of difficulty..'easy' or 'hard': ")
max_attempt = 10 if level == "easy" else 5
computer_choice = random.randint(1, 50)

print(f"You have {max_attempt} attempts to guess the number!")


for i in range(max_attempt):
    guessed_number = int(input("Make a guess: "))
    if guessed_number > 50:
        print("Please guess the number between 1 to 50.")
    elif guessed_number > computer_choice:
        print("The number is to high")
    elif guessed_number < computer_choice:
        print("The number is too low")
    else:
        print(f"You win! the number was {computer_choice}")
        break
    max_left = max_attempt - i - 1
    if max_left > 0:
        print(f"You have {max_left} attempt to guess the number")
    else:
        print(f"You lose!, you have entered the maximum number")
