class Table:
    direction_diff_value = {'cw': 1, 'ccw': -1}

    def __init__(self, players, direction='cw', current_player_index=0):
        self.players = players
        self.direction = direction
        self.current_player_index = current_player_index

    def next_player(self):
        self.current_player_index += self.direction_diff_value[self.direction]
        self.current_player_index += len(self.players)
        self.current_player_index %= len(self.players)
        return self.current_player()

    def get_current_player(self):
        return self.players[self.current_player_index]

    def reverse_direction(self):
        self.direction = 'ccw' if self.direction == 'cw' else 'cw'

    def get_player_by(self, title):
        player = None
        player = next((p for p in self.players if p.title == title), None)
        return player
