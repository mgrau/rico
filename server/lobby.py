from __future__ import division

class Lobby(object):
    def __init__(self):
        self.player_list = set()
        self.chat_msgs = []

    def add_player(self, player):
        self.player_list.add(player)

    def remove_player(self, player):
        try:
            self.player_list.remove(player)
        except KeyError:
            pass

    def new_chat_msg(self, user, msg):
        self.chat_msgs.append((user, msg))