#!/usr/bin/python3
"""Test City Module"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

if __name__ == "__main__":
    unittest.main()
  
