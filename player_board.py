import pygame
from plantations import *
from buildings import *
from roles import *

gray = pygame.Color(0,0,0,10)
brown = pygame.Color(128,40,40)
magenta = pygame.Color(236,0,140)

island = pygame.image.load('res/island.png').convert()
pygame.font.init()
h1 = pygame.font.Font('res/fertigo.ttf',45)
font = pygame.font.Font('res/fertigo.ttf',18)

quarry = pygame.image.load('res/quarry.png').convert()
corn = pygame.image.load('res/corn.png').convert()
indigo = pygame.image.load('res/indigo.png').convert()
sugar = pygame.image.load('res/sugar.png').convert()
tobacco = pygame.image.load('res/tobacco.png').convert()
coffee = pygame.image.load('res/coffee.png').convert()
#quarry.set_colorkey(quarry.get_at((0,0)))
corn.set_colorkey(corn.get_at((0,0)))
#indigo.set_colorkey(indigo.get_at((0,0)))
#sugar.set_colorkey(sugar.get_at((0,0)))
#tobacco.set_colorkey(tobacco.get_at((0,0)))
#coffee.set_colorkey(coffee.get_at((0,0)))

corn_barrel = pygame.image.load('res/corn_barrel.png').convert()
indigo_barrel = pygame.image.load('res/indigo_barrel.png').convert()
sugar_barrel = pygame.image.load('res/sugar_barrel.png').convert()
tobacco_barrel = pygame.image.load('res/tobacco_barrel.png').convert()
coffee_barrel = pygame.image.load('res/coffee_barrel.png').convert()
corn_barrel.set_colorkey(corn_barrel.get_at((0,0)))
indigo_barrel.set_colorkey(indigo_barrel.get_at((0,0)))
sugar_barrel.set_colorkey(sugar_barrel.get_at((0,0)))
tobacco_barrel.set_colorkey(tobacco_barrel.get_at((0,0)))
coffee_barrel.set_colorkey(coffee_barrel.get_at((0,0)))

small_indigo_plant = pygame.image.load('res/small_indigo_plant.png').convert()
indigo_plant = pygame.image.load('res/indigo_plant.png').convert()
small_sugar_mill = pygame.image.load('res/small_sugar_mill.png').convert()
sugar_mill = pygame.image.load('res/sugar_mill.png').convert()
tobacco_storage = pygame.image.load('res/tobacco_storage.png').convert()
coffee_roaster = pygame.image.load('res/coffee_roaster.png').convert()
small_violet = pygame.image.load('res/small_violet.png').convert()
large_violet = pygame.image.load('res/large_violet.png').convert()

settler_tile = pygame.image.load('res/settler.png').convert()
mayor_tile = pygame.image.load('res/mayor.png').convert()
builder_tile = pygame.image.load('res/builder.png').convert()
craftsman_tile = pygame.image.load('res/craftsman.png').convert()
trader_tile = pygame.image.load('res/trader.png').convert()
captain_tile = pygame.image.load('res/captain.png').convert()
prospector_tile = pygame.image.load('res/prospector.png').convert()
settler_tile.set_colorkey(settler_tile.get_at((0,0)))
mayor_tile.set_colorkey(mayor_tile.get_at((0,0)))
builder_tile.set_colorkey(builder_tile.get_at((0,0)))
craftsman_tile.set_colorkey(craftsman_tile.get_at((0,0)))
trader_tile.set_colorkey(trader_tile.get_at((0,0)))
captain_tile.set_colorkey(captain_tile.get_at((0,0)))
prospector_tile.set_colorkey(prospector_tile.get_at((0,0)))


