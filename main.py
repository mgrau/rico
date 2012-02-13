import pygame
try:
    import android
except ImportError:
    android = None
    
screen = pygame.display.set_mode( (800,600) )

from gui_game import GUI_Game
from gui_player import GUI_Player
import tiles

def main():
    pygame.init()
    tiles.convert_all()
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    game = GUI_Game(screen.get_size())
    game.players.append(GUI_Player(0,"Matt",screen))
    game.players.append(GUI_Player(1,"Amy",screen))
    game.players.append(GUI_Player(2,"Dan",screen))
    game.setup()
    game.start()

if __name__ == '__main__':
    main()