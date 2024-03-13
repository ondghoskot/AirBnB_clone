#!/usr/bin/python3
"""defining Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """amnety constructor"""
        super().__init__(*args, **kwargs)
