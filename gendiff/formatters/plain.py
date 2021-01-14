"""Diff result plain formatter."""

COMPLEX_VALUE = '[complex value]'


def format_diff(diff: list) -> str:
    """
    Format diff resuls as a plain text.

    Parameters:
        diff: List with the diff result rows.

    Returns:
        String of diff rows, formatted as a plain text.
    """
    flate_diff = _flatten_diff(diff)
    return _make_string(flate_diff)


def _format_value(row_value: any) -> str:
    if row_value == '[complex value]':
        return row_value
    if row_value is None:
        return 'null'
    if isinstance(row_value, bool):
        return str(row_value).lower()

    if isinstance(row_value, int):
        return row_value

    return "'{0}'".format(row_value)


def _stringify_added_row(row: tuple) -> str:
    return "Property '{0}' was added with value: {1}".format(
        row[0],
        _format_value(row[1]),
    )


def _stringify_updated_row(row: tuple) -> str:
    return "Property '{0}' was updated. From {1} to {2}".format(
        row[0],
        _format_value(row[1]['old']),
        _format_value(row[1]['new']),
    )


def _stringify_removed_row(row: tuple) -> str:
    return "Property '{0}' was removed".format(
        row[0],
    )


def _make_string(diff):
    string_rows = []
    for row in diff:
        state = row[-1]
        if state == 'added':
            string_rows.append(_stringify_added_row(row))
        elif state == 'updated':
            string_rows.append(_stringify_updated_row(row))
        elif state == 'removed':
            string_rows.append(_stringify_removed_row(row))
    return '\n'.join(string_rows)


def _flatten_updated_row(row, complex_key):
    values_pair = row['value']
    if isinstance(values_pair['old'], list):
        values_pair['old'] = COMPLEX_VALUE
    if isinstance(values_pair['new'], list):
        values_pair['new'] = COMPLEX_VALUE
    return (complex_key, values_pair, row['state'])


def _flatten_added_row(row, complex_key):
    row_value = row['value']
    row_state = row['state']
    return (
        complex_key,
        COMPLEX_VALUE if isinstance(row_value, list) else row_value,
        row_state,
    )


def _flatten_diff(diff, parent_key='', sep='.'):
    flat_items = []
    for row in diff:
        row_state = row['state']
        row_value = row['value']
        new_key = parent_key + sep + row['key'] if parent_key else row['key']
        if row_state == 'removed':
            flat_items.append((new_key, row_state))
        elif row_state == 'added':
            flat_items.append(_flatten_added_row(row, new_key))
        elif row_state == 'unmodified' and isinstance(row_value, list):
            flat_items.extend(_flatten_diff(row_value, new_key, sep=sep))
        elif row_state == 'updated':
            flat_items.append(_flatten_updated_row(row, new_key))
    return flat_items
