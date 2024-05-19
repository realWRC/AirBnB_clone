#!/usr/bin/python3
"""Unittest for class Amenity."""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
import os
import unittest

class TestAmenity(unittest.TestCase):
    """Test cases for class Amenity"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down as clean up."""
        self.reset()
        pass

    def reset(self):
        """Resets FileStorage."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_5_instantiation(self):
        """Tests instantiation of the Amenity class."""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertEqual(str(type(obj)), "<class 'models.amenity.Amenity'>")


if __name__ == "__main__":
    unittest.main()
