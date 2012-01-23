from buildings import *

class Role:
	def __init__(self,name=""):
		self.coins = 0
		self.name = name
	def __repr__(self):
		return self.name+"("+str(self.coins)+")"
	def __call__(self,Game,index):
		return

class Settler(Role):
	def __init__(self):
		Role.__init__(self,name="Settler")
	def __call__(self,game,index):
		print "Settler Phase"
		for player in game.players[index:] + game.players[:index]:
			if len(player.plantations) < 12:
				print player.name
				choice = []
				if len(game.quarries)>0 and (player.index == index or player.use_building(ConstructionHut)):
					while choice not in range(len(game.plantations)+1):
						choice = player.settler(game,index)
						if choice not in range(len(game.plantations)+1):
							print "invalid choice"
				else:
					while choice not in range(len(game.plantations)):
						choice = player.settler(game,index)
						if choice not in range(len(game.plantations)):
							print "invalid choice"
				print choice
				if choice == len(game.plantations):
					player.plantations.append(game.quarries.pop())
				else:
					player.plantations.append(game.plantations.pop(choice))
				if player.use_building(Hospice) and game.colonists:
					player.plantations[-1].colonists = 1
					game.colonists -= 1
			game.draw_plantations()


class Mayor(Role):
	def __init__(self):
		Role.__init__(self,name="Mayor")
	def __call__(self,game,index):
		if game.colonists > 0:
			game.players[index].san_juan += 1
			game.colonists -= 1
		i = index
		while game.colonist_ship > 0:
			game.players[i].san_juan += 1
			game.colonist_ship -= 1
			i += 1
			if i >= len(game.players):
				i = 0
		for player in game.players[index:] + game.players[:index]:
			player.mayor(game,index)
		game.fill_colonist_ship()

			
class Builder(Role):
	def __init__(self):
		Role.__init__(self,name="Builder")
	def __call__(self,Game,index):
		return
		
		
class Craftsman(Role):
	def __init__(self):
		Role.__init__(self,name="Craftsman")
	def __call__(self,Game,index):
		return

class Trader(Role):
	def __init__(self):
		Role.__init__(self,name="Trade")
	def __call__(self,Game,index):
		return

class Captain(Role):
	def __init__(self):
		Role.__init__(self,name="Captain")
	def __call__(self,Game,index):
		return

class Prospector(Role):
	def __init__(self):
		Role.__init__(self,name="Prospector")
	def __call__(self,game,index):
		game.players[index].coins += 1