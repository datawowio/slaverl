from components.deck import Deck
from components.player import Player
from components.table import Table


table = Table(players=[Player() for _ in range(4)])
deck = Deck()

while not deck.is_empty():
    for p in table.players:
        p.draw_card(deck)
