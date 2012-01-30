from __future__ import division
import random
from player import *


class AIPlayer(Player):
    pass

class RandomPlayer(AIPlayer):
    def choose_role(self, game):
        """
        Chooses a random role
        """
        n_roles = len(game.roles)
        role_idx = random.randint(0, n_roles-1) #todo: ensure only a valid (ie previously un-chosen) role is chosen
        return role_idx

class TreeSearchPlayer(AIPlayer):
    # Implements minimax Markov Tree Search
    pass



