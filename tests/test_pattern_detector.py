"""
Unit tests for the pattern detector module
"""

import unittest
import pandas as pd
from nfscan.pattern_detector import PatternDetector


class TestPatternDetector(unittest.TestCase):
    
    def setUp(self):
        """Set up test data"""
        self.data = pd.DataFrame({
            'Open': [100, 105, 102, 110, 108],
            'High': [110, 115, 112, 120, 118],
            'Low': [95, 100, 98, 105, 103],
            'Close': [108, 102, 110, 106, 115]
        })
        self.detector = PatternDetector(self.data)
    
    def test_detector_initialization(self):
        """Test detector initialization"""
        self.assertIsNotNone(self.detector.data)
        self.assertEqual(len(self.detector.data), 5)
    
    def test_detect_doji(self):
        """Test Doji detection"""
        result = self.detector.detect_doji()
        self.assertIsInstance(result, pd.Series)
        self.assertEqual(len(result), len(self.data))
    
    def test_detect_hammer(self):
        """Test Hammer detection"""
        result = self.detector.detect_hammer()
        self.assertIsInstance(result, pd.Series)
        self.assertEqual(len(result), len(self.data))
    
    def test_detect_all_patterns(self):
        """Test detection of all patterns"""
        patterns = self.detector.detect_all_patterns()
        self.assertIsInstance(patterns, dict)
        self.assertIn('Doji', patterns)
        self.assertIn('Hammer', patterns)
    
    def test_get_pattern_summary(self):
        """Test pattern summary generation"""
        self.detector.detect_all_patterns()
        summary = self.detector.get_pattern_summary()
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertIn('Pattern', summary.columns)
        self.assertIn('Count', summary.columns)


if __name__ == '__main__':
    unittest.main()
