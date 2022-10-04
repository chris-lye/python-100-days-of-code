# from replit import clear
import os
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

auction_cont = True
bidders = {}
while auction_cont:
    name = input("What is your name?\n")
    bid = int(input("What is your bid amount?\n"))
    bidders[name] = bid

    cont = input("Any more bidders? (y/n)\n").lower()

    if cont == "y":
        # clear for windows. for linux/mac use os.system('clear')
        os.system('cls')
    else:
        auction_cont = False
        os.system('cls')
     
print("Auction is over!\n")
max_key = ""
max_value = 0
for key, value in bidders.items():
    if value > max_value:
        max_value = value
        max_key = key

print(f"The winner of the bid is {max_key}")