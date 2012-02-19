import pygame

tiles = []
barrels = []

island = pygame.image.load('res/island.png')
tiles.append(island)

points = pygame.image.load('res/points.png')
tiles.append(points)
gold = pygame.image.load('res/gold_coin.png')
tiles.append(gold)
silver = pygame.image.load('res/silver_coin.png')
tiles.append(silver)

quarry = pygame.image.load('res/quarry.png')
corn = pygame.image.load('res/corn.png')
indigo = pygame.image.load('res/indigo.png')
sugar = pygame.image.load('res/sugar.png')
tobacco = pygame.image.load('res/tobacco.png')
coffee = pygame.image.load('res/coffee.png')
tiles.append(quarry)
tiles.append(corn)
tiles.append(indigo)
tiles.append(sugar)
tiles.append(tobacco)
tiles.append(coffee)

corn_barrel = pygame.image.load('res/corn_barrel.png')
indigo_barrel = pygame.image.load('res/indigo_barrel.png')
sugar_barrel = pygame.image.load('res/sugar_barrel.png')
tobacco_barrel = pygame.image.load('res/tobacco_barrel.png')
coffee_barrel = pygame.image.load('res/coffee_barrel.png')
barrels.append(corn_barrel)
barrels.append(indigo_barrel)
barrels.append(sugar_barrel)
barrels.append(tobacco_barrel)
barrels.append(coffee_barrel)
tiles.extend(barrels)

small_indigo_plant = pygame.image.load('res/small_indigo_plant.png')
indigo_plant = pygame.image.load('res/indigo_plant.png')
small_sugar_mill = pygame.image.load('res/small_sugar_mill.png')
sugar_mill = pygame.image.load('res/sugar_mill.png')
tobacco_storage = pygame.image.load('res/tobacco_storage.png')
coffee_roaster = pygame.image.load('res/coffee_roaster.png')
small_violet = pygame.image.load('res/small_violet.png')
large_violet = pygame.image.load('res/large_violet.png')
tiles.append(small_indigo_plant)
tiles.append(indigo_plant)
tiles.append(small_sugar_mill)
tiles.append(sugar_mill)
tiles.append(tobacco_storage)
tiles.append(coffee_roaster)
tiles.append(small_violet)
tiles.append(large_violet)

settler = pygame.image.load('res/settler.png')
mayor = pygame.image.load('res/mayor.png')
builder = pygame.image.load('res/builder.png')
craftsman = pygame.image.load('res/craftsman.png')
trader = pygame.image.load('res/trader.png')
captain = pygame.image.load('res/captain.png')
prospector = pygame.image.load('res/prospector.png')
tiles.append(settler)
tiles.append(mayor)
tiles.append(builder)
tiles.append(craftsman)
tiles.append(trader)
tiles.append(captain)
tiles.append(prospector)

def convert_all():
    for tile in tiles:
        tile.convert_alpha()
        tile.convert()


