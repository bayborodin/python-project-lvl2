import json

from gendiff.gendiff import generate_diff

json_file1 = 'tests/fixtures/file1.json'
json_file2 = 'tests/fixtures/file2.json'
yaml_file1 = 'tests/fixtures/file1.yml'
yaml_file2 = 'tests/fixtures/file2.yml'

json_ref_file = 'tests/fixtures/json_reference_output.txt'
plain_ref_file = 'tests/fixtures/plain_reference_output.txt'
stylish_ref_file = 'tests/fixtures/stylish_reference_output.txt'


def read_data(file_name):
    with open(file_name, 'r') as f:
        result = f.read()
    return result


def test_json_gen_diff():
    assert generate_diff(json_file1, json_file2) == read_data(stylish_ref_file)
    assert generate_diff(json_file1, json_file2,
                         'stylish') == read_data(stylish_ref_file)
    assert generate_diff(json_file1, json_file2,
                         'plain') == read_data(plain_ref_file)

    data = generate_diff(json_file1, json_file2, 'json')
    assert isinstance(json.loads(data), dict)


def test_yaml_gen_diff():
    assert generate_diff(yaml_file1, yaml_file2) == read_data(stylish_ref_file)
    assert generate_diff(yaml_file1, yaml_file2,
                         'stylish') == read_data(stylish_ref_file)
    assert generate_diff(yaml_file1, yaml_file2,
                         'plain') == read_data(plain_ref_file)

    json_output = generate_diff(yaml_file1, yaml_file2, 'json')
    assert isinstance(json.loads(json_output), dict)
