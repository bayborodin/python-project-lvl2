"""Diff result formatter."""
import types

STATES = types.MappingProxyType({
    'added': '+',
    'removed': '-',
    'updated': ' ',
    'unmodified': ' ',
})


def stylish(diff: list) -> str:
    """
    Format diff resuls as strings with indents.

    Parameters:
        diff: List with the diff result rows.

    Returns:
        String of diff rows, structured by indents.
    """
    string = ''.join(map(_format_diff_row, diff))
    return _convert_to_json_string(f'{{\n{string}}}')  # noqa: WPS305


def _convert_to_json_string(string: str) -> str:
    return string.replace(
        'True', 'true',
    ).replace(
        'False', 'false',
    ).replace(
        'None', 'null',
    )


def _format_diff_row(row: str, indent: str = 2) -> str:
    spaces = ' ' * indent

    if row['state'] == 'updated':
        string = ''

        old_value = row['value']['old']
        new_value = row['value']['new']

        string += '{0}- {1}: {2}\n'.format(spaces, row['key'], old_value)
        string += '{0}+ {1}: {2}\n'.format(spaces, row['key'], new_value)

        return string

    return '{0}{1} {2}: {3}\n'.format(
        spaces, STATES[row['state']], row['key'], row['value'],
    )
