"""Additional tests to cover remaining functions and methods."""

from calculator import addition
from calculator import multiply as mul_alias
from calculator import subtraction
from calculator.calculator import Calculator


def test_module_level_functions():
    """Cover functions in src/calculator/__init__.py"""
    assert addition(2, 3) == 5
    assert subtraction(5, 2) == 3
    assert mul_alias(3, 4) == 12


def test_update_display_and_memory_arithmetic():
    calc = Calculator()
    # update display
    calc.update_display(123)
    assert hasattr(calc, "display") and calc.display == "123"

    # memory add/subtract
    calc.memory_store(10)
    calc.memory_add(5)
    assert calc.memory_recall() == 15
    calc.memory_subtract(3)
    assert calc.memory_recall() == 12


def test_scientific_methods_on_calculator():
    calc = Calculator()
    assert calc.square_root(16) == 4
    assert calc.power(2, 5) == 32
