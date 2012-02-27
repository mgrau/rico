#!/usr/bin/python
import pygame
try:
    import android
except ImportError:
    android = None

screen = pygame.display.set_mode( (800,600) )

from gui.game import GUI_Game
from gui.player import GUI_Player
from gui.ai_player import GUI_AI_Player
import gui.tiles
from gui.start_screen import Start_Screen

def main():
    pygame.init()
    gui.tiles.convert_all()

    players = [("Matt",True,False),("Dan",True,False),("Amy",True,False),("Maya",True,False)]
    game = GUI_Game(screen)
    for i,player in enumerate(players):
        name = player[0]
        ai = player[1]
        invert = player[2]
        if name is not None:
            if ai:
                game.players.append(GUI_AI_Player(i,name,screen))
            else:
                game.players.append(GUI_Player(i,name,screen,invert))

    if len(game.players)>=2:
        game.setup()

#        for player in game.players:
#            for i in range(3):
#                player.goods.append(CornBarrel())
#                player.goods.append(IndigoBarrel())
#                player.goods.append(SugarBarrel())
#                player.goods.append(TobaccoBarrel())
#                player.goods.append(CoffeeBarrel())
#            player.buildings.append(Wharf(1))
#            player.buildings.append(SmallMarket(0))
#            player.buildings.append(CoffeeRoaster(1))
#            player.buildings.append(SugarMill(1))
#            player.buildings.append(SmallIndigoPlant(1))
#            player.buildings.append(SmallWarehouse(1))
#            player.buildings.append(LargeWarehouse(1))
#            player.coins = 99
        game.draw(0)
        game.start()

        game.draw(0)
        game.start()
        game.draw_scores()
        valid_input = False
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    valid_input = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        valid_input = True

if __name__ == '__main__':
    main()




        
