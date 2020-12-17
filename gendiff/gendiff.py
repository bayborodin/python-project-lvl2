"""Diff builder."""

from gendiff.comparator import compare
from gendiff.formatter import stylish
from gendiff.reader import read_data


def generate_diff(file_path1: str, file_path2: str) -> str:
    """
    Generate a diff for a given files.

    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.

    Returns:
        Diff of the given files.
    """
    data_collection1 = read_data(file_path1)
    data_collection2 = read_data(file_path2)
    diff = compare(data_collection1, data_collection2)

    return stylish(diff)
