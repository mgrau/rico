class Plantation:
	def __init__(self,colonists=0,name=""):
		self.colonists = colonists
		self.name=name
	def __repr__(self):
		return self.name+"("+str(self.colonists)+")"


class Quarry(Plantation):
	def __init__(self,colonists=0):
		Plantation.__init__(self,colonists,"quarry")
class Corn(Plantation):
	def __init__(self,colonists=0):
		Plantation.__init__(self,colonists,"corn")
class Indigo(Plantation):
	def __init__(self,colonists=0):
		Plantation.__init__(self,colonists,"indigo")
class Sugar(Plantation):
	def __init__(self,colonists=0):
		Plantation.__init__(self,colonists,"sugar")
class Tobacco(Plantation):
	def __init__(self,colonists=0):
		Plantation.__init__(self,colonists,"tobacco")
class Coffee(Plantation):
	def __init__(self,colonists=0):
		Plantation.__init__(self,colonists,"coffee")