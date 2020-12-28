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
    Convert a dictionary of a diff parameters row to the list of parameters.

    Parameters:
        row: Dictionary of a row diff parametes.

    Returns:
        A list of a row diff parametes.
    """
    return [row['key'], row['state'], row['value']]


def stringify_added_row(row: tuple) -> str:
    """
    Convert an added row to the plain string.

    Parameters:
        row: Tuple of the added row parametes.

    Returns:
        The plain string representation of the row.
    """
    return "Property '{0}' was added with value: {1}".format(
        row[0],
        format_value(row[1]),
    )


def stringify_updated_row(row: tuple) -> str:
    """
    Convert an updated row to the plain string.

    Parameters:
        row: Tuple of the updated row parametes.

    Returns:
        The plain string representation of the row.
    """
    return "Property '{0}' was updated. From {1} to {2}".format(
        row[0],
        format_value(row[1]['old']),
        format_value(row[1]['new']),
    )


def stringify_removed_row(row: tuple) -> str:
    """
    Convert an removed row to the plain string.

    Parameters:
        row: Tuple of the removed row parametes.

    Returns:
        The plain string representation of the row.
    """
    return "Property '{0}' was removed".format(
        row[0],
    )


def format_value(row_value: any) -> str:
    """
    Format the plain string row value.

    Parameters:
        row_value: plain string row value to format

    Returns:
        The formatted value.
    """
    if row_value == '[complex value]':
        return row_value
    if row_value is None:
        return 'null'
    if isinstance(row_value, bool):
        return str(row_value).lower()

    if isinstance(row_value, int):
        return row_value

    return "'{0}'".format(row_value)
