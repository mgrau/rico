try:
    import android
except ImportError:
    android = None
    import code
import sys
sys.path.append('..')
from engine.player import Player
from player_board import *


class GUI_Player(Player):
    def __init__(self,index,name,screen,invert=False):
        Player.__init__(self,index,name)
        self.screen = screen
        self.board = Board(screen.get_size())
        self.points_visible = False
        self.invert = invert

    def get_input(self,game,build=False):
        if build:
            self.screen.blit(pygame.transform.flip(game.surface,self.invert,self.invert),(0,0))
        else:
            self.screen.blit(pygame.transform.flip(self.board.surface,self.invert,self.invert),(0,0))
        pygame.display.update()
        visible_player = self.index
        game_board = build
        valid_input = False

        swipe = 30
        speed = 40
        rel = (0,0)
        while not valid_input and not game.gui_game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game.gui_game_end = True
                        sys.exit()
                    elif event.key == pygame.K_BACKQUOTE:
                        if android is None:
                            code.interact(local=locals())
                    elif event.key == pygame.K_LEFT and not game_board:
                        if visible_player == len(game.players)-1:
                            next_player = 0
                        else:
                            next_player = visible_player+1
                        for i in range(800,-1,-4*speed):
                            self.screen.blit(pygame.transform.flip(game.players[visible_player].board.surface,self.invert,self.invert),(i-800,0))
                            self.screen.blit(pygame.transform.flip(game.players[next_player].board.surface,self.invert,self.invert),(i,0))
                            pygame.display.update()
                        visible_player = next_player
                    elif event.key == pygame.K_RIGHT and not game_board:
                        if not visible_player:
                            next_player = len(game.players)-1
                        else:
                            next_player = visible_player-1
                        for i in range(0,800+1,4*speed):
                            self.screen.blit(pygame.transform.flip(game.players[visible_player].board.surface,self.invert,self.invert),(i,0))
                            self.screen.blit(pygame.transform.flip(game.players[next_player].board.surface,self.invert,self.invert),(i-800,0))
                            pygame.display.update()
                        visible_player = next_player
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        if game_board:
                            nextscreen = pygame.transform.flip(game.players[visible_player].board.surface,self.invert,self.invert)
                            thisscreen = pygame.transform.flip(game.surface,self.invert,self.invert)
                        else:
                            nextscreen = pygame.transform.flip(game.surface,self.invert,self.invert)
                            thisscreen = pygame.transform.flip(game.players[visible_player].board.surface,self.invert,self.invert)
                        if event.key == pygame.K_DOWN:
                            for i in range(0,600+1,3*speed):
                                self.screen.blit(thisscreen,(0,i))
                                self.screen.blit(nextscreen,(0,i-600))
                                pygame.display.update()
                        else:
                            for i in range(600,-1,-3*speed):
                                self.screen.blit(nextscreen,(0,i))
                                self.screen.blit(thisscreen,(0,i-600))
                                pygame.display.update()
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
                        nextscreen = pygame.transform.flip(game.players[visible_player].board.surface,self.invert,self.invert)
                        thisscreen = pygame.transform.flip(game.players[next_player].board.surface,self.invert,self.invert)
                        for i in range(800,-1,-4*speed):
                            self.screen.blit(nextscreen,(i-800,0))
                            self.screen.blit(thisscreen,(i,0))
                            pygame.display.update()
                        visible_player = next_player
                    elif (rel[0]>swipe and abs(rel[0])>abs(rel[1])) and not game_board:
                        if not visible_player:
                            next_player = len(game.players)-1
                        else:
                            next_player = visible_player-1
                        thisscreen = pygame.transform.flip(game.players[visible_player].board.surface,self.invert,self.invert)
                        nextscreen = pygame.transform.flip(game.players[next_player].board.surface,self.invert,self.invert)
                        for i in range(0,800+1,4*speed):
                            self.screen.blit(thisscreen,(i,0))
                            self.screen.blit(nextscreen,(i-800,0))
                            pygame.display.update()
                        visible_player = next_player
                    elif abs(rel[1])>swipe and abs(rel[1])>abs(rel[0]):
                        if game_board:
                            nextscreen = pygame.transform.flip(game.players[visible_player].board.surface,self.invert,self.invert)
                            thisscreen = pygame.transform.flip(game.surface,self.invert,self.invert)
                        else:
                            nextscreen = pygame.transform.flip(game.surface,self.invert,self.invert)
                            thisscreen = pygame.transform.flip(game.players[visible_player].board.surface,self.invert,self.invert)
                        if rel[1]>0:
                            for i in range(0,600+1,3*speed):
                                self.screen.blit(thisscreen,(0,i))
                                self.screen.blit(nextscreen,(0,i-600))
                                pygame.display.update()
                        else:
                            for i in range(600,-1,-3*speed):
                                self.screen.blit(nextscreen,(0,i))
                                self.screen.blit(thisscreen,(0,i-600))
                                pygame.display.update()
                        game_board = not game_board
                    elif event.type == pygame.MOUSEBUTTONUP and abs(rel[0])<swipe and abs(rel[1])<swipe:
                        if self.invert:
                            pos = (800-event.pos[0],600-event.pos[1])
                        else:
                            pos = event.pos
                        if self.board.points_rect.collidepoint(pos) and visible_player == self.index and not game_board:
                            self.points_visible = not self.points_visible
                            self.board.draw_points(self)
                            if self.invert:
                                self.screen.blit(pygame.transform.flip(self.board.surface,self.invert,self.invert),self.board.invert_points_rect,self.board.invert_points_rect)
                            else:
                                self.screen.blit(self.board.surface,self.board.points_rect,self.board.points_rect)
                            pygame.display.update(self.board.points_rect)
                        elif (visible_player == self.index and not game_board) or game_board:
                            return pos

    def choose_role(self,game):
        for player in game.players:
            player.board.update(player)
        self.board.update(self)
        game.update()
        self.board.draw_current_player_marker()
        self.board.draw_role_selection(game)
        
        while True:
            pos = self.get_input(game)
            for choice,rect in enumerate(self.board.role_grid):
                if rect.collidepoint(pos):
                    self.board.draw_current_player_marker(clear=True)
                    self.board.clear_notifications()
                    return choice

    def settler(self,game):
        self.board.update(self)
        game.update()
        self.board.draw_current_player_marker()
        game.draw_plantation_supply(self.board.surface)
        if len(game.quarries)>0 and (self.index == game.current_player or self.use_building(ConstructionHut)):
            self.board.draw_plantation(Quarry(),self.board.choose_plantation_grid[len(game.plantations)])
        instructions = fonts.reg.render("Please select a plantation",1,(255,255,255))
        self.board.surface.blit(instructions,(25,480))
        while True:
            pos = self.get_input(game)
            for choice,rect in enumerate(game.plantation_grid):
                if rect.collidepoint(pos):
                    if self.use_building(Hacienda) and len(self.plantations)<12-1:
                        self.board.draw_plantation(game.plantation_deck[0],self.board.plantation_grid[len(self.plantations)+1])
                    if choice<len(game.plantations):
                        plantation = game.plantations[choice]
                        if self.use_building(Hospice):
                            plantation.colonists = 1
                        self.board.draw_plantation(plantation,self.board.plantation_grid[len(self.plantations)])
                        self.board.draw_current_player_marker(clear=True)
                        self.board.clear_notifications()
                        return choice
                    elif self.index==game.current_player or self.use_building(ConstructionHut):
                        if self.use_building(Hospice):
                            self.board.draw_plantation(Quarry(1),self.board.plantation_grid[len(self.plantations)])
                        else:
                            self.board.draw_plantation(Quarry(0),self.board.plantation_grid[len(self.plantations)])
                        self.board.draw_current_player_marker(clear=True)
                        self.board.clear_notifications()
                        return choice

    def mayor(self,game):
        self.board.update(self)
        game.update()
        self.board.draw_current_player_marker()
        button = fonts.h1.render("Done",1,(255,255,255),(100,0,0))
        self.board.surface.blit(button,(25,500))
        button = button.get_rect()
        button.topleft = (25,500)
        
        self.board.draw_san_juan(self)

        instructions = fonts.reg.render("Please place your colonists",1,(255,255,255))
        self.board.surface.blit(instructions,(25,480))
        self.screen.blit(self.board.surface,(0,0))
        pygame.display.update()
        
        done = False
        while not done:
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
                    self.board.draw_plantation(self.plantations[choice],rect)
                    pygame.display.update(rect)
                    self.board.draw_san_juan(self)
                    pygame.display.update(self.board.san_juan_rect)
                    break
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
                    self.board.draw_building(self.buildings[choice],rect)
                    pygame.display.update(rect)
                    self.board.draw_san_juan(self)
                    pygame.display.update(self.board.san_juan_rect)
                    break
            if button.collidepoint(pos):
                if self.san_juan ==0 or self.open_spots()==0:
                    self.board.draw_current_player_marker(clear=True)
                    self.board.clear_notifications()
                    return

    def builder(self,game):
        self.board.update(self)
        game.update()
        self.board.draw_current_player_marker()
        
        name = fonts.h1.render(self.name,1,(255,255,255))
        game.surface.blit(name,(400,390))
        name = name.get_rect()
        name.topleft = (400,390)

        coins = fonts.reg.render(str(self.coins),1,(0,0,0))
        if self.coins >= 5:
            game.surface.blit(tiles.gold,(353,397))
        else:
            game.surface.blit(tiles.silver,(353,397))
        if self.coins > 9:        #280,130+12,10
            game.surface.blit(coins, (353+12,397+10))
        else:
            game.surface.blit(coins, (353+16,397+10))

        button = fonts.h1.render("Don't Buy",1,(255,255,255),(100,0,0))
        game.surface.blit(button,(350,440))
        button = button.get_rect()
        button.topleft = (350,440)

        while True:
            pos = self.get_input(game,build=True)
            for id,rect in enumerate(game.building_grid):
                if rect.collidepoint(pos):
                    for choice,building in enumerate(game.buildings):
                        if building.id == id and self.afford_building(building) and (not self.have_building(building.__class__)) and (sum([b.size for b in self.buildings])+building.size<=12):
                            self.board.draw_current_player_marker(clear=True)
                            self.board.clear_notifications()
                            if building.size > 1:
                                if self.board.building_grid[len(self.buildings)].top<390:
                                    self.board.building_grid[len(self.buildings)].union_ip(self.board.building_grid.pop(len(self.buildings)+1))
                                else:
                                    x = len(self.buildings)
                                    self.board.building_grid[x+1].union_ip(self.board.building_grid.pop(x+2))
                                    self.board.building_grid.append(self.board.building_grid.pop(x))
