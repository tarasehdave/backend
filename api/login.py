from flask import Blueprint, jsonify
from flask import Flask # import flask to enable endpoints
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
#Initialize flask

def InitLogin_app():
    app = Flask (__name__)
    api = Api(app)

login_api = Blueprint('login_api', __name__,
                   url_prefix='/api/login')

api = Api(login_api)


class Login(Resource):
    def post(self):
        return{},200
 # Adding endpoints for login
api.add_resource(Login,"/login")
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
InitLogin_app()








