width = float(input("width(m): "))
height = float(input("height(m): "))
tileCost = float(input("cost(/m2): "))
area = width * height
cost = "{:.2f}".format(area*tileCost)
print(cost)