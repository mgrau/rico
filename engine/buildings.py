class Building:
    def __init__(self, id=-1, colonists=0, cost=0, points=0, capacity=0, size=0, name="",text=""):
        self.id = id
        self.colonists = colonists
        self.cost = cost
        self.points = points
        self.capacity = capacity
        self.size = size
        self.name = name
        self.text = text
    def __repr__(self):
        return self.name+"("+str(self.colonists)+")"
    def __cmp__(self,other):
        return cmp(self.id,other.id)

class VioletBuilding:
    pass
class ProductionBuilding:
    pass

class SmallIndigoPlant(Building,ProductionBuilding):
    def __init__(self,colonists=0):
        Building.__init__(self,id=0,colonists=colonists,cost=1,points=1,capacity=1,size=1,name="Small Indigo Plant")

class SmallSugarMill(Building,ProductionBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=1,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Small Sugar Mill")

class SmallMarket(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=2,colonists=colonists,cost=1,points=1,capacity=1,size=1,name="Small Market",text="+1 doubloon with sale")

class Hacienda(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=3,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Hacienda",text="+1 plantation from supply")

class ConstructionHut(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=4,colonists=colonists,cost=2,points=1,capacity=1,size=1,name="Construction Hut",text="\nquarry instead of plantation")

class SmallWarehouse(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=5,colonists=colonists,cost=3,points=1,capacity=1,size=1,name="Small Warehouse",text="\nstore 1 kind of good")

class IndigoPlant(Building,ProductionBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=6,colonists=colonists,cost=3,points=2,capacity=3,size=1,name="Indigo Plant")

class SugarMill(Building,ProductionBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=7,colonists=colonists,cost=4,points=2,capacity=3,size=1,name="Sugar Mill")

class Hospice(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=8,colonists=colonists,cost=4,points=2,capacity=1,size=1,name="Hospice",text="+1 colonist for settling")

class Office(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=9,colonists=colonists,cost=5,points=2,capacity=1,size=1,name="Office",text="sell same kind of goods")

class LargeMarket(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=10,colonists=colonists,cost=5,points=2,capacity=1,size=1,name="Large Market",text="+2 doubloons with sale")

class LargeWarehouse(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=11,colonists=colonists,cost=6,points=2,capacity=1,size=1,name="Large Warehouse",text="\nstore 2 kinds of goods")

class TobaccoStorage(Building,ProductionBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=12,colonists=colonists,cost=5,points=3,capacity=3,size=1,name="Tobacco Storage")

class CoffeeRoaster(Building,ProductionBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=13,colonists=colonists,cost=6,points=3,capacity=2,size=1,name="Coffee Roaster")

class University(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=14,colonists=colonists,cost=7,points=3,capacity=1,size=1,name="University",text="+1 colonist for building")

class Factory(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=15,colonists=colonists,cost=8,points=3,capacity=1,size=1,name="Factory",text="+0/1/2/3/5 doubloons with production")

class Harbor(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=16,colonists=colonists,cost=8,points=3,capacity=1,size=1,name="Harbor",text="+1 victory point per delivery")

class Wharf(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=17,colonists=colonists,cost=9,points=3,capacity=1,size=1,name="Wharf",text="your own ship")

class GuildHall(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=18,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Guild Hall",text="2 victory points for each large building\n\n1 victory points for each small building")

class Residence(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=19,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Residence",text="4 VP for <10\n5 VP for 10\n6 VP for 11\n7 VP for 12\n occupied island spaces")

class Fortress(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=20,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Fortress",text="1 victory point for every 3 colonists")

class CustomsHouse(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=21,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="Customs House",text="\n1 victory point for every 4 victory point chip")

class CityHall(Building,VioletBuilding):
    def __init__(self, colonists=0):
        Building.__init__(self,id=22,colonists=colonists,cost=10,points=4,capacity=1,size=2,name="City Hall",text="1 victory point for each violet building")