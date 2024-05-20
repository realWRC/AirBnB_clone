#!/usr/bin/python3
""" Module for class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class that defines objects of type Review """

    place_id = ""
    user_id = ""
    text = ""
