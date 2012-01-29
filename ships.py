class Ship():
    def __init__(self,capacity=0):
        self.capacity = capacity
        self.goods = []
    def __repr__(self):
        return "\n"+str(self.capacity)+": "+str(self.goods)
    def full(self):
        return len(self.goods)>=self.capacity
    def can_load(self,good):
        if not self.full():
            if not len(self.goods):
                return True
            elif good in self.goods:
                return True
        return False
