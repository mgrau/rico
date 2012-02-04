import pygame
from pygame.locals import *
try:
    import android
except ImportError:
    android = None
from random import shuffle

################################################################
class Ship:
    def __init__(self,capacity=0):
        self.capacity = capacity
        self.goods = []
    def __repr__(self):
        if self.capacity >= 999:
            return "\nwharf: "+str(self.goods)
        else:
            return "\n"+str(self.capacity)+": "+str(self.goods)
    def full(self):
        return len(self.goods)>=self.capacity
    def can_load(self,good):
        if not self.full():
            if not len(self.goods):
                return True
            elif good in self.goods:
                return True
        return False

################################################################
class Barrel:
    def __init__(self, cost=-1, name=""):
        self.cost = cost
        self.name=name
    def __repr__(self):
        return self.name
    def __cmp__(self,other):
        return cmp(self.cost,other.cost)


class CornBarrel(Barrel):
    def __init__(self, cost=0):
        Barrel.__init__(self,cost,"corn")

class IndigoBarrel(Barrel):
    def __init__(self, cost=1):
        Barrel.__init__(self,cost,"indigo")

class SugarBarrel(Barrel):
    def __init__(self, cost=2):
        Barrel.__init__(self,cost,"sugar")

class TobaccoBarrel(Barrel):
    def __init__(self, cost=3):
        Barrel.__init__(self,cost,"tobacco")

class CoffeeBarrel(Barrel):
    def __init__(self, cost=4):
        Barrel.__init__(self,cost,"coffee")

################################################################
class Plantation:
    def __init__(self, colonists=0, name=""):
        self.colonists = colonists
        self.name=name
    def __repr__(self):
        return self.name+"("+str(self.colonists)+")"


class Quarry(Plantation):
    def __init__(self, colonists=0):
        Plantation.__init__(self,colonists,"quarry")

class Corn(Plantation):
    def __init__(self, colonists=0):
        Plantation.__init__(self,colonists,"corn")

class Indigo(Plantation):
    def __init__(self, colonists=0):
        Plantation.__init__(self,colonists,"indigo")

class Sugar(Plantation):
    def __init__(self, colonists=0):
        Plantation.__init__(self,colonists,"sugar")

class Tobacco(Plantation):
    def __init__(self, colonists=0):
        Plantation.__init__(self,colonists,"tobacco")

class Coffee(Plantation):
    def __init__(self, colonists=0):
        Plantation.__init__(self,colonists,"coffee")

################################################################
class Building:
    def __init__(self, id=-1, colonists=0, cost=0, points=0, capacity=0, size=0, name=""):
        self.id = id
        self.colonists = colonists
        self.cost = cost
        self.points = points
        self.capacity = capacity
        self.size = size
        self.name = name
    def __repr__(self):
        return self.name+"("+str(self.colonists)+")"
    def __cmp__(self,other):
        return cmp(self.id,other.id)

class SmallIndigoPlant(Building):
    def __init__(self,colonists=0):
        Building.__init__(self,id=0,colonists=colonists,cost=1,points=1,capacity=1,size=1,name="Small Indigo Plant")

