from __future__ import division
import random
import collections
from player import *


class AIPlayer(Player):
    pass

class RandomPlayer(AIPlayer):
    def choose_role(self, game):
        """
        Chooses a random role
        """
        n_roles = len(game.roles)
        role_idx = random.choice(xrange(n_roles)) #todo: ensure only a valid (ie previously un-chosen) role is chosen
        return role_idx

    # todo: the construction of valid choice sets at various decision points should be refactored out of human_player and into player.py since it is common to human and AI players
    def builder(self,game):
        choice_set = collections.defaultdict(lambda: [])
        for idx, building in enumerate(game.buildings):
            if self.afford_building(building) and (not self.have_building(building.__class__)):
                choice_set[building.__class__].append(idx)
        building_class = random.choice(choice_set.keys())
        building_idx = choice_set[building_class][0]
        return building_idx

    def settler(self, game):
        p = list(game.plantations)
        if self.index==game.current_player or self.use_building(ConstructionHut):
            p.append(Quarry()) #am i handling quarry correctly?
        return random.choice(xrange(len(p)))





class TreeSearchPlayer(AIPlayer):
    # Implements minimax Markov Tree Search
    pass



