from buildings import *

class Role:
	def __init__(self,name=""):
		self.coins = 0
		self.name = name
	def __repr__(self):
		return self.name+"("+str(self.coins)+")"
	def __call__(self,game):
		return

class Settler(Role):
	def __init__(self):
		Role.__init__(self,name="Settler")
		
	def __call__(self,game):
		print "Settler Phase"
		for player in game.players[game.current_player:] + game.players[:game.current_player]:
			if len(player.plantations) < 12:
				if len(game.quarries)>0 and (player.index == game.current_player or player.use_building(ConstructionHut)):
					choice = player.settler(game)
					while choice not in range(len(game.plantations)+1):
						print "invalid choice"
						choice = player.settler(game)
				else:
					choice = player.settler(game)
					while choice not in range(len(game.plantations)):
						print "invalid choice"
						choice = player.settler(game)
				if choice == len(game.plantations):
					player.plantations.append(game.quarries.pop())
				else:
					player.plantations.append(game.plantations.pop(choice))
				if player.use_building(Hospice) and game.colonists:
					player.plantations[-1].colonists = 1
					game.colonists -= 1
		game.plantation_discard += game.plantations
		game.plantations = []
		game.draw_plantations()


class Mayor(Role):
	def __init__(self):
		Role.__init__(self,name="Mayor")
		
	def __call__(self,game):
		print "Mayor Phase"
		if game.colonists > 0:
			game.players[game.current_player].san_juan += 1
			game.colonists -= 1
		i = game.current_player
		while game.colonist_ship > 0:
			game.players[i].san_juan += 1
			game.colonist_ship -= 1
			i += 1
			if i >= len(game.players):
				i = 0
		for player in game.players[game.current_player:] + game.players[:game.current_player]:
			player.mayor(game)
		game.fill_colonist_ship()

			
class Builder(Role):
	def __init__(self):
		Role.__init__(self,name="Builder")
	def __call__(self,game):
		print "Builder Phase"
		for player in game.players[game.current_player:] + game.players[:game.current_player]:
			if not(player.city_full()):
				choice = player.builder(game)
				while choice not in range(len(game.buildings)):
					print "invalid choice"
					choice = player.builder(game)
				print choice
				player.buildings.append(game.buildings.pop(choice))
				player.coins -= player.buildings[-1].cost
				if player.use_building(University) and game.colonists:
					player.buildings[-1].colonists = 1
					game.colonists -= 1
		
class Craftsman(Role):
	def __init__(self):
		Role.__init__(self,name="Craftsman")
	def __call__(self,game):
		print "Craftsman Phase"
		for player in game.players[game.current_player:] + game.players[:game.current_player]:
			goods_wanted = player.produce_goods()
			for good in goods_wanted:
				if good in game.goods:
					game.goods.remove(good)
					player.goods.append(good)
			good = game.players[game.current_player].craftsman()
			if good in game.players[game.current_player].goods:
				game.goods.remove(good)
				game.players[game.current_player].goods.append(good)

class Trader(Role):
	def __init__(self):
		Role.__init__(self,name="Trade")
	def __call__(self,game):
		print "Trader Phase"
		for player in game.players[game.current_player:] + game.players[:game.current_player]:
			good = player.trader()
			if good in player.goods:
				if length(game.trading_house)<4:
					if player.use_building(Office) or (good not in game.trading_house):
							player.goods.remove(good)
							game.trading_house.append(good)
				
		if length(game.trading_house)>=4:
			game.goods += game.trading_house
			game.trading_house = []

class Captain(Role):
	def __init__(self):
		Role.__init__(self,name="Captain")
	def __call__(self,game):
		return

class Prospector(Role):
	def __init__(self):
		Role.__init__(self,name="Prospector")
		
	def __call__(self,game):
		game.players[game.current_player].coins += 1