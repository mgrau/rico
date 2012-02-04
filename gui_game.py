import pygame
from game import Game
from buildings import *
from player_board import *

class GUI_Game(Game):
    def __init__(self,size=(1024,768)):
        Game.__init__(self)
        self.surface = pygame.Surface(size)
        self.clock = pygame.time.Clock()
        self.building_grid = []
        for row in range(4):
            for column in range(6):
                self.building_grid.append(pygame.Rect( (25+(154+10)*column, 32+(83+10)*row),(154,83)))
    def draw(self,index):
        for player in self.players:
            if player.index == index:
                player.board.draw(player,True)
            else:
                player.board.draw(player)
                
        self.surface.blit(island, (0,0))

        already_printed = []
        for i,building in enumerate(self.buildings):
            if building.__class__ not in already_printed:
                self.draw_building(building,self.building_grid[building.id])
                already_printed.append(building.__class__)
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
