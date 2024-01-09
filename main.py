import random

original_deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# creating a new deck with 52 cards at the start of each game
deck = []
for i in range(4):
    deck.extend(original_deck)

print(len(deck))
computer_cards = []
player_cards = []

for i in range(2):
    card = random.choice(deck)
    computer_cards.append(card)
    deck.remove(card)

card = random.choice(deck)
player_cards.append(card)

