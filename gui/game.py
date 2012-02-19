import sys
sys.path.append('..')

from engine.game import Game
from player_board import *
import textrect
import tiles

class GUI_Game(Game):
    def __init__(self,screen):
        Game.__init__(self)
        self.gui_game_end = False
        self.screen = screen
        self.surface = pygame.Surface(screen.get_size())
        self.clock = pygame.time.Clock()
        self.building_grid = []
        self.trading_house_grid = []
        self.ships_grid = []
        self.plantation_grid = []
        self.barrel_grid = []
        for row in range(3):
            for column in range(6):
                self.building_grid.append(pygame.Rect(25+(120+6)*column, 25+(65+6)*row,120,65))
        for column in range(6):
            self.building_grid.append(pygame.Rect(25+(120+6)*column, 25+(65+6)*3,120,136))
        for column in range(4):
            self.trading_house_grid.append(pygame.Rect(column*45+575,550,40,40))
        for column in range(3):
            self.ships_grid.append(pygame.Rect(column*45+575,480,40,40))
        for column in range(8):
            self.plantation_grid.append(pygame.Rect(column*(75+5)+25,502,75,75))
        for column in range(5):
            self.barrel_grid.append(pygame.Rect(130 +40*column,450,40,40))
            
    def draw(self,index):
        for player in self.players:
            if player.index == index:
                player.board.draw(player,True)
            elif index>=0:
                player.board.draw(player)
                
        self.surface.blit(tiles.island, (0,0))

        self.draw_plantation_supply(self.surface)
        self.draw_trading_house(self.surface)
        self.draw_ships(self.surface)
        already_printed = []
        for i,building in enumerate(self.buildings):
            if building.__class__ not in already_printed:
                self.draw_building(building,self.building_grid[building.id])
                already_printed.append(building.__class__)

        trading_house = fonts.reg.render("Trading House",1,(0,0,0))
        self.surface.blit(trading_house,(575,530))
        ships = fonts.reg.render("Ships",1,(0,0,0))
        self.surface.blit(ships,(575,460))
        self.update()

        title = fonts.reg.render("Colonist Ship",1,(0,0,0))
        self.surface.blit(title,(687,275))

        title = fonts.reg.render("Supply",1,(0,0,0))
        self.surface.blit(title,(25,430))

        ships = fonts.reg.render("Ships",1,(0,0,0))
        self.surface.blit(ships,(575,460))

    def update(self):
        self.draw_supply()
        self.draw_goods_supply()
        self.draw_plantation_supply(self.surface)
        self.draw_ships(self.surface)
        self.draw_trading_house(self.surface)
        self.draw_colonist_ship()

    def draw_colonist_ship(self):
        colonist_ship = fonts.reg.render(str(self.colonist_ship),1,(255,255,255))
        pygame.draw.circle(self.surface, brown, (730,310), 12)
        self.surface.blit(colonist_ship,(724,300))

    def draw_supply(self):

        colonist_supply = fonts.lg.render(str(max(0,self.colonists)),1,(255,255,255))
        pygame.draw.circle(self.surface, brown, (45,470), 20)
        self.surface.blit(colonist_supply,(35,457))

        points_supply = fonts.lg.render(str(max(0,self.points)),1,(255,215,0))
        self.surface.blit(tiles.points,(82,450))
        self.surface.blit(points_supply,(91,457))
        
    def draw_goods_supply(self):
        for pos,barrel,texture in zip(self.barrel_grid,[CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()],tiles.barrels):
            if barrel in self.goods:
                amount = fonts.reg.render(str(reduce(lambda a,b:a+(b==barrel),self.goods,0)),1,(255,255,255))
                self.surface.blit(texture,pos)
                pygame.draw.circle(self.surface, (96,96,96), pos.center, 10)
                self.surface.blit(amount,(pos[0]+15,pos[1]+10))
            else:
                self.surface.blit(tiles.island,pos,pos)
        
    def draw_plantation_supply(self,surface):
        for pos,plantation in zip(self.plantation_grid,self.plantations):
            if isinstance(plantation,Corn):
                surface.blit(tiles.corn,pos)
            if isinstance(plantation,Indigo):
                surface.blit(tiles.indigo,pos)
            if isinstance(plantation,Sugar):
                surface.blit(tiles.sugar,pos)
            if isinstance(plantation,Tobacco):
                surface.blit(tiles.tobacco,pos)
            if isinstance(plantation,Coffee):
                surface.blit(tiles.coffee,pos)
            if isinstance(plantation,Quarry):
                surface.blit(tiles.quarry,pos)

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

            text = textrect.render_textrect(building.text,fonts.sm,pygame.Rect(0,0,90,155),(192,192,192))
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
    
    def draw_trading_house(self,surface):
        trading_space = pygame.Surface((40,40),pygame.SRCALPHA)
        trading_space.fill(pygame.Color(0,0,0,32))
        for i,pos in enumerate(self.trading_house_grid):
            surface.blit(tiles.island,pos,pos)
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
        ship_space = pygame.Surface((40,40),pygame.SRCALPHA)
        ship_space.fill(pygame.Color(0,0,0,32))

        for pos,ship in zip(self.ships_grid,self.ships):
            surface.blit(tiles.island,pos,pos)
            surface.blit(ship_space,pos)
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
            pygame.draw.circle(surface, (96,96,96), pos.center, 10)
            surface.blit(fonts.reg.render(str(ship.space()),1,(255,255,255)),(pos[0]+15,pos[1]+10))

    def game_end(self):
        return self.gui_game_end or Game.game_end(self)

    def draw_scores(self):
        self.screen.blit(tiles.island,(0,0))
        self.screen.blit(fonts.h1.render("Scores",1,(255,255,255)),(25,25))

        for i,player in enumerate(self.players):
            self.screen.blit(fonts.h1.render(str(player.name),1,(255,255,255)),(25,125+75*i))

            self.screen.blit(fonts.h1.render(str(player.total_points()),1,(255,255,255)),(400,125+75*i))

        pygame.display.update()