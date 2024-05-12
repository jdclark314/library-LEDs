"""
Config files to be shared with multiple test files
"""


import pytest
from flask import Flask
from app.routes import create_routes_blueprint

@pytest.fixture
def client(mocker):
    """
    A fixture to mock the flask app for testing
    """
    app = Flask(__name__)
    # Mock the MongoDB collection
    mock_collection = mocker.MagicMock()
    main_blueprint = create_routes_blueprint(mock_collection)
    app.register_blueprint(main_blueprint)
    with app.test_client() as testing_client:
        yield testing_client, mock_collection
