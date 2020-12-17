from gendiff.reader import read_data
from gendiff.comparator import compare


def test_diff_json():
    data1 = read_data("tests/fixtures/input_json/flat_data1.json")
    data2 = read_data("tests/fixtures/input_json/flat_data2.json")
    expected = read_data("tests/fixtures/expected/compare_flat.json")["diff"]
    result = compare(data1, data2)
    assert(result == expected)


def test_diff_json_reversed():
    data1 = read_data("tests/fixtures/input_json/flat_data1.json")
    data2 = read_data("tests/fixtures/input_json/flat_data2.json")
    expected = read_data(
        "tests/fixtures/expected/compare_flat_reversed.json")["diff"]
    result = compare(data2, data1)
    assert(result == expected)


def test_diff_yaml():
    data1 = read_data("tests/fixtures/input_yaml/flat_data1.yml")
    data2 = read_data("tests/fixtures/input_yaml/flat_data2.yml")
    expected = read_data("tests/fixtures/expected/compare_flat.json")["diff"]
    result = compare(data1, data2)
    assert(result == expected)


def test_diff_yaml_reversed():
    data1 = read_data("tests/fixtures/input_yaml/flat_data1.yml")
    data2 = read_data("tests/fixtures/input_yaml/flat_data2.yml")
    expected = read_data(
        "tests/fixtures/expected/compare_flat_reversed.json")["diff"]
    result = compare(data2, data1)
    assert(result == expected)
