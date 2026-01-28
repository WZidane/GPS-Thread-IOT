import os
from flask import Flask
from blueprints import register_blueprints
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_blueprints(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("BACK_PORT"))