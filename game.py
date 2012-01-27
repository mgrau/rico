from player import *
from plantations import *
from buildings import *
from barrels import *
from ships import *
from roles import *
from UI import *
from random import shuffle

class Game:
    def __init__(self,player_names=[""]):
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

        self.UI = TextUI() #todo: make this configurable

    def __repr__(self):
            return  "::Rico::\n"+\
                "turn: "+str(self.turn)+"\n"+\
                "points: "+str(self.points)+"\n"+\
                "colonists: "+str(self.colonists)+"\n"+\
                "governor: "+self.players[self.governor].name+"\n"+\
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
            self.quarries = 5*[Quarry()]
            self.plantation_deck = 6*[Corn()]+8*[Indigo()]+8*[Sugar()]+6*[Tobacco()]+5*[Coffee()]
            self.goods = 8*[CornBarrel()]+9*[IndigoBarrel()]+9*[SugarBarrel()]+7*[TobaccoBarrel()]+7*[CoffeeBarrel()]
            self.ships = [Ship(4),Ship(6)]
            self.roles = [Settler(),Mayor(),Builder(),Craftsman(),Trader(),Captain(),Prospector()]

            self.players[0].coins = 3
            self.players[0].plantations.append(Indigo())
            self.players[1].coins = 2
            self.players[1].plantations.append(Corn())

        elif len(self.players)==3:
            self.colonists = 58
            self.points = 75
            self.quarries = 8*[Quarry()]
            self.plantation_deck = 9*[Corn()]+10*[Indigo()]+11*[Sugar()]+9*[Tobacco()]+8*[Coffee()]
            self.goods = 10*[CornBarrel()]+11*[IndigoBarrel()]+11*[SugarBarrel()]+9*[TobaccoBarrel()]+9*[CoffeeBarrel()]
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
            self.quarries = 8*[Quarry()]
            self.plantation_deck = 8*[Corn()]+10*[Indigo()]+11*[Sugar()]+9*[Tobacco()]+8*[Coffee()]
            self.goods = 10*[CornBarrel()]+11*[IndigoBarrel()]+11*[SugarBarrel()]+9*[TobaccoBarrel()]+9*[CoffeeBarrel()]
            self.ships = [Ships(5),Ships(6),Ships(7)]
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
            self.quarries = 8*[Quarry()]
            self.plantation_deck = 8*[Corn()]+9*[Indigo()]+11*[Sugar()]+9*[Tobacco()]+8*[Coffee()]
            self.goods = 10*[CornBarrel()]+11*[IndigoBarrel()]+11*[SugarBarrel()]+9*[TobaccoBarrel()]+9*[CoffeeBarrel()]
            self.ships = [Ships(6),Ships(7),Ships(8)]
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
        self.colonist_ship = max(len(self.players),spots)
        self.colonists -= self.colonist_ship

    def get_buildings(self):
        self.buildings = []
        for i in range(min(4,len(self.players))):
            self.buildings.append(SmallIndigoPlant())
            self.buildings.append(SmallSugarMill())
        for i in range(min(3,len(self.players))):
            self.buildings.append(IndigoPlant())
            self.buildings.append(SugarMill())
            self.buildings.append(TobaccoStorage())
            self.buildings.append(CoffeeRoaster())
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
        self.buildings.append(GuildHall())
        self.buildings.append(Residence())
        self.buildings.append(Fortress())
        self.buildings.append(CustomsHouse())
        self.buildings.append(CityHall())

    def do_round(self):
        for player in self.players[self.governor:]+self.players[:self.governor]:
            self.current_player = player.index
            choice = -1
            while choice not in range(len(self.roles)):
                choice = player.choose_role(self)
            player.role = self.roles.pop(int(choice))
            player.coins += player.role.coins
            player.role.coins = 0
            player.role(self)

        self.governor += 1
        if self.governor >= len(self.players):
            self.governor = 0

        for role in self.roles:
            role.coins += 1
        for player in self.players:
            self.roles.append(player.role)
            player.role = Role()
        self.roles.sort()
        self.turn += 1