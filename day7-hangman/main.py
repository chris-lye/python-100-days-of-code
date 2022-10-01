#Step 1 
import random
import hangman_words
import hangman_art

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
guessed = []
lives = 6
game_running = True

for letter in chosen_word:
    display.append("_")

while  game_running and lives >= 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print(f"{guess} has been guessed. Try again.")
        continue
    else:
        guessed.append(guess)
    for idx, letter in enumerate(chosen_word):
        if letter == guess:
            display[idx] = guess
        
    if guess not in chosen_word:
        print(f"You guessed {guess}. It's not in the word, you lose 1 life." )
        lives -= 1
        

    print(hangman_art.stages[lives])
    print(" ".join(display))

    print("\n")
    if "_" not in display:
        game_running = False
        print("You Win!")
    if lives < 1:
        game_running = False
        print("You Lose!")

    

