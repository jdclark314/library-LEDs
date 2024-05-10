"""
Module docstring to come detailing the routes and functions later
So far only test functions here
"""

from flask import jsonify, Blueprint, request
from pymongo.collection import Collection

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
    
    @main.route("/singleBookByTitle", methods=["POST"])
    def get_single_book_by_title():
        """ Takes a book title and searches for the LED light position in the database"""
        try:
            request_data = SingleBookByTitleRequest(**request.json)
            request_data.validate()
            documents = collection.find({'Title': request_data.title}, {'_id': 0})
            books = [Book(**doc) for doc in documents]
            print("LED Position: ", books[0].LED_position)
            #TODO Pass the LED Position to the Light Controller functions 
            # This should also handle multiple copies of the same book correctly

            return "success"
        except ValueError as e:
            return jsonify({'error': str(e)})
        except Exception as e:
            return jsonify({'error': f"Unexpected error: {e}"})    

    return main
