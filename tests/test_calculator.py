"""Tests for the Calculator class."""

# pylint: disable=redefined-outer-name
import pytest

from calculator.calculator import Calculator


@pytest.fixture
def calc_fixture():
    """Create and return a Calculator instance for testing."""
    return Calculator()


def test_calculator_initialization(calc_fixture):
    """Test that calculator initializes with memory set to 0."""
    assert calc_fixture.memory_recall() == 0


def test_calculator_operations(calc_fixture):
    """Test the basic calculator operations."""
    assert calc_fixture.add(1, 2) == 3
    assert calc_fixture.subtract(5, 3) == 2
    assert calc_fixture.multiply(2, 4) == 8
    assert calc_fixture.divide(10, 2) == 5


def test_memory_store_and_recall(calc_fixture):
    """Test the memory store and recall functions."""
    calc_fixture.memory_store(5)
    assert calc_fixture.memory_recall() == 5


def test_memory_clear(calc_fixture):
    """Test the memory clear function."""
    calc_fixture.memory_store(5)
    calc_fixture.memory_clear()
    assert calc_fixture.memory_recall() == 0
