from flask import Blueprint, jsonify, request
from flask import Flask # import flask to enable endpoints
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import json
import os
#Initialize flask

def InitCart_app():
    app = Flask (__name__)
    api = Api(app)

cart_api = Blueprint('cart_api', __name__,
                   url_prefix='/api/cart')

api = Api(cart_api)


class Cart(Resource):
    def post(self):
        body = request.get_json()
        with open('./cart.txt', "w") as f:
            f.write(json.dumps(body))

        return {},201
    
    def get(self):
        content = '{}'
        if(os.path.exists('./cart.txt')):
            with open('./cart.txt', 'r') as content_file:
                content = content_file.read()
        return json.loads(content),200
    
    def delete(self):
        if(os.path.exists('./cart.txt')):
            os.remove('./cart.txt')
        return {},200

 # Adding endpoints for login
api.add_resource(Cart,'/')
# main
if __name__ == "__main__":
    server = "http://127.0.0.1:8350"
    url = server + "/api/login"
    responses = []
    for response in responses:
        print(response)
        try:    
            print(response.json())
        except:
            print("unknown error")

# Initialize the Flasks app and start the server 
InitCart_app()








