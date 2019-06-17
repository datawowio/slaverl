from components.player import Player
from components.table import Table


def action_function(game_state, possible_actions, player):
    # TODO: Placeholder function to interact with environment
    return possible_actions[0]



class Game(object):
    def __init__(self, num_players):
        self.table = Table(
            players=[Player(player_id=i) for i in range(num_players)])

    def play_match(self):
        self.table.reset_for_next_round()
        while not self.is_match_ended():
            self.play_round()

        self.table.reset_for_next_match()

    def play_round(self):
        current_player = self.table.get_current_player()
        while not self.is_round_ended():
            while True:
                # TODO: Get action from user injected function
                action = action_function(game_state=self.state,
                                         possible_actions=[],
                                         player=current_player)
                # TODO: Interact to the enviroment with the action acquired

            current_player = self.table.next_player()

        # TODO: Check if it has to reverse the direction. Then set current
        # player to the correct one

        self.table.reset_for_next_round()

    def is_round_ended(self):
        return sum(1 for p in self.table.players if p.need_action()) == 1

    def is_match_ended(self):
        return sum(1 for p in self.table.players if not p.has_won()) == 1

    def is_action_valid(self, action):
        return True


game = Game(num_players=4)
game.play_match()
