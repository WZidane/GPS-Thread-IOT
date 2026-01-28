from flask import Blueprint, jsonify
from pymongo import MongoClient
from config import Config

users = Blueprint('users', __name__)

userA = {"name": "Alice"}

client = MongoClient(Config.MONGO_URI)
db = client["gps_thread_iot_db"]
collection = db["users"]

@users.route('/create', methods=['GET'])
def set_users():
    result = collection.insert_one(userA)
    return jsonify({"message": "Utilisateur créé"})

@users.route('/', methods=['GET'])
def get_users():
    users = list(collection.find({}, {"_id": 0, "name": 1}))
    return jsonify(users)