from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from db import db
from config import Config
from jwt_callbacks import initialize_jwt_callbacks
from dotenv import load_dotenv

from resources.user import blp as UserBlueprint

# Load environment variables from .env file
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt = JWTManager(app)
    initialize_jwt_callbacks(jwt)

    db.init_app(app)
    Migrate(app, db)
    api = Api(app)
    api.register_blueprint(UserBlueprint)

    return app
