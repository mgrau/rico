import pygame

screen = pygame.display.set_mode( (800,600) )

from gui.game import GUI_Game
from gui.player import GUI_Player
from text_player import *
from engine.game import Game
from ai.ai_player import Random_Player
from gui import tiles

tiles.convert_all()
game = GUI_Game(screen.get_size())
#game = Game()
#game.players.append(Random_Player(0,"Matt"))
#game.players.append(Random_Player(0,"Amy"))
#game.players.append(Random_Player(0,"Dan"))
game.players.append(GUI_Player(0,"Matt",screen))
game.players.append(GUI_Player(1,"Amy",screen))
game.players.append(GUI_Player(2,"Dan",screen))

game.setup()
from engine.barrels import *
from engine.plantations import *
from engine.buildings import *
for player in game.players:
    for i in range(3):
        player.goods.append(CornBarrel())
        player.goods.append(IndigoBarrel())
        player.goods.append(SugarBarrel())
        player.goods.append(TobaccoBarrel())
        player.goods.append(CoffeeBarrel())
#    player.buildings.append(Wharf(1))
    player.buildings.append(SmallMarket(0))
    player.buildings.append(CoffeeRoaster(1))
    player.buildings.append(SugarMill(1))
    player.buildings.append(SmallIndigoPlant(1))
    player.buildings.append(SmallWarehouse(1))
    player.buildings.append(LargeWarehouse(1))
    player.coins = 99
game.players[0].buildings.append(Wharf(1))
game.draw(0)
game.start()

for player in game.players:
    print player.name + ": "+str(player.total_points())+" points"
#
#points = [0,0,0,0,0]
#
#for i in xrange(1000):
#    game.setup()
#    game.start()
#    for j,player in enumerate(game.players):
#        if player.total_points()>100:
#            print player.total_points(),player.total_points(),player.points,sum([building.points for building in player.buildings])
#
#        points[j]+=player.total_points()
#
#for i in xrange(len(points)):
#    points[i]/=1000.0
#
#print points



        