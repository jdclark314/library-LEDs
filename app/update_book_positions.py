"""
This module contains:
- the communication to the Google AI system
- updating the list of books and LED in the database
- correlating the position of books to LED lights

"""

from pymongo.collection import Collection
import vertexai
from vertexai.generative_models import GenerativeModel


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

def get_ai_response():
    """
    Generate a response from Vertex AI
    Currently only pulls in the textPrompt variable
    """
    vertexai.init(project="library-leds", location="us-central1")
    model = GenerativeModel(
      "gemini-1.5-flash-001",
    )
    responses = model.generate_content(
        [TEXT_PROMPT],
        generation_config=generation_config,
        stream=True,
    )
    return responses


def parse_text_response_from_vertex_ai(responses):
    """
    Parse the response from Vertex AI into a list of tuples
    Responses - value returned from AI request
    """
    text_list = []
    for response in responses:
        text_list.append(response.text)

    single_string_text_response = "".join(text_list)

    items_to_create = single_string_text_response.strip().split(');')
    parsed_data = []
    for item in items_to_create:
        item = item.strip(' (')
        if item:
            parsed_data.append(tuple(map(str.strip, item.split(','))))

    return parsed_data

# only here as placeholder to generate a text prompt later
TEXT_PROMPT = """
                Please send me back a list of 5 random book titles, with positions on a bookshelf in inches,
                the left and right sides of the book. Assume all books are side by side on bookshelf.
                Create the list in this format
                "(book_title, book_left_position, book_right_position);(book_title_2, book_left_position_2, book_right_position_3)".
                Continue this until all books are filled.
                Provide the list in a single string.
                Do not provide any other text other than the strings of books
            """

def update_titles_in_DB(resp: list, collection: Collection):
    """
    Updates titles in the DB. Assumes list passed in is all books in library
    resp is the parsed list of the response from the AI
    Collection is the mongo DB to store values
    """

    for r in resp:
        # change this to append doc to alist
        # after the for loop use .insert_many
        doc = {
            "title": r[0],
            "left_pos": r[1],
            "right_pos": r[2]
        }
        collection.insert_one(doc)


def start_book_position_update(collection: Collection):
    """
    Main driving function of updating book positions
    Collection is the mongo DB to store values
    """
    # generate prompt to send to AI system
    # send image and prompt to AI
    responses = get_ai_response()
    # accept and parse response
    parsed_response = parse_text_response_from_vertex_ai(responses)
    # need to determine LED positions of the books
    # need to clear out the collection prior to updating DB
    #   we will just clear it out and make a new list of the entries
    #   just cause its less code to wipe clean than to conditionally find fields to update
    update_titles_in_DB(parsed_response, collection)
