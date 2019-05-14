import random

from .card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = Card.suits.keys()
        values = Card.values
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def draw(self):
        return self.cards.pop(0)

    def __repr__(self):
        return str(self.cards)

    def is_empty(self):
        return not bool(self.cards)
