import unittest
from main import calculate_pi_to_5_digits


class TestPiCalculation(unittest.TestCase):
    """Test cases for pi calculation function"""
    
    def test_pi_to_5_digits(self):
        """Test that pi is calculated correctly to 5 digits"""
        pi_value = calculate_pi_to_5_digits()
        # Pi ≈ 3.14159...
        expected_pi = 3.14159
        
        # Check that the value is close to the expected value (within 0.00001)
        self.assertAlmostEqual(pi_value, expected_pi, places=5)
    
    def test_pi_is_positive(self):
        """Test that pi value is positive"""
        pi_value = calculate_pi_to_5_digits()
        self.assertGreater(pi_value, 0)
    
    def test_pi_is_reasonable(self):
        """Test that pi is within reasonable bounds"""
        pi_value = calculate_pi_to_5_digits()
        # Pi should be between 3 and 4
        self.assertGreater(pi_value, 3)
        self.assertLess(pi_value, 4)
    
    def test_pi_first_5_digits(self):
        """Test the first 5 digits of pi"""
        pi_value = calculate_pi_to_5_digits()
        # Round to 5 decimal places and check
        pi_rounded = round(pi_value, 5)
        # Pi to 5 digits after decimal: 3.14159
        self.assertEqual(pi_rounded, 3.14159)
    
    def test_multiple_calls_consistency(self):
        """Test that multiple calls return the same value"""
        pi_value_1 = calculate_pi_to_5_digits()
        pi_value_2 = calculate_pi_to_5_digits()
        self.assertEqual(pi_value_1, pi_value_2)


if __name__ == "__main__":
    unittest.main()
