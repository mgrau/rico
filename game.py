from plantations import *
from barrels import *
from ships import *
from roles import *
from random import shuffle

class Game:
    def __init__(self):
        self.players = []
        
        self.turn = 0
        self.current_player = 0
        self.governor = 0

        self.points = 0
        self.roles = []

        self.quarries = []
        self.plantation_deck = []
        self.plantation_discard = []
        self.plantations = []

        self.colonists = 0
        self.colonist_ship = 0

        self.buildings = []

        self.goods = []

        self.trading_house = []

        self.ships = []

    def __repr__(self):
        return  "::Rico::\n"+\
            "turn: "+str(self.turn)+"\n"+\
            "points: "+str(self.points)+"\n"+\
            "colonists: "+str(self.colonists)+"\n"+\
            "colonist ship: "+str(self.colonist_ship)+"\n"+\
            "governor: "+self.players[self.governor].name+"\n"+\
            "current player: "+self.players[self.current_player].name+"\n"+\
            "plantations: "+str(self.plantations)+"\n"+\
            "trading house: "+str(self.trading_house)+"\n"+\
            "ships: "+str(self.ships)+"\n"+\
            "players: "+str(self.players)

    def setup(self):
        for player in self.players:
            player.reset()
        if len(self.players) not in range(2,5):
            print "wrong number of players"
            return
        elif len(self.players)==2:
            self.colonists = 42
            self.points = 65
            self.quarries = [Quarry() for i in range(5)]
            self.plantation_deck = [Corn() for i in range(6)]+[Indigo() for i in range(8)]+[Sugar() for i in  range(8)]+[Tobacco() for i in range(6)]+[Coffee() for i in range(5)]
            self.goods = [CornBarrel() for i in range(8)]+[IndigoBarrel() for i in range(9)]+[SugarBarrel() for i in range(9)]+[TobaccoBarrel() for i in range(7)]+[CoffeeBarrel() for i in range(7)]
            self.ships = [Ship(4),Ship(6)]
            self.roles = [Settler(),Mayor(),Builder(),Craftsman(),Trader(),Captain(),Prospector()]

            self.players[0].coins = 3
            self.players[0].plantations.append(Indigo())
            self.players[1].coins = 2
            self.players[1].plantations.append(Corn())
        elif len(self.players)==3:
            self.colonists = 58
            self.points = 75
            self.quarries = [Quarry() for i in range(8)]
            self.plantation_deck = [Corn() for i in range(9)]+[Indigo() for i in range(10)]+[Sugar() for i in range(11)]+[Tobacco() for i in range(9)]+[Coffee() for i in range(8)]
            self.goods = [CornBarrel() for i in range(10)]+[IndigoBarrel() for i in range(11)]+[SugarBarrel() for i in range(11)]+[TobaccoBarrel() for i in range(9)]+[CoffeeBarrel() for i in range(9)]
            self.ships = [Ship(4),Ship(5),Ship(6)]
            self.roles = [Settler(),Mayor(),Builder(),Craftsman(),Trader(),Captain()]

            self.players[0].coins = 2
            self.players[0].plantations.append(Indigo())
            self.players[1].coins = 2
            self.players[1].plantations.append(Indigo())
            self.players[2].coins = 1
            self.players[2].plantations.append(Corn())
        elif len(self.players)==4:
            self.colonists = 79
            self.points = 100
            self.quarries = [Quarry() for i in range(8)]
            self.plantation_deck = [Corn()for i in range(8)]+[Indigo() for i in range(10)]+[Sugar() for i in range(11)]+[Tobacco() for i in range(9)]+[Coffee() for i in range(8)]
            self.goods = [CornBarrel() for i in range(10)]+[IndigoBarrel() for i in range(11)]+[SugarBarrel() for i in range(11)]+[TobaccoBarrel() for i in range(9)]+[CoffeeBarrel() for i in range(9)]
            self.ships = [Ship(5),Ship(6),Ship(7)]
            self.roles = [Settler(),Mayor(),Builder(),Craftsman(),Trader(),Captain(),Prospector()]

            self.players[0].coins = 3
            self.players[0].plantations.append(Indigo())
            self.players[1].coins = 3
            self.players[1].plantations.append(Indigo())
            self.players[2].coins = 2
            self.players[2].plantations.append(Corn())
            self.players[3].coins = 2
            self.players[3].plantations.append(Corn())
        elif len(self.players)==5:
            self.colonists = 100
            self.points = 122
            self.quarries = [Quarry() for i in range(8)]
            self.plantation_deck = [Corn()for i in range(8)]+[Indigo() for i in range(9)]+[Sugar() for i in range(11)]+[Tobacco() for i in range(9)]+[Coffee() for i in range(8)]
            self.goods = [CornBarrel() for i in range(10)]+[IndigoBarrel() for i in range(11)]+[SugarBarrel() for i in range(11)]+[TobaccoBarrel() for i in range(9)]+[CoffeeBarrel() for i in range(9)]
            self.ships = [Ship(6),Ship(7),Ship(8)]
            self.roles = [Settler(),Mayor(),Builder(),Craftsman(),Trader(),Captain(),Prospector()]

            self.players[0].coins = 4
            self.players[0].plantations.append(Indigo())
            self.players[1].coins = 4
            self.players[1].plantations.append(Indigo())
            self.players[2].coins = 4
            self.players[2].plantations.append(Indigo())
            self.players[3].coins = 3
            self.players[3].plantations.append(Corn())
            self.players[4].coins = 3
            self.players[4].plantations.append(Corn())
        self.plantation_discard = []
        shuffle(self.plantation_deck)
        self.draw_plantations()
        self.fill_colonist_ship()
        self.get_buildings()

        self.turn = 1
        self.current_player = 0
        self.governor = 0

    def draw_plantations(self):
        self.plantation_discard += self.plantations
        self.plantations = []
        if len(self.plantation_deck)<len(self.players)+1:
            shuffle(self.plantation_discard)
            self.plantation_deck += self.plantation_discard
            self.plantation_discard = []
        for i in range(len(self.players)+1):
            self.plantations.append(self.plantation_deck.pop())

    def fill_colonist_ship(self):
        spots = 0
        for player in self.players:
            spots += player.open_buildings()
        self.colonist_ship = min(max(len(self.players),spots),self.colonists)
        self.colonists -= max(len(self.players),spots)
        # this is for the game end condition. The game only ends if there are not enough colonists to fill the colonist
        # ship. Thus, we allow self.colonists to go negative so we can see if the condition has been met. If it is
        # simply zero then the correct number of colonists were loaded onto the ship and we did not meet the condition.

    def get_buildings(self): # this is correct for 2-5 players, I haven't checked for 6
        self.buildings = [] # clear buildings
        # one small production building per player, with a maximum of 4
        for i in range(min(4,len(self.players))):
            self.buildings.append(SmallIndigoPlant())
            self.buildings.append(SmallSugarMill())
        # one production building per player, with a maximum of 3
        for i in range(min(3,len(self.players))):
            self.buildings.append(IndigoPlant())
            self.buildings.append(SugarMill())
            self.buildings.append(TobaccoStorage())
            self.buildings.append(CoffeeRoaster())
        # 2 violet buildings, but if there are 2 players, only one of each
        for i in range(min(2,len(self.players)-1)):
            self.buildings.append(SmallMarket())
            self.buildings.append(Hacienda())
            self.buildings.append(ConstructionHut())
            self.buildings.append(SmallWarehouse())
            self.buildings.append(Hospice())
            self.buildings.append(Office())
            self.buildings.append(LargeMarket())
            self.buildings.append(LargeWarehouse())
            self.buildings.append(University())
            self.buildings.append(Factory())
            self.buildings.append(Harbor())
            self.buildings.append(Wharf())
        # we always have 5 prestige buildings
        self.buildings.append(GuildHall())
        self.buildings.append(Residence())
        self.buildings.append(Fortress())
        self.buildings.append(CustomsHouse())
        self.buildings.append(CityHall())

    def can_anyone_ship(self):
        return any([self.can_player_ship(player) for player in self.players])

    def can_player_ship(self,player):
        if len(player.goods):
            for ship in self.ships+[player.wharf]:
                if not ship.full():
                    if not(len(ship.goods)):
                        return True
                    elif ship.goods[0] in player.goods:
                        return True
        return False

    def ship(self,ship,player,good):
        if ship.can_load(good) and good in player.goods and player.use_building(Harbor):
            player.points += 1
        while ship.can_load(good) and good in player.goods:
            player.goods.remove(good)
            ship.goods.append(good)
            player.points += 1
            self.points -= 1

    def round(self):
        # iterate through all players, beginning with the governor
        for player in self.players[self.governor:]+self.players[:self.governor]:
            self.current_player = player.index

            # enforce that choice is valid
            choice = -1
            while choice not in range(len(self.roles)):
                choice = player.choose_role(self)
            player.role = self.roles.pop(int(choice)) #give player the role card
            player.coins += player.role.coins # give player coins from role card
            player.role.coins = 0 # remove coins from role
            player.role(self) # execute actions associated with role
        # round is over, pass governor
        self.governor += 1
        if self.governor >= len(self.players):
            self.governor = 0
        # add bribes to those roles that were not chosen
        for role in self.roles:
            role.coins += 1
        # get chosen roles back from players
        for player in self.players:
            self.roles.append(player.role)
            player.role = Role() # fill player.role with the superclass (sort of like null?)
        self.roles.sort() # this is not strictly necessary, but matt likes to have them in order
        self.turn += 1 #increment turn
    
    def game_end(self):
        return self.points < 0 or (self.colonists < 0) or any([player.city_full() for player in self.players])