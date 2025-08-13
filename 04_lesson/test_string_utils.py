import pytest
from string_utils import StringUtils

utils = StringUtils()

# capitalize
def test_capitalize_positive():
    assert utils.capitalize("sky") == "Sky"

def test_capitalize_empty():
    assert utils.capitalize("") == ""

# trim
def test_trim_positive():
    assert utils.trim("   hello   ") == "hello"

def test_trim_empty():
    assert utils.trim("") == ""

# to_list
def test_to_list_positive():
    assert utils.to_list("a,b,c", ",") == ["a", "b", "c"]

def test_to_list_empty():
    assert utils.to_list("", ",") == []

# contains
def test_contains_positive():
    assert utils.contains("hello", "ell") is True

def test_contains_negative():
    assert utils.contains("hello", "xyz") is False

# delete_symbol
def test_delete_symbol_positive():
    assert utils.delete_symbol("hello", "l") == "heo"

def test_delete_symbol_no_symbol():
    assert utils.delete_symbol("hello", "z") == "hello"

# starts_with
def test_starts_with_positive():
    assert utils.starts_with("hello", "he") is True

def test_starts_with_negative():
    assert utils.starts_with("hello", "lo") is False

# end_with
def test_end_with_positive():
    assert utils.end_with("hello", "lo") is True

def test_end_with_negative():
    assert utils.end_with("hello", "he") is False

# is_empty
def test_is_empty_true():
    assert utils.is_empty("") is True

def test_is_empty_false():
    assert utils.is_empty("text") is False

# list_to_string
def test_list_to_string_positive():
    assert utils.list_to_string(["a", "b", "c"], ",") == "a,b,c"

def test_list_to_string_empty():
    assert utils.list_to_string([], ",") == ""

