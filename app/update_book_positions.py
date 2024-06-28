"""
This module contains:
- the communication to the Google AI system
- updating the list of books and LED in the database
- correlating the position of books to LED lights

"""

import vertexai
from vertexai.generative_models import GenerativeModel


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

def generate():
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

    print("here is my parsed data: ", parsed_data)
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
def start_book_position_update():
    """
    Main driving function of updating book positions
    """
    # generate prompt to send to AI system
    # send image and prompt to AI
    responses = generate()
    # accept and parse response
    parsed_response = parse_text_response_from_vertex_ai(responses)
    print("this is the parsed response: ", parsed_response)


    # update titles of books in database
    # update positions of books in database
