#!/usr/bin/python3
"""Unit tests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Set up test objects."""
        self.base_model = BaseModel()
        self.base_model.name = "My_First_Model"
        self.base_model.my_number = 89

    def test_attributes(self):
        """Test public instance attributes."""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertTrue(hasattr(self.base_model, 'name'))
        self.assertTrue(hasattr(self.base_model, 'my_number'))

    def test_str_method(self):
        """Test __str__ method."""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """Test save method."""
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method."""
        obj_dict = self.base_model.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('name' in obj_dict)
        self.assertTrue('my_number' in obj_dict)

    def test_to_dict_method_types(self):
        """Test types of values in dictionary returned by to_dict method."""
        obj_dict = self.base_model.to_dict()
        self.assertEqual(type(obj_dict['__class__']), str)
        self.assertEqual(type(obj_dict['created_at']), str)
        self.assertEqual(type(obj_dict['updated_at']), str)
        self.assertEqual(type(obj_dict['name']), str)
        self.assertEqual(type(obj_dict['my_number']), int)

    def test_create_instance_from_dict(self):
        """Test creating instance from dictionary representation."""
        my_model_json = self.base_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertTrue(isinstance(my_new_model, BaseModel))
        self.assertEqual(my_new_model.id, self.base_model.id)
        self.assertEqual(my_new_model.name, self.base_model.name)
        self.assertEqual(my_new_model.my_number, self.base_model.my_number)
        self.assertEqual(my_new_model.created_at, self.base_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.base_model.updated_at)

if __name__ == "__main__":
    unittest.main()
      
