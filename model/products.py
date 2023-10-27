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
    "Tomato"
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
    ""
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

    ''

]

def initProducts(): 
    product_id = 0 
    for product in product_list: 
        products_data.append({"id": product_id, "product": product, "category": "$1.00"})
        product_id += 1
    

#Get function: returns all data
def getProducts(): 
    return(products_data)


#Get function: returns product by id
def getProduct(category):
    return(products_data[id])
