import random
from cards import *
from game import *


original_deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
usual_menu = "Enter your option with its corresponding number:\n1. Stand\n2. Hit\n"
play_again_menu = "Do you want to play again?\n1. Yes\n2. No\n"

# Hoping to add these features at a later time
# split_menu = "Enter your option with its corresponding number:\n1. Stand\n2. Hit\n3. Split\n"
# double_menu = "Enter your option with its corresponding number:\n1. Stand\n2. Hit\n3. Double Down\n"
# both_menu = "Enter your option with its corresponding number:\n1. Stand\n2. Hit\n3. Double Down\n4. Split\n"

continue_playing = True
while continue_playing:
    # creating a new deck with 52 cards at the start of each game
    deck = []
    for i in range(6):
        deck.extend(original_deck)

    # make new instance of a game
    current_game = Game(deck)

    print(f"The computer's first card is {current_game.computer_cards[0]}.")

    iterating_menu = True
    if current_game.computer_total > 21:
        print("The computer bust!")
        iterating_menu = False

    while iterating_menu:
        if current_game.player_total == 21:
            print("You got lucky! Your total is 21.")
            break
        else:
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
                print(f"Oh no! You've lost. Your total is {current_game.player_total}.")
                iterating_menu = False
            elif current_game.player_total == 21 and current_game.computer_total == 21:
                print("Uh oh! Standoff with 21 with dealer")
                iterating_menu = False
            elif current_game.player_total == 21:
                print("You've won! 21 total!")
                iterating_menu = False
        else:
            if current_game.computer_total > current_game.player_total:
                print("Computer won the round!")
                iterating_menu = False
            elif current_game.computer_total == current_game.player_total:
                print("Stand-off! There was a draw.")
                iterating_menu = False
            else:
                print("You've won the round!")
                iterating_menu = False

    print(f"The computer's cards were {current_game.print_card_string('computer')}, and its total was {current_game.computer_total}.")
    answer = ""
    while True:
        answer = input(play_again_menu)
        if answer != '1' and answer != '2':
            print("Invalid input!")
        else:
            break
    if answer == "1":
        print("Yay!\n")
    else:
        print("Have a good day!\n")
        continue_playing = False
