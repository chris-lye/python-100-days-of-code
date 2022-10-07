import art
import game_data
import random
import os

data = game_data.data
data_length = len(data)
score = 0
# def useful functions
def make_text(account):
  return f"{account['name']}, {account['description']}, from {account['country']}. "

choice1 = random.randint(0, len(data)-1)
first_acc = data.pop(choice1)

# start game
game_cont = True
while game_cont:
  print(art.logo)

  
  
  choice2 = random.randint(0, len(data)-1)
  second_acc = data.pop(choice2)

  # Compare text
  print(f"Compare A: {make_text(first_acc)}")
  print(art.vs)
  print(f"Against B: {make_text(second_acc)}")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  os.system("cls")
  if answer == 'a' and (first_acc['follower_count'] > second_acc['follower_count']):
    # answer is correct
    score += 1
    print(f"You're right! Current score: {score}")
  elif answer == 'b' and (first_acc['follower_count'] > second_acc['follower_count']):
    # answer is correct
    score += 1
    print(f"You're right! Current score: {score}")
    first_acc = second_acc
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    break
  
  
