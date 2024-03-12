#!/usr/bin/python3
"""Deining User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User inheriting from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
