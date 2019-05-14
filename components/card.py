class Card:
    suits = {'Spades': '♠', 'Hearts': '♡', 'Diamonds': '♢', 'Clubs': '♣'}
    suit_values = {'Spades': 4, 'Hearts': 3, 'Diamonds': 2, 'Clubs': 1}
    values = list(map(str, range(3, 11))) + [*'JQKA2']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.value + self.suits[self.suit]

    def ordering_number(self):
        return self.values.index(self.value) * 10 + self.suit_values[self.suit]
