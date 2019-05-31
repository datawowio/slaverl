from .deck import Deck


class Table(object):
    direction_diff_value = {'cw': 1, 'ccw': -1}

    def __init__(self, players, direction='cw', current_player_index=0):
        self.players = players
        self.direction = direction
        self.current_player_index = current_player_index
        self.reset_for_next_match()

    def next_player(self):
        self.current_player_index += self.direction_diff_value[self.direction]
        self.current_player_index += len(self.players)
        self.current_player_index %= len(self.players)
        return self.get_current_player()

    def get_current_player(self):
        return self.players[self.current_player_index]

    def set_current_player(self, player):
        # print(f"{player} {player.title}")
        # print(f"----")
        self.current_player_index = self.players.index(player)

    def reverse_direction(self):
        self.direction = 'ccw' if self.direction == 'cw' else 'cw'

    def get_player_by_title(self, title):
        return next((p for p in self.players if p.title == title), None)

    def get_player_with_the_smallest_card(self):
        return next((p for p in self.players if p.has_the_smallest_card), None)

    def _get_distance_to_the_king(self):
        for i in range(len(self.players)):
            if self.get_current_player() == self.get_player_by_title('king'):
                distance = i
            self.next_player()
        return distance

    def reset_for_next_round(self):
        for player in self.players:
            player.reset_for_next_round()

    def reset_for_next_match(self):
        deck = Deck().shuffle()

        for player in self.players:
            player.reset_for_next_match()

        slave = self.get_player_by_title('slave')
        if slave:
            self.set_current_player(slave)
            distance_to_king = self._get_distance_to_the_king()
            print(f"dis {distance_to_king}")
            if distance_to_king > len(self.players) / 2:
                self.direction = 'cw'
            if distance_to_king < len(self.players) / 2:
                self.direction = 'ccw'

        while not deck.is_empty():
            self.get_current_player().draw_card(deck)
            self.next_player()

        if slave:
            self.set_current_player(slave)
        else:
            self.set_current_player(self.get_player_with_the_smallest_card())
