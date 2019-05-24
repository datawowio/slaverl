from functools import total_ordering


@total_ordering
class Card:
    suits = {'Spades': '♠', 'Hearts': '♡', 'Diamonds': '♢', 'Clubs': '♣'}
    suit_values = {'Spades': 4, 'Hearts': 3, 'Diamonds': 2, 'Clubs': 1}
    ranks = list(map(str, range(3, 11))) + [*'JQKA2']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.rank + self.suits[self.suit]

    def ordering_number(self):
        return self.ranks.index(self.rank) * 10 + self.suit_values[self.suit]

    def __lt__(self, other):
        return self.ordering_number() < other.ordering_number()

    def __eq__(self, other):
        return self.ordering_number() == other.ordering_number()
