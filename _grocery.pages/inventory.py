class GroceryStore:
    def __init__(self):
        self.inventory = {}

    def add_item(self, category, item_name, price):
        if category not in self.inventory:
            self.inventory[category] = {}
        self.inventory[category][item_name] = price

    def display_inventory(self):
        print("Grocery Store Inventory:")
        for category, items in self.inventory.items():
            print(f"{category}:")
            for item, price in items.items():
                print(f"- {item}: ${price:.2f}")
    


# Create a grocery store object
store = GroceryStore()

# Add produce items to the inventory
store.add_item("Produce", "Tomatoes", 2.99)
store.add_item("Produce", "Carrots", 1.49)
store.add_item("Produce", "Lettuce", 1.99)

# Add fruit items to the inventory
store.add_item("Fruits", "Apples", 0.99)
store.add_item("Fruits", "Bananas", 0.59)
store.add_item("Fruits", "Oranges", 0.79)

# Add wheat items to the inventory
store.add_item("Wheat", "Whole Wheat Bread", 3.49)
store.add_item("Wheat", "Pasta", 2.29)
store.add_item("Wheat", "Flour", 2.99)

# Display the grocery store inventory
store.display_inventory()