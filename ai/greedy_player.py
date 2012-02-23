import random
from engine.player import *


class Greedy_Player(Player):
    def can_trade(self,game):
        if len(game.trading_house)>=4:
            return False
        for good in self.goods:
            if good not in game.trading_house or self.use_building(Office):
                return True
        return False

    def buy_building(self,game,wanted):
        b = wanted()
        if self.afford_building(b):
            for i,building in enumerate(game.buildings):
                if isinstance(building,wanted):
                    return i
        return None

    def distribute_colonists(self):
        for building in self.buildings:
            if building.colonists < building.capacity and self.san_juan>0 and isinstance(building,VioletBuilding):
                diff = min(self.san_juan,building.capacity-building.colonists)
                building.colonists += diff
                self.san_juan -= diff
        for plantation in self.plantations:
            if plantation.colonists<1 and self.san_juan>0:
                plantation.colonists = 1
                self.san_juan -= 1
        for building in self.buildings:
            if building.colonists < building.capacity and self.san_juan>0 and isinstance(building,ProductionBuilding):
                diff = min(self.san_juan,building.capacity-building.colonists)
                building.colonists += diff
                self.san_juan -= diff
    def choose_role(self, game):
        """
        Chooses a random role
        """
        roles = []
        for i,role in enumerate(game.roles):
            if role.coins:
                if isinstance(role,Settler):
                    if len(self.plantations)<12:
                        roles.append(i)
                if isinstance(role,Mayor):
                    if self.open_spots():
                        roles.append(i)
                if isinstance(role,Builder):
                    if True:
                        roles.append(i)
                if isinstance(role,Craftsman):
                    if True:
                        roles.append(i)
                if isinstance(role,Trader):
                    if self.can_trade(game):
                        roles.append(i)
                if isinstance(role,Captain):
                    if game.can_player_ship(self):
                        roles.append(i)
                if isinstance(role,Prospector):
                    if True:
                        roles.append(i)
        if len(roles):
            return random.choice(roles)
        for i,role in enumerate(game.roles):
            if role.coins:
                roles.append(i)
        if len(roles):
            return random.choice(roles)
        for i,role in enumerate(game.roles):
            if isinstance(role,Settler):
                if len(self.plantations)<12:
                    roles.append(i)
            if isinstance(role,Mayor):
                if self.open_spots():
                    roles.append(i)
            if isinstance(role,Builder):
                if True:
                    roles.append(i)
            if isinstance(role,Craftsman):
                if False:
                    roles.append(i)
            if isinstance(role,Trader):
                if self.can_trade(game):
                    roles.append(i)
            if isinstance(role,Captain):
                if game.can_player_ship(self):
                    roles.append(i)
            if isinstance(role,Prospector):
                if False:
                    roles.append(i)
        if len(roles):
            return random.choice(roles)
        for i,role in enumerate(game.roles):
            if isinstance(role,Prospector):
                return i
        return random.choice(xrange(len(game.roles)))

    def settler(self,game):
        """
        Choose a quarry if we can get one, otherwise, choose corn, or random
        """
        if (self.index==game.current_player or self.use_building(ConstructionHut)) and len(game.quarries) and not Quarry() in self.plantations:
            return len(game.plantations)
        for i,plantation in enumerate(game.plantations):
            if isinstance(plantation,Corn):
                return i
        return random.choice(xrange(len(game.plantations)))

    def mayor(self,game):
        self.distribute_colonists()
        return

    def builder(self,game):
        """
        Chooses a random building
        """
        if self.have_plantation(Coffee) and not self.have_building(CoffeeRoaster):
            choice = self.buy_building(game,CoffeeRoaster)
            if choice is not None:
                return choice

        if self.have_plantation(Tobacco) and not self.have_building(TobaccoStorage):
            choice = self.buy_building(game,TobaccoStorage)
            if choice is not None:
                return choice

        if self.have_plantation(Sugar) and not self.have_building(SugarMill):
            choice = self.buy_building(game,SugarMill)
            if choice is not None:
                return choice

        if self.have_plantation(Sugar) and not self.have_building(SmallSugarMill) and not self.have_building(SugarMill):
            choice = self.buy_building(game,SmallSugarMill)
            if choice is not None:
                return choice

        if self.have_plantation(Indigo) and not self.have_building(SmallIndigoPlant):
            choice = self.buy_building(game,SmallIndigoPlant)
            if choice is not None:
                return choice

        if self.have_plantation(Indigo) and not self.have_building(IndigoPlant) and not self.have_building(SmallIndigoPlant):
            choice = self.buy_building(game,IndigoPlant)
            if choice is not None:
                return choice

        if not self.have_building(Harbor):
            choice = self.buy_building(game,Harbor)
            if choice is not None:
                return choice

        if not self.have_building(Factory):
            choice = self.buy_building(game,Factory)
            if choice is not None:
                return choice

        if not self.have_building(Wharf):
            choice = self.buy_building(game,Wharf)
            if choice is not None:
                return choice

        if not self.have_building(SmallMarket):
            choice = self.buy_building(game,SmallMarket)
            if choice is not None:
                return choice

        choices = [-1]
        for i,building in enumerate(game.buildings):
            if self.afford_building(building) and not self.have_building(building.__class__) and i not in choices:
                choices.append(i)
        return random.choice(choices)

    def craftsman(self,game):
        """
        Choose a random good
        """
        goods = self.produce_goods()
        goods.sort()
        if self.use_building(Office):
            return goods[0]
        for good in goods:
            if good not in game.trading_house:
                return good
        return random.choice(self.goods)

    def trader(self,game):
        """
        Sell most valuable good not in trading house
        if we have an office, use that
        """
        self.goods.sort()
        if self.use_building(Office):
            return self.goods[0]
        for good in self.goods:
            if good not in game.trading_house:
                return good
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
        self.goods.sort()
        if self.use_building(Office):
            return [self.goods[0]]
        for good in self.goods:
            if good not in game.trading_house:
                return [good]
        return [random.choice(self.goods)]