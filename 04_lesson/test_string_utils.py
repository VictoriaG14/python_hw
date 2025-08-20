import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.pos
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.neg
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.pos
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("Student", "Student"),
    (" August", "August"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.neg
@pytest.mark.parametrize("input_str, expected", [
    ("55sample", "55sample"),
    ("skypro  ", "skypro  "),
    ("cola zero", "cola zero"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.pos
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("morning", "o", True),
    ("Bye", "B", True),
    ("", "", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains("Skypro", "S") is True


@pytest.mark.neg
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("12345", "1", False),
    ("Morning", "m", False),
    ("evening", "a", False),
])
def test_contains_neg(input_str, symbol, expected):
    assert string_utils.contains("hello", "H") is False


@pytest.mark.pos
@pytest.mark.parametrize("input_str, symbol, new_result", [
    ("Moscow", "w", "Mosco"),
    ("good evening", "d", "goo evening"),
    ("87654", "6", "8754"),
])
def test_delete_symbol_pos(input_str, symbol, new_result):
    utils = StringUtils()
    result = utils.delete_symbol(input_str, symbol)
    assert result == new_result


@pytest.mark.neg
@pytest.mark.parametrize("input_str, symbol, new_result", [
    ("", "a", ""),
    ("fix", "k", "fix"),
    ("None", "", "None")
])
def test_delete_symbol_negative(input_str, symbol, new_result):
    utils = StringUtils()
    result = utils.delete_symbol(input_str, symbol)
    assert result == new_result
