"""Diff format helpers."""


def build_string_from_list(str_list: list) -> str:
    """
    Concatinate list members to the single string.

    Parameters:
        str_list: The list of strings.

    Returns:
        The string, result of concatination.
    """
    return ''.join(str_list)


def build_diff_dict(row_key: str, row_value: str, row_state: str) -> dict:
    """
    Build a dictionary from a given diff row parameters.

    Parameters:
        row_key: The key of a key-value pair in a row.
        row_value: The value of a key-value pair in a row.
        row_state: The diff result rescription.

    Returns:
        A dictionary with a diff row parameters.
    """
    return {'key': row_key, 'value': row_value, 'state': row_state}


def get_row_dict_values(row: dict) -> list:
    """
    Convert a dictionary of a row diff parameters to the list of parameters.

    Parameters:
        row: Dictionary of a row diff parametes.

    Returns:
        A list of a row diff parametes.
    """
    return [row['key'], row['state'], row['value']]
