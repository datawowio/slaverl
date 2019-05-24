from functools import total_ordering


@total_ordering
class Card(object):
    suits = {'spade': '♠', 'heart': '♡', 'diamond': '♢', 'club': '♣'}
    suit_values = {'spade': 4, 'heart': 3, 'diamond': 2, 'club': 1}
    ranks = list(map(str, range(3, 11))) + [*'JQKA2']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.rank + self.suits[self.suit]

    def __lt__(self, other):
        return self._value() < other._value()

    def __eq__(self, other):
        return self._value() == other._value()

    def _value(self):
        return self.ranks.index(self.rank) * 10 + self.suit_values[self.suit]

    @staticmethod
    def superior_hand(hand1, hand2):
        if len(hand1) != len(hand2):
            if len(hand1) != len(hand2) + 2 and len(hand1) + 2 != len(hand2):
                raise InvalidComparisonException

        if not Card.valid_hand(hand1) or not Card.valid_hand(hand2):
            raise InvalidHandException

        if len(hand1) > len(hand2):
            return True

        max_hand1 = max(hand1, key=lambda h: h._value())
        max_hand2 = max(hand2, key=lambda h: h._value())
        return max_hand1 > max_hand2

    @staticmethod
    def valid_hand(hand):
        for card in hand:
            print(card)
            if card.rank != hand[0].rank:
                return False
        return True


class InvalidComparisonException(BaseException):
    """"Raised when compare 2 different kinds"""


class InvalidHandException(BaseException):
    """"Raised when compare 2 different kinds"""
