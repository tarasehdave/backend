import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.players import initPlayers


# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.player import player_api


# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(player_api)
app.register_blueprint(app_projects) # register app pages

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

@app.before_first_request
def activate_job():  # activate these items 
    initJokes()
    initUsers()
    initPlayers()

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8086")

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

<<<<<<< HEAD
=======
\
    
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocery_store.db'
db = SQLAlchemy(app)

class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.String(50), nullable=False)
    GroceryItemID = db.Column(db.String(50), nullable=False)
    ItemCount = db.Column(db.Integer, nullable=False)

@app.route('/order-details', methods=['POST'])
def create_order_detail():
    data = request.json
    order_detail = OrderDetail(OrderID=data['OrderID'], GroceryItemID=data['GroceryItemID'], ItemCount=data['ItemCount'])
    db.session.add(order_detail)
    db.session.commit()
    return jsonify({'message': 'Order detail created successfully'})

@app.route('/order-details', methods=['GET'])
def get_order_details():
    order_details = OrderDetail.query.all()
    order_details_list = [{'OrderDetailID': detail.id, 'OrderID': detail.OrderID, 'GroceryItemID': detail.GroceryItemID, 'ItemCount': detail.ItemCount} for detail in order_details]
    return jsonify(order_details_list)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


https://prod.liveshare.vsengsaas.visualstudio.com/join?C87CE6087C8E4A6C7EAE378221D2555A2DC4

import json

# Sample user data (you should use a database for this)
user_data = {
    "1234": {
        "email": "user1@example.com",
        "username": "user1",
        "first_name": "John",
        "last_name": "Doe",
    },
    "5678": {
        "email": "user2@example.com",
        "username": "user2",
        "first_name": "Jane",
        "last_name": "Smith",
    }
}

def login():
    user_id = input("User ID: ")
    email = input("Email: ")
    username = input("Username: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    if user_id in user_data and user_data[user_id]["email"] == email and user_data[user_id]["username"] == username and user_data[user_id]["first_name"] == first_name and user_data[user_id]["last_name"] == last_name:
        print("Login successful!")
    else:
        print("Login failed. Please check your credentials.")

if __name__ == "__main__":
    while True:
        choice = input("Do you want to login (L) or exit (E)? ").strip().lower()
        if choice == "l":
            login()
        elif choice == "e":
            break
        else:
            print("Invalid choice. Please enter 'L' to login or 'E' to exit.")
>>>>>>> 161682f9e9c9939e7bc63f21997ae11de4206bb4


