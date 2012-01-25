from plantations import *
from buildings import *
from game import *

class Player:
	def __init__(self,index=0,name=""):
		self.name = name
		self.index = index
		self.reset()
		
	def __repr__(self):
		return  "\n"+self.name+"\n"+\
				"coins: "+str(self.coins)+"\n"+\
				"points: "+str(self.points)+"\n"+\
				"plantations: "+str(self.plantations)+"\n"+\
				"buildings: "+str(self.buildings)
	
	def reset(self):
		self.coins = 0
		self.points = 0
		self.goods = []
		self.plantations = []
		self.buildings = []
		self.san_juan = 0;
    
	def choose_role(self,game):
		print "\n"+self.name+"'s Turn"
		print "choose a role:"
		for i,role in enumerate(game.roles):
			print str(i)+": "+str(role)
		choice = []
		while choice not in [str(i) for i in range(len(game.roles))]:
			choice = raw_input("choice? ")
  		return int(choice)
  		
  	def settler(self,game):
  		print "\n"+self.name+" choose a plantation"
  		if self.index==game.current_player or self.use_building(ConstructionHut):
  			for i,plantation in enumerate(game.plantations+[Quarry()]):
	  			print str(i)+": "+str(plantation)
  		else: 
	  		for i,plantation in enumerate(game.plantations):
	  			print str(i)+": "+str(plantation)
	  	choice = []
  		if self.index==game.current_player or self.use_building(ConstructionHut):
	  		while choice not in [str(i) for i in range(len(game.plantations)+1)]:
				choice = raw_input("choice? ")
  		else:
			while choice not in [str(i) for i in range(len(game.plantations))]:
				choice = raw_input("choice? ")
  		return int(choice)
  		
  	def mayor(self,game):
  		return

  	def builder(self,game):
  		return
  		
	def craftsman(self,game):
  		return
  		
	def trader(self,game):
  		return
  		
	def captain(self,game):
  		return	
 
	def get_plantation(self,plantation):
		if len(self.plantations)<12:
			self.plantations.append(plantation)
		if self.use_building(Hospice):
			self.plantations[-1].colonists=1
	
	def get_building(self,building_type=Building):
		self.buildings.append(building_type())
		
	def afford_building(self,building_type=Building):
		b = building_type()
		return self.coins >= b.cost
			
	def buy_building(self,building_type=Building):
		if not(self.have_building(building_type)):
			if self.afford_building(building_type):
				self.get_building(building_type)
				self.coins -= self.buildings[-1].cost
				if self.use_building(University):
					self.buildings[-1].colonists=1
				return True
		return False

	def have_plantation(self,plantation_type=Plantation):
		return any([isinstance(plantation,plantation_type) for plantation in self.plantations])
			
	def have_building(self,building_type=Building):
		return any([isinstance(building,building_type) for building in self.buildings])
		
	def use_building(self,building_type=Building):
		if self.have_building(building_type):
			return self.buildings[[isinstance(building,Building) for building in self.buildings].index(True)].colonists > 0
		else:
			return False
			
	def city_full(self):
		return False
		
	def island_full(self):
		return False
		
	def colonists(self):
		colonists = self.san_juan
		colonists += reduce(lambda a,b: a+b.colonists,self.plantations,0)
		colonists += reduce(lambda a,b: a+b.colonists,self.buildings,0)
		return colonists
		
	def open_plantations(self):
		return sum([(1-plantation.colonists) for plantation in self.plantations])
		
	def open_buildings(self):
		return sum([building.capacity-building.colonists for building in self.buildings])
		
	def open_spots(self):
		return self.open_buildings() + self.open_plantations()