"""
Module docstring to come detailing the routes and functions later
So far only test functions here
"""

from flask import jsonify, Blueprint, request
from pymongo.collection import Collection
from app.light_controller import turn_on_lights
from app.models import Book, SingleBookByTitleRequest

def create_routes_blueprint(collection: Collection) -> Blueprint:
    """Create and return the routes blueprint with the given collection."""
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

    @main.route("/testGet", methods=["GET"])
    def test_get_request():
        """A test function for gets"""
        title = "Echoes of Eternity"
        result = list(collection.find({'Title': title}, {'_id': 0}))
        return jsonify(result)


    @main.route("/testLight", methods=["POST"])
    def test_light_code():
        """A test function to learn about the light controller code"""
        print("We succeeded with test post")
        turn_on_lights([1,2,3])
        # going to want to create a function here that passes a list of ints
        # the function will just loop through the list and enable those lights
        # if that function gets to the end successfully send a success response back to here
        # this should allow me to mock out the implementation to send success/fail responses
        # later on on can develop the light control and figure that out more
        # random test return response
        response = {
            'message': 'Success',
        }
        return jsonify(response)

    @main.route("/singleBookByTitle", methods=["POST"])
    def get_single_book_by_title():
        """
        Takes a book title and searches for the LED light position in the database
        """
        try:
            request_data = SingleBookByTitleRequest(**request.json)
            request_data.validate()
            documents = collection.find({'title': request_data.title}, {'_id': 0})
            books = [Book(**doc) for doc in documents]
            led_positions = []
            for book in books:
                led_positions.append(book.led_position)
            turn_on_lights(led_positions)
            return "success"
        except ValueError as e:
            return jsonify({'error': str(e)})


    return main
