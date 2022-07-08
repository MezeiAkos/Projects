import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
label = tk.Label(text="Hello, Tkinter",
                  width=10,
                  height=10)
label.pack()

window.mainloop()

class Product:
    def __init__(self, price, product_id, quantity):
        self.price = price
        self.productID = product_id
        self.quantity = quantity

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_inventory_value(self):
        value = 0
        for product in self.products:
            value += product.get_quantity() * product.get_price()

        return value


p1 = Product(10, "01", 10)
p2 = Product(20, "02", 10)
p3 = Product(25, "03", 10)

inventory = Inventory()
inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

print(inventory.get_inventory_value())
