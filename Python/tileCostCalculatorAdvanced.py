#TODO fix this shit it no worky

floorWidth = float(input("width(m): "))
floorHeight = float(input("height(m): "))
tileCost = float(input("cost(/m2): "))
tileWidth = float(input("tile width(m): "))
tileHeight = float(input("tile height(m): "))

floorArea = tileWidth * floorHeight
tileArea = tileWidth * tileHeight
numberOfWholeTiles = int(floorArea/tileArea)
remainingFloorSize =floorArea - numberOfWholeTiles

#calculate tile cost per tile
wholeTileCost = tileArea * tileCost
wholeTileCost2 = numberOfWholeTiles * wholeTileCost
remainingTilesCost = remainingFloorSize * tileCost
print("{:.2f}".format(wholeTileCost2), "{:.2f}".format(remainingTilesCost))