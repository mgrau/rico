class Ship():
	def __init__(self,capacity=0):
		self.capacity = capacity
		self.goods = []
	def __repr__(self):
		return self.goods