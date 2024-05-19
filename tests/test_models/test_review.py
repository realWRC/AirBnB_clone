#!/usr/bin/python3
"""Unittest for class Review."""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.review import Review
import os
import unittest

class TestReview(unittest.TestCase):
    """Test cases for class Review"""

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
        """Tests instantiation of the Review class."""
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertEqual(str(type(obj)), "<class 'models.review.Review'>")


if __name__ == "__main__":
    unittest.main()
