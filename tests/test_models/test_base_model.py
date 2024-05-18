#!/usr/bin/python3
"""Unittests for class BaseModel."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for class BaseModel."""

    def setUp(self):
        """Sets up methods for tests."""
        pass

    def tearDown(self):
        """Tears down methods as clean up post tests."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Instantiation test of BaseModel class object."""
        obj = BaseModel()
        self.assertEqual(str(type(obj)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(issubclass(type(obj), BaseModel))

    def test_no_args(self):
        """Tests __init__ method with no arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError) as bug:
            BaseModel.__init__()
        text = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(bug.exception), text)

    def test_many_args(self):
        """Many arguments test for __init__."""
        self.resetStorage()
        args = [i for i in range(1000)]
        obj = BaseModel(56, 23, 22, 83, 74, 95, 56, 27, 78, 39)
        obj = BaseModel(*args)

    def test_id(self):
        """Tests for unique user ids."""
        store = []
        for i in range(1000):
            store.append(BaseModel().id)
        self.assertEqual(len(set(store)), len(store))

    def test_datetime(self):
        """Tests attributes updated_at and created_at are correct"""
        date_now = datetime.now()
        obj = BaseModel()
        dif = obj.updated_at - obj.created_at
        self.assertTrue(abs(dif.total_seconds()) < 0.01)
        dif = obj.created_at - date_now
        self.assertTrue(abs(dif.total_seconds()) < 0.1)

    def test_save(self):
        """Tests the save() method."""
        obj = BaseModel()
        time.sleep(0.5)
        now = datetime.now()
        obj.save()
        dif = obj.updated_at - now
        self.assertTrue(abs(dif.total_seconds()) < 0.01)
    
    def test_3_str(self):
        """Tests for __str__ method."""
        b = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)


if __name__ == '__main__':
    unittest.main()
