from player import *
import code

class Human_Player(Player):
    def print_board(self,game):
        print game

    def choose_role(self,game):
        self.print_board(game)
        print "\n"+self.name+"'s Turn"
        print "choose a role:"
        for i,role in enumerate(game.roles):
            print str(i)+": "+str(role)
        choice = []
        while choice not in [str(i) for i in range(len(game.roles))]:
            choice = raw_input("choice? ")
            if choice == 'debug':
                code.interact(local=locals())
        return int(choice)

    def settler(self,game):
        self.print_board(game)
        print "\n"+self.name+", choose a plantation"
        if self.index==game.current_player or self.use_building(ConstructionHut):
            for i,plantation in enumerate(game.plantations+[Quarry()]):
                print str(i)+": "+str(plantation)
        else:
            for i,plantation in enumerate(game.plantations):
                print str(i)+": "+str(plantation)
        choice = []
        if self.index==game.current_player or self.use_building(ConstructionHut):
            while choice not in [str(i) for i in range(len(game.plantations)+1)]:
                choice = raw_input("choice? ")
        else:
            while choice not in [str(i) for i in range(len(game.plantations))]:
                choice = raw_input("choice? ")
        return int(choice)

    def mayor(self,game):
        self.print_board(game)
        done = False
        print "\n"+self.name+", place your colonists"
        while (not done) or (self.san_juan>0 and self.open_spots()>0):
            choice = []
            choices = []
            print "Colonists: "+str(self.san_juan)
            for i,plantation in enumerate(self.plantations):
                print str(len(choices))+": "+str(plantation)
                choices.append(i)
            for i,building in enumerate(self.buildings):
                print str(len(choices))+": "+str(building)
                choices.append(i)
            print str(len(choices))+": Done"
            choices.append(-1)
            while choice not in [str(i) for i in range(len(choices))]:
                choice = raw_input("choice? ")
            choice = int(choice)
            done = False
            if choices[choice] < 0:
                done = True
            else:
                if choice < len(self.plantations):
                    if self.plantations[choices[choice]].colonists > 0:
                        self.san_juan += self.plantations[choices[choice]].colonists
                        self.plantations[choices[choice]].colonists = 0
                    else:
                        if self.san_juan > 0:
                            self.plantations[choices[choice]].colonists = 1
                            self.san_juan -= 1
                else:
                    if self.buildings[choices[choice]].colonists >= self.buildings[choices[choice]].capacity:
                        self.san_juan += self.buildings[choices[choice]].colonists
                        self.buildings[choices[choice]].colonists = 0
                    else:
                        if self.san_juan > 0:
                            self.buildings[choices[choice]].colonists += 1
                            self.san_juan -= 1
                        elif self.buildings[choices[choice]].colonists > 0:
                            self.buildings[choices[choice]].colonists -= 1
                            self.san_juan += 1
        return

    def builder(self,game):
        self.print_board(game)
        print "\n"+self.name+", choose a building to buy"
        choices = []
        already_printed = []
        for i,building in enumerate(game.buildings):
            if self.afford_building(building) and (not self.have_building(building.__class__)) and (building.__class__ not in already_printed):
                print str(len(choices))+": "+building.name+"("+str(building.cost)+")"
                choices.append(i)
                already_printed.append(building.__class__)
        print str(len(choices))+": don't buy a building"
        choices.append(-1)
        choice = []
        while choice not in [str(i) for i in range(len(choices))]:
            choice = raw_input("choice? ")
        return choices[int(choice)]

    def craftsman(self,game):
        self.print_board(game)
        print "\n"+self.name+", choose an extra good"
        choices = []
        for i,good in enumerate(self.goods):
            if (good not in choices) and (good in game.goods):
                print str(len(choices))+": "+str(good)
                choices.append(good)
        if len(choices)==1:
            return choices[0]
        elif len(choices):
            choice = ''
            while choice not in [str(i) for i in range(len(choices))]:
                choice = raw_input("choice? ")
            return choices[int(choice)]
        else:
            return Barrel()


    def trader(self,game):
        self.print_board(game)
        print "\n"+self.name+", choose a good to trade"
        choices = []
        for good in self.goods:
            if good not in choices and (good not in game.trading_house or self.use_building(Office)):
                print str(len(choices))+": "+str(good)
                choices.append(good)
        if not len(choices):
            return Barrel()
        print str(len(choices))+": don't trade a good"
        choices.append(Barrel())
        choice = []
        while choice not in [str(i) for i in range(len(choices))]:
            choice = raw_input("choice? ")
        return choices[int(choice)]

    def captain(self,game):
        self.print_board(game)
        print "\n"+self.name+", choose a shipment"
        choices = []
        for ship in game.ships:
            for good in self.goods:
                if ship.can_load(good) and (ship,good) not in choices:
                    print str(len(choices))+": ship "+str(good)+" on ship("+str(ship.capacity)+")"
                    choices.append((ship,good))
        if len(choices)==1:
            return choices[0]
        choice = ''
        while choice not in [str(i) for i in range(len(choices))]:
            choice = raw_input("choice? ")
        return choices[int(choice)]