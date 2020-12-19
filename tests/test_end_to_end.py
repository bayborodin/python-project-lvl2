from gendiff import generate_diff


def test_diff_and_format_json():
    result = generate_diff(
        'tests/fixtures/input_json/flat_data1.json',
        'tests/fixtures/input_json/flat_data2.json'
    )

    with open("tests/fixtures/expected/format_stylish.txt") as file_descriptor:
        expected = file_descriptor.read()

    assert(result == expected)


def test_diff_and_format_json_nested():
    result = generate_diff(
        'tests/fixtures/input_json/nested_data1.json',
        'tests/fixtures/input_json/nested_data2.json'
    )

    with open(
        "tests/fixtures/expected/format_stylish_nested.txt"
    ) as file_descriptor:
        expected = file_descriptor.read()

    assert(result == expected)


def test_diff_and_format_yaml():
    result = generate_diff(
        'tests/fixtures/input_yaml/flat_data1.yml',
        'tests/fixtures/input_yaml/flat_data2.yml'
    )

    with open("tests/fixtures/expected/format_stylish.txt") as file_descriptor:
        expected = file_descriptor.read()

    assert(result == expected)


def test_diff_and_format_yaml_stylish():
    result = generate_diff(
        'tests/fixtures/input_yaml/nested_data1.yml',
        'tests/fixtures/input_yaml/nested_data2.yml'
    )

    with open(
        "tests/fixtures/expected/format_stylish_nested.txt"
    ) as file_descriptor:
        expected = file_descriptor.read()

    assert(result == expected)
