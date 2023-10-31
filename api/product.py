from flask import Blueprint, jsonify
from flask_restful import Api, Resource

from model.products import getProducts, getProductsByCategory  # Import functions from the correct module

product_api = Blueprint('product_api', __name__,
                   url_prefix='/api/products')

api = Api(product_api)

class ProductsAPI: 
    class _Create(Resource):
        def post(self, product, category):
            pass
    
    class _Read(Resource):
        def get(self):
            return jsonify(getProducts())
    
    # getProduct
    class _ReadCategory(Resource): 
        def get(self, category):
            return jsonify(getProductsByCategory(category))
        
    api.add_resource(_Create, '/create/<string:product>/<string:category>')
    api.add_resource(_Read, '/all')
    api.add_resource(_ReadCategory, '/<string:category>')

if __name__ == "__main__": 
    server = "http://127.0.0.1:8350"
    url = server + "/api/products"
    responses = []

    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
            