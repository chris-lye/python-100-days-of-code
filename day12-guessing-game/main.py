import art
import random

def print_lives():
    print(f"You have {lives} attempts remaining to guess the number.")

# instantiate global variables
lives = 0
answer = random.randint(1, 100)
game_cont = True

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {answer}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    lives = 10
else:
    lives = 5



while game_cont:
    print_lives()
    if lives <= 0:
        print("You Lose!")
        break
    guess = int(input("Make a guess: "))

    if guess == answer:
        print("You win!")
        break
    elif guess < answer:
        print("Too low.\nGuess again.")
        lives -= 1
    else:
        print("Too high.\nGuess again.")
        lives -= 1
    print("----------")


    
