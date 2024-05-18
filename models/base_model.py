#!/usr/bin/python3
""" Module containing BaseModel """

import uuid
from models import storage
from datetime import datetime


class BaseModel:

    """
    Defines class BaseModel which is a parent class for all classes in this
    project
    """

    def __init__(self, *args, **kwargs):
        """ Initialises instance attributes """

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = uuid.UUID(value)
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ Updates updated_at instance attribute """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns dictionary of attribute value pairs in instance namespace:
            self_cpy - copy of instace __dict__ dictionary
        """

        self_cpy = self.__dict__.copy()
        self_cpy['__class__'] = type(self).__name__
        self_cpy['created_at'] = (self.created_at).isoformat()
        self_cpy['updated_at'] = (self.updated_at).isoformat()
        return self_cpy

    def __str__(self):

        """ Returns string representation of the class instance """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)
