products_data = [] 
product_list = [
    "Apples",
    "Bananas",
    "Oranges",
    "Plums",
    "Grapefruit",
    "Salmon",
    "Crackers",
    "Cookies",
    "Cheetos",
    "Chicken",
    "Pear",
    "Salad",
    "Tomato",
    "Brown Bread",
    "White Bread",
    "Tortilla",
    "Muffin",
    "Lettuce",
    "Spinach",
    "Okra",
    "Onions",
    "Cabbage",
    "Potatoes",
    "Mushroom"
]

category_list = [
    "Fruit", 
    "Fruit",
    "Fruit",
    "fruit",
    "Fruit",
    "Meat", 
    "Snack", 
    "Snack",
    "Snack",
    "Meat",
    "Fruit",
    "Vegtable",
    "Vegtable",
    "Vegtable",
    "Wheat",
    "Wheat",
    "Wheat",
    "Vegtable",
    "Vegtable",
    "Vegtable",
    "Vegtable",
    "Vegtable",
    "Vegtable",
    "Vegtable",

]

def initProducts():
    product_id = 1
    for product, category in zip(product_list, category_list):
        products_data.append({"id": product_id, "product": product, "category": category})
        product_id += 1

    
#Get function: returns all data
def getProducts(): 
    return(products_data)


#Get function: retuns product by id
def getProductsByCategory(category):
    matching_products = []
    for product_data in products_data:
        if product_data["category"] == category:
            matching_products.append(product_data)
    return matching_products


if __name__ == "__main__": 
    initProducts()  # initialize jokes
    getProducts() # return product data after initialization
    
   