import pygame
try:
    import android
except ImportError:
    android = None
    
screen = pygame.display.set_mode( (800,600) )

from gui.game import GUI_Game
from gui.player import GUI_Player
from gui.ai_player import GUI_Random_Player
import gui.tiles
from gui.start_screen import Start_Screen

def main():
    pygame.init()
    gui.tiles.convert_all()
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    start_screen = Start_Screen(screen)
    start_screen.draw()
    players = start_screen.get_player()

    game = GUI_Game(screen)
    for i,player in enumerate(players):
        name = player[0]
        ai = player[1]
        invert = player[2]
        if name is not None:
            if ai:
                game.players.append(GUI_Random_Player(i,name,screen))
            else:
                game.players.append(GUI_Player(i,name,screen,invert))
    if len(game.players)>=2:
        game.setup()
        game.draw(0)
        game.start()
        game.draw_scores()
        valid_input = False
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    valid_input = True

if __name__ == '__main__':
    main()