class SmallSugarMill(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=1,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Small Sugar Mill")

class SmallMarket(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=2,colonists=colonists,cost=1,points=1,capacity=1,size=1,name="Small Market")

class Hacienda(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=3,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Hacienda")

class ConstructionHut(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=4,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Construction Hut")

class SmallWarehouse(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=5,colonists=colonists,cost=3,points=1,capacity=1,size=1,name="Small Warehouse")

class IndigoPlant(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=6,colonists=colonists,cost=3,points=2,capacity=3,size=1,name="Indigo Plant")

class SugarMill(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=7,colonists=colonists,cost=4,points=2,capacity=3,size=1,name="Sugar Mill")

class Hospice(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=8,colonists=colonists,cost=4,points=2,capacity=1,size=1,name="Hospice")

class Office(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=9,colonists=colonists,cost=5,points=2,capacity=1,size=1,name="Office")

class LargeMarket(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=10,colonists=colonists,cost=5,points=2,capacity=1,size=1,name="Large Market")

class LargeWarehouse(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=11,colonists=colonists,cost=6,points=2,capacity=1,size=1,name="Large Warehouse")

class TobaccoStorage(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=12,colonists=colonists,cost=5,points=3,capacity=3,size=1,name="Tobacco Storage")

class CoffeeRoaster(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=13,colonists=colonists,cost=6,points=3,capacity=2,size=1,name="Coffee Roaster")

class University(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=14,colonists=colonists,cost=7,points=3,capacity=1,size=1,name="University")

class Factory(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=15,colonists=colonists,cost=8,points=3,capacity=1,size=1,name="Factory")

class Harbor(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=16,colonists=colonists,cost=8,points=3,capacity=1,size=1,name="Harbor")

class Wharf(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=17,colonists=colonists,cost=9,points=3,capacity=1,size=1,name="Wharf")

class GuildHall(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=18,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Guild Hall")

class Residence(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=19,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Residence")

class Fortress(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=20,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Fortress")

class CustomsHouse(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=21,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Customs House")

class CityHall(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=22,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="City Hall")

################################################################
class Player:
    def __init__(self,index=0,name=""):
        self.name = name
        self.index = index
        self.wharf = Ship(999)
        self.reset()

    def __repr__(self):
        return  "\n"+self.name+"\n"+\
                "coins: "+str(self.coins)+"\n"+\
                "san juan: "+str(self.san_juan)+"\n"+\
                "plantations: "+str(self.plantations)+"\n"+\
                "buildings: "+str(self.buildings)+"\n"+\
                "goods: "+str(self.goods)

    def reset(self):
        self.coins = 0
        self.points = 0
        self.goods = []
        self.plantations = []
        self.buildings = []
        self.san_juan = 0
        self.role = Role()


    def choose_role(self,game):
        return 0

    def settler(self,game):
        return 0

    def mayor(self,game):
        self.distribute_colonists()
        return

    def builder(self,game):
        return -1

    def craftsman(self,game):
        if len(self.goods):
            return self.goods[0]
        else:
            return Barrel()

    def trader(self,game):
        return Barrel()

    def captain(self,game):
        return

    def rot(self,game):
        return

    def discount(self,building=Building()):
        discount = sum([plantation.colonists*isinstance(plantation,Quarry) for plantation in self.plantations])
        discount = min(discount,building.points) # you can't use more quarries than points the building is worth
        if isinstance(self.role,Builder):
            discount+=1
        return discount

    def afford_building(self,building=Building()):
        return self.coins >= (building.cost-self.discount(building))

    def have_plantation(self,plantation_type=Plantation):
        return any([isinstance(plantation,plantation_type) for plantation in self.plantations])

    def have_building(self,building_type=Building):
        return any([isinstance(building,building_type) for building in self.buildings])

    def use_building(self,building_type=Building):
        if self.have_building(building_type):
            return self.buildings[[isinstance(building,building_type) for building in self.buildings].index(True)].colonists
        else:
            return False

    def produce_goods(self):
        num_corn = sum([plantation.colonists*isinstance(plantation,Corn) for plantation in self.plantations])
        num_indigo = sum([plantation.colonists*isinstance(plantation,Indigo) for plantation in self.plantations])
        num_sugar = sum([plantation.colonists*isinstance(plantation,Sugar) for plantation in self.plantations])
        num_tobacco = sum([plantation.colonists*isinstance(plantation,Tobacco) for plantation in self.plantations])
        num_coffee = sum([plantation.colonists*isinstance(plantation,Coffee) for plantation in self.plantations])

        num_indigo = min(num_indigo,self.use_building(SmallIndigoPlant)+self.use_building(IndigoPlant))
        num_sugar = min(num_sugar,self.use_building(SmallSugarMill)+self.use_building(SugarMill))
        num_tobacco = min(num_tobacco,self.use_building(TobaccoStorage))
        num_coffee = min(num_coffee,self.use_building(CoffeeRoaster))

        return [CornBarrel() for i in range(num_corn)]+[IndigoBarrel() for i in range(num_indigo)]+[SugarBarrel() for i in range(num_sugar)]+[TobaccoBarrel() for i in range(num_tobacco)]+[CoffeeBarrel() for i in range(num_coffee)]

    def city_full(self):
        return sum([building.size for building in self.buildings]) >= 12

    def island_full(self):
        return len(self.plantations) >= 12

    def colonists(self):
        colonists = self.san_juan
        colonists += reduce(lambda a,b: a+b.colonists,self.plantations,0)
        colonists += reduce(lambda a,b: a+b.colonists,self.buildings,0)
        return colonists

    def distribute_colonists(self):
        for plantation in self.plantations:
            if plantation.colonists<1 and self.san_juan>0:
                plantation.colonists = 1
                self.san_juan -= 1
        for building in self.buildings:
            if building.colonists < building.capacity and self.san_juan>0:
                building.colonists += max(self.san_juan,building.capacity-building.colonists)
                self.san_juan += max(self.san_juan,building.capacity-building.colonists)

    def open_plantations(self):
        return sum([(1-plantation.colonists) for plantation in self.plantations])

    def open_buildings(self):
        return sum([(building.capacity-building.colonists) for building in self.buildings])

    def open_spots(self):
        return self.open_buildings() + self.open_plantations()

    def total_points(self):
        points = self.points # the victory point chips
        points += sum([building.points for building in self.buildings]) # points for the buildings in the city

        # now add points for any prestige buildings iff they have a colonist
        if self.use_building(GuildHall):
            for building_type in [SmallIndigoPlant, SmallSugarMill]:
                if self.have_building(building_type):
                    points += 1 # one point for the small production buildings
            for building_type in [IndigoPlant, SugarMill, TobaccoStorage, CoffeeRoaster]:
                if self.have_building(building_type):
                    points += 2 # two points for the large production buildings
        if self.use_building(Residence):
            points += min(len(self.plantations)-5,4)
        if self.use_building(Fortress):
            points += int(self.colonists()/3) # 1 point for every 3 colonists
        if self.use_building(CustomsHouse):
            points += int(self.points/4) # 1 point for every 4 victory point chips
        if self.use_building(CityHall):
            for building in self.buildings:
                # victory point for each violet building (large production buildings have non unity capacities)
                if building.capacity==1 and not isinstance(building,SmallIndigoPlant) and not isinstance(building,SmallSugarMill):
                    points += 1
        return points

################################################################
class Role:
    def __init__(self,name=""):
        self.coins = 0
        self.name = name
    def __repr__(self):
        return self.name+"("+str(self.coins)+")"
    def __call__(self,game):
        return


class Settler(Role):
    def __init__(self):
        Role.__init__(self,name="Settler")
    def __call__(self,game):
        for player in game.players[game.current_player:] + game.players[:game.current_player]:
            if len(player.plantations) < 12:
                if len(game.quarries)>0 and (player.index == game.current_player or player.use_building(ConstructionHut)):
                    choice = player.settler(game)
                    while choice not in range(len(game.plantations)+1):
                        print "invalid choice"
                        choice = player.settler(game)
                else:
                    choice = player.settler(game)
                    while choice not in range(len(game.plantations)):
                        print "invalid choice"
                        choice = player.settler(game)
                if choice == len(game.plantations):
                    player.plantations.append(game.quarries.pop())
                else:
                    player.plantations.append(game.plantations.pop(choice))
                if player.use_building(Hospice) and game.colonists:
                    player.plantations[-1].colonists = 1
                    game.colonists -= 1
            if len(player.plantations) < 12 and player.use_building(Hacienda):
                player.plantations.append(game.plantation_deck.pop())
        game.draw_plantations()


class Mayor(Role):
    def __init__(self):
        Role.__init__(self,name="Mayor")
    def __call__(self,game):
        if game.colonists > 0:
            game.players[game.current_player].san_juan += 1
            game.colonists -= 1
        i = game.current_player
        while game.colonist_ship > 0:
            game.players[i].san_juan += 1
            game.colonist_ship -= 1
            i += 1
            if i >= len(game.players):
                i = 0
        for player in game.players[game.current_player:] + game.players[:game.current_player]:
            player.mayor(game)
            while player.san_juan > 0 and player.open_spots() and (not any([plantation.colonists > 1 for plantation in player.plantations]+[building.colonists > building.capacity for building in player.buildings])):
                player.mayor(game)
        game.fill_colonist_ship()


class Builder(Role):
    def __init__(self):
        Role.__init__(self,name="Builder")
    def __call__(self,game):
        for player in game.players[game.current_player:] + game.players[:game.current_player]:
            if not(player.city_full()):
                choice = player.builder(game)
                while choice not in range(-1,len(game.buildings)):
                    print "invalid choice"
                    choice = player.builder(game)
                if choice >= 0:
                    if player.afford_building(game.buildings[choice]):
                        player.buildings.append(game.buildings.pop(choice))
                        player.coins -= (player.buildings[-1].cost-player.discount(player.buildings[-1]))
                        if player.use_building(University) and game.colonists:
                            player.buildings[-1].colonists = 1
                            game.colonists -= 1


class Craftsman(Role):
    def __init__(self):
        Role.__init__(self,name="Craftsman")
    def __call__(self,game):
        for player in game.players[game.current_player:] + game.players[:game.current_player]:
            goods_wanted = player.produce_goods()
            goods_obtained = []
            for good in goods_wanted:
                if good in game.goods:
                    game.goods.remove(good)
                    goods_obtained.append(good)
            if player.use_building(Factory):
                unique_number = 0
                for barrel in [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]:
                    if barrel in goods_obtained:
                        unique_number += 1
                if unique_number == 5:
                    player.coins += 5
                elif unique_number in [2,3,4]:
                    player.coins += unique_number-1
            player.goods.extend(goods_obtained)
            player.goods.sort()
        if len(game.players[game.current_player].goods)>0:
            good = game.players[game.current_player].craftsman(game)
            if good in game.players[game.current_player].goods and good in game.goods:
                game.goods.remove(good)
                game.players[game.current_player].goods.append(good)
                game.players[game.current_player].goods.sort()


class Trader(Role):
    def __init__(self):
        Role.__init__(self,name="Trader")
    def __call__(self,game):
        for player in game.players[game.current_player:] + game.players[:game.current_player]:
            if len(player.goods):
                good = player.trader(game)
                if good in player.goods:
                    if len(game.trading_house)<4:
                        if player.use_building(Office) or (good not in game.trading_house):
                            player.goods.remove(good)
                            game.trading_house.append(good)
                            player.coins += good.cost + 1*player.use_building(SmallMarket) + 2*player.use_building(LargeMarket) + 1*(player.index == game.current_player)
        if len(game.trading_house)>=4:
            game.goods += game.trading_house
            game.trading_house = []


class Captain(Role):
    def __init__(self):
        Role.__init__(self,name="Captain")
    def __call__(self,game):
        i = game.current_player
        if game.can_player_ship(game.players[i]):
            game.players[i].points += 1
            game.points -= 1
        while game.can_anyone_ship():
            player = game.players[i]
            valid_shipping_order = False
            while not valid_shipping_order and game.can_player_ship(player):
                (ship,good) = player.captain(game)
                if good in player.goods and ship.can_load(good) and not any([good in othership.goods for othership in filter(lambda x:x!=ship,game.ships)]):
                    if not(ship==player.wharf and not player.use_building(Wharf)):
                        valid_shipping_order = True
                        game.ship(ship,player,good)
            i += 1
            if i >= len(game.players):
                i = 0
        for ship in game.ships:
            if ship.full():
                game.goods += ship.goods
                ship.goods = []
        for wharf in [player.wharf for player in game.players]:
                game.goods += wharf.goods
                wharf.goods = []
                wharf.capacity = 999
        for player in game.players[game.current_player:] + game.players[:game.current_player]:
            print player.name
            print len(player.goods)>1
            if len(player.goods) > 1:
                storage = []
                goods_to_keep = [Barrel()]
                print goods_to_keep[0] not in player.goods
                while goods_to_keep[0] not in player.goods:
                    goods_to_keep = player.rot(game)
                player.goods.remove(goods_to_keep[0])
                storage.append(goods_to_keep[0])
                if player.use_building(LargeWarehouse):
                    for good in goods_to_keep[2:3]:
                        while good in player.goods:
                            player.goods.remove(good)
                            storage.append(good)
                if player.use_building(SmallWarehouse):
                    while goods_to_keep[1] in player.goods:
                        player.goods.remove(goods_to_keep[1])
                        storage.append(goods_to_keep[1])
                game.goods += player.goods
                player.goods = storage
        return


class Prospector(Role):
    def __init__(self):
        Role.__init__(self,name="Prospector")
    def __call__(self,game):
        game.players[game.current_player].coins += 1

################################################################
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

    def start(self):
        while not self.game_end():
            self.round()


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

        self.buildings.sort()

    def can_anyone_ship(self):
        return any([self.can_player_ship(player) for player in self.players])

    def can_player_ship(self,player):
        if len(player.goods):
            ships = list(self.ships)
            if player.use_building(Wharf):
                ships += [player.wharf]
            for ship in ships:
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

class GUI_Game(Game):
    def __init__(self,size=(1024,768)):
        Game.__init__(self)
        self.surface = pygame.Surface(size)
        self.clock = pygame.time.Clock()
        self.building_grid = []
        for row in range(4):
            for column in range(6):
                self.building_grid.append(pygame.Rect( (25+(154+10)*column, 32+(83+10)*row),(154,83)))
    def draw(self,index):
        for player in self.players:
            if player.index == index:
                player.board.draw(player,True)
            else:
                player.board.draw(player)

        self.surface.blit(island, (0,0))

        already_printed = []
        for i,building in enumerate(self.buildings):
            if building.__class__ not in already_printed:
                self.draw_building(building,self.building_grid[building.id])
                already_printed.append(building.__class__)
    def draw_building(self,building,pos):
        if isinstance(building,SmallIndigoPlant):
            self.surface.blit(small_indigo_plant,pos)
        elif isinstance(building,SmallSugarMill):
            self.surface.blit(small_sugar_mill,pos)
        elif isinstance(building,IndigoPlant):
            self.surface.blit(indigo_plant,pos)
        elif isinstance(building,SugarMill):
            self.surface.blit(sugar_mill,pos)
        elif isinstance(building,TobaccoStorage):
            self.surface.blit(tobacco_storage,pos)
        elif isinstance(building,CoffeeRoaster):
            self.surface.blit(coffee_roaster,pos)
        else:
            if building.points < 4:
                self.surface.blit(small_violet,pos)
            else:
                self.surface.blit(large_violet,pos)
            name = font.render(building.name,1,(255,255,255))
            self.surface.blit(name,(pos[0]+6,pos[1]+3))
        cost = font.render(str(building.cost),1,(255,255,255))
        points = font.render(str(building.points),1,(180,0,0))
        self.surface.blit(points,(pos[0]+134,pos[1]+1))
        self.surface.blit(cost,(pos[0]+126,pos[1]+47))

        if building.colonists > 0:
            if building.size < 2:
                pygame.draw.circle(self.surface, brown, (pos[0]+130,pos[1]+59), 15)
            else:
                pygame.draw.circle(self.surface, brown, (pos[0]+130,pos[1]+148), 15)
        if building.colonists > 1:
            pygame.draw.circle(self.surface, brown, (pos[0]+90,pos[1]+59), 15)
        if building.colonists > 2:
            pygame.draw.circle(self.surface, brown, (pos[0]+50,pos[1]+59), 15)

################################################################
gray = pygame.Color(0,0,0,10)
brown = pygame.Color(128,40,40)
magenta = pygame.Color(236,0,140)

island = pygame.image.load('res/island.png')
pygame.font.init()
h1 = pygame.font.Font('res/fertigo.ttf',45)
font = pygame.font.Font('res/fertigo.ttf',18)

quarry = pygame.image.load('res/quarry.png')
corn = pygame.image.load('res/corn.png')
indigo = pygame.image.load('res/indigo.png')
sugar = pygame.image.load('res/sugar.png')
tobacco = pygame.image.load('res/tobacco.png')
coffee = pygame.image.load('res/coffee.png')
#quarry.set_colorkey(quarry.get_at((0,0)))
corn.set_colorkey(corn.get_at((0,0)))
#indigo.set_colorkey(indigo.get_at((0,0)))
#sugar.set_colorkey(sugar.get_at((0,0)))
#tobacco.set_colorkey(tobacco.get_at((0,0)))
#coffee.set_colorkey(coffee.get_at((0,0)))

corn_barrel = pygame.image.load('res/corn_barrel.png')
indigo_barrel = pygame.image.load('res/indigo_barrel.png')
sugar_barrel = pygame.image.load('res/sugar_barrel.png')
tobacco_barrel = pygame.image.load('res/tobacco_barrel.png')
coffee_barrel = pygame.image.load('res/coffee_barrel.png')
corn_barrel.set_colorkey(corn_barrel.get_at((0,0)))
indigo_barrel.set_colorkey(indigo_barrel.get_at((0,0)))
sugar_barrel.set_colorkey(sugar_barrel.get_at((0,0)))
tobacco_barrel.set_colorkey(tobacco_barrel.get_at((0,0)))
coffee_barrel.set_colorkey(coffee_barrel.get_at((0,0)))

small_indigo_plant = pygame.image.load('res/small_indigo_plant.png')
indigo_plant = pygame.image.load('res/indigo_plant.png')
small_sugar_mill = pygame.image.load('res/small_sugar_mill.png')
sugar_mill = pygame.image.load('res/sugar_mill.png')
tobacco_storage = pygame.image.load('res/tobacco_storage.png')
coffee_roaster = pygame.image.load('res/coffee_roaster.png')
small_violet = pygame.image.load('res/small_violet.png')
large_violet = pygame.image.load('res/large_violet.png')

settler_tile = pygame.image.load('res/settler.png')
mayor_tile = pygame.image.load('res/mayor.png')
builder_tile = pygame.image.load('res/builder.png')
craftsman_tile = pygame.image.load('res/craftsman.png')
trader_tile = pygame.image.load('res/trader.png')
captain_tile = pygame.image.load('res/captain.png')
prospector_tile = pygame.image.load('res/prospector.png')
settler_tile.set_colorkey(settler_tile.get_at((0,0)))
mayor_tile.set_colorkey(mayor_tile.get_at((0,0)))
builder_tile.set_colorkey(builder_tile.get_at((0,0)))
craftsman_tile.set_colorkey(craftsman_tile.get_at((0,0)))
trader_tile.set_colorkey(trader_tile.get_at((0,0)))
captain_tile.set_colorkey(captain_tile.get_at((0,0)))
prospector_tile.set_colorkey(prospector_tile.get_at((0,0)))


class Board():
    def __init__(self,size=(1024,768)):
        self.width,self.height = size
        self.surface = pygame.Surface(size)
        padding = 32
        spacing = 6
        size = (96,96)
        self.plantation_grid = []
        for row in [3,2,1,0]:
            for column in [0,1,2]:
                self.plantation_grid.append(pygame.Rect((padding+(size[0]+spacing)*column, self.height*0.8-padding -size[1]-(size[1]+spacing)*row),size))
        size = (154,83)
        self.building_grid = []
        for row in [2,1,0]:
            for column in [0,1,2,3]:
                self.building_grid.append(pygame.Rect((2*padding + 2*spacing + 3*96+(size[0]+spacing)*column, self.height*0.8-padding -size[1]-(size[1]+spacing)*row),size))
        self.role_grid = []
        for column in range(8):
            self.role_grid.append(pygame.Rect((10+column*128,619),(118,144)))
        self.choose_plantation_grid = []
        for column in range(8):
            self.choose_plantation_grid.append(pygame.Rect((column*128+32,639),(96,96)))
        self.barrel_grid = []
        for column in range(5):
            self.barrel_grid.append(pygame.Rect((2*padding + 2*spacing + 3*96+60*column,250),(50,60)))
        self.choose_barrel_grid = []
        for column in range(5):
            self.choose_barrel_grid.append(pygame.Rect((column*75+32,675),(50,60)))

    def draw(self,player,reveal_points=False):
        self.surface.blit(island, (0,0))
        name = h1.render(player.name,1,(255,255,255))
        self.surface.blit(name,(100,32))


        if reveal_points:
            points = h1.render(str(player.points),1,(255,215,0))
            pygame.draw.circle(self.surface, (255,215,0), (64,60), 28)
            pygame.draw.circle(self.surface, (192,0,0), (64,60), 25)
            self.surface.blit(points,(50,31))

        coins = font.render(str(player.coins),1,(0,0,0))
        pygame.draw.circle(self.surface, (119,136,153), (400,200), 23)
        if player.coins >= 5:
            pygame.draw.circle(self.surface, (255,215,0), (400,200), 20)
        else:
            pygame.draw.circle(self.surface, (192,192,192), (400,200), 20)
        self.surface.blit(coins, (395,189))


        if player.san_juan:
            san_juan = font.render(str(player.san_juan),1,(255,255,255))
            pygame.draw.circle(self.surface, brown, (650,160), 15)
            self.surface.blit(san_juan,(645,148))

        if player.role:
            pos = (874,32)
            if isinstance(player.role,Settler):
                self.surface.blit(settler_tile,pos)
            if isinstance(player.role,Mayor):
                self.surface.blit(mayor_tile,pos)
            if isinstance(player.role,Builder):
                self.surface.blit(builder_tile,pos)
            if isinstance(player.role,Craftsman):
                self.surface.blit(craftsman_tile,pos)
            if isinstance(player.role,Trader):
                self.surface.blit(trader_tile,pos)
            if isinstance(player.role,Captain):
                self.surface.blit(captain_tile,pos)
            if isinstance(player.role,Prospector):
                self.surface.blit(prospector_tile,pos)

        plantation_space = pygame.Surface((96,96),pygame.SRCALPHA)
        plantation_space.fill(gray)
        building_space= pygame.Surface((154,83),pygame.SRCALPHA)
        building_space.fill(gray)

        for rect in self.plantation_grid:
            self.surface.blit(plantation_space,rect)
            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]-6,rect[1]-6),(6,rect[3]+6)))
            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0],rect[1]-6),(rect[2]+6,6)))
            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]+rect[2],rect[1]),(6,rect[3]+6)))
            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]-6,rect[1]+rect[3]),(rect[2]+6,6)))

        for rect in self.building_grid:
            self.surface.blit(building_space,rect)
            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]-6,rect[1]-6),(6,rect[3]+6)))
            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0],rect[1]-6),(rect[2]+6,6)))
            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]+rect[2],rect[1]),(6,rect[3]+6)))
            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]-6,rect[1]+rect[3]),(rect[2]+6,6)))

        for pos,plantation in zip(self.plantation_grid,player.plantations):
            self.draw_plantation(plantation,pos)

        for pos,building in zip(self.building_grid,player.buildings):
            self.draw_building(building,pos)

        for pos,barrel,texture in zip(self.barrel_grid,[CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()],[corn_barrel, indigo_barrel, sugar_barrel, tobacco_barrel, coffee_barrel]):
            if barrel in player.goods:
                amount = font.render(str(reduce(lambda a,b:a+(b==barrel),player.goods,0)),1,(255,255,255))
                self.surface.blit(texture,pos)
                self.surface.blit(amount,(pos[0]+15,pos[1]+12))


    def draw_roles(self,game):
        for pos,role in zip(self.role_grid,game.roles):
            if isinstance(role,Settler):
                self.surface.blit(settler_tile,pos)
            if isinstance(role,Mayor):
                self.surface.blit(mayor_tile,pos)
            if isinstance(role,Builder):
                self.surface.blit(builder_tile,pos)
            if isinstance(role,Craftsman):
                self.surface.blit(craftsman_tile,pos)
            if isinstance(role,Trader):
                self.surface.blit(trader_tile,pos)
            if isinstance(role,Captain):
                self.surface.blit(captain_tile,pos)
            if isinstance(role,Prospector):
                self.surface.blit(prospector_tile,pos)

            if role.coins:
                coins = font.render(str(role.coins),1,(0,0,0))
                pos = (pos.bottomright[0]-25,pos.bottomright[1]-33)
                pygame.draw.circle(self.surface, (119,136,153), pos, 17)
                if role.coins >= 5:
                    pygame.draw.circle(self.surface, (255,215,0), pos, 15)
                else:
                    pygame.draw.circle(self.surface, (192,192,192), pos, 15)
                self.surface.blit(coins, (pos[0]-5,pos[1]-12))

    def draw_plantation(self,plantation,pos):
        if isinstance(plantation,Corn):
            self.surface.blit(corn,pos)
        if isinstance(plantation,Indigo):
            self.surface.blit(indigo,pos)
        if isinstance(plantation,Sugar):
            self.surface.blit(sugar,pos)
        if isinstance(plantation,Tobacco):
            self.surface.blit(tobacco,pos)
        if isinstance(plantation,Coffee):
            self.surface.blit(coffee,pos)
        if isinstance(plantation,Quarry):
            self.surface.blit(quarry,pos)
        if plantation.colonists > 0:
            pygame.draw.circle(self.surface, brown, (pos[0]+72,pos[1]+72), 15)

    def draw_building(self,building,pos):
        if isinstance(building,SmallIndigoPlant):
            self.surface.blit(small_indigo_plant,pos)
        elif isinstance(building,SmallSugarMill):
            self.surface.blit(small_sugar_mill,pos)
        elif isinstance(building,IndigoPlant):
            self.surface.blit(indigo_plant,pos)
        elif isinstance(building,SugarMill):
            self.surface.blit(sugar_mill,pos)
        elif isinstance(building,TobaccoStorage):
            self.surface.blit(tobacco_storage,pos)
        elif isinstance(building,CoffeeRoaster):
            self.surface.blit(coffee_roaster,pos)
        else:
            if building.points < 4:
                self.surface.blit(small_violet,pos)
            else:
                self.surface.blit(large_violet,pos)
            name = font.render(building.name,1,(255,255,255))
            self.surface.blit(name,(pos[0]+6,pos[1]+3))
        cost = font.render(str(building.cost),1,(255,255,255))
        points = font.render(str(building.points),1,(180,0,0))
        self.surface.blit(points,(pos[0]+134,pos[1]+1))
        self.surface.blit(cost,(pos[0]+126,pos[1]+47))

        if building.colonists > 0:
            if building.size < 2:
                pygame.draw.circle(self.surface, brown, (pos[0]+130,pos[1]+59), 15)
            else:
                pygame.draw.circle(self.surface, brown, (pos[0]+130,pos[1]+148), 15)
        if building.colonists > 1:
            pygame.draw.circle(self.surface, brown, (pos[0]+90,pos[1]+59), 15)
        if building.colonists > 2:
            pygame.draw.circle(self.surface, brown, (pos[0]+50,pos[1]+59), 15)


