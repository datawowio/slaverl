class Player:
    def __init__(self, player_id=None):
        self.cards = []
        self.won_place = None
        self.title = None
        self.player_id = player_id
        self.is_passing = False

    def draw_card(self, deck):
        self.cards.append(deck.draw())

    def has_won(self):
        return len(self.cards) == 0

    def __repr__(self):
        return f"player[id={self.player_id}]"
