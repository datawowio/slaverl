class Player:
    def __init__(self):
        self.cards = []

    def draw_card(self, deck):
        self.cards.append(deck.draw())
