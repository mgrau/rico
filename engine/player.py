from game import *
from ships import *

class Player:
    def __init__(self,index,name):
        self.name = name
        self.index = index
        self.wharf = WharfShip()
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
        self.roles = []


    def choose_role(self,game):
        return 0

    def settler(self,game):
        return 0

    def mayor(self,game):
        self.distribute_colonists()
        return

    def builder(self,game):
        return -1

    def craftsman(self,game):
        if len(self.goods):
            return self.goods[0]
        else:
            return Barrel()

    def trader(self,game):
        return Barrel()

    def captain(self,game):
        return

    def rot(self,game):
        return

    def discount(self,building=Building()):
        discount = sum([plantation.colonists*isinstance(plantation,Quarry) for plantation in self.plantations])
        discount = min(discount,building.points) # you can't use more quarries than points the building is worth
        if len(self.roles):
            if isinstance(self.roles[-1],Builder):
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
        colonists += sum([plantation.colonists for plantation in self.plantations])
        colonists += sum([building.colonists for building in self.buildings])
        return colonists

    def distribute_colonists(self):
        #Lower priority means it gets colonists first
        priority_dict={"quarry":2,
                       "corn":2,
                       "indigo":7,
                       "sugar":5,
                       "tobacco":4,
                       "coffee":4,
                       "Small Indigo Plant":7,
                       "Small Sugar Mill":5,
                       "Small Market":2,
                       "Hacienda":2,
                       "Construction Hut":4,
                       "Small Warehouse":2,
                       "Indigo Plant":8,
                       "Sugar Mill":6,
                       "Hospice":3,
                       "Office":3,
                       "Large Market":1,
                       "Large Warehouse":3,
                       "Tobacco Storage":4,
                       "Coffee Roaster":3,
                       "University":3,
                       "Factory":1,
                       "Harbor":2,
                       "Wharf":1,
                       "Guild Hall":1,
                       "Residence":1,
                       "Fortress":1,
                       "Customs House":1,
                       "City Hall":1}
        employers=self.buildings
        employers.append(self.plantations)
        priority_employer_tuples=[(priority_dict[x.name],x) for x in employers].sort()
        for employer_tuple in priority_employer_tuples:
            employer=employer_tuple[1]
            capacity=1
            if isinstance(employer,Building):
                capacity=building.capacity
            if employer.colonists < capacity and self.san_juan>0:
                employer.colonists += max(self.san_juan,capacity-employer.colonists)
                self.san_juan -= max(self.san_juan,capacity-employer.colonists)

    def open_plantations(self):
        return sum([(1-plantation.colonists) for plantation in self.plantations])
    
    def open_buildings(self):
        return sum([(building.capacity-building.colonists) for building in self.buildings])

    def open_spots(self):
        return self.open_buildings() + self.open_plantations()
    
    def total_points(self):
        points = self.points # the victory point chips
        points += sum([building.points for building in self.buildings]) # points for the buildings in the city

        # now add points for any prestige buildings iff they have a colonist
        if self.use_building(GuildHall):
            for building_type in [SmallIndigoPlant, SmallSugarMill]:
                if self.have_building(building_type):
                    points += 1 # one point for the small production buildings
            for building_type in [IndigoPlant, SugarMill, TobaccoStorage, CoffeeRoaster]:
                if self.have_building(building_type):
                    points += 2 # two points for the large production buildings
        if self.use_building(Residence):
            points += min(len(self.plantations)-5,4)
        if self.use_building(Fortress):
            points += self.colonists()/3 # 1 point for every 3 colonists
        if self.use_building(CustomsHouse):
            points += int(self.points/4) # 1 point for every 4 victory point chips
        if self.use_building(CityHall):
            for building in self.buildings:
                # victory point for each violet building (large production buildings have non unity capacities)
                if building.capacity==1 and not isinstance(building,SmallIndigoPlant) and not isinstance(building,SmallSugarMill):
                    points += 1
        return points

