"""
Unit tests for Examples/basic_class.py
Tests the basic Plane class implementation.
"""
import unittest
import sys
from pathlib import Path

# Add Examples directory to path
examples_path = Path(__file__).parent.parent / "Examples"
sys.path.insert(0, str(examples_path))

from basic_class import Plane


class TestPlane(unittest.TestCase):
    """Test cases for the Plane class."""

    def setUp(self):
        """Set up test fixtures."""
        self.plane = Plane("Boeing 787", "200")

    def test_plane_creation(self):
        """Test that a Plane object is created correctly."""
        self.assertEqual(self.plane.plane_model, "Boeing 787")
        self.assertEqual(self.plane.number_seats, "200")

    def test_plane_with_different_values(self):
        """Test Plane creation with different values."""
        cesna = Plane("Cesna 070", "4")
        self.assertEqual(cesna.plane_model, "Cesna 070")
        self.assertEqual(cesna.number_seats, "4")

    def test_plane_attributes_are_accessible(self):
        """Test that Plane attributes can be accessed."""
        self.assertTrue(hasattr(self.plane, 'plane_model'))
        self.assertTrue(hasattr(self.plane, 'number_seats'))
    
    def test_change_model(self):
        """Test changing the plane model."""
        self.plane.change_model("Airbus A380")
        self.assertEqual(self.plane.plane_model, "Airbus A380")
    
    def test_change_seats(self):
        """Test changing the number of seats."""
        self.plane.change_seats(250)
        self.assertEqual(self.plane.number_seats, 250)


if __name__ == '__main__':
    unittest.main()