#                                    self.board.building_grid[x],self.board.building_grid[x+1] = self.board.building_grid[x+1],self.board.building_grid[x]
                            if self.use_building(University):
                                building.colonists = 1
                            self.board.draw_building(building,self.board.building_grid[len(self.buildings)])
                            game.surface.blit(tiles.island,name,name)
                            game.surface.blit(tiles.island,button,button)
                            game.surface.blit(tiles.island,(353,397,40,40),(353,397,40,40))
                            if game.buildings.count(building) == 1:
                                game.surface.blit(tiles.island,rect,rect)
                            return choice
            if button.collidepoint(pos):
                self.board.draw_current_player_marker(clear=True)
                self.board.clear_notifications()
                game.surface.blit(tiles.island,name,name)
                game.surface.blit(tiles.island,button,button)
                game.surface.blit(tiles.island,(353,397,40,40),(353,397,40,40))
                return -1

    def craftsman(self,game):
        for player in game.players:
            player.board.update(player)
        game.update()
        self.board.draw_current_player_marker()
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]
        for pos,barrel,texture in zip(self.board.choose_barrel_grid,barrel_types,[tiles.corn_barrel, tiles.indigo_barrel, tiles.sugar_barrel, tiles.tobacco_barrel, tiles.coffee_barrel]):
            if barrel in self.produce_goods() and barrel in game.goods:
                self.board.surface.blit(texture,pos)
        instructions = fonts.reg.render("Please select an extra good",1,(255,255,255))
        self.board.surface.blit(instructions,(25,500))

        while True:
            pos = self.get_input(game)
            for barrel,rect in zip(barrel_types,self.board.choose_barrel_grid):
                if rect.collidepoint(pos) and barrel in self.produce_goods() and barrel in game.goods:
                    self.board.draw_current_player_marker(clear=True)
                    self.board.clear_notifications()
                    return barrel

    def trader(self,game):
        for player in game.players:
            player.board.update(player)
        game.update()
        self.board.draw_current_player_marker()
        button = fonts.h1.render("Don't Sell",1,(255,255,255),(100,0,0))
        self.board.surface.blit(button,(25,500))
        button = button.get_rect()
        button.topleft = (25,500)
        
        game.draw_trading_house(self.board.surface)
        instructions = fonts.reg.render("Please select a good to sell",1,(255,255,255))
        self.board.surface.blit(instructions,(25,480))
        
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        while True:
            pos = self.get_input(game)
            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                if rect.collidepoint(pos) and (barrel in self.goods) and (barrel not in game.trading_house or self.use_building(Office)):
                    self.board.draw_current_player_marker(clear=True)
                    self.board.clear_notifications()
                    return barrel
            if button.collidepoint(pos):
                self.board.draw_current_player_marker(clear=True)
                self.board.clear_notifications()
                return Barrel()


    def captain(self,game):
        for player in game.players:
            player.board.update(player)
        game.update()
        self.board.draw_current_player_marker()
        game.draw_ships(self.board.surface)
        self.board.draw_wharf(self)
        instructions = fonts.reg.render("Please select a good to ship",1,(255,255,255))
        self.board.surface.blit(instructions,(25,500))
        
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        barrel = Barrel()

        button = pygame.Rect(-10,-10,1,1)
        if self.use_building(Wharf) and not self.wharf.passed:
            ships = [self.wharf]+game.ships
            ships_grid = [pygame.Rect(500,480,40,40)]+game.ships_grid
            button = fonts.lg.render("Don't use Wharf",1,(255,255,255),(100,0,0))
            self.board.surface.blit(button,(500,530))
            button = button.get_rect()
            button.topleft = (500,530)
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
                elif button.collidepoint(pos):
                    self.wharf.passed = True
                    self.board.draw_current_player_marker(clear=True)
                    self.board.clear_notifications()
                    return game.ships[0],Barrel()

        instructions = fonts.reg.render("Please select a ship to load",1,(255,255,255))
        self.board.surface.blit(instructions,(25,520))

        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for ship,rect in zip(ships,ships_grid):
                if rect.collidepoint(pos) and ship.can_load(barrel):
                    self.board.draw_current_player_marker(clear=True)
                    self.board.clear_notifications()
                    return ship,barrel
                elif button.collidepoint(pos):
                    self.wharf.passed = True
                    self.board.draw_current_player_marker(clear=True)
                    self.board.clear_notifications()
                    return game.ships[0],Barrel()

    def rot(self,game):
        for player in game.players:
            player.board.update(player)
        self.board.draw_current_player_marker()
        instructions = fonts.reg.render("Please select a good to keep",1,(255,255,255))
        self.board.surface.blit(instructions,(25,500))
        
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        goods_to_keep = [Barrel(),Barrel(),Barrel(),Barrel()]
        
        valid_input = False
        while not valid_input:
            pos = self.get_input(game)
            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                if rect.collidepoint(pos) and (barrel in self.goods):
                    valid_input = True
                    goods_to_keep[0] = barrel
                    break

        if self.use_building(SmallWarehouse):
            button = fonts.h1.render("None",1,(255,255,255),(100,0,0))
            self.board.surface.blit(button,(500,500))
            button = button.get_rect()
            button.topleft = (500,500)
        
            instructions = fonts.reg.render("Please select one kind of good to store in small warehouse",1,(255,255,255))
            self.board.surface.blit(instructions,(25,520))
            valid_input = False
            while not valid_input:
                pos = self.get_input(game)
                for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                    if rect.collidepoint(pos) and (barrel in self.goods):
                        valid_input = True
                        goods_to_keep[1] = barrel
                        break
                    elif button.collidepoint(pos):
                        valid_input = True
                        break
        
        if self.use_building(LargeWarehouse):
            button = fonts.h1.render("None",1,(255,255,255),(100,0,0))
            self.board.surface.blit(button,(500,500))
            button = button.get_rect()
            button.topleft = (500,500)
        
            instructions = fonts.reg.render("Please select two kinds of goods to store in large warehouse",1,(255,255,255))
            self.board.surface.blit(instructions,(25,540))
            valid_input = False
            index = 2
            while not valid_input and index<4:
                pos = self.get_input(game)
                for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                    if rect.collidepoint(pos) and (barrel in self.goods):
                        goods_to_keep[index] = barrel
                        index += 1
                        break
                    elif button.collidepoint(pos):
                        valid_input = True
                        break                   
                    
        self.board.draw_current_player_marker(clear=True)
        self.board.clear_notifications()
        return goods_to_keep
