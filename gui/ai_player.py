import sys
sys.path.append('..')

from ai.ai_player import *
from player import GUI_Player

class GUI_Random_Player(Random_Player,GUI_Player):
    def __init__(self,index,name,screen):
        GUI_Player.__init__(self,index,name,screen)