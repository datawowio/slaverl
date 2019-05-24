class Player:
    def __init__(self):
        self.cards = []
        self.won_place = None
        self.title = None

    def draw_card(self, deck):
        self.cards.append(deck.draw())

    def is_finished(self):
        return len(self.cards) == 0
