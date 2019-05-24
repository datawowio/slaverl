from components.player import Player
from components.table import Table


class Game(object):
    def __init__(self):
        self.table = Table(players=[Player(player_id=i) for i in range(4)])

    def play_round(self):
        self.table.reset_for_next_round()
        for p in self.table.players:
            print(f"{p}{p.cards} {p.title}")


game = Game()
game.play_round()
