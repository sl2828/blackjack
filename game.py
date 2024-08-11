import random
from cards import *


class Game:
    def __init__(self, deck):
        """initializes the game by drawing cards for computer and the first two cards for the player"""
        # deck for this instance of game
        self.deck = deck
        # to give the computer/dealer its cards, following the "17 rule"
        self.computer_cards = []
        self.computer_total = 0
        computer_ace_1 = 0
        while self.computer_total < 17:
            card = random.choice(self.deck)
            self.computer_cards.append(card)
            self.deck.remove(card)
            self.computer_total += card_value(card)
            # recalculate total if there's computer total is a bust if an Ace is counted as 11
            if self.computer_cards.count('A') > computer_ace_1 and self.computer_total > 21:
                self.computer_total = self.computer_total - 10
                computer_ace_1 += 1

        # to give the player their first two cards
        self.player_cards = []
        self.player_total = 0
        self.player_ace_1 = 0
        for i in range(2):
            card = random.choice(self.deck)
            self.player_cards.append(card)
            self.deck.remove(card)
            self.player_total += card_value(card)

    def print_card_string(self, who):
        """Helps print out the list of cards for the player to see"""
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
        """Series of events that happen when users decide to hit"""
        card = random.choice(self.deck)
        print(f"You drew a {card}.")
        self.player_cards.append(card)
        self.deck.remove(card)
        self.player_total += card_value(card)
        if self.player_cards.count('A') > self.player_ace_1 and self.player_total > 21:
            self.player_total = self.player_total - 10
            self.player_ace_1 += 1
