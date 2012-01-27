from __future__ import division

class UI:
    def choose_role(self, game, player):
        pass

class TextUI(UI):
    def choose_role(self, game, player):
        print "\n"+player.name+"'s Turn"
        print "choose a role:"
        for i,role in enumerate(game.roles):
            print str(i)+": "+str(role)
        choice = []
        while choice not in [str(i) for i in range(len(game.roles))]:
            choice = raw_input("choice? ")
        return int(choice)