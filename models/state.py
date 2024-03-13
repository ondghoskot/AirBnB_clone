#!/usr/bin/python3
"""defining State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """State constructor"""
        super().__init__(*args, **kwargs)
