import unittest
from discount_calculator import calculate_discount

class TestCalculateDiscount(unittest.TestCase):
    
    def test_discount_applied(self):
        # Test case where discount is 20% or higher
        self.assertEqual(calculate_discount(100, 20), 80.00)
        self.assertEqual(calculate_discount(50, 50), 25.00)
        self.assertEqual(calculate_discount(200, 30), 140.00)

    def test_no_discount_applied(self):
        # Test case where discount is less than 20%
        self.assertEqual(calculate_discount(100, 10), 100.00)
        self.assertEqual(calculate_discount(75, 5), 75.00)

    def test_invalid_discount_percentage(self):
        # Test invalid discount percentages
        with self.assertRaises(ValueError):
            calculate_discount(100, -5)  # Negative discount
        with self.assertRaises(ValueError):
            calculate_discount(100, 105)  # Discount over 100%

if __name__ == "__main__":
    unittest.main()
