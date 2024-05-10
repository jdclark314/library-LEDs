"""
Models to support the project
"""

from dataclasses import dataclass
from typing import Optional
from bson import ObjectId

@dataclass
class SingleBookByTitleRequest:
    """
    A dataclass for handling book retrieval requests by title.

    Attributes:
        title (str): The title of the book to retrieve.

    Methods:
        validate: Validates that the title is a non-empty string.
    """
    title: str

    def validate(self):
        """
        Validate the incoming request to ensure that the title is a non-empty string.

        Raises:
            ValueError: If the title is not a string or is an empty string.
        """
        if not isinstance(self.title, str):
            raise ValueError("Invalid title: must be a string")
        if not self.title.strip():
            raise ValueError("Invalid title: cannot be empty.")

@dataclass
class Book:
    """
    A dataclass that represents a book record in a MongoDB collection.

    Attributes:
        _id (Optional[ObjectId]): The MongoDB document identifier, optional for new entries.
        Title (str): The title of the book.
        Author (str): The name of the book's author.
        publish_year (int): The year the book was published.
        LED_position (int): The position of the book's associated LED indicator.

    TODO:
        - Fix the casing in the attribute names to match Python style guidelines.
        - Update the collection schema to reflect attribute name changes.
    """
    _id: Optional[ObjectId] = None  # Use Optional to handle None values during insertion
    title: str = ''
    author: str = ''
    publish_year: int = 0
    led_position: int = -1
