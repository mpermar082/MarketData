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
        # Create an instance of MarketData and verify it's an instance of the class
        instance = MarketData()
        self.assertIsInstance(instance, MarketData)
        
    def test_run_method(self):
        """Test the run method."""
        # Create an instance of MarketData and verify the run method returns True
        instance = MarketData()
        self.assertTrue(instance.run())
        
    def test_run_method_failure(self):
        """Test the run method with a failure scenario."""
        # Create an instance of MarketData with a failure scenario (e.g. invalid input)
        # and verify the run method returns False
        instance = MarketData(failure=True)
        self.assertFalse(instance.run())

if __name__ == "__main__":
    unittest.main()