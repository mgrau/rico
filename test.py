import game
from player import Player

test = game.Game()
test.players.append(Player(0,"Matt"))
test.players.append(Player(1,"Amy"))
test.players.append(Player(2,"Dan"))
test.setup()
test.do_round()