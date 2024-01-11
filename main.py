import random
from cards import *
from game import *

original_deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
usual_menu = "Enter your option with its corresponding number:\n1. Stand\n2. Hit\n"
split_menu = "Enter your option with its corresponding number:\n1. Stand\n2. Hit\n3. Split\n"
double_menu = "Enter your option with its corresponding number:\n1. Stand\n2. Hit\n3. Double Down\n"
both_menu = "Enter your option with its corresponding number:\n1. Stand\n2. Hit\n3. Double Down\n4. Split\n"
# creating a new deck with 52 cards at the start of each game
deck = []
for i in range(4):
    deck.extend(original_deck)

# make new instance of a game
current_game = Game(deck)

print(current_game.computer_cards)
print(current_game.computer_total)
print(current_game.player_cards)

print(f"The computer's first card is {current_game.computer_cards[0]}.")


round_continues = True
while round_continues:
    print(f"Your cards are {current_game.print_card_string('player')}. Your total is {current_game.player_total}.")
    choice = ""
    while True:
        choice = input(usual_menu)
        if choice != '1' and choice != '2':
            print("Invalid input!")
        else:
            break
    if choice == '2':
        current_game.hit()
        if current_game.player_total > 21:
            print(f"Oh no! You've lost. Your total is {current_game.player_total}")
            round_continues = False
        elif current_game.player_total == 21 and current_game.computer_total == 21:
            print("Uh oh! Standoff with 21 with dealer")
            round_continues = False
        elif current_game.player_total == 21:
            print("You've won! 21 total!")
            round_continues = False
    else:
        if current_game.computer_total > 21:
            print("You've won the round!")
        elif current_game.computer_total > current_game.player_total:
            print("Computer won the round!")
        elif current_game.computer_total == current_game.player_total:
            print("Stand-off!")
        else:
            print("You've won the round!")
        round_continues = False

