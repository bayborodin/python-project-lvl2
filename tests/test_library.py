import json
import pytest

from gendiff.gendiff import generate_diff

json_ref_file = 'tests/fixtures/json_reference_output.txt'
plain_ref_file = 'tests/fixtures/plain_reference_output.txt'
stylish_ref_file = 'tests/fixtures/stylish_reference_output.txt'


def read_data(file_name):
    with open(file_name, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize('file_format', ['json', 'yml'])
def test_gen_diff(file_format):
    file1 = 'tests/fixtures/file1.{0}'.format(file_format)
    file2 = 'tests/fixtures/file2.{0}'.format(file_format)

    assert generate_diff(file1, file2) == read_data(stylish_ref_file)
    assert generate_diff(file1, file2, 'stylish') == read_data(stylish_ref_file)
    assert generate_diff(file1, file2, 'plain') == read_data(plain_ref_file)

    data = generate_diff(file1, file2, 'json')
    assert isinstance(json.loads(data), dict)
