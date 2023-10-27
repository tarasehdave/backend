from flask import Blueprint, jsonify 
from flask_restful import Api, Resource 
import requests 
import random

from model.jokes import * 
