"""
35_testing_advanced.py

This file demonstrates advanced testing techniques in Python.
Covers pytest (popular testing framework), mocking, fixtures, parametrization,
and test coverage.
"""

# PYTEST BASICS
# pytest is more pythonic and feature-rich than unittest

# Basic test function (no class needed)
def test_basic():
    """Basic pytest test."""
    assert 1 + 1 == 2
    assert "hello".upper() == "HELLO"

# PYTEST FIXTURES
# Reusable test setup code

import pytest

@pytest.fixture
def sample_data():
    """Fixture that provides sample data."""
    return {"name": "Alice", "age": 30}

def test_with_fixture(sample_data):
    """Test using fixture."""
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30

# FIXTURE WITH SETUP AND TEARDOWN
# Fixtures can have setup and cleanup

@pytest.fixture
def database_connection():
    """Fixture with setup and teardown."""
    # Setup
    print("Setting up database connection")
    conn = {"connected": True, "data": []}
    
    yield conn  # Provide connection
    
    # Teardown
    print("Closing database connection")
    conn["connected"] = False

def test_database(database_connection):
    """Test using database fixture."""
    assert database_connection["connected"] is True
    database_connection["data"].append("test")

# PARAMETRIZED TESTS
# Run same test with different inputs

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(a, b, expected):
    """Parametrized test for addition."""
    assert a + b == expected

# MULTIPLE PARAMETRIZATIONS
# Combine parameters

@pytest.mark.parametrize("operation", ["add", "subtract"])
@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),  # For subtract
    (2, 3, 5),  # For add
])
def test_operations(operation, a, b, expected):
    """Test multiple operations."""
    if operation == "add":
        assert a + b == expected
    elif operation == "subtract":
        assert a - b == expected

# MOCKING WITH PYTEST
# Mock external dependencies

from unittest.mock import Mock, MagicMock, patch, Mock, call

def test_with_mock():
    """Test using mock."""
    # Create mock
    mock_service = Mock()
    mock_service.get_data.return_value = {"result": "success"}
    
    # Use mock
    result = mock_service.get_data()
    assert result["result"] == "success"
    
    # Verify calls
    mock_service.get_data.assert_called_once()

# PATCHING WITH PYTEST
# Replace objects during testing

def fetch_data(url):
    """Function that fetches data."""
    # In real code, this would make HTTP request
    import requests
    return requests.get(url).json()

@patch('requests.get')
def test_fetch_data(mock_get):
    """Test fetch_data with mocked requests."""
    # Configure mock response
    mock_response = Mock()
    mock_response.json.return_value = {"data": "test"}
    mock_get.return_value = mock_response
    
    # Test function
    result = fetch_data("http://example.com/api")
    
    # Verify
    assert result == {"data": "test"}
    mock_get.assert_called_once_with("http://example.com/api")

# MONKEYPATCH
# Pytest's way to patch objects

def test_with_monkeypatch(monkeypatch):
    """Test using monkeypatch."""
    # Patch a function
    def mock_get():
        return {"mocked": "data"}
    
    monkeypatch.setattr("builtins.print", lambda x: None)  # Suppress print
    
    # Test code here
    assert True

# TESTING EXCEPTIONS
# Test that functions raise exceptions

def divide(a, b):
    """Divide function that raises error."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# TESTING WITH FIXTURES AND MARKS
# Organize tests with markers

@pytest.mark.slow
def test_slow_operation():
    """Slow test marked with @pytest.mark.slow."""
    import time
    time.sleep(0.1)  # Simulate slow operation
    assert True

@pytest.mark.unit
def test_unit():
    """Unit test."""
    assert 1 + 1 == 2

@pytest.mark.integration
def test_integration():
    """Integration test."""
    assert True

# CONFTEST.PY PATTERN
# Shared fixtures across test files
# (Create conftest.py file with shared fixtures)

# Example conftest.py content:
"""
import pytest

@pytest.fixture
def shared_fixture():
    return {"shared": "data"}
"""

# TEST COVERAGE
# Measure what code is tested

# Install: pip install pytest-cov
# Run: pytest --cov=module_name --cov-report=html

def uncovered_function():
    """Function not covered by tests."""
    return "not tested"

# MOCK OBJECTS - ADVANCED
# More complex mocking scenarios

class APIClient:
    """API client for testing."""
    
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, endpoint):
        """GET request."""
        # Would make actual HTTP request
        pass

def test_api_client():
    """Test API client with mocks."""
    client = APIClient("http://api.example.com")
    
    # Mock the get method
    client.get = Mock(return_value={"status": "ok"})
    
    result = client.get("/users")
    assert result == {"status": "ok"}

# SPY PATTERN
# Monitor real object calls without replacing

def test_spy_pattern():
    """Test using spy pattern."""
    from unittest.mock import MagicMock
    
    # Create spy that wraps real function
    real_list = []
    spy_append = MagicMock(wraps=real_list.append)
    
    spy_append("item")
    assert real_list == ["item"]
    spy_append.assert_called_once_with("item")

# TEST DOUBLES
# Different types of test doubles

def test_doubles():
    """Different test double patterns."""
    # Dummy - not used, just to satisfy interface
    dummy = None
    
    # Stub - returns predefined values
    stub = Mock(return_value="stub_value")
    
    # Mock - records interactions
    mock_obj = Mock()
    mock_obj.method()
    mock_obj.method.assert_called_once()
    
    # Spy - wraps real object
    from unittest.mock import MagicMock
    real_obj = {"key": "value"}
    spy = MagicMock(wraps=real_obj)
    spy.get("key")
    
    # Fake - simplified implementation
    class FakeDatabase:
        def __init__(self):
            self.data = {}
        
        def get(self, key):
            return self.data.get(key)
    
    fake_db = FakeDatabase()
    assert fake_db.get("missing") is None

# TESTING ASYNC CODE
# Test asynchronous functions

import asyncio

async def async_function():
    """Async function to test."""
    await asyncio.sleep(0.01)
    return "result"

@pytest.mark.asyncio
async def test_async_function():
    """Test async function."""
    result = await async_function()
    assert result == "result"

# FIXTURE DEPENDENCIES
# Fixtures can depend on other fixtures

@pytest.fixture
def base_data():
    """Base fixture."""
    return {"base": "data"}

@pytest.fixture
def extended_data(base_data):
    """Fixture depending on base_data."""
    extended = base_data.copy()
    extended["extended"] = True
    return extended

def test_extended_data(extended_data):
    """Test with fixture dependency."""
    assert extended_data["base"] == "data"
    assert extended_data["extended"] is True

# TESTING WITH TEMPORARY FILES
# Create temporary files for testing

import tempfile
import os

def test_with_temp_file(tmp_path):
    """Test using temporary file."""
    # tmp_path is a pytest fixture
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    
    assert file_path.read_text() == "test content"

# MOCKING CLASS INSTANCES
# Mock entire classes

@patch('builtins.open', create=True)
def test_file_operations(mock_open):
    """Test file operations with mocked open."""
    mock_file = MagicMock()
    mock_file.read.return_value = "file content"
    mock_open.return_value.__enter__.return_value = mock_file
    
    with open("test.txt") as f:
        content = f.read()
    
    assert content == "file content"

print("Advanced testing demonstration complete!")
print("\nNote: To run pytest tests:")
print("  pip install pytest pytest-asyncio pytest-cov")
print("  pytest 35_testing_advanced.py -v")
print("  pytest --cov=module_name --cov-report=html")

