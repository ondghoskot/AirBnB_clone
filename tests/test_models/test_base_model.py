#!/usr/bin/python3
"""Test file for BaseModel"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the super class BaseModel"""
    # Testing public instance attrs
    def test_id(self):
        """tests if id is a string"""
        my_model = BaseModel()
        self.assertTrue(type(my_model.id) == str)

    def test_uid(self):
        """tests if id is unique"""
        my_model0 = BaseModel()
        my_model1 = BaseModel()
        self.assertNotEqual(my_model0.id, my_model1.id)

    def test_time_at(self):
        """tests if created_at and updated_at are valid"""
        my_model = BaseModel()
        self.assertTrue(type(my_model.created_at) == datetime
                and type(my_model.updated_at == datetime))
    
    # Testing the magic method __str__
    def test_magic_str(self):
        """tests if __str__ method returns the correct format"""
        my_model = BaseModel()
        self.assertEqual(str(my_model),
                "[{}] ({}) {}".format(my_model.__class__.__name__,
                my_model.id, my_model.__dict__))
    
    # Testing public instance methods
    def test_save(self):
        """tests save method and if updated_at time has been updated after save()"""
        my_model = BaseModel()
        self.assertRaises(TypeError, my_model.save, "argument")
        original_datetime = my_model.updated_at
        my_model.save()
        current_datetime = my_model.updated_at
        self.assertGreater(current_datetime, original_datetime)

    def test_to_dict(self):
        """tests if to_dict works"""
        my_model = BaseModel()
        my_model.name = "akira"
        my_model.my_number = 68
        dicti = my_model.__dict__.copy()
        dicti["__class__"] = my_model.__class__.__name__
        dicti["created_at"] = my_model.created_at.isoformat()
        dicti["updated_at"] = my_model.updated_at.isoformat()
        self.assertEqual(my_model.to_dict(), dicti)

if __name__ == '__main__':
    unittest.main()
