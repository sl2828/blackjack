import random
from cards import *


class Game:
    def __init__(self, deck):
        # deck for this instance of game
        self.deck = deck
        # to give the computer/dealer its cards, following the "17 rule"
        self.computer_cards = []
        self.computer_total = 0
        while self.computer_total < 17:
            card = random.choice(self.deck)
            self.computer_cards.append(card)
            self.deck.remove(card)
            self.computer_total += card_value(card)
        # recalculate total if there's computer total is a bust if Ace is counted as 11
        if 'A' in self.computer_cards and self.computer_total > 21:
            self.computer_total = self.computer_total - 10

        # to give the player their first two cards
        self.player_cards = []
        self.player_total = 0
        for i in range(2):
            card = random.choice(self.deck)
            self.player_cards.append(card)
            self.deck.remove(card)
            self.player_total += card_value(card)

    def print_card_string(self, who):
        self_cards = self.player_cards
        if who == "computer":
            self_cards = self.computer_cards
        if len(self_cards) == 1:
            return self_cards[0]
        elif len(self_cards) == 2:
            return self_cards[0] + " and " + self_cards[1]
        else:
            string = ""
            for i in range(len(self_cards)):
                if i == len(self_cards) - 1:
                    string += "and " + self_cards[i]
                else:
                    string += self_cards[i] + ", "
            return string

    def hit(self):
        card = random.choice(self.deck)
        print(f"You drew a {card}.")
        self.player_cards.append(card)
        self.deck.remove(card)
        self.player_total += card_value(card)
        if self.player_total > 21 and 'A' in self.player_cards:
            self.player_total -= 10
