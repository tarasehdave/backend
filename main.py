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



