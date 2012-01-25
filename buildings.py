class Building:
	def __init__(self, colonists=0, cost=0, points=0, capacity=0, size=0, name=""):
		self.colonists = colonists
		self.cost = cost
		self.points = points
		self.capacity = capacity
		self.size = size
		self.name = name
	def __repr__(self):
		return self.name+"("+str(self.colonists)+")"

		
class SmallIndigoPlant(Building):
	def __init__(self,colonists=0):
		Building.__init__(self,colonists=colonists,cost=1,points=1,capacity=1,size=1,name="sm_indigo")

class SmallSugarMill(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="sm_sugar")
		
class SmallMarket(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=1,points=1,capacity=1,size=1,name="sm_market")
		
class Hacienda(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="hacienda")
		
class ConstructionHut(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="con_hut")
		
class SmallWarehouse(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=3,points=1,capacity=1,size=1,name="sm_warehouse")
		
class IndigoPlant(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=3,points=2,capacity=31,size=1,name="lg_indigo")
		
class SugarMill(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=4,points=2,capacity=3,size=1,name="lg_sugar")
		
class Hospice(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=4,points=2,capacity=1,size=1,name="hospice")
		
class Office(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=5,points=2,capacity=1,size=1,name="office")
		
class LargeMarket(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=5,points=2,capacity=1,size=1,name="lg_market")
		
class LargeWarehouse(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=6,points=2,capacity=1,size=1,name="lq_warehouse")
		
class TobaccoStorage(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=5,points=3,capacity=3,size=1,name="tob_store")
		
class CoffeeRoaster(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=6,points=3,capacity=3,size=1,name="cof_roast")
		
class University(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=7,points=3,capacity=1,size=1,name="university")
		
class Factory(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=8,points=3,capacity=1,size=1,name="factory")
		
class Harbor(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=8,points=3,capacity=1,size=1,name="harbor")
		
class Wharf(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=9,points=3,capacity=1,size=1,name="wharf")
		
class GuildHall(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="guild_hall")
		
class Residence(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="residence")
		
class Fortress(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="fortress")
		
class CustomsHouse(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="customs")
		
class CityHall(Building):
	def __init__(self, colonists=0):
		Building.__init__(self,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="city_hall")