class Board():
    def __init__(self,size=(1024,768)):
        self.width,self.height = size
        self.surface = pygame.Surface(size)
        padding = 32
        spacing = 6
        size = (96,96)
        self.plantation_grid = []
        for row in [3,2,1,0]:
            for column in [0,1,2]:
                self.plantation_grid.append(pygame.Rect((padding+(size[0]+spacing)*column, self.height*0.8-padding -size[1]-(size[1]+spacing)*row),size))
        size = (154,83)        
        self.building_grid = []
        for row in [2,1,0]:
            for column in [0,1,2,3]:
                self.building_grid.append(pygame.Rect((2*padding + 2*spacing + 3*96+(size[0]+spacing)*column, self.height*0.8-padding -size[1]-(size[1]+spacing)*row),size))
        self.role_grid = []
        for column in range(8):
            self.role_grid.append(pygame.Rect((10+column*128,619),(118,144)))
        self.choose_plantation_grid = []
        for column in range(8):
            self.choose_plantation_grid.append(pygame.Rect((column*128+32,639),(96,96)))
        self.barrel_grid = []
        for column in range(5):
            self.barrel_grid.append(pygame.Rect((2*padding + 2*spacing + 3*96+60*column,250),(50,60)))
        self.choose_barrel_grid = []
        for column in range(5):
            self.choose_barrel_grid.append(pygame.Rect((column*75+32,675),(50,60)))
        
    def draw(self,player,reveal_points=False):
        self.surface.blit(island, (0,0))
        name = h1.render(player.name,1,(255,255,255))
        self.surface.blit(name,(100,32))


        if reveal_points:
            points = h1.render(str(player.points),1,(255,215,0))
            pygame.draw.circle(self.surface, (255,215,0), (64,60), 28)
            pygame.draw.circle(self.surface, (192,0,0), (64,60), 25)
            self.surface.blit(points,(50,31))

        coins = font.render(str(player.coins),1,(0,0,0))
        pygame.draw.circle(self.surface, (119,136,153), (400,200), 23)
        if player.coins >= 5:
            pygame.draw.circle(self.surface, (255,215,0), (400,200), 20)
        else:
            pygame.draw.circle(self.surface, (192,192,192), (400,200), 20)
        self.surface.blit(coins, (395,189))


        if player.san_juan:
            san_juan = font.render(str(player.san_juan),1,(255,255,255))
            pygame.draw.circle(self.surface, brown, (650,160), 15)
            self.surface.blit(san_juan,(645,148))

        if player.role:
            pos = (874,32)
            if isinstance(player.role,Settler):
                self.surface.blit(settler_tile,pos)
            if isinstance(player.role,Mayor):
                self.surface.blit(mayor_tile,pos)
            if isinstance(player.role,Builder):
                self.surface.blit(builder_tile,pos)
            if isinstance(player.role,Craftsman):
                self.surface.blit(craftsman_tile,pos)
            if isinstance(player.role,Trader):
                self.surface.blit(trader_tile,pos)
            if isinstance(player.role,Captain):
                self.surface.blit(captain_tile,pos)
            if isinstance(player.role,Prospector):
                self.surface.blit(prospector_tile,pos)
        
        plantation_space = pygame.Surface((96,96),pygame.SRCALPHA)
        plantation_space.fill(gray)
        building_space= pygame.Surface((154,83),pygame.SRCALPHA)
        building_space.fill(gray)
        
        for rect in self.plantation_grid:
            self.surface.blit(plantation_space,rect)
#            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]-6,rect[1]-6),(6,rect[3]+6)))
#            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0],rect[1]-6),(rect[2]+6,6)))
#            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]+rect[2],rect[1]),(6,rect[3]+6)))
#            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]-6,rect[1]+rect[3]),(rect[2]+6,6)))
            
        for rect in self.building_grid:
            self.surface.blit(building_space,rect)
