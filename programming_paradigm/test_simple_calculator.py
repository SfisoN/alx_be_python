import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-5, 5), 0)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-3, 5), -8)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 7), -7)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(50, 0), 0)

    # --- Division Tests ---
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))  # also None

if __name__ == "__main__":
    unittest.main()
