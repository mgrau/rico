from human_player import *

game = Game()
game.players.append(Human_Player(0,"Matt"))
game.players.append(Human_Player(1,"Amy"))
game.players.append(Human_Player(2,"Dan"))
game.setup()

from barrels import *
for player in game.players:
    for i in range(3):
        player.goods.append(CornBarrel())
        player.goods.append(IndigoBarrel())
        player.goods.append(SugarBarrel())
        player.goods.append(CoffeeBarrel())
    player.buildings.append(Wharf(1))

while not game.game_end():
    game.round()

for player in game.players:
    print player.name + ": "+str(player.points)+" points"