#            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]-6,rect[1]-6),(6,rect[3]+6)))
#            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0],rect[1]-6),(rect[2]+6,6)))
#            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]+rect[2],rect[1]),(6,rect[3]+6)))
#            pygame.draw.rect(self.surface,(127,127,127),pygame.Rect((rect[0]-6,rect[1]+rect[3]),(rect[2]+6,6)))

        for pos,plantation in zip(self.plantation_grid,player.plantations):
            self.draw_plantation(plantation,pos)

        for pos,building in zip(self.building_grid,player.buildings):
            self.draw_building(building,pos)
        
        for pos,barrel,texture in zip(self.barrel_grid,[CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()],[corn_barrel, indigo_barrel, sugar_barrel, tobacco_barrel, coffee_barrel]):
            if barrel in player.goods:
                amount = font.render(str(reduce(lambda a,b:a+(b==barrel),player.goods,0)),1,(255,255,255))
                self.surface.blit(texture,pos)
                self.surface.blit(amount,(pos[0]+15,pos[1]+12))


    def draw_roles(self,game):
        for pos,role in zip(self.role_grid,game.roles):
            if isinstance(role,Settler):
                self.surface.blit(settler_tile,pos)
            if isinstance(role,Mayor):
                self.surface.blit(mayor_tile,pos)
            if isinstance(role,Builder):
                self.surface.blit(builder_tile,pos)
            if isinstance(role,Craftsman):
                self.surface.blit(craftsman_tile,pos)
            if isinstance(role,Trader):
                self.surface.blit(trader_tile,pos)
            if isinstance(role,Captain):
                self.surface.blit(captain_tile,pos)
            if isinstance(role,Prospector):
                self.surface.blit(prospector_tile,pos)

            if role.coins:
                coins = font.render(str(role.coins),1,(0,0,0))
                pos = (pos.bottomright[0]-25,pos.bottomright[1]-33)
                pygame.draw.circle(self.surface, (119,136,153), pos, 17)
                if role.coins >= 5:
                    pygame.draw.circle(self.surface, (255,215,0), pos, 15)
                else:
                    pygame.draw.circle(self.surface, (192,192,192), pos, 15)
                self.surface.blit(coins, (pos[0]-5,pos[1]-12))

    def draw_plantation(self,plantation,pos):
        if isinstance(plantation,Corn):
            self.surface.blit(corn,pos)
        if isinstance(plantation,Indigo):
            self.surface.blit(indigo,pos)
        if isinstance(plantation,Sugar):
            self.surface.blit(sugar,pos)
        if isinstance(plantation,Tobacco):
            self.surface.blit(tobacco,pos)
        if isinstance(plantation,Coffee):
            self.surface.blit(coffee,pos)
        if isinstance(plantation,Quarry):
            self.surface.blit(quarry,pos)
        if plantation.colonists > 0:
            pygame.draw.circle(self.surface, brown, (pos[0]+72,pos[1]+72), 15)
            
    def draw_building(self,building,pos):
        if isinstance(building,SmallIndigoPlant):
            self.surface.blit(small_indigo_plant,pos)
        elif isinstance(building,SmallSugarMill):
            self.surface.blit(small_sugar_mill,pos)
        elif isinstance(building,IndigoPlant):
            self.surface.blit(indigo_plant,pos)
        elif isinstance(building,SugarMill):
            self.surface.blit(sugar_mill,pos)
        elif isinstance(building,TobaccoStorage):
            self.surface.blit(tobacco_storage,pos)
        elif isinstance(building,CoffeeRoaster):
            self.surface.blit(coffee_roaster,pos)
        else:
            if building.points < 4:
                self.surface.blit(small_violet,pos)
            else:
                self.surface.blit(large_violet,pos)
            name = font.render(building.name,1,(255,255,255))
            self.surface.blit(name,(pos[0]+6,pos[1]+3))
        cost = font.render(str(building.cost),1,(255,255,255))
        points = font.render(str(building.points),1,(180,0,0))
        self.surface.blit(points,(pos[0]+134,pos[1]+1))
        self.surface.blit(cost,(pos[0]+126,pos[1]+47))
            
        if building.colonists > 0:
            if building.size < 2:
                pygame.draw.circle(self.surface, brown, (pos[0]+130,pos[1]+59), 15)
            else:
                pygame.draw.circle(self.surface, brown, (pos[0]+130,pos[1]+148), 15)
        if building.colonists > 1:
            pygame.draw.circle(self.surface, brown, (pos[0]+90,pos[1]+59), 15)
        if building.colonists > 2:
            pygame.draw.circle(self.surface, brown, (pos[0]+50,pos[1]+59), 15)