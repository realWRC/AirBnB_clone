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

    def test_1_instantiation_args(self):
        """Tests instantiation of BaseModel class object."""
        obj = BaseModel()
        self.assertEqual(str(type(obj)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(issubclass(type(obj), BaseModel))

    def test_1_instantiation_kwags(self):
        """Tests instantiation of BaseModel with **kwargs."""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(new_obj.to_dict(), obj.to_dict())

    def test_1_instantiation_dict(self):
        """Tests instantiation with from custom dict with **kwargs."""
        c = {"__class__": "BaseModel",
             "updated_at":
             datetime(2077, 9, 28, 21, 3, 54, 52298).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "name": "Wongani",
             "age": 26,
             "grade": 98.89}
        new = BaseModel(**c)
        self.assertEqual(new.to_dict(), c)

    def test_1_zero_args(self):
        """Tests __init__ method with no arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError) as bug:
            BaseModel.__init__()
        text = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(bug.exception), text)

    def test_1_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        args = [i for i in range(1000)]
        obj = BaseModel(56, 23, 22, 83, 74, 95, 56, 27, 78, 39)
        obj = BaseModel(*args)

    def test_1_id(self):
        """Tests for instance attribute ids."""
        store = []
        for i in range(1000):
            store.append(BaseModel().id)
        self.assertEqual(len(set(store)), len(store))

    def test_1_datetime(self):
        """Tests attributes updated_at and created_at are correct"""
        date_now = datetime.now()
        obj = BaseModel()
        dif = obj.updated_at - obj.created_at
        self.assertTrue(abs(dif.total_seconds()) < 0.01)
        dif = obj.created_at - date_now
        self.assertTrue(abs(dif.total_seconds()) < 0.1)

    def test_1_save(self):
        """Tests the save() method."""
        obj = BaseModel()
        time.sleep(0.5)
        now = datetime.now()
        obj.save()
        dif = obj.updated_at - now
        self.assertTrue(abs(dif.total_seconds()) < 0.01)

    def test_1_str(self):
        """Tests for __str__ method."""
        obj = BaseModel()
        pattern = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        key = pattern.match(str(obj))
        self.assertIsNotNone(key)
        self.assertEqual(key.group(1), "BaseModel")
        self.assertEqual(key.group(2), obj.id)
        value = key.group(3)
        value = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", value)
        dict_1 = json.loads(value.replace("'", '"'))
        dict_2 = obj.__dict__.copy()
        dict_2["created_at"] = repr(dict_2["created_at"])
        dict_2["updated_at"] = repr(dict_2["updated_at"])
        self.assertEqual(dict_1, dict_2)

    def test_1_to_dict(self):
        """Tests to_dict() method."""
        obj = BaseModel()
        obj.last_name = "Chulu"
        obj.age = 26
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["__class__"], type(obj).__name__)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(obj_dict["last_name"], obj.last_name)
        self.assertEqual(obj_dict["age"], obj.age)

    def test_1_to_dict_many_args(self):
        """Tests to_dict() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as error:
            BaseModel.to_dict(self, 567)
        mg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), mg)

    def test_1_to_dict_zero_args(self):
        """Tests to_dict() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as error:
            BaseModel.to_dict()
        mg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), mg)

    def test_1_save(self):
        """Tests save() methods intergration with storage.save()."""
        self.resetStorage()
        obj = BaseModel()
        obj.save()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        new_obj = {key: obj.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(len(file.read()), len(json.dumps(new_obj)))
            file.seek(0)
            self.assertEqual(json.load(file), new_obj)

    def test_1_save_zero_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as error:
            BaseModel.save()
        mg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), mg)

    def test_1_save_many_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as error:
            BaseModel.save(self, 557)
        mg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), mg)


if __name__ == '__main__':
    unittest.main()
