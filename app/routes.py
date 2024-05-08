from flask import Flask, jsonify, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def hello_world():
    """A test function that can be removed when no longer needed"""
    print("test2")
    return "<p>Hello, World2!</p>"

@main.route("/testPost", methods=["POST"])
def testPostRequest():
    print("We succeeded with test post")
    # random test return response
    response = {
        'message': 'Data received',
        'name': "my name",
        'age': 25,
        'refactorTest': "success"
    }
    return jsonify(response)