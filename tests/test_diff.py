import typing
from gendiff.gendiff import generate_diff
import os
import pytest
import json


def get_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def get_file_data(file_name):
    return read(get_path(file_name))


result_stylish = get_file_data('result_stylish')
result_plain = get_file_data('result_plain')
result_json = get_file_data('result_json')

test_cases = ['yml', 'json']


@pytest.mark.parametrize('format', test_cases)
def test_generate_diff(format):
    file_path1 = get_path('file1.{0}'.format(format))
    file_path2 = get_path('file2.{0}'.format(format))

    assert isinstance(
        generate_diff, typing.Callable), 'gendiff.generate_diff must be function'
    assert generate_diff(file_path1, file_path2) == result_stylish
    assert generate_diff(file_path1, file_path2, 'stylish') == result_stylish
    assert generate_diff(file_path1, file_path2, 'plain') == result_plain

    data = generate_diff(file_path1, file_path2, 'json')
    assert isinstance(json.loads(data), dict)
