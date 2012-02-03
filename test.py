import pygame
pygame.init()
screen = pygame.display.set_mode( (1024,768) )

from text_player import *
from gui_player import *

game = Game()
game.players.append(GUI_Player(0,"Matt",screen))
game.players.append(GUI_Player(1,"Amy",screen))
game.players.append(GUI_Player(2,"Dan",screen))
game.setup()

from barrels import *
from plantations import *
from buildings import *
for player in game.players:
#    for i in range(3):
#        player.goods.append(CornBarrel())
#        player.goods.append(IndigoBarrel())
#        player.goods.append(SugarBarrel())
#        player.goods.append(TobaccoBarrel())
#        player.goods.append(CoffeeBarrel())
#    player.buildings.append(Wharf(1))
#    player.buildings.append(Office(1))
#    player.buildings.append(SmallMarket(0))    
#    player.buildings.append(CoffeeRoaster(1))
#    player.buildings.append(SugarMill(1))
#    player.buildings.append(SmallIndigoPlant(1))
    player.coins = 100





game.start()

for player in game.players:
    print player.name + ": "+str(player.points)+" points"