################################################################
################################################################
class GUI_Player(Player):
    def __init__(self,index=0,name="",screen=0):
        Player.__init__(self,index,name)

        if not screen:
            self.screen = pygame.display.set_mode( (1024,768) )
        else:
            self.screen = screen
        self.board = Board((1024,768))

    def print_board(self,game):
        print game

    def get_input(self,game,build=False):
        self.screen.blit(self.board.surface,(0,0))
        pygame.display.flip()
        visible_player = self.index
        game_board = False
        valid_input = False
        rel = (0,0)
        while not valid_input:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                rel = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                rel = (event.pos[0]-rel[0],event.pos[1]-rel[1])
                if rel[0]<-75 and abs(rel[0])>abs(rel[1]) and not game_board:
                    if visible_player == len(game.players)-1:
                        next_player = 0
                    else:
                        next_player = visible_player+1
                    for i in range(1024,-1,-256):
                        self.screen.blit(game.players[visible_player].board.surface,(i-1024,0))
                        self.screen.blit(game.players[next_player].board.surface,(i,0))
                        pygame.display.flip()
                    visible_player = next_player
                elif rel[0]>75 and abs(rel[0])>abs(rel[1]) and not game_board:
                    if visible_player == 0:
                        next_player = len(game.players)-1
                    else:
                        next_player = visible_player-1
                    for i in range(0,1024+1,256):
                        self.screen.blit(game.players[visible_player].board.surface,(i,0))
                        self.screen.blit(game.players[next_player].board.surface,(i-1024,0))
                        pygame.display.flip()
                    visible_player = next_player
                elif (abs(rel[1])>75 and abs(rel[1])>abs(rel[0])):
                    if game_board:
                        nextscreen = game.players[visible_player].board.surface
                        thisscreen = game.surface
                    else:
                        nextscreen = game.surface
                        thisscreen = game.players[visible_player].board.surface
                    if rel[1]>0:
                        for i in range(0,768+1,192):
                            self.screen.blit(thisscreen,(0,i))
                            self.screen.blit(nextscreen,(0,i-768))
                            pygame.display.flip()
                        slide_up = False
                    else:
                        for i in range(768,-1,-192):
                            self.screen.blit(nextscreen,(0,i))
                            self.screen.blit(thisscreen,(0,i-768))
                            pygame.display.flip()
                    game_board = not game_board
                else:
                    if (visible_player == self.index and not game_board) or (build and game_board):
                        return event.pos
            game.clock.tick(30)


    def choose_role(self,game):
        game.draw(self.index)
        self.board.draw_roles(game)


        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for choice,rect in enumerate(self.board.role_grid):
                if rect.collidepoint(pos):
                    return choice

    def settler(self,game):
        game.draw(self.index)
        for pos,plantation in zip(self.board.choose_plantation_grid,game.plantations):
            self.board.draw_plantation(plantation,pos)
        if len(game.quarries)>0 and (self.index == game.current_player or self.use_building(ConstructionHut)):
            self.board.draw_plantation(Quarry(),self.board.choose_plantation_grid[len(game.plantations)])
        instructions = font.render("Please select a plantation",1,(255,255,255))
        self.board.surface.blit(instructions,(32,736))
        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for choice,rect in enumerate(self.board.choose_plantation_grid):
                if self.index==game.current_player or self.use_building(ConstructionHut):
                    if rect.collidepoint(pos) and choice<=len(game.plantations):
                        return choice
                else:
                    if rect.collidepoint(pos) and choice<=len(game.plantations)-1:
                        return choice

    def mayor(self,game):
        done = False
        while not done:
            game.draw(self.index)
            button = h1.render("Done",1,(255,255,255),(100,0,0))
            instructions = font.render("Please place your colonists",1,(255,255,255))
            self.board.surface.blit(button,(32,676))
            button = button.get_rect()
            button.topleft = (32,676)
            self.board.surface.blit(instructions,(32,736))
            self.screen.blit(self.board.surface,(0,0))
            pygame.display.flip()

            pos = self.get_input(game)
            for choice,rect in enumerate(self.board.plantation_grid):
                if rect.collidepoint(pos) and choice<len(self.plantations):
                    if self.plantations[choice].colonists > 0:
                        self.san_juan += self.plantations[choice].colonists
                        self.plantations[choice].colonists = 0
                    else:
                        if self.san_juan > 0:
                            self.plantations[choice].colonists = 1
                            self.san_juan -= 1
            for choice,rect in enumerate(self.board.building_grid):
                if rect.collidepoint(pos) and choice<len(self.buildings):
                    if self.buildings[choice].colonists >= self.buildings[choice].capacity:
                        self.san_juan += self.buildings[choice].colonists
                        self.buildings[choice].colonists = 0
                    else:
                        if self.san_juan > 0:
                            self.buildings[choice].colonists += 1
                            self.san_juan -= 1
                        elif self.buildings[choice].colonists > 0:
                            self.buildings[choice].colonists -= 1
                            self.san_juan += 1
            if button.collidepoint(pos):
                if self.san_juan ==0 or self.open_spots()==0:
                    return

    def builder(self,game):
        game.draw(self.index)
        button = h1.render("Don't Buy",1,(255,255,255),(100,0,0))
        game.surface.blit(button,(32,676))
        button = button.get_rect()
        button.topleft = (32,676)
        event = pygame.event.Event(pygame.MOUSEBUTTONUP)
        event.pos = (0,-10000)
        pygame.event.post(event)

        valid_input = False
        while not valid_input:
            pos = self.get_input(game,build=True)
            for id,rect in enumerate(game.building_grid):
                if rect.collidepoint(pos):
                    for choice,building in enumerate(game.buildings):
                        if building.id == id:
                            if self.afford_building(building) and (not self.have_building(building.__class__)):
                                return choice
            if button.collidepoint(pos):
                return -1

    def craftsman(self,game):
        game.draw(self.index)
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]
        for pos,barrel,texture in zip(self.board.choose_barrel_grid,barrel_types,[corn_barrel, indigo_barrel, sugar_barrel, tobacco_barrel, coffee_barrel]):
            if barrel in self.produce_goods() and barrel in game.goods:
                self.board.surface.blit(texture,pos)
        instructions = font.render("Please select an extra good",1,(255,255,255))
        self.board.surface.blit(instructions,(32,736))

        valid_input = False
        while not valid_input:
            pos = self.get_input(game,build=True)
            for barrel,rect in zip(barrel_types,self.board.choose_barrel_grid):
                if rect.collidepoint(pos) and barrel in self.produce_goods() and barrel in game.goods:
                    return barrel

    def trader(self,game):
        game.draw(self.index)
        button = h1.render("Don't Sell",1,(255,255,255),(100,0,0))
        self.board.surface.blit(button,(32,676))
        button = button.get_rect()
        button.topleft = (32,676)
        instructions = font.render("Please select a good to sell",1,(255,255,255))
        self.board.surface.blit(instructions,(32,736))

        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        valid_input = False
        while not valid_input:
            pos = self.get_input(game,build=True)
            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                if rect.collidepoint(pos) and (barrel in self.goods) and (barrel not in game.trading_house or self.use_building(Office)):
                    return barrel
            if button.collidepoint(pos):
                return Barrel()


    def captain(self,game):
        game.draw(self.index)
        instructions = font.render("Please select a good to ship",1,(255,255,255))
        self.board.surface.blit(instructions,(32,736))

        valid_input = False
