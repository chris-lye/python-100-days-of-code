import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_img = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice < 0  or player_choice >= 3:
    print("Invalid number, you lose!")
else:
    print(game_img[player_choice])

    computer_choice = random.randint(0,2)

    print("Computer chooses:" )

    print(game_img[computer_choice])

    choice_list = [player_choice, computer_choice]

    if player_choice == computer_choice:
        print("Draw!")
    elif choice_list == [0,1] or choice_list == [1,2] or choice_list == [2,0]:
        print("You Lose!")
    elif choice_list == [0,2] or choice_list == [1,0] or choice_list == [2,1]:
        print("You Win!")

