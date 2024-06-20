"""
This module contains:
- the communication to the Google AI system
- updating the list of books and LED in the database
- correlating the position of books to LED lights

"""

import vertexai
from vertexai.generative_models import GenerativeModel
# import vertexai.preview.generative_models as generative_models
# from vertexai.preview import generative_models

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

# only removed to push code cause not dealing with lint errors right now
# safety_settings = {
#     generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH:
# generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:
# generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT:
# generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT:
# generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
# }

def generate():
    """
    Mock function to test connection to Google AI
    """
    vertexai.init(project="library-leds", location="us-central1")
    model = GenerativeModel(
      "gemini-1.5-flash-001",
    )
    # mock content to test, update with correct values
    responses = model.generate_content(
        ["""Please tell me a poem in haiku format"""],
        generation_config=generation_config,
        # safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

def start_book_position_update():
    """
    Main driving function of updating book positions
    """
    # connect to AI system
    # print(connect_to_google())
    generate()
    # generate prompt to send to AI system
    # send image and prompt to AI
    # accept and parse response
    # update titles of books in database
    # update positions of books in database
