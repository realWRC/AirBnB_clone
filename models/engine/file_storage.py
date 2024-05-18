#!/usr/bin/python3
""" Module containing FileStorage """

import os
import json


class FileStorage:
    """
    Definition for class FileStorage for serialising instances to JSON and
    deserialising JSON to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object to the dictionary __objects with key <classname>.<id>
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialises __objects to the JSON file at __file_path """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            data = {}
            for key, value in FileStorage.__objects.items():
                data[key] = value.to_dict()
            json.dump(data, file)
