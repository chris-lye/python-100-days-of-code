############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

## imports
import random
import art
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_continue = True

def deal_card():
    return random.choice(cards)

def calculate_score(cards: list):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    elif sum(cards) == 21:
        return 0
    while 11 in cards:
        if sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)

def game_over(player_score, computer_score):
    if player_score == 0 and computer_score == 0:
        return True
    elif player_score == 0:
        return True
    elif computer_score == 0:
        return True
    elif player_score > 21:
        return True
    else:
        return False

def compare(user_score, com_score):
    if user_score == com_score:
        return "Draw"
    elif com_score == 0:
        return "Computer Blackjack, you Lose."
    elif user_score == 0:
        return "You got Blackjack, you Win."
    elif user_score > 21:
        return "You went over 21, you Lose."
    elif com_score > 21:
        return "Computer went over 21, you Win."
    elif user_score > com_score:
        return "You Win!"
    else:
        return "You Lose!"  

def print_cards(hand, com_hand):
    print(f"""
    Your cards: {hand}, current score: {calculate_score(hand)}
    Computer's first card: {com_hand[0]}
    """)

play_on = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while game_continue:
    if play_on == 'y':
        game_continue = True
    else:
        break

    print(art.logo)

    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    print_cards(player_hand, computer_hand)
    

    # player draw stage
    if (game_over(player_score, computer_score) == False):
        player_draw_stage = True
        while player_draw_stage:
            draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw == "y":
                player_hand.append(deal_card())
                player_draw_stage = not game_over(calculate_score(player_hand), calculate_score(computer_hand))
                print_cards(player_hand, computer_hand)
            else:
                player_draw_stage = False
    # computer draw stage
    if game_over(calculate_score(player_hand), calculate_score(computer_hand)) == False:
        while calculate_score(computer_hand) < 17:
            computer_hand.append(deal_card())

    # print outcome
    user_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)
    print(f"""
    Your final hand: {player_hand}, final score: {user_score}
    Computer's final hand: {computer_hand}, final score: {computer_score}
    {compare(user_score, computer_score)}
    """)

    play_on = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    if play_on == "y":
        os.system('cls')

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

