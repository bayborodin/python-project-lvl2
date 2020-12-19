from gendiff.formatters.stylish import format_diff
from gendiff.reader import read_data


def test_stylish_formatter():
    data = read_data("tests/fixtures/expected/compare_flat.json")["diff"]
    result = format_diff(data)

    with open("tests/fixtures/expected/format_stylish.txt") as file_descriptor:
        expected = file_descriptor.read()

    assert(result == expected)


def test_stylish_nested_formatter():
    data = read_data("tests/fixtures/expected/compare_nested.json")["diff"]
    result = format_diff(data)

    with open("tests/fixtures/expected/format_stylish_nested.txt") as file_descriptor:
        expected = file_descriptor.read()

    assert(result == expected)
