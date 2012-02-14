import pygame

import sys
sys.path.append('..')
from engine.plantations import *
from engine.roles import *
import tiles
import fonts
import textrect

gray = pygame.Color(0,0,0,32)
brown = pygame.Color(128,40,40)
magenta = pygame.Color(255,180,100)

class Board():
    def __init__(self,size):
        self.width,self.height = size
        self.surface = pygame.Surface(size)
        padding = 25
        spacing = 5
        size = (75,75)
        self.plantation_grid = []
        for row in [3,2,1,0]:
            for column in [0,1,2]:
                self.plantation_grid.append(pygame.Rect((padding+(size[0]+spacing)*column, self.height*0.8-padding -size[1]-(size[1]+spacing)*row),size))
        size = (120,65)
        self.building_grid = []
        for row in [2,1,0]:
            for column in [0,1,2,3]:
                self.building_grid.append(pygame.Rect((2*padding + 2*spacing + 3*75+(size[0]+spacing)*column, self.height*0.8-padding -size[1]-(size[1]+spacing)*row),size))
        self.role_grid = []
        for column in range(8):
            self.role_grid.append(pygame.Rect(10+column*100,490,90,100))
        self.choose_plantation_grid = []
        for column in range(8):
            self.choose_plantation_grid.append(pygame.Rect(column*(75+padding)+padding,502,75,75))
        self.barrel_grid = []
        for column in range(5):
            self.barrel_grid.append(pygame.Rect(2*padding+2*spacing+3*75 +50*column,200,40,40))
        self.choose_barrel_grid = []
        for column in range(5):
            self.choose_barrel_grid.append(pygame.Rect(column*50+padding,520,40,40))
        
    def draw(self,player,current_player=False):
        self.surface.blit(tiles.island, (0,0))
        name = fonts.h1.render(player.name,1,(255,255,255))
        self.surface.blit(name,(100,32))


        if current_player:
            pygame.draw.circle(self.surface, (255,215,0), (64,60), 28)
            pygame.draw.circle(self.surface, (192,0,0), (64,60), 25)

        coins = fonts.reg.render(str(player.coins),1,(0,0,0))
        pygame.draw.circle(self.surface, (119,136,153), (300,150), 18)
        if player.coins >= 5:
            pygame.draw.circle(self.surface, (255,215,0), (300,150), 15)
        else:
            pygame.draw.circle(self.surface, (192,192,192), (300,150), 15)
        self.surface.blit(coins, (296,140))

        if player.san_juan:
            title = fonts.reg.render("San Juan",1,(0,0,0))
            self.surface.blit(title,(537,157))
            san_juan = fonts.reg.render(str(player.san_juan),1,(255,255,255))
            #pygame.draw.circle(self.surface, brown, (500,125), 12)
            pygame.draw.circle(self.surface, brown, (530,150), 12)
            self.surface.blit(san_juan,(526,140))

        for i,role in enumerate(player.roles):
            pos = (800-125-100*i,25)
            if isinstance(role,Settler):
                self.surface.blit(tiles.settler,pos)
            elif isinstance(role,Mayor):
                self.surface.blit(tiles.mayor,pos)
            elif isinstance(role,Builder):
                self.surface.blit(tiles.builder,pos)
            elif isinstance(role,Craftsman):
                self.surface.blit(tiles.craftsman,pos)
            elif isinstance(role,Trader):
                self.surface.blit(tiles.trader,pos)
            elif isinstance(role,Captain):
                self.surface.blit(tiles.captain,pos)
            elif isinstance(role,Prospector):
                self.surface.blit(tiles.prospector,pos)

        plantation_space = pygame.Surface((75,75),pygame.SRCALPHA)
        plantation_space.fill(gray)
        building_space = pygame.Surface((120,65),pygame.SRCALPHA)
        building_space.fill(gray)

        for rect in self.plantation_grid:
            self.surface.blit(plantation_space,rect)

        for rect in self.building_grid:
            self.surface.blit(building_space,rect)

        for pos,plantation in zip(self.plantation_grid,player.plantations):
            self.draw_plantation(plantation,pos)

        for pos,building in zip(self.building_grid,player.buildings):
            self.draw_building(building,pos)

        for pos,barrel,texture in zip(self.barrel_grid,[CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()],tiles.barrels):
            if barrel in player.goods:
                amount = fonts.reg.render(str(reduce(lambda a,b:a+(b==barrel),player.goods,0)),1,(255,255,255))
                self.surface.blit(texture,pos)
                self.surface.blit(amount,(pos[0]+15,pos[1]+12))

    def draw_points(self,player):
        if player.points_visible:
            points = fonts.h1.render(str(player.points),1,(255,215,0))
            self.surface.blit(points,(50,31))
        else:
            pygame.draw.circle(self.surface, (192,0,0), (64,60), 25)

    def draw_wharf(self,player):
        if player.use_building(Wharf):
            pos = (300,520)
            wharf = fonts.reg.render("Wharf",1,(0,0,0))
            player.board.surface.blit(wharf,(300,500))
            ship_space = pygame.Surface((40,40),pygame.SRCALPHA)
            ship_space.fill(pygame.Color(0,0,0,32))
            player.board.surface.blit(ship_space,pos)
            if len(player.wharf.goods):
                good = player.wharf.goods[0]
                if good == CornBarrel():
                    player.board.surface.blit(tiles.corn_barrel,pos)
                elif good == IndigoBarrel():
                    player.board.surface.blit(tiles.indigo_barrel,pos)
                elif good == SugarBarrel():
                    player.board.surface.blit(tiles.sugar_barrel,pos)
                elif good == TobaccoBarrel():
                    player.board.surface.blit(tiles.tobacco_barrel,pos)
                elif good == CoffeeBarrel():
                    player.board.surface.blit(tiles.coffee_barrel,pos)
