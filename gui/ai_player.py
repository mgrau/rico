import sys
sys.path.append('..')

from ai.greedy_player import *
from player import GUI_Player

class GUI_AI_Player(Greedy_Player,GUI_Player):
    def __init__(self,index,name,screen):
        GUI_Player.__init__(self,index,name,screen)
    def choose_role(self,game):
        choice = Greedy_Player.choose_role(self,game)
        self.board.draw(self)
        game.draw(-1)
        return choice
    def settler(self,game):
        choice = Greedy_Player.settler(self,game)
        self.board.draw(self)
        return choice
    def mayor(self,game):
        choice = Greedy_Player.mayor(self,game)
        self.board.draw(self)
        return choice
    def builder(self,game):
        choice = Greedy_Player.builder(self,game)
        self.board.draw(self)
        return choice
    def craftsman(self,game):
        choice = Greedy_Player.craftsman(self,game)
        self.board.draw(self)
        return choice
    def trader(self,game):
        choice = Greedy_Player.trader(self,game)
        self.board.draw(self)
        return choice
    def captain(self,game):
        choice = Greedy_Player.captain(self,game)
        self.board.draw(self)
        return choice
