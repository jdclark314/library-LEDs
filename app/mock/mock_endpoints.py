"""
Mock third party API requests
"""
from unittest.mock import patch


def mock_generate_content(*_args, **_kwargs):
    """
    Mock function for calls to Google Vertex AI
    """
    class MockResponse:
        """
        Mock response object for Vertex AI
        """
        # pylint: disable=too-few-public-methods
        def __init__(self, text):
            self.text = text

    return [MockResponse("""(The Adventures of Sherlock Holmes, 0, 6.5);
                         (The Hitchhiker's Guide to the Galaxy, 6.5, 13);
                         (Pride and Prejudice, 13, 19.5);
                         (The Lord of the Rings, 19.5, 26);
                         (The Great Gatsby, 26, 32.5)""")]

def apply_mock():
    """
    Setup the needed mocks
    """
    patch('vertexai.generative_models.GenerativeModel.generate_content',
          side_effect=mock_generate_content).start()
