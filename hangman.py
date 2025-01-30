import random
words = ["python", "java", "javascript", "c++", "c", "html", "css"]
chosen_word = random.choice(words)
words_display = ['_' for _ in chosen_word]
attempt = 8
while attempt > 0 and '_' in words_display:
    print("\n" + ' '.join(words_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                words_display[index] = guess
    else:
        print("The letter does do not appear in the word!")
        attempt -= 1
if '_' not in words_display:
    print('You guessed the word correctly!')
    print(' '.join(words_display))
    print("You Win!")
else:
    print(f"You lose!, the word was {chosen_word}")