"""
config.py: Application Configuration Module

This module defines configuration settings for the Flask application.

Classes:
- `Config`:
  - The base configuration class, providing common settings.
  - Sets the `SECRET_KEY` from the environment variable `SECRET_KEY` or a default value.

- `DevelopmentConfig`:
  - Inherits from `Config` and provides settings specific to the development environment.
  - Enables debugging with `DEBUG = True`.
  - Sets `MONGO_URI` to either
        - to a local MongoDB development database 
        - to the environment variable `DEV_MONGO_URI`.

- `ProductionConfig`:
  - Inherits from `Config` and provides settings for the production environment.
  - Disables debugging with `DEBUG = False`.
  - Sets `MONGO_URI` to either
        - connect to a production MongoDB database via the environment variable `MONGO_URI`
        - localhost string 
  - TODO: update the production config default to error handle successfully

This module allows for easy switching between different environments based on application needs.
"""

import os

class Config:
    """Base configuration class with common settings."""
    # pylint: disable=too-few-public-methods
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mydefaultsecretkey')

class DevelopmentConfig(Config):
    """Development environment settings."""
    # pylint: disable=too-few-public-methods
    DEBUG = True
    MONGO_URI = os.environ.get('DEV_MONGO_URI', 'mongodb://localhost:27017/dev_db')

class ProductionConfig(Config):
    """Production environment settings."""
    # pylint: disable=too-few-public-methods
    DEBUG = False
    MONGO_URI = os.environ.get('PROD_MONGO_URI', 'mongodb://localhost:27017/prod_db')
