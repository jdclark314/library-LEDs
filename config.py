import os

class Config:
    """Base configuration class with common settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mydefaultsecretkey')

class DevelopmentConfig(Config):
    """Development environment settings."""
    DEBUG = True
    MONGO_URI = os.environ.get('DEV_MONGO_URI', 'mongodb://localhost:27017/dev_db')

class ProductionConfig(Config):
    """Production environment settings."""
    DEBUG = False
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/prod_db')