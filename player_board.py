import pygame
from plantations import *
from buildings import *
from roles import *

island = pygame.image.load('res/island.png').convert()
pygame.font.init()
h1 = pygame.font.Font('res/fertigo.ttf',36)
font = pygame.font.Font('res/fertigo.ttf',18)

quarry = pygame.image.load('res/quarry.png').convert()
corn = pygame.image.load('res/corn.png').convert()
indigo = pygame.image.load('res/indigo.png').convert()
sugar = pygame.image.load('res/sugar.png').convert()
tobacco = pygame.image.load('res/tobacco.png').convert()
tobacco.set_colorkey(pygame.Color(236,0,140))
coffee = pygame.image.load('res/coffee.png').convert()

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

gray = pygame.Color(0,0,0,10)
brown = pygame.Color(128,40,40)

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
            self.role_grid.append(pygame.Rect((column*128,614),(128,154)))
        self.choose_plantation_grid = []
        for column in range(8):
            self.choose_plantation_grid.append(pygame.Rect((column*128+32,639),(96,96)))
        self.good_grid = []
        for column in range(5):
            self.good_grid.append(pygame.Rect((2*padding + 2*spacing + 3*96+(96+15)*column,180),(96,96)))   
        
    def draw(self,player):
        self.surface.blit(island, (0,0))
        name = h1.render(player.name,1,(255,255,255))
        coins = font.render("coins: "+str(player.coins),1,(255,255,255))
        points = font.render("points: "+str(player.points),1,(255,255,255))        
        san_juan = font.render("san juan: "+str(player.san_juan),1,(255,255,255))         
        self.surface.blit(name,(32,32)) 
        self.surface.blit(coins,(32,64))
        self.surface.blit(points,(32,80))
        self.surface.blit(san_juan,(32,96))
        
        
        plantation_space = pygame.Surface((96,96),pygame.SRCALPHA)
        plantation_space.fill(gray)
        building_space= pygame.Surface((154,83),pygame.SRCALPHA)
        building_space.fill(gray)
        
        for rect in self.plantation_grid:
            self.surface.blit(plantation_space,rect.topleft)
            
        for rect in self.building_grid:
            self.surface.blit(building_space,rect.topleft)

        for pos,plantation in zip(self.plantation_grid,player.plantations):
            self.draw_plantation(plantation,pos)

        for pos,building in zip(self.building_grid,player.buildings):
            self.draw_building(building,pos)
        
        for i,barrel in enumerate([CornBarrel(), IndigoBarrel(), SugarBarrel(), TobaccoBarrel(), CoffeeBarrel()]):
            if barrel in player.goods:
                self.draw_plantation(Corn(),self.good_grid[i])

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