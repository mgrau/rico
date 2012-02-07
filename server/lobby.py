from __future__ import division

class Lobby(object):
    def __init__(self):
        self.player_list = set()

    def add_player(self, player):
        self.player_list.add(player)

    def remove_player(self, player):
        try:
            self.player_list.remove(player)
        except KeyError:
            pass