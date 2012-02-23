import random
from ai_player import AIPlayer
from engine.player import *


class Random_Player(AIPlayer):
    def choose_role(self, game):
        """
        Chooses a random role
        """
        return random.choice(xrange(len(game.roles)))

    def settler(self,game):
        """
        Chooses a random plantation
        """
        if (self.index==game.current_player or self.use_building(ConstructionHut)) and len(game.quarries):
            return random.choice(xrange(len(game.plantations)+1))
        else:
            return random.choice(xrange(len(game.plantations)))

    def mayor(self,game):
        self.distribute_colonists()
        return

    def builder(self,game):
        """
        Chooses a random building
        """
        choices = [-1]
        for i,building in enumerate(game.buildings):
            if self.afford_building(building) and not self.have_building(building.__class__) and i not in choices:
                choices.append(i)
        return random.choice(choices)

    def craftsman(self,game):
        """
        Choose a random good
        """
        return random.choice(self.produce_goods())

    def trader(self,game):
        """
        Choose a random good to sell
        """
        return random.choice(self.goods)


    def captain(self,game):
        choices = []
        for ship in game.ships:
            for good in self.goods:
                if (ship,good) not in choices and ship.can_load(good) and not any([good in othership.goods for othership in filter(lambda x:x!=ship,game.ships)]):
                    choices.append((ship,good))
        if self.use_building(Wharf) and not self.wharf.full():
            for good in self.goods:
                if (self.wharf,good) not in choices and self.wharf.can_load(good) and not any([good in othership.goods for othership in game.ships]):
                    choices.append((self.wharf,good))
        return random.choice(choices)

    def rot(self,game):
        return [random.choice(self.goods)]