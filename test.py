from human_player import *

test = Game()
test.players.append(Human_Player(0,"Matt"))
test.players.append(Human_Player(1,"Amy"))
test.players.append(Human_Player(2,"Dan"))
test.setup()
test.do_round()