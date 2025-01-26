import random
import stages
fruit_list = ['apple', 'orange', 'mango', 'grapes', 'banana']
lives = 6
choice_list = random.choice(fruit_list)
#print(choice_list)
display = []

for letter in fruit_list:
    display += '_'
print(display)

game_over = False
while not game_over:
    guessed_letter = input("guess a letter: ").lower()
    for i in range(len(choice_list)):
        letter = choice_list[i]
        if letter == guessed_letter:
            display[i] = guessed_letter
    print(display)
    if guessed_letter not in choice_list:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose")
    if '_' not in display:
        game_over = True
        print('You Win!!')

    print(stages.stages[lives])