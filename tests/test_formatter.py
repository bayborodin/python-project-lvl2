from gendiff.formatter import stylish
from gendiff.reader import read_data


def test_stylish_formatter():
    data = read_data("tests/fixtures/expected/compare_flat.json")["diff"]
    result = stylish(data)

    with open("tests/fixtures/expected/format_stylish.txt") as file_descriptor:
        expected = file_descriptor.read()

    assert(result == expected)
