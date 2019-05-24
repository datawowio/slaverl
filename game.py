from components.deck import Deck
from components.player import Player
from components.table import Table


table = Table(players=[Player(player_id=i) for i in range(4)])
deck = Deck().shuffle()

while not deck.is_empty():
    for p in table.players:
        p.draw_card(deck)
