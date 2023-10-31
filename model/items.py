
from flask import Flask, request, jsonify

app = Flask()

# Sample list of items with categories
items = [
    {"id": 1, "name": "Product 1", "category": "Electronics"},
    {"id": 2, "name": "Product 2", "category": "Clothing"},
    {"id": 3, "name": "Product 3", "category": "Home & Kitchen"},
    {"id": 4, "name": "Product 4", "category": "Sports & Outdoors"},
]

# Endpoint to get a list of all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": items})

# Endpoint to get items by category
@app.route('/items/<string:category>', methods=['GET'])
def get_items_by_category(category):
    category_items = [item for item in items if item["category"] == category]
    return jsonify({"items": category_items})

if __name__ == '__main__':
    app.run(debug=True)
    
