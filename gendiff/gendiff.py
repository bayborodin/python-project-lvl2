"""Diff builder."""

from gendiff.comparator import compare
from gendiff.formatters.formatter import DEFAULT_FORMAT, format_diff
from gendiff.reader import read_data


def generate_diff(file_path1: str, file_path2: str, fmt=DEFAULT_FORMAT) -> str:
    """
    Generate a diff for a given files.

    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.
        fmt: Diff output format.

    Returns:
        Diff of the given files.
    """
    data_collection1 = read_data(file_path1)
    data_collection2 = read_data(file_path2)
    diff = compare(data_collection1, data_collection2)

    return format_diff(diff, fmt)
