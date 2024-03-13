#!/usr/bin/python3
"""defining City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City constructor"""
        super().__init__(*args, **kwargs)
