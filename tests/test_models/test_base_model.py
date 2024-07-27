#!/usr/bin/python3
"""
Test base_model
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Testing attributes and methods of BaseModel
    """
    def setUp(self):
        """
        setting up basic attributes for tests
        """
        self.base = BaseModel()

    def test_init(self):
        """Test BaseModel initialisation"""
        self.assertEqual(self.base.created_at, self.base.updated_at)
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertIsInstance(self.base.created_at, datetime)

    def test_save(self):
        """Test BaseModel.save() method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict() method"""
        self.myJSON = self.base.__dict__.copy()
        self.assertNotIn("__class__", self.myJSON)
        self.myJSON = self.base.to_dict()
        self.assertIn("__class__", self.myJSON)
        self.assertIsInstance(self.base.dict_obj["updated_at"], str)
        self.assertIsInstance(self.base.dict_obj["created_at"], str)

    def test_str(self):
        """Test the __str__() method"""
        self.baseStr = self.base.str()
        self.assertIsInstance(self.baseStr, str)
        self.baseStr = self.baseStr.split()
        self.assertIn("[BaseModel]", self.baseStr)

if __name__ == '__main__':
    unittest.main()
