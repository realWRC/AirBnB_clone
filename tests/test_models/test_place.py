#!/usr/bin/python3
"""Unittest for class Place."""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
import os
import unittest


class TestPlace(unittest.TestCase):
    """Test cases for class Place"""

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

    def test_3_instantiation(self):
        """Tests instantiation of the Place class."""
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertEqual(str(type(obj)), "<class 'models.place.Place'>")


if __name__ == "__main__":
    unittest.main()
