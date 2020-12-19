"""Diff result formatter."""
import types

from gendiff.formatters.format_utils import (
    build_diff_dict,
    build_string_from_list,
    get_row_dict_values,
)

INDENT_SYMBOL = ' '

STATES = types.MappingProxyType({
    'added': '+',
    'removed': '-',
    'updated': INDENT_SYMBOL,
    'unmodified': INDENT_SYMBOL,
})


def format_diff(diff: list) -> str:
    """
    Format diff resuls as strings with indents.

    Parameters:
        diff: List with the diff result rows.

    Returns:
        String of diff rows, structured by indents.
    """
    string = build_string_from_list(map(_format_diff_row, diff))
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
    spaces = INDENT_SYMBOL * indent
    string = ''

    row_key, row_state, row_value = get_row_dict_values(row)

    if row_state == 'updated':
        old_value = row_value['old']
        new_value = row_value['new']

        if isinstance(old_value, list):
            string += _format_nested(
                build_diff_dict(row_key, old_value, 'removed'),
                indent,
            )
        else:
            string += '{0}- {1}: {2}\n'.format(spaces, row_key, old_value)

        if isinstance(new_value, list):
            string += _format_nested(
                build_diff_dict(row_key, old_value, 'added'),
                indent,
            )
        else:
            string += '{0}+ {1}: {2}\n'.format(spaces, row_key, new_value)

        return string

    if isinstance(row_value, list):
        string += _format_nested(
            build_diff_dict(row_key, row_value, row_state),
            indent,
        )
        return string

    return '{0}{1} {2}: {3}\n'.format(
        spaces, STATES[row_state], row_key, row_value,
    )


def _format_nested(row: str, indent: str = 2, string: str = '') -> str:
    spaces = INDENT_SYMBOL * indent
    row_key, row_state, row_value = get_row_dict_values(row)

    string += '{0}{1} {2}: {{\n'.format(
        spaces,
        STATES[row_state],
        row_key,
    )

    indent += 4

    string += build_string_from_list(
        map(
            _get_formatter_with_indent(indent),
            sorted(row_value, key=lambda nested: nested['key']),
        ),
    )
    string += '{0}  }}\n'.format(spaces)

    return string


def _get_formatter_with_indent(indent=2):
    def inner(row):  # noqa: WPS430
        return _format_diff_row(row, indent)
    return inner
