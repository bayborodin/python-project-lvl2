import pytest

from gendiff.formatters.formatter import format_diff
from gendiff.reader import read_data


def test_stylish_formatter():
    data = read_data("tests/fixtures/expected/compare_flat.json")["diff"]
    result = format_diff(data)

    with open("tests/fixtures/expected/format_stylish.txt") as f:
        expected = f.read()

    assert(result == expected)


def test_stylish_nested_formatter():
    data = read_data("tests/fixtures/expected/compare_nested.json")["diff"]
    result = format_diff(data)

    with open("tests/fixtures/expected/format_stylish_nested.txt") as f:
        expected = f.read()

    assert(result == expected)


def test_plain_formatter():
    data = read_data("tests/fixtures/expected/compare_nested.json")["diff"]
    result = format_diff(data, 'plain')

    with open("tests/fixtures/expected/format_plain_nested.txt") as f:
        expected = f.read()

    assert(result == expected)


def test_json_formatter():
    data = read_data("tests/fixtures/expected/compare_nested.json")["diff"]
    result = format_diff(data, 'json')

    with open("tests/fixtures/expected/format_json_output.txt") as f:
        expected = f.read()

    assert(result == expected)


def test_unsupported_output_format():
    data = read_data("tests/fixtures/expected/compare_nested.json")["diff"]
    with pytest.raises(ValueError):
        format_diff(data, 'unknown')
