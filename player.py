from game import *

class Player:
    def __init__(self,index=0,name=""):
        self.name = name
        self.index = index
        self.reset()

    def __repr__(self):
        return  "\n"+self.name+"\n"+\
                "coins: "+str(self.coins)+"\n"+\
                "san juan: "+str(self.san_juan)+"\n"+\
                "plantations: "+str(self.plantations)+"\n"+\
                "buildings: "+str(self.buildings)+"\n"+\
                "goods: "+str(self.goods)

    def reset(self):
        self.coins = 0
        self.points = 0
        self.goods = []
        self.plantations = []
        self.buildings = []
        self.san_juan = 0
        self.role = Role()

    def choose_role(self,game):
        return game.UI.choose_role(game, self)

    def settler(self,game):
        return

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

    def discount(self,building=Building()):
        discount = sum([plantation.colonists*isinstance(plantation,Quarry) for plantation in self.plantations])
        discount = min(discount,building.points) # you can't use more quarries than points the building is worth
        if isinstance(self.role,Builder):
            discount+=1
        return discount

    def afford_building(self,building=Building()):
        return self.coins >= (building.cost-self.discount(building))

    def have_plantation(self,plantation_type=Plantation):
        return any([isinstance(plantation,plantation_type) for plantation in self.plantations])

    def have_building(self,building_type=Building):
        return any([isinstance(building,building_type) for building in self.buildings])

    def use_building(self,building_type=Building):
        if self.have_building(building_type):
            return self.buildings[[isinstance(building,building_type) for building in self.buildings].index(True)].colonists
        else:
            return False

    def produce_goods(self):
        num_corn = sum([plantation.colonists*isinstance(plantation,Corn) for plantation in self.plantations])
        num_indigo = sum([plantation.colonists*isinstance(plantation,Indigo) for plantation in self.plantations])
        num_sugar = sum([plantation.colonists*isinstance(plantation,Sugar) for plantation in self.plantations])
        num_tobacco = sum([plantation.colonists*isinstance(plantation,Tobacco) for plantation in self.plantations])
        num_coffee = sum([plantation.colonists*isinstance(plantation,Coffee) for plantation in self.plantations])

        num_indigo = min(num_indigo,self.use_building(SmallIndigoPlant)+self.use_building(IndigoPlant))
        num_sugar = min(num_sugar,self.use_building(SmallSugarMill)+self.use_building(SugarMill))
        num_tobacco = min(num_tobacco,self.use_building(TobaccoStorage))
        num_coffee = min(num_coffee,self.use_building(CoffeeRoaster))

        return [CornBarrel() for i in range(num_corn)]+[IndigoBarrel() for i in range(num_indigo)]+[SugarBarrel() for i in range(num_sugar)]+[TobaccoBarrel() for i in range(num_tobacco)]+[CoffeeBarrel() for i in range(num_coffee)]

    def city_full(self):
        return sum([building.size for building in self.buildings]) >= 12

    def island_full(self):
        return len(self.plantations) >= 12

    def colonists(self):
        colonists = self.san_juan
        colonists += reduce(lambda a,b: a+b.colonists,self.plantations,0)
        colonists += reduce(lambda a,b: a+b.colonists,self.buildings,0)
        return colonists

    def open_plantations(self):
        return sum([(1-plantation.colonists) for plantation in self.plantations])

    def open_buildings(self):
        return sum([(building.capacity-building.colonists) for building in self.buildings])

    def open_spots(self):
        return self.open_buildings() + self.open_plantations()

    def total_points(self):
        return self.points + sum([building.points for building in self.buildings]) # + prestige buildings
