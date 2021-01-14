import json
import pytest
import subprocess

json_ref_file = 'tests/fixtures/json_reference_output.txt'
plain_ref_file = 'tests/fixtures/plain_reference_output.txt'
stylish_ref_file = 'tests/fixtures/stylish_reference_output.txt'


def read_data(file_name):
    with open(file_name, 'r') as f:
        result = f.read()
    return '{0}\n'.format(result)


def exec_app(file_path1, file_path2, format=None):
    args = ['poetry', 'run', 'gendiff']
    if format is not None:
        args.extend(['-f', format])
    args.extend([file_path1, file_path2])
    return subprocess.check_output(args, universal_newlines=True)


@pytest.mark.parametrize('file_format', ['json', 'yml'])
def test_console(file_format):
    file1 = 'tests/fixtures/file1.{0}'.format(file_format)
    file2 = 'tests/fixtures/file2.{0}'.format(file_format)

    assert exec_app(file1, file2) == read_data(stylish_ref_file)
    assert exec_app(file1, file2, 'stylish') == read_data(stylish_ref_file)
    assert exec_app(file1, file2, 'plain') == read_data(plain_ref_file)
    data = exec_app(file1, file2, 'json')
    assert isinstance(json.loads(data), dict)
