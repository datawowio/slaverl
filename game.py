from components.player import Player
from components.table import Table


class Game(object):
    def __init__(self):
        self.table = Table(players=[Player(player_id=i) for i in range(4)])

    def play_match(self):
        self.table.reset_for_next_round()
        while not self.is_match_ended():
            self.play_round()

    def play_round(self):
        pass

    def is_round_end(self):
        def can_play(player):
            return not player.has_won() and not player.is_passing()

        return sum(1 for p in self.table.players if can_play(p)) == 1

    def is_match_ended(self):
        return sum(1 for p in self.table.players if not p.has_won()) == 1


game = Game()
game.play_match()
