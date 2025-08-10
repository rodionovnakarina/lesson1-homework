import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitilize_positive():
    assert utils.capitilize("sky") == "Sky"

def test_capitilize_negative():
    assert utils.capitilize("") == ""

