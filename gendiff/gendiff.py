"""Diff builder."""

import json


def generate_diff(file_path1: str, file_path2: str) -> str:
    """
    Generate a diff for a given files.

    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.

    Returns:
        Diff of the given files.
    """
    json1 = _read_json_file(file_path1)
    json2 = _read_json_file(file_path2)

    keys = json1.keys() | json2.keys()
    diff = []
    for key in keys:
        diff.append({
            'param': key,
            'old': _get_json_value(json1, key),
            'new': _get_json_value(json2, key),
        })
    diff.sort(key=lambda diff_string: diff_string['param'])

    return _get_diff_string_representation(diff)


def _get_diff_string_representation(diff: list) -> str:
    """
    Generate a string representation for a diff.

    Parameters:
        diff: A list of diffs.

    Returns:
        The string representation of the diff.
    """
    diffs = []
    diffs.append('\n{\n')
    for string in diff:
        diffs.append(_format_diff_string(string))

    return '{0}{1}'.format(''.join(diffs), '}')


def _format_diff_string(string: str) -> str:
    """
    Create the two strings diff representation.

    Parameters:
        string: the pair of old and new strings

    Returns:
        diff representation
    """
    old_val = string['old']
    new_val = string['new']
    parameter = string['param']

    if old_val == new_val:
        return '   {0}: {1}\n'.format(parameter, old_val)
    elif old_val and not new_val:
        return ' - {0}: {1}\n'.format(parameter, old_val)
    elif new_val and not old_val:
        return ' + {0}: {1}\n'.format(parameter, new_val)
    elif old_val != new_val:
        return ' - {0}: {1}\n + {0}: {2}\n'.format(parameter, old_val, new_val)


def _read_json_file(filename: str):
    """
    Read a file from a given filename to json.

    Parameters:
        filename: The name of file to read.

    Returns:
        Dictionary with json data.
    """
    with open(filename) as json_file:
        return json.load(json_file)


def _get_json_value(json_string, key):
    """
    Extract the value from json string for a given key.

    Parameters:
        json_string: The source json string where from to extract a value.
        key: The key for the key/vaue pair.

    Returns:
        The value for a given key.
    """
    json_value = json_string.get(key, None)

    if isinstance(json_value, bool):
        json_value = str(json_value).lower()

    return json_value
