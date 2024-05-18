#!/usr/bin/python3
""" Module for class Place """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class that defines objects of type Place """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
