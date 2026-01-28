from flask import Blueprint, render_template
from datetime import datetime
from config import Config

home = Blueprint('home', __name__, template_folder='templates')

BACK_URL = Config.BACK_URL

@home.route('/')
def index():
    date = datetime.now().year
    return render_template('index.html', date=date)