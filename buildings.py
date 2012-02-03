class Building:
    def __init__(self, id=-1, colonists=0, cost=0, points=0, capacity=0, size=0, name=""):
        self.id = id
        self.colonists = colonists
        self.cost = cost
        self.points = points
        self.capacity = capacity
        self.size = size
        self.name = name
    def __repr__(self):
        return self.name+"("+str(self.colonists)+")"
    def __cmp__(self,other):
        return cmp(self.id,other.id)

class SmallIndigoPlant(Building):
    def __init__(self,colonists=0):
        Building.__init__(self,id=0,colonists=colonists,cost=1,points=1,capacity=1,size=1,name="Small Indigo Plant")

class SmallSugarMill(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=1,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Small Sugar Mill")

class SmallMarket(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=2,colonists=colonists,cost=1,points=1,capacity=1,size=1,name="Small Market")

class Hacienda(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=3,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Hacienda")

class ConstructionHut(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=4,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Construction Hut")

class SmallWarehouse(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=5,colonists=colonists,cost=3,points=1,capacity=1,size=1,name="Small Warehouse")

class IndigoPlant(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=6,colonists=colonists,cost=3,points=2,capacity=3,size=1,name="Indigo Plant")

class SugarMill(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=7,colonists=colonists,cost=4,points=2,capacity=3,size=1,name="Sugar Mill")

class Hospice(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=8,colonists=colonists,cost=4,points=2,capacity=1,size=1,name="Hospice")

class Office(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=9,colonists=colonists,cost=5,points=2,capacity=1,size=1,name="Office")

class LargeMarket(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=10,colonists=colonists,cost=5,points=2,capacity=1,size=1,name="Large Market")

class LargeWarehouse(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=11,colonists=colonists,cost=6,points=2,capacity=1,size=1,name="Large Warehouse")

class TobaccoStorage(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=12,colonists=colonists,cost=5,points=3,capacity=3,size=1,name="Tobacco Storage")

class CoffeeRoaster(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=13,colonists=colonists,cost=6,points=3,capacity=2,size=1,name="Coffee Roaster")

class University(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=14,colonists=colonists,cost=7,points=3,capacity=1,size=1,name="University")

class Factory(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=15,colonists=colonists,cost=8,points=3,capacity=1,size=1,name="Factory")

class Harbor(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=16,colonists=colonists,cost=8,points=3,capacity=1,size=1,name="Harbor")

class Wharf(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=17,colonists=colonists,cost=9,points=3,capacity=1,size=1,name="Wharf")

class GuildHall(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=18,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Guild Hall")

class Residence(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=19,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Residence")

class Fortress(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=20,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Fortress")

class CustomsHouse(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=21,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Customs House")

class CityHall(Building):
    def __init__(self, colonists=0):
        Building.__init__(self,id=22,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="City Hall")