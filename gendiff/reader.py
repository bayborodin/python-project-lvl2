"""Files reading and parsing module."""
import json
import os

import yaml


def read_data(file_path: str) -> dict:
    """
    Read files with a given file names and return list of files structure.

    Parameters:
        file_path: The path to the file to read.

    Raises:
        ValueError: if call to something fails.

    Returns:
        File content, parsed to the dictionary.
    """
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    with open(file_path, 'r') as file_descriptor:
        if extension == '.json':
            return json.load(file_descriptor)
        elif extension in ('.yml', '.yaml'):  # noqa: WPS510
            return yaml.safe_load(file_descriptor)
        raise ValueError('Unknown file format: {0}'.format(extension))
