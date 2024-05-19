#!/usr/bin/python3
"""Unittest for class City."""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
import os
import unittest

class TestCity(unittest.TestCase):
    """Test cases for class City"""

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

    def test_4_instantiation(self):
        """Tests instantiation of the City class."""
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertEqual(str(type(obj)), "<class 'models.city.City'>")


if __name__ == "__main__":
    unittest.main()
