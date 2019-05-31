from components.player import Player
from components.table import Table


class Game(object):
    def __init__(self, num_players):
        self.table = Table(
            players=[Player(player_id=i) for i in range(num_players)])

    def play_match(self):
        self.table.reset_for_next_round()
        while not self.is_match_ended():
            self.play_round()

    def play_round(self):
        pass

    def is_round_ended(self):
        return sum(1 for p in self.table.players if p.need_action()) == 1

    def is_match_ended(self):
        return sum(1 for p in self.table.players if not p.has_won()) == 1


game = Game(num_players=4)
game.play_match()
