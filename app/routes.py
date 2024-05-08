"""
Module docstring to come detailing the routes and functions later
So far only test functions here
"""

from flask import jsonify, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def hello_world():
    """A test function that can be removed when no longer needed"""
    print("test2")
    return "<p>Hello, World2!</p>"

@main.route("/testPost", methods=["POST"])
def test_post_request():
    """A test function that can be removed when no longer needed"""
    print("We succeeded with test post")
    # random test return response
    response = {
        'message': 'Data received',
        'name': "my name",
        'age': 25,
        'refactorTest': "success"
    }
    return jsonify(response)
