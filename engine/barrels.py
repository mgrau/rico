class Barrel:
    def __init__(self, cost=-1, name=""):
        self.cost = cost
        self.name=name
    def __repr__(self):
        return self.name
    def __cmp__(self,other):
        return cmp(self.cost,other.cost)


class CornBarrel(Barrel):
    def __init__(self, cost=0):
        Barrel.__init__(self,cost,"corn")

class IndigoBarrel(Barrel):
    def __init__(self, cost=1):
        Barrel.__init__(self,cost,"indigo")

class SugarBarrel(Barrel):
    def __init__(self, cost=2):
        Barrel.__init__(self,cost,"sugar")

class TobaccoBarrel(Barrel):
    def __init__(self, cost=3):
        Barrel.__init__(self,cost,"tobacco")

class CoffeeBarrel(Barrel):
    def __init__(self, cost=4):
        Barrel.__init__(self,cost,"coffee")