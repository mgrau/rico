from player import *
from player_board import *
from plantations import *

class GUI_Player(Player):
    def __init__(self,index=0,name="",screen=0):
        Player.__init__(self,index,name)

        if not screen:
            self.screen = pygame.display.set_mode( (1024,768) )
        else:
            self.screen = screen
        self.board = Board((1024,768))

    def print_board(self,game):
        print game

    def get_input(self,game,build=False):
        self.screen.blit(self.board.surface,(0,0))
        pygame.display.flip()
        visible_player = self.index
        game_board = False
        valid_input = False
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_rel()
                if event.type == pygame.MOUSEBUTTONUP:
                    rel = pygame.mouse.get_rel()
                    if rel[0]<-10 and abs(rel[0])>abs(rel[1]) and not game_board:
                        if visible_player == len(game.players)-1:
                            next_player = 0
                        else:
                            next_player = visible_player+1
                        for i in range(1024,-1,-128):
                            self.screen.blit(game.players[visible_player].board.surface,(i-1024,0))
                            self.screen.blit(game.players[next_player].board.surface,(i,0))
                            pygame.display.flip()
                        visible_player = next_player
                    if rel[0]>10 and abs(rel[0])>abs(rel[1]) and not game_board:
                        if visible_player == 0:
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
                                pygame.display.flip()
                        else:
                            for i in range(768,-1,-96):
                                self.screen.blit(nextscreen,(0,i))
                                self.screen.blit(thisscreen,(0,i-768))
                                pygame.display.flip()
                        game_board = not game_board
                if event.type == pygame.MOUSEBUTTONUP:
                    if (visible_player == self.index and not game_board) or (build and game_board):
                        return event.pos
            game.clock.tick(30)


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
        instructions = font.render("Please select a plantation",1,(255,255,255))
        self.board.surface.blit(instructions,(32,736))
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
            button = h1.render("Done",1,(255,255,255),(100,0,0))
            instructions = font.render("Please place your colonists",1,(255,255,255))
            self.board.surface.blit(button,(32,676))
            button = button.get_rect()
            button.topleft = (32,676)
            self.board.surface.blit(instructions,(32,736))
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
        button = h1.render("Don't Buy",1,(255,255,255),(100,0,0))
        game.surface.blit(button,(32,676))
        button = button.get_rect()
        button.topleft = (32,676)
        event = pygame.event.Event(pygame.KEYDOWN)
        event.key = pygame.K_UP
        pygame.event.post(event)

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
        for pos,barrel,texture in zip(self.board.choose_barrel_grid,barrel_types,[corn_barrel, indigo_barrel, sugar_barrel, tobacco_barrel, coffee_barrel]):
            if barrel in self.produce_goods() and barrel in game.goods:
                self.board.surface.blit(texture,pos)
        instructions = font.render("Please select an extra good",1,(255,255,255))
        self.board.surface.blit(instructions,(32,736))

        valid_input = False
        while not valid_input:
            pos = self.get_input(game,build=True)
            for barrel,rect in zip(barrel_types,self.board.choose_barrel_grid):
                if rect.collidepoint(pos) and barrel in self.produce_goods() and barrel in game.goods:
                    return barrel

    def trader(self,game):
        game.draw(self.index)
        button = h1.render("Don't Sell",1,(255,255,255),(100,0,0))
        self.board.surface.blit(button,(32,676))
        button = button.get_rect()
        button.topleft = (32,676)
        instructions = font.render("Please select a good to sell",1,(255,255,255))
        self.board.surface.blit(instructions,(32,736))
        
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        valid_input = False
        while not valid_input:
            pos = self.get_input(game,build=True)
            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
                if rect.collidepoint(pos) and (barrel in self.goods) and (barrel not in game.trading_house or self.use_building(Office)):
                    return barrel
            if button.collidepoint(pos):
                return Barrel()


    def captain(self,game):
        game.draw(self.index)
        instructions = font.render("Please select a good to ship",1,(255,255,255))
        self.board.surface.blit(instructions,(32,736))

        valid_input = False
#        while not valid_input:
#            pos = self.get_input(game,build=True)
#            for barrel,rect in zip(barrel_types,self.board.barrel_grid):
#                if rect.collidepoint(pos) and (barrel in self.goods) and (barrel not in game.trading_house or self.use_building(Office)):
        print "\n"+self.name+", choose a shipment"
        choices = []
        for ship in game.ships:
            for good in self.goods:
                if (ship,good) not in choices and ship.can_load(good) and not any([good in othership.goods for othership in filter(lambda x:x!=ship,game.ships)]):
                    print str(len(choices))+": ship "+str(good)+" on ship("+str(ship.capacity)+")"
                    choices.append((ship,good))
        if self.use_building(Wharf) and not self.wharf.full():
            for good in self.goods:
                if (self.wharf,good) not in choices and self.wharf.can_load(good) and not any([good in othership.goods for othership in game.ships]):
                    print str(len(choices))+": ship "+str(good)+" on wharf"
                    choices.append((self.wharf,good))
            print str(len(choices))+": do not use wharf this turn"
            choices.append((self.wharf,Barrel()))
        if len(choices)==1:
            return choices[0]
        choice = ''
        while choice not in [str(i) for i in range(len(choices))]:
            choice = self.get_input(game)
        if self.use_building(Wharf) and not self.wharf.full() and int(choice) == len(choices)-1:
            self.wharf.capacity = -1
        return choices[int(choice)]

    def rot(self,game):
        self.print_board(game)
        print "\n"+self.name+", choose a good to keep"
        choices = []
        for good in self.goods:
            if good not in choices:
                print str(len(choices))+": "+str(good)
                choices.append(good)
        choice = ''
        while choice not in [str(i) for i in range(len(choices))]:
            choice = self.get_input(game)
        goods_to_keep = [choices[int(choice)]]

        # TODO: deal with warehouses
        return goods_to_keep
