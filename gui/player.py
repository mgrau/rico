import sys

sys.path.append('..')
from engine.player import Player
from engine.plantations import *
from player_board import *


class GUI_Player(Player):
    def __init__(self,index,name,screen):
        Player.__init__(self,index,name)
        self.screen = screen
        self.board = Board(screen.get_size())
        self.points_visible = False

    def print_board(self,game):
        print game

    def get_input(self,game,build=False):
        if build:
            self.screen.blit(game.surface,(0,0))
        else:
            self.screen.blit(self.board.surface,(0,0))
        pygame.display.update()
        visible_player = self.index
        game_board = build
        valid_input = False

        swipe = 20
        speed = 40
        rel = (0,0)
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_LEFT and not game_board:
                        if visible_player == len(game.players)-1:
                            next_player = 0
                        else:
                            next_player = visible_player+1
                        for i in range(800,-1,-4*speed):
                            self.screen.blit(game.players[visible_player].board.surface,(i-800,0))
                            self.screen.blit(game.players[next_player].board.surface,(i,0))
                            pygame.display.flip()
                        visible_player = next_player
                    elif event.key == pygame.K_RIGHT and not game_board:
                        if not visible_player:
                            next_player = len(game.players)-1
                        else:
                            next_player = visible_player-1
                        for i in range(0,800+1,4*speed):
                            self.screen.blit(game.players[visible_player].board.surface,(i,0))
                            self.screen.blit(game.players[next_player].board.surface,(i-800,0))
                            pygame.display.flip()
                        visible_player = next_player
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        if game_board:
                            nextscreen = game.players[visible_player].board.surface
                            thisscreen = game.surface
                        else:
                            nextscreen = game.surface
                            thisscreen = game.players[visible_player].board.surface
                        if event.key == pygame.K_DOWN:
                            for i in range(0,600+1,3*speed):
                                self.screen.blit(thisscreen,(0,i))
                                self.screen.blit(nextscreen,(0,i-600))
                                pygame.display.flip()
                        else:
                            for i in range(600,-1,-3*speed):
                                self.screen.blit(nextscreen,(0,i))
                                self.screen.blit(thisscreen,(0,i-600))
                                pygame.display.flip()
                        game_board = not game_board
                elif event.type == pygame.MOUSEBUTTONDOWN and not event.pos == (0,0):
                    rel = event.pos
                elif event.type == pygame.MOUSEBUTTONUP and not event.pos == (0,0):
                    rel = (event.pos[0]-rel[0],event.pos[1]-rel[1])
                    if (rel[0]<-swipe and abs(rel[0])>abs(rel[1])) and not game_board:
                        if visible_player == len(game.players)-1:
                            next_player = 0
                        else:
                            next_player = visible_player+1
                        for i in range(1024,-1,-128):
                            self.screen.blit(game.players[visible_player].board.surface,(i-1024,0))
                            self.screen.blit(game.players[next_player].board.surface,(i,0))
                            pygame.display.flip()
                        visible_player = next_player
                    if (rel[0]>swipe and abs(rel[0])>abs(rel[1])) and not game_board:
                        if not visible_player:
                            next_player = len(game.players)-1
                        else:
                            next_player = visible_player-1
                        for i in range(0,1024+1,128):
                            self.screen.blit(game.players[visible_player].board.surface,(i,0))
                            self.screen.blit(game.players[next_player].board.surface,(i-1024,0))
                            pygame.display.flip()
                        visible_player = next_player
                    if abs(rel[1])>10 and abs(rel[1])>abs(rel[0]):
                        if game_board:
                            nextscreen = game.players[visible_player].board.surface
                            thisscreen = game.surface
                        else:
                            nextscreen = game.surface
                            thisscreen = game.players[visible_player].board.surface
                        if rel[1]>0:
                            for i in range(0,768+1,96):
                                self.screen.blit(thisscreen,(0,i))
                                self.screen.blit(nextscreen,(0,i-768))
                                pygame.display.update()
                        else:
                            for i in range(768,-1,-96):
                                self.screen.blit(nextscreen,(0,i))
                                self.screen.blit(thisscreen,(0,i-768))
                                pygame.display.update()
                        game_board = not game_board
                    if event.type == pygame.MOUSEBUTTONUP and abs(rel[0])<swipe and abs(rel[1])<swipe:
                        if pygame.Rect(36,32,56,56).collidepoint(event.pos) and visible_player == self.index and not game_board:
                            self.points_visible = not self.points_visible
                            self.board.draw_points(self)
                            self.screen.blit(self.board.surface,pygame.Rect(36,32,56,56),pygame.Rect(36,32,56,56))
                            pygame.display.update()
                        elif (visible_player == self.index and not game_board) or game_board:
                            return event.pos

    def choose_role(self,game):
        game.draw(self.index)
        self.board.draw_roles(game)
        
        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for choice,rect in enumerate(self.board.role_grid):
                if rect.collidepoint(pos):
                    return choice

    def settler(self,game):
        game.draw(self.index)
        for pos,plantation in zip(self.board.choose_plantation_grid,game.plantations):
            self.board.draw_plantation(plantation,pos)
        if len(game.quarries)>0 and (self.index == game.current_player or self.use_building(ConstructionHut)):
            self.board.draw_plantation(Quarry(),self.board.choose_plantation_grid[len(game.plantations)])
        instructions = fonts.reg.render("Please select a plantation",1,(255,255,255))
        self.board.surface.blit(instructions,(25,480))
        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for choice,rect in enumerate(self.board.choose_plantation_grid):
                if self.index==game.current_player or self.use_building(ConstructionHut):
                    if rect.collidepoint(pos) and choice<=len(game.plantations):
                        return choice
                else:
                    if rect.collidepoint(pos) and choice<=len(game.plantations)-1:
                        return choice

    def mayor(self,game):
        done = False
        while not done:
            game.draw(self.index)
            button = fonts.h1.render("Done",1,(255,255,255),(100,0,0))
            instructions = fonts.reg.render("Please place your colonists",1,(255,255,255))
            self.board.surface.blit(button,(25,500))
            button = button.get_rect()
            button.topleft = (25,500)
            self.board.surface.blit(instructions,(25,480))
            self.screen.blit(self.board.surface,(0,0))
            pygame.display.flip()
            
            pos = self.get_input(game)
            for choice,rect in enumerate(self.board.plantation_grid):
                if rect.collidepoint(pos) and choice<len(self.plantations):
                    if self.plantations[choice].colonists > 0:
                        self.san_juan += self.plantations[choice].colonists
                        self.plantations[choice].colonists = 0
                    else:
                        if self.san_juan > 0:
                            self.plantations[choice].colonists = 1
                            self.san_juan -= 1
            for choice,rect in enumerate(self.board.building_grid):
                if rect.collidepoint(pos) and choice<len(self.buildings):
                    if self.buildings[choice].colonists >= self.buildings[choice].capacity:
                        self.san_juan += self.buildings[choice].colonists
                        self.buildings[choice].colonists = 0
                    else:
                        if self.san_juan > 0:
                            self.buildings[choice].colonists += 1
                            self.san_juan -= 1
                        elif self.buildings[choice].colonists > 0:
                            self.buildings[choice].colonists -= 1
                            self.san_juan += 1
            if button.collidepoint(pos):
                if self.san_juan ==0 or self.open_spots()==0:
                    return

    def builder(self,game):
        game.draw(self.index)
        name = fonts.h1.render(self.name,1,(255,255,255))
        game.surface.blit(name,(68,450))
        
        coins = fonts.reg.render(str(self.coins),1,(0,0,0))
        pygame.draw.circle(game.surface, (119,136,153), (43,476), 18)
        if self.coins >= 5:
            pygame.draw.circle(game.surface, (255,215,0), (43,476), 15)
        else:
            pygame.draw.circle(game.surface, (192,192,192), (43,476), 15)
        game.surface.blit(coins, (39,466))

        button = fonts.h1.render("Don't Buy",1,(255,255,255),(100,0,0))
        game.surface.blit(button,(25,500))
        button = button.get_rect()
        button.topleft = (25,500)

        valid_input = False
        while not valid_input:
            pos = self.get_input(game,build=True)
            for id,rect in enumerate(game.building_grid):
                if rect.collidepoint(pos):
                    for choice,building in enumerate(game.buildings):
                        if building.id == id:
                            if self.afford_building(building) and (not self.have_building(building.__class__)):
                                return choice
            if button.collidepoint(pos):
                return -1

    def craftsman(self,game):
        game.draw(self.index)
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]
        for pos,barrel,texture in zip(self.board.choose_barrel_grid,barrel_types,[tiles.corn_barrel, tiles.indigo_barrel, tiles.sugar_barrel, tiles.tobacco_barrel, tiles.coffee_barrel]):
            if barrel in self.produce_goods() and barrel in game.goods:
                self.board.surface.blit(texture,pos)
        instructions = fonts.reg.render("Please select an extra good",1,(255,255,255))
        self.board.surface.blit(instructions,(25,500))

        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for barrel,rect in zip(barrel_types,self.board.choose_barrel_grid):
                if rect.collidepoint(pos) and barrel in self.produce_goods() and barrel in game.goods:
                    return barrel

    def trader(self,game):
        game.draw(self.index)
        button = fonts.h1.render("Don't Sell",1,(255,255,255),(100,0,0))
        self.board.surface.blit(button,(25,500))
        button = button.get_rect()
        button.topleft = (25,500)
        
        game.draw_trading_house(self.board.surface)
        instructions = fonts.reg.render("Please select a good to sell",1,(255,255,255))
        self.board.surface.blit(instructions,(25,480))
        
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                if rect.collidepoint(pos) and (barrel in self.goods) and (barrel not in game.trading_house or self.use_building(Office)):
                    return barrel
            if button.collidepoint(pos):
                return Barrel()


    def captain(self,game):
        game.draw(self.index)
        
        game.draw_ships(self.board.surface)
        self.board.draw_wharf(self)
        instructions = fonts.reg.render("Please select a good to ship",1,(255,255,255))
        self.board.surface.blit(instructions,(25,460))
        
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        barrel = Barrel()

        for player in game.players:
            print player.wharf

        if self.use_building(Wharf):
            ships = game.ships+[self.wharf]
            ships_grid = game.ships_grid + [pygame.Rect((300,520,40,40))]
        else:
            ships = game.ships
            ships_grid = game.ships_grid

        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                if rect.collidepoint(pos) and (barrel in self.goods) and any([ship.can_load(barrel) for ship in ships]):
                    valid_input = True
                    break

        instructions = fonts.reg.render("Please select a ship to load",1,(255,255,255))
        self.board.surface.blit(instructions,(25,480))

        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for ship,rect in zip(ships,ships_grid):
                if rect.collidepoint(pos) and ship.can_load(barrel):
                    return ship,barrel

    def rot(self,game):
        game.draw(self.index)
        
        instructions = fonts.reg.render("Please select a good to keep",1,(255,255,255))
        self.board.surface.blit(instructions,(25,500))
        
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                if rect.collidepoint(pos) and (barrel in self.goods):
                    return [barrel]
