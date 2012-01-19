qua, cor, ind, sug, tob, cof = range(6)
err, smind, smsug, smmar, hac, conhut, smwar, indpl, sugmi, hospi, offic, lgmar, lgwar, tobst, cofro, unive, facto, harbo, wharf = range(19)

class Player:
	def __init__(self):
		self.coins = 0
		self.points = 0
		self.goods = [0, 0, 0, 0, 0]
		self.plantations = []
		self.buildings = []
		self.san_juan = 0;
		
	
		
	def get_plantation(self,type=0):
		if len(self.plantations)<12
			self.plantations.append(Plantation(type=type))
	
	def get_building(self,type=0):
		self.buildings.append(Building(type=type))
		
	def afford_building(self,type=0):
		b = Building(type=type)
		if self.coins >= b.cost:
			return True
		else:
			return False
			
	def buy_building(self,type=0):
		if not(self.have_building(type=type)):
			if self.afford_building(type=type):
				self.get_building(type=type)
				self.coins -= self.buildings[-1].cost
				if self.use_building(unive)
					self.buildings[-1].colonists=1
				return True
		return False

	def have_plantation(self,type=0):
		return type in [plantation.type for plantation in self.plantations]
			
	def have_building(self,type=0):
		return type in [building.type for building in self.buildings]
		
	def use_building(self,type=0):
		types = [building.type for building in self.buildings]
		if type in types:
				return self.buildings[types.index(type)].colonists
		else:
			return 0
		
	def colonists(self):
		colonists = reduce(lambda a,b: a+b.colonists,self.plantations,0)
		colonists += reduce(lambda a,b: a+b.colonists,self.buildings,0)
		return colonists
		
	def open_plantations(self):
		return sum([1*(plantation.colonists==0) for plantation in self.plantations])
		
	def open_buildings(self):
		return sum([1*(building.colonists==0) for building in self.buildings])
		
	def open_spots(self):
		return self.open_buildings() + self.open_plantations()
		
	
class Plantation:
	def __init__(self,type=0,colonists=0):
		self.type = type
		self.colonists = colonists
	
	def __repr__(self):
		if self.type == 1:
			return "corn("+str(self.colonists)+")"
		elif self.type == 2:
			return "indigo("+str(self.colonists)+")"
		elif self.type == 3:
			return "sugar("+str(self.colonists)+")"
		elif self.type == 4:
			return "tobacco("+str(self.colonists)+")"
		elif self.type == 5:
			return "coffee("+str(self.colonists)+")"
		else:
			return "quarry("+str(self.colonists)+")"
	
class Building:
	def __init__(self,type=0,colonists=0):
		self.type = type
		self.colonists = colonists
		self.cost = 0
		self.points = 0
		if self.type == 1:
			self.cost = 1
			self.points = 1		
		elif self.type == 2:
			self.cost = 2
			self.points = 1
		elif self.type == 3:
			self.cost = 1
			self.points = 1
		elif self.type == 4:
			self.cost = 2
			self.points = 1
		elif self.type == 5:
			self.cost = 2
			self.points = 1
		elif self.type == 6:
			self.cost = 3
			self.points = 1
		elif self.type == 7:
			self.cost = 3
			self.points = 2
		elif self.type == 8:
			self.cost = 4
			self.points = 2
		elif self.type == 9:
			self.cost = 4
			self.points = 2
		elif self.type == 10:
			self.cost = 5
			self.points = 2
		elif self.type == 11:
			self.cost = 5
			self.points = 2
		elif self.type == 12:
			self.cost = 6
			self.points = 2
		elif self.type == 13:
			self.cost = 5
			self.points = 3
		elif self.type == 14:
			self.cost = 6
			self.points = 3
		elif self.type == 15:
			self.cost = 7
			self.points = 3
		elif self.type == 16:
			self.cost = 8
			self.points = 3
		elif self.type == 17:
			self.cost = 8
			self.points = 3
		elif self.type == 18:
			self.cost = 9
			self.points = 3

	def __repr__(self):
		if self.type == 1:
			return "small indigo plant("+str(self.colonists)+")"
		elif self.type == 2:
			return "small sugar mill("+str(self.colonists)+")"
		elif self.type == 3:
			return "small market("+str(self.colonists)+")"
		elif self.type == 4:
			return "hacienda("+str(self.colonists)+")"
		elif self.type == 5:
			return "construction hut("+str(self.colonists)+")"
		elif self.type == 6:
			return "small warehouse("+str(self.colonists)+")"
		elif self.type == 7:
			return "indigo plant("+str(self.colonists)+")"
		elif self.type == 8:
			return "sugar mill("+str(self.colonists)+")"
		elif self.type == 9:
			return "hospice("+str(self.colonists)+")"
		elif self.type == 10:
			return "office("+str(self.colonists)+")"
		elif self.type == 11:
			return "large market("+str(self.colonists)+")"
		elif self.type == 12:
			return "large warehouse("+str(self.colonists)+")"
		elif self.type == 13:
			return "tobacco storage("+str(self.colonists)+")"
		elif self.type == 14:
			return "coffee roaster("+str(self.colonists)+")"
		elif self.type == 15:
			return "university("+str(self.colonists)+")"
		elif self.type == 16:
			return "factory("+str(self.colonists)+")"
		elif self.type == 17:
			return "harbor("+str(self.colonists)+")"
		elif self.type == 18:
			return "wharf("+str(self.colonists)+")"
		else:
			return "error()"
