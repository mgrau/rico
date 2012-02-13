from game import Game
from player_board import *
import textrect
import tiles

class GUI_Game(Game):
    def __init__(self,size):
        Game.__init__(self)
        self.surface = pygame.Surface(size)
        self.clock = pygame.time.Clock()
        self.building_grid = []
        self.trading_house_grid = []
        self.ships_grid = []
        for row in range(4):
            for column in range(6):
                self.building_grid.append(pygame.Rect(25+(120+6)*column, 25+(65+6)*row,120,65))
        for column in range(4):
            self.trading_house_grid.append(pygame.Rect(column*45+575,520,40,40))
        for column in range(4):
            self.ships_grid.append(pygame.Rect(400+column*45,520,40,40))
    def draw(self,index):
        for player in self.players:
            if player.index == index:
                player.board.draw(player,True)
            else:
                player.board.draw(player)
                
        self.surface.blit(tiles.island, (0,0))

        self.draw_trading_house(self.surface)
        self.draw_ships(self.surface)
        already_printed = []
        for i,building in enumerate(self.buildings):
            if building.__class__ not in already_printed:
                self.draw_building(building,self.building_grid[building.id])
                already_printed.append(building.__class__)

        title = fonts.reg.render("Colonist Ship",1,(0,0,0))
        self.surface.blit(title,(687,275))
        colonist_ship = fonts.reg.render(str(self.colonist_ship),1,(255,255,255))
        pygame.draw.circle(self.surface, brown, (730,310), 12)
        self.surface.blit(colonist_ship,(726,300))
        

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
    
    def draw_trading_house(self,surface):
        trading_house = fonts.reg.render("Trading House",1,(0,0,0))
        surface.blit(trading_house,(575,500))
        trading_space = pygame.Surface((40,40),pygame.SRCALPHA)
        trading_space.fill(pygame.Color(0,0,0,10))
        for i,pos in enumerate(self.trading_house_grid):
            surface.blit(trading_space,pos)
            if i<len(self.trading_house):
                good = self.trading_house[i]
            else:
                good = Barrel()
            if good == CornBarrel():
                surface.blit(tiles.corn_barrel,pos)
            elif good == IndigoBarrel():
                surface.blit(tiles.indigo_barrel,pos)
            elif good == SugarBarrel():
                surface.blit(tiles.sugar_barrel,pos)
            elif good == TobaccoBarrel():
                surface.blit(tiles.tobacco_barrel,pos)
            elif good == CoffeeBarrel():
                surface.blit(tiles.coffee_barrel,pos)
                
    def draw_ships(self,surface):
        ships = fonts.reg.render("Ships",1,(0,0,0))
        surface.blit(ships,(400,500))
        ship_space = pygame.Surface((40,40),pygame.SRCALPHA)
        ship_space.fill(pygame.Color(0,0,0,10))
        for pos,ship in zip(self.ships_grid,self.ships):
            if len(ship.goods):
                good = ship.goods[0]            
                if good == CornBarrel():
                    surface.blit(tiles.corn_barrel,pos)
                elif good == IndigoBarrel():
                    surface.blit(tiles.indigo_barrel,pos)
                elif good == SugarBarrel():
                    surface.blit(tiles.sugar_barrel,pos)
                elif good == TobaccoBarrel():
                    surface.blit(tiles.tobacco_barrel,pos)
                elif good == CoffeeBarrel():
                    surface.blit(tiles.coffee_barrel,pos)
            else:
                surface.blit(ship_space,pos)
            surface.blit(fonts.reg.render(str(ship.space()),1,(0,0,0)),(pos[0]+20,pos[1]+20))