from buildings import *
from barrels import *

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
        if len(game.players[game.current_player].produce_goods()) and len(game.goods):
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
                wharf.passed = False
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