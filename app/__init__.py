# app/__init__.py

from flask import Flask
from flask_pymongo import PyMongo
import os

# Initialize the database
mongo = PyMongo()


def create_app():
    """Create and configure the Flask app instance."""
    app = Flask(__name__)

    # setup different environment variables here, when ready
    env = os.getenv('FLASK_ENV', 'DevelopmentConfig')
    app.config.from_object(f'config.{env}')

    # Initialize extensions with the app
    mongo.init_app(app)

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app