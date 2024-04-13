#Create a class Product


class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name: str, author: str, price: int, quantity: int):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"This book is {self.name} written by {self.author}. Price is {self.price} and {self.quantity} books available")


newbook = Book("Book", "Me", 20, 1)
newbook.read()


# Restaurant class


class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

    def display_menu(self):
        print(f"{self.name} serves {self.cuisine} cuisine:")
        for dish, price in self.menu.items():
            print(f"{dish}: ${price}")


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
        self._update_available_quantity()

    def _update_available_quantity(self):
        for dish, dish_info in self.menu.items():
            self.menu[dish]["available"] = dish_info["quantity"]

    def order(self, dish_name, quantity):
        if dish_name not in self.menu:
            return f"Sorry, {dish_name} is not available in our menu."

        dish_info = self.menu[dish_name]
        available_quantity = dish_info["available"]

        if quantity > available_quantity:
            return f"Sorry, we only have {available_quantity} {dish_name}(s) available."

        total_cost = dish_info["price"] * quantity
        self.menu[dish_name]["available"] -= quantity

        return f"Your order of {quantity} {dish_name}(s) costs ${total_cost}. Enjoy your meal!"


menu = {
    "burger": {"price": 5, "quantity": 10},
    "pizza": {"price": 10, "quantity": 20},
    "drink": {"price": 1, "quantity": 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))
print(mc.order('burger', 15))
print(mc.order('soup', 5))