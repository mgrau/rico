from human_player import *

game = Game()
game.players.append(Human_Player(0,"Matt"))
game.players.append(Human_Player(1,"Amy"))
game.players.append(Human_Player(2,"Dan"))
game.setup()

while not game.game_end():
    game.round()