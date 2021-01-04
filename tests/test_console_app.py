import json
import subprocess


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
    return '{0}\n'.format(result)


def exec_app(file_path1, file_path2, format=None):
    args = ['poetry', 'run', 'gendiff']
    if format is not None:
        args.extend(['-f', format])
    args.extend([file_path1, file_path2])
    return subprocess.check_output(args, universal_newlines=True)


def test_console_json():
    assert exec_app(json_file1, json_file2) == read_data(stylish_ref_file)
    assert exec_app(json_file1, json_file2,
                    'stylish') == read_data(stylish_ref_file)
    assert exec_app(json_file1, json_file2,
                    'plain') == read_data(plain_ref_file)
    data = exec_app(json_file1, json_file2, 'json')
    assert isinstance(json.loads(data), dict)


def test_console_yaml():
    assert exec_app(yaml_file1, yaml_file2) == read_data(stylish_ref_file)
    assert exec_app(yaml_file1, yaml_file2,
                    'stylish') == read_data(stylish_ref_file)
    assert exec_app(yaml_file1, yaml_file2,
                    'plain') == read_data(plain_ref_file)
    data = exec_app(yaml_file1, yaml_file2, 'json')
    assert isinstance(json.loads(data), dict)
