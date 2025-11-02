"""
34_unit_testing.py

This file demonstrates unit testing in Python.
Testing ensures code works correctly and helps prevent regressions.
Python provides unittest module and pytest is a popular third-party framework.
"""

import unittest

# BASIC UNIT TEST
# Create test cases by inheriting from unittest.TestCase

class Calculator:
    """Simple calculator for testing."""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures (runs before each test)."""
        self.calc = Calculator()
    
    def tearDown(self):
        """Clean up after tests (runs after each test)."""
        pass
    
    def test_add(self):
        """Test addition."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

# ASSERT METHODS
# Various assertion methods available

class TestAssertions(unittest.TestCase):
    """Examples of different assertion methods."""
    
    def test_equality(self):
        """Test equality assertions."""
        self.assertEqual(5, 5)
        self.assertNotEqual(5, 3)
    
    def test_comparison(self):
        """Test comparison assertions."""
        self.assertGreater(10, 5)
        self.assertLess(3, 7)
        self.assertGreaterEqual(5, 5)
        self.assertLessEqual(4, 4)
    
    def test_membership(self):
        """Test membership assertions."""
        self.assertIn(3, [1, 2, 3, 4])
        self.assertNotIn(5, [1, 2, 3, 4])
        self.assertIn("key", {"key": "value"})
    
    def test_type_checking(self):
        """Test type assertions."""
        self.assertIsInstance(5, int)
        self.assertIsInstance("hello", str)
        self.assertIsInstance([1, 2], list)
    
    def test_truthiness(self):
        """Test truthiness assertions."""
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertTrue(1)
        self.assertFalse(0)
    
    def test_none(self):
        """Test None assertions."""
        value = None
        self.assertIsNone(value)
        self.assertIsNotNone(42)
    
    def test_exceptions(self):
        """Test exception assertions."""
        # Test that exception is raised
        with self.assertRaises(ValueError):
            int("not a number")
        
        # Test exception with message
        with self.assertRaises(ValueError) as context:
            int("invalid")
        
        # Test exception type
        with self.assertRaises(TypeError):
            "string" + 5

# TEST DISCOVERY
# unittest can automatically discover tests

def run_tests():
    """Run all tests."""
    # Run tests in this file
    unittest.main(verbosity=2, exit=False)

# SETUP AND TEARDOWN METHODS
# Class-level and module-level setup

class TestWithSetup(unittest.TestCase):
    """Tests with setup and teardown."""
    
    @classmethod
    def setUpClass(cls):
        """Run once before all tests in class."""
        print("Setting up test class")
        cls.shared_resource = "shared data"
    
    @classmethod
    def tearDownClass(cls):
        """Run once after all tests in class."""
        print("Tearing down test class")
    
    def setUp(self):
        """Run before each test method."""
        self.data = [1, 2, 3]
    
    def tearDown(self):
        """Run after each test method."""
        self.data = None
    
    def test_with_setup(self):
        """Test using setup data."""
        self.assertIn(2, self.data)
        self.assertEqual(self.shared_resource, "shared data")

# SKIP TESTS
# Conditionally skip tests

class TestSkip(unittest.TestCase):
    """Examples of skipping tests."""
    
    @unittest.skip("Skipping this test")
    def test_skipped(self):
        """This test will be skipped."""
        self.fail("Should not run")
    
    @unittest.skipIf(True, "Condition is True")
    def test_skip_if(self):
        """Skip if condition is True."""
        self.fail("Should not run")
    
    @unittest.skipUnless(False, "Condition is False")
    def test_skip_unless(self):
        """Skip unless condition is True."""
        self.fail("Should not run")
    
    def test_not_skipped(self):
        """This test will run."""
        self.assertTrue(True)

# EXPECTED FAILURES
# Mark tests that are expected to fail

class TestExpectedFailures(unittest.TestCase):
    """Tests with expected failures."""
    
    @unittest.expectedFailure
    def test_buggy_feature(self):
        """This test is expected to fail."""
        # Known bug, test will pass even if it fails
        self.assertTrue(False)

# TEST SUITES
# Organize tests into suites

def create_test_suite():
    """Create a test suite."""
    suite = unittest.TestSuite()
    
    # Add specific tests
    suite.addTest(TestCalculator('test_add'))
    suite.addTest(TestCalculator('test_multiply'))
    
    # Add all tests from a class
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCalculator))
    
    return suite

# PARAMETRIZED TESTS (using unittest)
# Test same function with different inputs

class TestParametrized(unittest.TestCase):
    """Parametrized tests using subtests."""
    
    def test_multiple_values(self):
        """Test function with multiple values."""
        test_cases = [
            (1, 1, 2),
            (2, 3, 5),
            (0, 0, 0),
            (-1, 1, 0),
        ]
        
        calc = Calculator()
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(calc.add(a, b), expected)

# MOCKING WITH UNITTEST.MOCK
# Mock external dependencies

from unittest.mock import Mock, MagicMock, patch

class TestWithMocks(unittest.TestCase):
    """Tests using mocks."""
    
    def test_mock_object(self):
        """Test with mock object."""
        # Create a mock
        mock_obj = Mock()
        mock_obj.method.return_value = 42
        
        # Use mock
        result = mock_obj.method()
        self.assertEqual(result, 42)
        
        # Verify it was called
        mock_obj.method.assert_called_once()
    
    def test_mock_patch(self):
        """Test using patch decorator."""
        # Mock built-in function
        with patch('builtins.len', return_value=10):
            self.assertEqual(len([1, 2, 3]), 10)

# RUNNING TESTS
# Run tests from command line or programmatically

if __name__ == '__main__':
    # Run all tests in this file
    print("Running unit tests...\n")
    
    # Verbose output
    unittest.main(verbosity=2)
    
    # Or run specific test suite
    # runner = unittest.TextTestRunner(verbosity=2)
    # suite = create_test_suite()
    # runner.run(suite)

print("\nUnit testing demonstration complete!")
print("\nTo run these tests:")
print("  python -m unittest 34_unit_testing.py")
print("  python 34_unit_testing.py")

