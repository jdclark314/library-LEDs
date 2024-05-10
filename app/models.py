# no database models yet, left here as placeholder
from dataclasses import dataclass
from typing import Optional
from bson import ObjectId

@dataclass
class SingleBookByTitleRequest:
    title: str

    def validate(self):
        """ validate the incoming request"""
        if not isinstance(self.title, str):
            raise ValueError("Invalid title: must be a string")
        if not self.title.strip():
            raise ValueError("Invalid title: cannot be empty.")
        
@dataclass
class Book:
    #TODO fix the casing here and in the collection schema
    _id: Optional[ObjectId] = None  # Use Optional to handle None values during insertion
    Title: str = ''
    Author: str = ''
    publish_year: int = 0
    LED_position: int = -1