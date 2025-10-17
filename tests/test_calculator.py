"""
Unit tests for Examples/calculator.py
Tests the Calculator class implementation.
"""
import unittest
import sys
from pathlib import Path

# Add Examples directory to path
examples_path = Path(__file__).parent.parent / "Examples"
sys.path.insert(0, str(examples_path))

# Import only the class, not the module (to avoid running the interactive code)
from calculator import Calc


class TestCalculator(unittest.TestCase):
    """Test cases for the Calc class."""

    def test_addition(self):
        """Test addition operation."""
        result = Calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        """Test addition with negative numbers."""
        result = Calc.add(-5, 3)
        self.assertEqual(result, -2)

    def test_subtraction(self):
        """Test subtraction operation."""
        result = Calc.sub(10, 4)
        self.assertEqual(result, 6)

    def test_subtraction_negative_result(self):
        """Test subtraction resulting in negative number."""
        result = Calc.sub(3, 7)
        self.assertEqual(result, -4)

    def test_multiplication(self):
        """Test multiplication operation."""
        result = Calc.mul(4, 5)
        self.assertEqual(result, 20)

    def test_multiplication_by_zero(self):
        """Test multiplication by zero."""
        result = Calc.mul(5, 0)
        self.assertEqual(result, 0)

    def test_division(self):
        """Test division operation."""
        result = Calc.div(10, 2)
        self.assertEqual(result, 5)

    def test_division_float_result(self):
        """Test division with float result."""
        result = Calc.div(7, 2)
        self.assertEqual(result, 3.5)

    def test_division_by_zero(self):
        """Test division by zero raises appropriate error."""
        with self.assertRaises(ZeroDivisionError):
            Calc.div(10, 0)


if __name__ == '__main__':
    unittest.main()
