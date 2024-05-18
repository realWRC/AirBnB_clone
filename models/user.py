#!/usr/bin/python3
""" This is module defines class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Subclass of BaseModel for managing objects of type User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
