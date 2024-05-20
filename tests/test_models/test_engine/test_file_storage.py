#!/usr/bin/python3
"""Unittests for class FileStorage"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for class FileStorage"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.reset()
        pass

    def reset(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_2_instantiation(self):
        """Tests instantiation of storage."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_2_init_zero_args(self):
        """Tests __init__ with no arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            FileStorage.__init__()
        message = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(error.exception), message)

    def test_2_init_multi_args(self):
        """Tests __init__ with many arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            obj = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        message = "FileStorage() takes no arguments"
        self.assertEqual(str(error.exception), message)

    def test_2_attributes(self):
        """Tests class attributes."""
        self.reset()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def all_test_helper(self, classname):
        """Helper tests all() method for classname."""
        self.reset()
        self.assertEqual(storage.all(), {})
        obj = storage.classtype()[classname]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_2_all(self):
        """Tests all() method on classes."""
        self.all_test_helper("BaseModel")
        self.all_test_helper("User")
        self.all_test_helper("State")
        self.all_test_helper("City")
        self.all_test_helper("Amenity")
        self.all_test_helper("Place")
        self.all_test_helper("Review")

    def all_overload_test_helper(self, classname):
        """Helper tests all() method with many objects for classname."""
        self.reset()
        self.assertEqual(storage.all(), {})
        supported = storage.classtype()[classname]
        objs = [supported() for i in range(1000)]
        [storage.new(obj) for obj in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], obj)

    def test_2_all_overload(self):
        """Tests all() method with many objects."""
        self.all_overload_test_helper("BaseModel")
        self.all_overload_test_helper("User")
        self.all_overload_test_helper("State")
        self.all_overload_test_helper("City")
        self.all_overload_test_helper("Amenity")
        self.all_overload_test_helper("Place")
        self.all_overload_test_helper("Review")

    def test_2_all_zero_args(self):
        """Tests all() with no arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            FileStorage.all()
        message = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), message)

    def test_2_all_multi_args(self):
        """Tests all() with too many arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            FileStorage.all(self, 708)
        message = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), message)

    def new_test_helper(self, classname):
        """Helps tests new() method for all classes."""
        self.reset()
        supported = storage.classtype()[classname]
        obj = supported()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], obj)

    def test_2_new(self):
        """Tests new() method for all Classes."""
        self.new_test_helper("BaseModel")
        self.new_test_helper("User")
        self.new_test_helper("State")
        self.new_test_helper("City")
        self.new_test_helper("Amenity")
        self.new_test_helper("Place")
        self.new_test_helper("Review")

    def test_2_new_zero_args(self):
        """Tests new() with no arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            storage.new()
        message = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(error.exception), message)

    def test_2_new_multi_args(self):
        """Tests new() with too many arguments."""
        self.reset()
        obj = BaseModel()
        with self.assertRaises(TypeError) as error:
            storage.new(obj, 109)
        message = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(error.exception), message)

    def save_test_helper(self, classname):
        """Helps tests save() method for classname."""
        self.reset()
        supported = storage.classtype()[classname]
        obj = supported()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        obj_dict = {key: obj.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(len(file.read()), len(json.dumps(obj_dict)))
            file.seek(0)
            self.assertEqual(json.load(file), obj_dict)

    def test_2_save(self):
        """Tests save() method for BaseModel."""
        self.save_test_helper("BaseModel")
        self.save_test_helper("User")
        self.save_test_helper("State")
        self.save_test_helper("City")
        self.save_test_helper("Amenity")
        self.save_test_helper("Place")
        self.save_test_helper("Review")

    def test_2_save_zero_args(self):
        """Tests save() with no arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            FileStorage.save()
        message = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), message)

    def test_2_save_overload(self):
        """Tests save() with too many arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            FileStorage.save(self, 109)
        message = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), message)

    def reload_test_helper(self, classname):
        """Helps test reload() with multiple classes."""
        self.reset()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        supported = storage.classtype()[classname]
        obj = supported()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        storage.reload()
        self.assertEqual(obj.to_dict(), storage.all()[key].to_dict())

    def test_2_reload(self):
        """Tests reload() method for all classes."""
        self.reload_test_helper("BaseModel")
        self.reload_test_helper("User")
        self.reload_test_helper("State")
        self.reload_test_helper("City")
        self.reload_test_helper("Amenity")
        self.reload_test_helper("Place")
        self.reload_test_helper("Review")

    def reload_mismatch_test_helper(self, classname):
        """Helps test reload() method mismatch handling with classname."""
        self.reset()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        supported = storage.classtype()[classname]
        obj = supported()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        obj.name = "Wongani"
        storage.reload()
        self.assertNotEqual(obj.to_dict(), storage.all()[key].to_dict())

    def test_2_reload_mismatch(self):
        """Tests reload() method mismatch for all classes."""
        self.reload_mismatch_test_helper("BaseModel")
        self.reload_mismatch_test_helper("User")
        self.reload_mismatch_test_helper("State")
        self.reload_mismatch_test_helper("City")
        self.reload_mismatch_test_helper("Amenity")
        self.reload_mismatch_test_helper("Place")
        self.reload_mismatch_test_helper("Review")

    def test_2_reload_zero_args(self):
        """Tests reload() with no arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            FileStorage.reload()
        message = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), message)

    def test_2_reload_multi_args(self):
        """Tests reload() with too many arguments."""
        self.reset()
        with self.assertRaises(TypeError) as error:
            FileStorage.reload(self, 108)
        message = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), message)


if __name__ == '__main__':
    unittest.main()
