from flask import Blueprint, jsonify
from pymongo import MongoClient
from config import Config

users = Blueprint('users', __name__)

client = MongoClient(Config.MONGO_URI)
db = client["gps_thread_iot_db"]
collection = db["users"]