from flask import Flask
from .users import users

def register_blueprints(app: Flask):
	app.register_blueprint(users)