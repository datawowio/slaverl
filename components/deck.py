import random

from .card import Card


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = Card.suits.keys()
        ranks = Card.ranks
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def draw(self):
        return self.cards.pop(0)

    def __repr__(self):
        return str(self.cards)

    def is_empty(self):
        return len(self.cards) == 0
