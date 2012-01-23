from player import *
from buildings import *
from roles import *
from random import shuffle

class Game:
	def __init__(self,player_names=[""]):
		self.players = []
		for index,name in enumerate(player_names):
			self.players.append(Player(index,name))
		self.turn = 1
		self.governor = 0
		
		self.quarries = [Quarry()]*8

		
		if len(self.players)==3:
			self.points = 75
			self.colonists = 55
			self.roles = [Settler(),Mayor(),Builder(),Craftsman(),Trader(),Captain()]
			split = 2
		elif len(self.players)==4:
			self.points = 100
			self.colonists = 75
			self.roles = [Settler(),Mayor(),Builder(),Craftsman(),Trader(),Captain(),Prospector()]
			split = 2
		elif len(self.players)==5:
			self.points = 112
			self.colonists = 95
			self.roles = [Settler(),Mayor(),Builder(),Craftsman(),Trader(),Captain(),Prospector()]
			split = 3
		else:
			print "wrong number of players"
			
		self.colonist_ship = len(self.players)
		self.colonists -= len(self.players)
			
		self.plantation_deck = [Coffee()]*8+[Tobacco()]*9+[Sugar()]*11+[Indigo()]*(12-split)+[Corn()]*(10-(len(self.players))-split)
		self.plantation_discard = []
		shuffle(self.plantation_deck)
		self.plantations = []
		self.draw_plantations()
		
		for player in self.players[:split]:
			player.coins = len(self.players)-1
			player.plantations.append(Indigo())
		for player in self.players[split:]:
			player.coins = len(self.players)-2
			player.plantations.append(Corn())
			
	def __repr__(self):
			return  "::Rico::\n"+\
				"turn: "+str(self.turn)+"\n"+\
				"points: "+str(self.points)+"\n"+\
				"colonists: "+str(self.colonists)+"\n"+\
				"governor: "+self.players[self.governor].name+"\n"+\
				"players: "+str(self.players)
			
	def draw_plantations(self):
		if len(self.plantation_deck)<len(self.players)+1):
			shuffle(self.plantation_discard)
			self.plantation_deck += self.plantation_discard
			self.plantation_discard = []
		for i in range(len(self.players)+1):
			self.plantations.append(self.plantation_deck.pop())
		
	def do_round(self):
		for player in self.players[self.governor:]+self.players[:self.governor]:
			choice = []
			while choice not in range(len(self.roles)): 
				choice = player.choose_role(self)
			player.role = self.roles.pop(int(choice))		
			player.coins += player.role.coins
			player.role.coins = 0
			player.role(self,player.index)
			
		self.governor += 1
		if self.governor >= len(self.players):
			self.governor = 0
			
		for role in self.roles:
			role.coins += 1
		for player in self.players:
			self.roles.append(player.role)
			player.role = Role()
		self.roles.sort()	
		self.turn += 1