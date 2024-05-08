"""
__init__.py: Application Factory Module

This module serves as the entry point for the Flask application, providing
the application factory function `create_app` to initialize and configure the
Flask application instance.

- Imports:
  - `os`: Provides access to environment variables for dynamic configuration.
  - `Flask`: Core Flask framework for web application creation.
  - `PyMongo`: Flask extension for MongoDB database integration.

- Global Variables:
  - `mongo`: PyMongo instance for connecting to MongoDB.

- Functions:
  - `create_app`: Application factory function that:
    - Creates and configures the Flask app instance.
    - Loads environment-specific configurations.
    - Initializes database extensions.
    - Registers blueprints for routing and API management.

This file implements the "application factory" pattern, allowing for multiple
configurations and environments to be used during runtime by setting
the `FLASK_ENV` environment variable.
"""

import os
from flask import Flask
from flask_pymongo import PyMongo


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
