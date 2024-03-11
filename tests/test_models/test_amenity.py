#!/usr/bin/python3
"""Test Amenity Module"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

if __name__ == "__main__":
    unittest.main()
  
