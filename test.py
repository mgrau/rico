import pygame

screen = pygame.display.set_mode( (800,600) )

from gui_game import GUI_Game
from gui_player import GUI_Player
from text_player import *
import tiles

tiles.convert_all()
game = GUI_Game(screen.get_size())
game.players.append(GUI_Player(0,"Matt",screen))
game.players.append(GUI_Player(1,"Amy",screen))
#game.players.append(GUI_Player(2,"Dan",screen))
game.setup()

from barrels import *
from plantations import *
from buildings import *
for player in game.players:
    for i in range(3):
        player.goods.append(CornBarrel())
        player.goods.append(IndigoBarrel())
        player.goods.append(SugarBarrel())
        player.goods.append(TobaccoBarrel())
        player.goods.append(CoffeeBarrel())
    player.buildings.append(Wharf(1))
    player.buildings.append(Office(1))
    player.buildings.append(SmallMarket(0))
    player.buildings.append(CoffeeRoaster(1))
    player.buildings.append(SugarMill(1))
    player.buildings.append(SmallIndigoPlant(1))
    player.coins = 100
game.start()

for player in game.players:
    print player.name + ": "+str(player.points)+" points"