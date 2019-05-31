from .card import Card


class Player(object):
    def __init__(self, player_id=None, title=None):
        self.title = title
        self.player_id = player_id
        self.cards = []
        self.won_place = None
        self.is_passing = False

    def draw_card(self, deck):
        self.cards.append(deck.draw())

    def has_won(self):
        return len(self.cards) == 0

    def reset_for_next_round(self):
        self.is_passing = False
        self.won_place = False
        self.cards = []

    def has_the_smallest_card(self):
        for card in self.cards:
            if card == Card(suit='club', rank='3'):
                return True
        return False

    def need_action(self):
        return not self.has_won() and not self.is_passing()

    def __repr__(self):
        return f"player[id={self.player_id}]"
