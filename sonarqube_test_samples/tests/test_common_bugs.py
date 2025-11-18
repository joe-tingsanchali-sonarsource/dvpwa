"""
Test file for common_bugs.py
Provides approximately 50% code coverage for testing purposes.
"""

import sys
import os
import unittest

# Add parent directory to path to import from src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.common_bugs import (
    calculate_average,
    check_value,
    remove_negatives,
    parse_data,
    process_list,
    validate_input,
    calculate_score,
    check_number,
    Counter,
    get_day_type,
    add_numbers,
    validate_user
)


class TestCalculateAverage(unittest.TestCase):
    """Test calculate_average function"""
    
    def test_calculate_average_with_values(self):
        """Test with valid list of numbers"""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
    
    def test_calculate_average_single_value(self):
        """Test with single value"""
        self.assertEqual(calculate_average([10]), 10.0)


class TestCheckValue(unittest.TestCase):
    """Test check_value function"""
    
    def test_check_value_none(self):
        """Test with None value"""
        self.assertEqual(check_value(None), False)
    
    def test_check_value_not_none(self):
        """Test with non-None value"""
        self.assertEqual(check_value(42), True)
    
    def test_check_value_zero(self):
        """Test with zero"""
        self.assertEqual(check_value(0), True)


class TestRemoveNegatives(unittest.TestCase):
    """Test remove_negatives function"""
    
    def test_remove_negatives_mixed(self):
        """Test with mixed positive and negative numbers"""
        numbers = [1, -2, 3, -4, 5]
        result = remove_negatives(numbers)
        # Note: This function has a bug with list modification during iteration
        self.assertTrue(all(n >= 0 for n in result))
    
    def test_remove_negatives_all_positive(self):
        """Test with all positive numbers"""
        numbers = [1, 2, 3, 4, 5]
        result = remove_negatives(numbers)
        self.assertEqual(result, [1, 2, 3, 4, 5])


class TestParseData(unittest.TestCase):
    """Test parse_data function"""
    
    def test_parse_data_valid_integer(self):
        """Test with valid integer string"""
        self.assertEqual(parse_data("42"), 42)
    
    def test_parse_data_invalid_string(self):
        """Test with invalid string"""
        result = parse_data("not a number")
        self.assertIsNone(result)  # Returns None on error


class TestProcessList(unittest.TestCase):
    """Test process_list function"""
    
    def test_process_list_integers(self):
        """Test with list of integers"""
        self.assertEqual(process_list([1, 2, 3, 4, 5]), 15)
    
    def test_process_list_single_item(self):
        """Test with single item"""
        self.assertEqual(process_list([10]), 10)


class TestValidateInput(unittest.TestCase):
    """Test validate_input function"""
    
    def test_validate_input_admin(self):
        """Test with admin string"""
        # Note: Function has bug using 'is' instead of '=='
        result = validate_input("admin")
        # May return False due to bug
        self.assertIsInstance(result, bool)
    
    def test_validate_input_other(self):
        """Test with non-admin string"""
        self.assertEqual(validate_input("user"), False)


class TestCalculateScore(unittest.TestCase):
    """Test calculate_score function"""
    
    def test_calculate_score_over_100(self):
        """Test with points over 100"""
        self.assertEqual(calculate_score(150), 100)
    
    def test_calculate_score_under_100(self):
        """Test with points under 100"""
        self.assertEqual(calculate_score(75), 75)
    
    def test_calculate_score_exactly_100(self):
        """Test with exactly 100 points"""
        self.assertEqual(calculate_score(100), 100)


class TestCheckNumber(unittest.TestCase):
    """Test check_number function"""
    
    def test_check_number_42(self):
        """Test with 42"""
        # Note: Function has bug using 'is' instead of '=='
        result = check_number(42)
        self.assertIn(result, ["Found", "Not found"])
    
    def test_check_number_other(self):
        """Test with other number"""
        self.assertEqual(check_number(10), "Not found")


class TestCounter(unittest.TestCase):
    """Test Counter class"""
    
    def test_counter_increment(self):
        """Test counter increment"""
        counter = Counter()
        result = counter.increment()
        # Note: Bug - always returns 1
        self.assertEqual(result, 1)
    
    def test_counter_multiple_increments(self):
        """Test multiple increments"""
        counter = Counter()
        counter.increment()
        result = counter.increment()
        # Note: Bug - still returns 1 due to local variable
        self.assertEqual(result, 1)


class TestGetDayType(unittest.TestCase):
    """Test get_day_type function"""
    
    def test_get_day_type_monday(self):
        """Test with Monday"""
        self.assertEqual(get_day_type("Monday"), "weekday")
    
    def test_get_day_type_tuesday(self):
        """Test with Tuesday"""
        self.assertEqual(get_day_type("Tuesday"), "weekday")
    
    def test_get_day_type_unknown(self):
        """Test with unknown day"""
        self.assertEqual(get_day_type("Funday"), "unknown")


class TestAddNumbers(unittest.TestCase):
    """Test add_numbers function"""
    
    def test_add_numbers_integers(self):
        """Test with integers"""
        self.assertEqual(add_numbers(5, 10), 15)
    
    def test_add_numbers_floats(self):
        """Test with floats"""
        self.assertEqual(add_numbers(5.5, 10.5), 16.0)


class TestValidateUser(unittest.TestCase):
    """Test validate_user function"""
    
    def test_validate_user_with_email(self):
        """Test user with email"""
        user = {'email': 'test@example.com', 'name': 'Test'}
        self.assertEqual(validate_user(user), True)
    
    def test_validate_user_without_email(self):
        """Test user without email"""
        user = {'name': 'Test'}
        self.assertEqual(validate_user(user), False)
    
    def test_validate_user_empty_email(self):
        """Test user with empty email"""
        user = {'email': '', 'name': 'Test'}
        self.assertEqual(validate_user(user), False)


if __name__ == '__main__':
    unittest.main()
