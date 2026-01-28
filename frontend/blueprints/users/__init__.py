from flask import Blueprint, render_template
import requests
from config import Config

users = Blueprint('users', __name__, template_folder='templates')

BACK_URL = Config.BACK_URL

@users.route('/users/create')
def users_create():
    try:
        response = requests.get(f"{BACK_URL}/api/users/create")
        users = []
    except:
        users = []
    return render_template('index.html', users=users)

@users.route('/users')
def users_view():
    try:
        response = requests.get(f"{BACK_URL}/api/users")
        users = response.json() if response.status_code == 200 else []
    except:
        users = []
    return render_template('index.html', users=users)
