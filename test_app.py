"""
Simple unit tests to demonstrate testing in GitHub Actions.

These tests use pytest, a popular Python testing framework.
To run locally: pip install pytest && pytest test_app.py -v
"""

import pytest
import requests


def test_addition():
    """Test basic arithmetic - should always pass"""
    assert 2 + 2 == 4
    assert 10 + 5 == 15


def test_string_operations():
    """Test string operations"""
    text = "GitHub Actions"
    assert text.lower() == "github actions"
    assert len(text) == 14
    assert "Actions" in text


def test_list_operations():
    """Test list operations"""
    numbers = [1, 2, 3, 4, 5]
    assert sum(numbers) == 15
    assert max(numbers) == 5
    assert min(numbers) == 1


def test_requests_library():
    """Test that the requests library is installed and working"""
    # Just check that we can import and access the version
    assert hasattr(requests, '__version__')
    assert isinstance(requests.__version__, str)


def test_sum_of_range():
    """Test the same calculation we use in app.py"""
    result = sum(range(1, 101))
    expected = 5050
    assert result == expected, f"Expected {expected}, got {result}"


# This test is marked to expect failure - demonstrates pytest features
@pytest.mark.xfail(reason="This test is designed to show how pytest handles expected failures")
def test_intentional_failure():
    """This test is expected to fail - just for demonstration"""
    assert False, "This is an intentional failure for demonstration"


if __name__ == "__main__":
    # Allow running this file directly
    pytest.main([__file__, "-v"])
