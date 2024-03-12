#!/usr/bin/python3
"""defining Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        """Review constructor"""
        super().__init__(*args, **kwargs)
