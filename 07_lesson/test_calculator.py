import pytest

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError("Unsupported operation")

def test_calculator():
    assert calculator(2, 3, "+") == 5
    assert calculator(5, 2, "-") == 3
    assert calculator(3, 4, "*") == 12
    assert calculator(10, 2, "/") == 5
