"""Files reading and parsing module."""
import json
import os

import yaml


def read_data(file_path1: str, file_path2: str) -> list:
    """
    Read files with a given file names and return list of files structure.

    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.

    Returns:
        List of files structures.
    """
    ext1 = os.path.splitext(file_path1)[1]
    ext2 = os.path.splitext(file_path2)[1]
    if ext1 == ext2 == '.json':
        return _read_json_files(file_path1, file_path2)
    elif ext1 == ext2 == '.yml':
        return _read_yml_files(file_path1, file_path2)


def _read_json_files(file_path1: str, file_path2: str) -> list:
    """
    Wrap reading of two json files into list of two dicts.

    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.

    Returns:
        List of dicts with files structure.
    """
    return [_read_json_file(file_path1), _read_json_file(file_path2)]


def _read_yml_files(file_path1: str, file_path2: str) -> list:
    """
    Wrapp reading of two yaml files into list of two dicts.

    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.

    Returns:
        List of dicts with files structure.
    """
    return [_read_yml_file(file_path1), _read_yml_file(file_path2)]


def _read_json_file(filename: str) -> dict:
    """
    Read a file from a given filename to json.

    Parameters:
        filename: The name of file to read.

    Returns:
        Dictionary with json data.
    """
    with open(filename) as json_file:
        return json.load(json_file)


def _read_yml_file(filename: str) -> dict:
    """
    Read a file from a given filename to yaml.

    Parameters:
        filename: The name of file to read.

    Returns:
        Dictionary with yaml data.
    """
    with open(filename) as file_descriptor:
        return yaml.safe_load(file_descriptor)
