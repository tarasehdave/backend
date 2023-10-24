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

# Collects the order details
@app.route('/order-details', methods=['GET'])
def get_order_details():
    order_details = OrderDetail.query.all()
    order_details_list = [{'OrderDetailID': detail.id, 'OrderID': detail.OrderID, 'GroceryItemID': detail.GroceryItemID, 'ItemCount': detail.ItemCount} for detail in order_details]
    return jsonify(order_details_list)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)





