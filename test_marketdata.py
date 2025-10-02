# test_marketdata.py
"""
Tests for MarketData module.
"""

import unittest
from marketdata import MarketData

class TestMarketData(unittest.TestCase):
    """Test cases for MarketData class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MarketData()
        self.assertIsInstance(instance, MarketData)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MarketData()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
