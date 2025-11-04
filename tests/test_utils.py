"""
Unit tests for the utils module
"""

import unittest
import pandas as pd
from nfscan.utils import (
    validate_dataframe, 
    calculate_body_size, 
    calculate_upper_shadow,
    calculate_lower_shadow,
    get_date_range,
    format_currency
)


class TestUtils(unittest.TestCase):
    
    def setUp(self):
        """Set up test data"""
        self.valid_df = pd.DataFrame({
            'Open': [100, 105],
            'High': [110, 115],
            'Low': [95, 100],
            'Close': [108, 102]
        })
        
        self.invalid_df = pd.DataFrame({
            'Open': [100, 105],
            'Close': [108, 102]
        })
    
    def test_validate_dataframe_valid(self):
        """Test validation with valid dataframe"""
        self.assertTrue(validate_dataframe(self.valid_df))
    
    def test_validate_dataframe_invalid(self):
        """Test validation with invalid dataframe"""
        self.assertFalse(validate_dataframe(self.invalid_df))
    
    def test_calculate_body_size(self):
        """Test body size calculation"""
        row = self.valid_df.iloc[0]
        body_size = calculate_body_size(row)
        self.assertEqual(body_size, 8)  # abs(108 - 100)
    
    def test_calculate_upper_shadow(self):
        """Test upper shadow calculation"""
        row = self.valid_df.iloc[0]
        upper_shadow = calculate_upper_shadow(row)
        self.assertEqual(upper_shadow, 2)  # 110 - max(100, 108)
    
    def test_calculate_lower_shadow(self):
        """Test lower shadow calculation"""
        row = self.valid_df.iloc[0]
        lower_shadow = calculate_lower_shadow(row)
        self.assertEqual(lower_shadow, 5)  # min(100, 108) - 95
    
    def test_format_currency(self):
        """Test currency formatting"""
        formatted = format_currency(1234.56)
        self.assertEqual(formatted, "₹1,234.56")


if __name__ == '__main__':
    unittest.main()
