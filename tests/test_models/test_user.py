#!/usr/bin/python3
"""Unittest for class User."""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
import os
import unittest


class TestUser(unittest.TestCase):
    """Test cases for class User"""

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
        """Tests instantiation of the User class."""
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertEqual(str(type(obj)), "<class 'models.user.User'>")


if __name__ == "__main__":
    unittest.main()