#        while not valid_input:
#            pos = self.get_input(game,build=True)
#            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
#                if rect.collidepoint(pos) and (barrel in self.goods) and (barrel not in game.trading_house or self.use_building(Office)):
        print "\n"+self.name+", choose a shipment"
        choices = []
        for ship in game.ships:
            for good in self.goods:
                if (ship,good) not in choices and ship.can_load(good) and not any([good in othership.goods for othership in filter(lambda x:x!=ship,game.ships)]):
                    print str(len(choices))+": ship "+str(good)+" on ship("+str(ship.capacity)+")"
                    choices.append((ship,good))
        if self.use_building(Wharf) and not self.wharf.full():
            for good in self.goods:
                if (self.wharf,good) not in choices and self.wharf.can_load(good) and not any([good in othership.goods for othership in game.ships]):
                    print str(len(choices))+": ship "+str(good)+" on wharf"
                    choices.append((self.wharf,good))
            print str(len(choices))+": do not use wharf this turn"
            choices.append((self.wharf,Barrel()))
        if len(choices)==1:
            return choices[0]
        choice = ''
        while choice not in [str(i) for i in range(len(choices))]:
            choice = self.get_input(game)
        if self.use_building(Wharf) and not self.wharf.full() and int(choice) == len(choices)-1:
            self.wharf.capacity = -1
        return choices[int(choice)]

    def rot(self,game):
        self.print_board(game)
        print "\n"+self.name+", choose a good to keep"
        choices = []
        for good in self.goods:
            if good not in choices:
                print str(len(choices))+": "+str(good)
                choices.append(good)
        choice = ''
        while choice not in [str(i) for i in range(len(choices))]:
            choice = self.get_input(game)
        goods_to_keep = [choices[int(choice)]]

        # TODO: deal with warehouses
        return goods_to_keep


def main():
    pygame.init()
    screen = pygame.display.set_mode( (1024,768) )
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    game = GUI_Game()
    game.players.append(GUI_Player(0,"Matt",screen))
    game.players.append(GUI_Player(1,"Amy",screen))
    game.players.append(GUI_Player(2,"Dan",screen))
    game.setup()
    game.start()

if __name__ == '__main__':
    main()