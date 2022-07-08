class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


class Inventory:
    def __init__(self):
        self.flowers = []

    def add_flower_to_inventory(self, flower):
        self.flowers.append(flower)

    def remove_flower_from_inventory(self, flower):
        self.flowers.remove(flower)

# TODO keep track of how many items are the same


class Bouquet:
    def __init__(self):
        self.bouquets = []

    def add_flower(self, flower):
        self.bouquets.append(flower)

    def get_bouquet_contents(self):
        f = []
        for flower in self.bouquets:
            f.append([flower.get_color(), flower.get_name()])
        return f
# TODO make this less ghetto lmao


f1 = Flower("rose", "red")
f2 = Flower("lily", "pink")
b1 = Bouquet()
b1.add_flower(f1)
b1.add_flower(f1)
b1.add_flower(f2)

print(b1.get_bouquet_contents())

# TODO make adding and removing flowers possible
# TODO make bouquets remove flowers, only make bouquets if it's possible with flowers within inventory