#            if not player.wharf.passed:

    def draw_roles(self,game):
        for pos,role in zip(self.role_grid,game.roles):
            if isinstance(role,Settler):
                self.surface.blit(tiles.settler,pos)
            if isinstance(role,Mayor):
                self.surface.blit(tiles.mayor,pos)
            if isinstance(role,Builder):
                self.surface.blit(tiles.builder,pos)
            if isinstance(role,Craftsman):
                self.surface.blit(tiles.craftsman,pos)
            if isinstance(role,Trader):
                self.surface.blit(tiles.trader,pos)
            if isinstance(role,Captain):
                self.surface.blit(tiles.captain,pos)
            if isinstance(role,Prospector):
                self.surface.blit(tiles.prospector,pos)

            if role.coins:
                coins = fonts.reg.render(str(role.coins),1,(0,0,0))
                pos = (pos.bottomright[0]-25,pos.bottomright[1]-25)
                pygame.draw.circle(self.surface, (119,136,153), pos, 18)
                if role.coins >= 5:
                    pygame.draw.circle(self.surface, (255,215,0), pos, 15)
                else:
                    pygame.draw.circle(self.surface, (192,192,192), pos, 15)
                self.surface.blit(coins, (pos[0]-3,pos[1]-10))

    def draw_plantation(self,plantation,pos):
        if isinstance(plantation,Corn):
            self.surface.blit(tiles.corn,pos)
        if isinstance(plantation,Indigo):
            self.surface.blit(tiles.indigo,pos)
        if isinstance(plantation,Sugar):
            self.surface.blit(tiles.sugar,pos)
        if isinstance(plantation,Tobacco):
            self.surface.blit(tiles.tobacco,pos)
        if isinstance(plantation,Coffee):
            self.surface.blit(tiles.coffee,pos)
        if isinstance(plantation,Quarry):
            self.surface.blit(tiles.quarry,pos)
        if plantation.colonists > 0:
            pygame.draw.circle(self.surface, brown, (pos[0]+58,pos[1]+58), 11)
            
    def draw_building(self,building,pos):
        if isinstance(building,SmallIndigoPlant):
            self.surface.blit(tiles.small_indigo_plant,pos)
        elif isinstance(building,SmallSugarMill):
            self.surface.blit(tiles.small_sugar_mill,pos)
        elif isinstance(building,IndigoPlant):
            self.surface.blit(tiles.indigo_plant,pos)
        elif isinstance(building,SugarMill):
            self.surface.blit(tiles.sugar_mill,pos)
        elif isinstance(building,TobaccoStorage):
            self.surface.blit(tiles.tobacco_storage,pos)
        elif isinstance(building,CoffeeRoaster):
            self.surface.blit(tiles.coffee_roaster,pos)
        else:
            if building.size < 2:
                self.surface.blit(tiles.small_violet,pos)
            else:
                self.surface.blit(tiles.large_violet,pos)
            name = textrect.render_textrect(building.name,fonts.reg,pygame.Rect(0,0,95,55),(255,255,255))
            self.surface.blit(name,(pos[0]+5,pos[1]+2))

            text = textrect.render_textrect(building.text,fonts.sm,pygame.Rect(0,0,95,155),(192,192,192))
            self.surface.blit(text,(pos[0]+5,pos[1]+20))

        cost = fonts.reg.render(str(building.cost),1,(255,255,255))
        points = fonts.reg.render(str(building.points),1,(200,100,100))
        self.surface.blit(points,(pos[0]+105,pos[1]+1))
        if building.size < 2:
            self.surface.blit(cost,(pos[0]+100,pos[1]+39))
        else:
            self.surface.blit(cost,(pos[0]+96,pos[1]+110))

        if building.colonists > 0:
            if building.size < 2:
                pygame.draw.circle(self.surface, brown, (pos[0]+103,pos[1]+48), 11)
            else:
                pygame.draw.circle(self.surface, brown, (pos[0]+103,pos[1]+118), 11)
        if building.colonists > 1:
            pygame.draw.circle(self.surface, brown, (pos[0]+73,pos[1]+48), 11)
        if building.colonists > 2:
            pygame.draw.circle(self.surface, brown, (pos[0]+43,pos[1]+48), 11)