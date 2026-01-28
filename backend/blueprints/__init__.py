from flask import Flask
from .users import users


def register_blueprints(app: Flask, api_prefix: str = '/api'):
    app.register_blueprint(users, url_prefix=f"{api_prefix}/users")