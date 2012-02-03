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

    def get_input(self,game,text="choice? "):
        choice = raw_input(text)

        return choice

    def choose_role(self,game):
        self.board.draw(self)
        self.board.draw_roles(game)
        self.screen.blit(self.board.surface,(0,0))
        pygame.display.flip()

        choice = 0
        valid_input = False
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i,rect in enumerate(self.board.role_grid):
                        if rect.collidepoint(event.pos):
                            valid_input = True
                            choice = i
                            break
        return choice

    def settler(self,game):
        self.board.draw(self)
        for pos,plantation in zip(self.board.choose_plantation_grid,game.plantations):
            self.board.draw_plantation(plantation,pos)
        if len(game.quarries)>0 and (self.index == game.current_player or self.use_building(ConstructionHut)):
            self.board.draw_plantation(Quarry(),self.board.choose_plantation_grid[len(game.plantations)])
        self.screen.blit(self.board.surface,(0,0))
        pygame.display.flip()

        choice = 0
        valid_input = False
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i,rect in enumerate(self.board.choose_plantation_grid):
                        if rect.collidepoint(event.pos) and i<=len(game.plantations):
                            valid_input = True
                            choice = i
                            break
        return choice

    def mayor(self,game):

        
        done = False
        while not done:
            self.board.draw(self)
            self.screen.blit(self.board.surface,(0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i,rect in enumerate(self.board.plantation_grid):
                        if rect.collidepoint(event.pos) and i<len(self.plantations):
                            if self.plantations[i].colonists > 0:
                                self.san_juan += self.plantations[i].colonists
                                self.plantations[i].colonists = 0
                            else:
                                if self.san_juan > 0:
                                    self.plantations[i].colonists = 1
                                    self.san_juan -= 1
                    for i,rect in enumerate(self.board.building_grid):
                        if rect.collidepoint(event.pos) and i<len(self.buildings):
                            if self.buildings[i].colonists >= self.buildings[i].capacity:
                                self.san_juan += self.buildings[i].colonists
                                self.buildings[i].colonists = 0
                            else:
                                if self.san_juan > 0:
                                    self.buildings[i].colonists += 1
                                    self.san_juan -= 1
                                elif self.buildings[i].colonists > 0:
                                    self.buildings[i].colonists -= 1
                                    self.san_juan += 1
        return

    def builder(self,game):
        building_grid = []
        size = (154,83)
        for row in range(4):
            for column in range(6):
                building_grid.append(pygame.Rect( (25+(size[0]+10)*column, 158+(size[1]+10)*row),size))
        choices = []
        already_printed = []
        for i,building in enumerate(game.buildings):
            if building.__class__ not in already_printed:
                self.board.draw_building(building,building_grid[len(already_printed)])
                choices.append(i)
                already_printed.append(building.__class__)
        self.screen.blit(self.board.surface,(0,0))
        pygame.display.flip()
        choice = 0
        valid_input = False
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i,rect in zip(choices,building_grid):
                        if rect.collidepoint(event.pos):
                            if self.afford_building(game.buildings[i]) and (not self.have_building(game.buildings[i].__class__)):
                                valid_input = True
                                choice = i

        return choice
    def craftsman(self,game):
        self.board.draw(self)
        self.screen.blit(self.board.surface,(0,0))
        pygame.display.flip()

        choice = 0
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]
        valid_input = False
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for barrel,rect in zip(barrel_types,self.board.good_grid):
                        if rect.collidepoint(event.pos) and barrel in self.goods and barrel in game.goods:
                            valid_input = True
                            choice = barrel
                            break
        return choice


    def trader(self,game):
        self.board.draw(self)
        self.screen.blit(self.board.surface,(0,0))
        pygame.display.flip()
        
        barrel_types = [CornBarrel(),IndigoBarrel(),SugarBarrel(),TobaccoBarrel(),CoffeeBarrel()]

        choice = Barrel()
        valid_input = False
        while not valid_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for barrel,rect in zip(barrel_types,self.board.good_grid):
                        if rect.collidepoint(event.pos) and (barrel not in game.trading_house or self.use_building(Office)):
                            valid_input = True
                            choice = barrel
                            break 
        return choice

    def captain(self,game):
        self.print_board(game)
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
